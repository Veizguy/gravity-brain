import os
import json
import re
from datetime import datetime

VAULT_PATH = "/Users/mikkelfeld/obsidian/brain"
STATE_FILE = os.path.join(VAULT_PATH, "skills/taxonomy-moc/state.json")

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {"last_run": 0}

def save_state(last_run):
    with open(STATE_FILE, 'w') as f:
        json.dump({"last_run": last_run}, f)

def get_modified_files(last_run_ts):
    modified_files = []
    for root, dirs, files in os.walk(VAULT_PATH):
        # Skip hidden directories and specific system folders
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['openspec', 'gravity-brain', 'process-inbox']]
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                mtime = os.path.getmtime(file_path)
                if mtime > last_run_ts:
                    modified_files.append(file_path)
    return modified_files

def extract_metadata(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Simple regex to find YAML frontmatter
            match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
            if match:
                yaml_text = match.group(1)
                data = {}
                # Extract key-value pairs
                for line in yaml_text.split('\n'):
                    if ':' in line:
                        parts = line.split(':', 1)
                        if len(parts) == 2:
                            k, v = parts
                            data[k.strip()] = v.strip()
                return data
    except Exception as e:
        print(f"Error extracting metadata from {file_path}: {e}")
    return {}

def main():
    state = load_state()
    last_run = state["last_run"]
    
    files = get_modified_files(last_run)
    results = []
    
    for f in files:
        meta = extract_metadata(f)
        results.append({
            "path": f,
            "rel_path": os.path.relpath(f, VAULT_PATH),
            "metadata": meta
        })
    
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
