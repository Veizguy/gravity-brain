---
name: Todoist Sync
description: Synchronizes tasks from Obsidian markdown files and blocks to Todoist, including tags, due dates, and priority.
---

# Todoist Sync

This skill scans the Obsidian vault for tasks and synchronizes them with Todoist. It supports standard markdown task syntax, ` ```tasks ` blocks, and bidirectional status updates.

## Workflow

1.  **Scan Vault**: Periodically scans specified directories (e.g., `tasks/`, `daily/`) for tasks.
2.  **Parse Tasks**:
    - Identifies `- [ ]` lines.
    - Extracts `#tags` and maps them to Todoist labels.
    - Extracts due dates (e.g., `📅 YYYY-MM-DD`).
    - Extracts priority (e.g., `⏫`, `🔼`, `🔽`).
3.  **Sync to Todoist**:
    - Creates new tasks in Todoist if they don't have a `todoist_id`.
    - Stores the `todoist_id` as an inline field: `[todoist_id:: <id>]`.
4.  **Update Status**:
    - Checks Todoist for completion.
    - If a task is completed in Todoist, marks it as `[x]` in Obsidian.
    - If a task is checked in Obsidian, marks it as completed in Todoist.

## Tools

### Sync Script
Execute the synchronization script:
`python3 /Users/mikkelfeld/obsidian/brain/skills/todoist-sync/scripts/sync_todoist.py`

## Configuration
Requires `config.json` in `/Users/mikkelfeld/obsidian/brain/skills/todoist-sync/` with:
- `api_token`: Your Todoist API Token.
- `default_project`: The project ID to sync to.
- `scan_paths`: List of paths to scan for tasks.
