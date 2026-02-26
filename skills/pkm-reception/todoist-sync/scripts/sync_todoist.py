import os
import re
import json
import requests
from datetime import datetime

# Configuration
VAULT_ROOT = os.getenv('VAULT_ROOT', '/Users/mikkelfeld/obsidian/brain/')
SKILL_DIR = os.path.join(VAULT_ROOT, 'skills/todoist-sync/')
CONFIG_FILE = os.path.join(SKILL_DIR, 'config.json')

# New Unified API v1
BASE_URL = "https://api.todoist.com/api/v1"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, 'r') as f:
        return json.load(f)

def get_todoist_session(api_token):
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    })
    return session

def parse_tasks_from_content(content):
    tasks = []
    
    # 1. Standard markdown tasks: - [ ] Task description
    # Support inline todoist_id: - [ ] task description [todoist_id:: 12345]
    task_pattern = r'^\s*-\s*\[(?P<status>[ xX])\]\s*(?P<task_data>.*)$'
    
    lines = content.split('\n')
    for i, line in enumerate(lines):
        match = re.match(task_pattern, line)
        if match:
            status = match.group('status')
            data = match.group('task_data')
            
            # Check if already synced
            todoist_id = None
            id_match = re.search(r'\[todoist_id::\s*(\w+)\]', data)
            if id_match:
                todoist_id = id_match.group(1)
            
            # Extract tags #tag
            tags = re.findall(r'#(\w+)', data)
            # Extract due date 📅 YYYY-MM-DD
            due_match = re.search(r'📅\s*(\d{4}-\d{2}-\d{2})', data)
            due_date = due_match.group(1) if due_match else None
            
            # Extract priority ⏫ (4), 🔼 (3), 🔽 (2)
            priority = 1
            if '⏫' in data: priority = 4
            elif '🔼' in data: priority = 3
            elif '🔽' in data: priority = 2

            # Clean content for Todoist (remove tags and metadata)
            clean_content = data
            clean_content = re.sub(r'\[todoist_id::.*?\]', '', clean_content)
            clean_content = re.sub(r'#\w+', '', clean_content)
            clean_content = re.sub(r'[📅⏫🔼🔽].*', '', clean_content).strip()

            tasks.append({
                'line_index': i,
                'status': status,
                'todoist_id': todoist_id,
                'content': clean_content or data.strip(),
                'tags': tags,
                'due_date': due_date,
                'priority': priority,
                'raw_line': line
            })
            
    return tasks

def update_obsidian_task_status(file_lines, line_idx, new_status):
    line = file_lines[line_idx]
    # Replace [ ] or [x] with the new status
    updated_line = re.sub(r'\[[ xX]\]', f'[{new_status}]', line, count=1)
    if updated_line != line:
        file_lines[line_idx] = updated_line
        return True
    return False

def fetch_todoist_tasks(session):
    try:
        response = session.get(f"{BASE_URL}/tasks")
        response.raise_for_status()
        data = response.json()
        # The new unified API might return a list directly or an object with a list
        if isinstance(data, list):
            return data
        elif isinstance(data, dict):
            # Check for common patterns
            return data.get('results') or data.get('tasks') or data.get('items') or []
        return []
    except Exception as e:
        print(f"Error fetching Todoist tasks: {e}")
        return []

def main():
    config = load_config()
    token = config.get('api_token')
    if not token or token == "YOUR_TODOIST_API_TOKEN":
        print("Todoist API token missing.")
        return

    session = get_todoist_session(token)
    
    # 1. Build a map of existing tasks in Obsidian
    obsidian_tasks = {} # todoist_id -> {file_path, line_index, status, lines_ref}
    all_files_data = {} # file_path -> lines
    
    scan_paths = config.get('scan_paths', ['tasks'])
    for rel_path in scan_paths:
        abs_path = os.path.join(VAULT_ROOT, rel_path)
        if not os.path.exists(abs_path): continue
            
        for root, _, files in os.walk(abs_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        lines = f.readlines()
                    
                    all_files_data[file_path] = lines
                    tasks = parse_tasks_from_content("".join(lines))
                    for t in tasks:
                        if t['todoist_id']:
                            obsidian_tasks[t['todoist_id']] = {
                                'file_path': file_path,
                                'line_index': t['line_index'],
                                'status': t['status'],
                                'content': t['content']
                            }

    # 2. Fetch tasks from Todoist
    todoist_tasks = fetch_todoist_tasks(session)
    todoist_task_ids = {str(t['id']) for t in todoist_tasks}
    
    files_to_save = set()

    # 3. Handle status updates and new tasks from Todoist
    now = datetime.now()
    today_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M')
    daily_note_path = os.path.join(VAULT_ROOT, f'daily-logs/{today_str}.md')
    
    for t_task in todoist_tasks:
        tid = str(t_task['id'])
        if tid in obsidian_tasks:
            pass
        else:
            # New task from Todoist -> Add to Indbakke table in Daily Note
            os.makedirs(os.path.dirname(daily_note_path), exist_ok=True)
            
            # Reconstruct metadata for Description
            priority_map = {4: "⏫", 3: "🔼", 2: "🔽", 1: ""}
            p_sym = priority_map.get(t_task.get('priority', 1), "")
            due = f" 📅 {t_task['due']['date']}" if t_task.get('due') else ""
            labels = " ".join([f"#{l}" for l in t_task.get('labels', [])])
            desc = f"{labels}{due} {p_sym}".strip()
            
            # Format table row: | Time | Todoist | Subject | Description | Ref. | Status |
            # Include todoist_id in the description or as a hidden field
            row_subject = t_task['content']
            row_desc = f"{desc} [todoist_id:: {tid}]".strip()
            new_row = f"| {time_str} | Todoist | {row_subject} | {row_desc} | | - [ ] |"
            
            if not os.path.exists(daily_note_path):
                with open(daily_note_path, 'w') as f:
                    f.write(f"# {today_str}\n\n# Indbakke\n\n| Tid   | Type    | Emne                   | Beskrivelse                                                            | Ref. | Status            |\n| ----- | ------- | ---------------------- | ---------------------------------------------------------------------- | ---- | ----------------- |\n")
                    f.write(new_row + "\n")
            else:
                with open(daily_note_path, 'r') as f:
                    lines = f.readlines()
                
                # Find the table and insert after the header or last row
                table_start = -1
                for i, line in enumerate(lines):
                    if "| Tid" in line and "Type" in line:
                        table_start = i
                        break
                
                if table_start != -1:
                    # Insert after header separator (index + 2)
                    lines.insert(table_start + 2, new_row + "\n")
                    with open(daily_note_path, 'w') as f:
                        f.writelines(lines)
                else:
                    # No table found, append to end
                    with open(daily_note_path, 'a') as f:
                        f.write("\n" + new_row + "\n")
            
            print(f"Imported new task from Todoist to Indbakke table: {t_task['content']}")

    # 4. Handle completions (Todoist -> Obsidian)
    # If an ID is in obsidian_tasks but NOT in the active todoist_task_ids list, 
    # it *might* be completed (or deleted).
    for tid, o_task in obsidian_tasks.items():
        if tid not in todoist_task_ids and o_task['status'] == ' ':
            # Mark as completed in Obsidian
            f_path = o_task['file_path']
            f_lines = all_files_data[f_path]
            if update_obsidian_task_status(f_lines, o_task['line_index'], 'x'):
                files_to_save.add(f_path)
                print(f"Marked task as completed in Obsidian (via Todoist): {o_task['content']}")

    # 5. Handle new tasks (Obsidian -> Todoist)
    # (Re-running the scan to find tasks without IDs)
    for f_path, f_lines in all_files_data.items():
        content = "".join(f_lines)
        tasks = parse_tasks_from_content(content)
        changed = False
        for t in tasks:
            if t['status'] == ' ' and not t['todoist_id']:
                if sync_task(session, t, f_lines):
                    changed = True
                    files_to_save.add(f_path)
    
    # 6. Save all changed files
    for f_path in files_to_save:
        with open(f_path, 'w') as f:
            f.writelines(all_files_data[f_path])

if __name__ == "__main__":
    main()



