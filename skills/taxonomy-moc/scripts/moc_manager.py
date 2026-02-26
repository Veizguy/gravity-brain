import os
import re

VAULT_PATH = "/Users/mikkelfeld/obsidian/brain"
TAKSONOMI_DIR = os.path.join(VAULT_PATH, "00 The Brain/Taksonomi")
TAKSONOMI_INDEX = os.path.join(VAULT_PATH, "00 The Brain/00.01 Taksonomi.md")

def ensure_dir():
    if not os.path.exists(TAKSONOMI_DIR):
        os.makedirs(TAKSONOMI_DIR)

def read_moc(taxonomy_id):
    path = os.path.join(TAKSONOMI_DIR, f"{taxonomy_id}.md")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

def write_moc(taxonomy_id, content):
    ensure_dir()
    path = os.path.join(TAKSONOMI_DIR, f"{taxonomy_id}.md")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def update_index_links(taxonomy_id):
    if not os.path.exists(TAKSONOMI_INDEX):
        return
    
    with open(TAKSONOMI_INDEX, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    # Identify the row for the taxonomy_id and wrap the Taksonomi name in a wikilink
    # | ID  | Taksonomi | Beskrivelse | Nøgleord |
    # | 01  | Navn      | ...         | ...      |
    
    pattern = re.compile(rf"\|\s*{taxonomy_id}\s*\|\s*([^|]+)\s*\|")
    
    for line in lines:
        match = pattern.search(line)
        if match:
            name = match.group(1).strip()
            if not name.startswith("[["):
                # Convert to link
                moc_link = f"[[{taxonomy_id}]]" # Link to MoC (assuming it's in a way Obsidian finds it)
                # Actually, link to the file in Taksonomi/ID.md
                # Since it's in 00 The Brain/Taksonomi/, Obsidian usually likes [[ID]] or [[Taksonomi/ID]]
                moc_name_link = f"[[{name}]]" # If we renamed the MoC to the name, but ID is safer
                # The user wants "Taksonomi" column to be the link.
                # Let's use [[00 The Brain/Taksonomi/{taxonomy_id}|{name}]]
                link_text = f"[[00 The Brain/Taksonomi/{taxonomy_id}|{name}]]"
                line = line.replace(name, link_text)
        new_lines.append(line)
        
    with open(TAKSONOMI_INDEX, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def update_index_keywords(taxonomy_id, new_keywords):
    if not os.path.exists(TAKSONOMI_INDEX):
        return
    
    with open(TAKSONOMI_INDEX, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    pattern = re.compile(rf"\|\s*{taxonomy_id}\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|")
    
    for line in lines:
        match = pattern.search(line)
        if match:
            existing_keywords = match.group(3).strip()
            # Merge keywords
            k_list = [k.strip() for k in existing_keywords.split(',') if k.strip()]
            for nk in new_keywords:
                if nk.lower() not in [ek.lower() for ek in k_list]:
                    k_list.append(nk)
            
            merged = ", ".join(k_list)
            # Find the keywords part and replace
            parts = line.split('|')
            if len(parts) >= 5:
                parts[4] = f" {merged} "
                line = "|".join(parts)
        new_lines.append(line)
        
    with open(TAKSONOMI_INDEX, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "update_keywords" and len(sys.argv) > 3:
            update_index_keywords(sys.argv[2], sys.argv[3:])
        elif cmd == "update_links" and len(sys.argv) > 2:
            update_index_links(sys.argv[2])
