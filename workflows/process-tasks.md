---
name: "Process Tasks"
description: "Synkroniserer dine opgaver fra Obsidian til Todoist."
---

# /process-tasks Workflow

Dette workflow bruges til at tvinge en synkronisering af dine opgaver til Todoist.

## 1. Kør Synkronisering
// turbo
- Kør synkroniserings-scriptet:
  `python3 ./skills/pkm-reception/todoist-sync/scripts/sync_todoist.py`

## 2. Rapportér Status
- Giv en opsummering af:
    - Hvor mange nye opgaver der blev oprettet.
    - Eventuelle fejl under synkroniseringen.

## 3. Logning
- Åbn dagens note i `daily-logs/` og find sektionen `## Antigravity log`.
- **Tilføj ny række øverst** i tabellen (nyeste først):
  `| [HH:MM] | Reception | Todoist Sync | Synkroniserede opgaver | ✅ | N/A |`
