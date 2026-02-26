import os
import time
import subprocess
import logging
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURATION ---
VAULT_ROOT = Path("/Users/mikkelfeld/obsidian/brain")
INBOX_DIR = VAULT_ROOT / "1 - Inbox"
EXTRACT_SCRIPT = VAULT_ROOT / "skills/pkm-extractor/scripts/extract.py"
PYTHON_BIN = Path("/Users/mikkelfeld/.brian/envs/extractor/bin/python3")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(VAULT_ROOT / "agent/ocr_watcher.log"),
        logging.StreamHandler()
    ]
)

class OCRHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.process_file(event.src_path)
            
    def on_moved(self, event):
        # Also catch files moved INTO the inbox
        if not event.is_directory:
            self.process_file(event.dest_path)

    def process_file(self, file_path):
        path = Path(file_path)
        # Only process binary files, ignore .md, .json, and hidden files
        if path.suffix.lower() in ['.pdf', '.png', '.jpg', '.jpeg', '.tiff'] and not path.name.startswith('.'):
            # Wait a bit for the file to be fully written/moved
            time.sleep(1)
            
            md_filename = f"{path.stem} (OCR).md"
            md_path = INBOX_DIR / md_filename
            
            if md_path.exists():
                logging.info(f"Skipping {path.name}, OCR note already exists.")
                return

            logging.info(f"Processing {path.name}...")
            
            try:
                # Run extraction
                result = subprocess.run(
                    [str(PYTHON_BIN), str(EXTRACT_SCRIPT), str(path)],
                    capture_output=True,
                    text=True,
                    check=True
                )
                
                extracted_text = result.stdout.strip()
                
                if not extracted_text:
                    logging.warning(f"No text extracted from {path.name}")
                    extracted_text = "[Ingen tekst fundet ved OCR]"

                # Create MD note
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Handling relative link - if file is in subfolder or root
                try:
                    rel_path = path.relative_to(INBOX_DIR)
                except ValueError:
                    rel_path = path.name

                content = f"""---
created: {now}
modified: {now}
taxonomy: [Inbox]
type: note
tags: 
  - status/raw
  - type/ocr
source: "[[{path.name}]]"
---

# {path.stem} (OCR)

![[{rel_path}]]

## Indhold
{extracted_text}
"""
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                logging.info(f"Successfully created {md_path.name}")

            except subprocess.CalledProcessError as e:
                logging.error(f"Error processing {path.name}: {e.stderr}")
            except Exception as e:
                logging.error(f"Unexpected error for {path.name}: {e}")

def main():
    if not INBOX_DIR.exists():
        INBOX_DIR.mkdir(parents=True, exist_ok=True)
        
    event_handler = OCRHandler()
    observer = Observer()
    # Watch INBOX_DIR instead of assets
    observer.schedule(event_handler, str(INBOX_DIR), recursive=True)
    
    logging.info(f"Watching {INBOX_DIR} for new files...")
    
    # Initial scan
    for root, dirs, files in os.walk(INBOX_DIR):
        for file in files:
            full_path = Path(root) / file
            event_handler.process_file(str(full_path))
            
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
