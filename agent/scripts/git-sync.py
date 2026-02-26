#!/usr/bin/env python3
import subprocess
import os
import sys
from datetime import datetime

def run_command(command, cwd=None):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, cwd=cwd)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command {' '.join(command)}: {e.stderr}")
        return None

def sync():
    # Identify agent
    agent_name = sys.argv[1] if len(sys.argv) > 1 else "Antigravity"
    
    # Root directory (where .git is)
    root_dir = "/Users/mikkelfeld/obsidian/brain"
    os.chdir(root_dir)
    
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting GitHub sync for {agent_name}...")
    
    # 1. Add changes
    run_command(["git", "add", "."])
    
    # 2. Check for changes
    status = run_command(["git", "status", "--porcelain"])
    if not status:
        print("No local changes to commit. Checking for remote updates...")
    else:
        # 3. Commit
        print(f"Committing local changes for {agent_name}...")
        run_command(["git", "commit", "-m", f"chore: updates by {agent_name}"])

    # 4. Fetch and Rebase
    print("Fetching remote changes and rebasing...")
    run_command(["git", "fetch", "origin"])
    
    rebase_result = subprocess.run(["git", "rebase", "origin/main"], capture_output=True, text=True)
    
    if rebase_result.returncode != 0:
        print("CONFLICT during rebase! Attempting to resolve using 'ours' (local) strategy as files are synced via Obsidian...")
        # Since Obsidian Sync already made the files the same, 'ours' or 'theirs' shouldn't matter much, 
        # but 'ours' is safer if we just committed what we have.
        # Actually, in a rebase, 'theirs' is the incoming commit.
        # Let's try to abort and suggest manual fix if it's too complex.
        run_command(["git", "rebase", "--abort"])
        print("Rebase failed and was aborted. Please resolve conflicts manually.")
        sys.exit(1)
    
    # 5. Push
    print("Pushing to remote...")
    push_result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    if push_result.returncode == 0:
        print("Sync complete! Consolidated changelog updated.")
    else:
        print(f"Push failed: {push_result.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    sync()
