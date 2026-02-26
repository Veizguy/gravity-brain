# Architecture Decision: Workspace Organization

## Context
The workspace exists on multiple machines (e.g., this Mac and "Brian" on the Agent-PC) and is synchronized via **Obsidian Sync**. 

## Problem
1. **Obsidian Sync** ignores dot-folders and dot-files (e.g., `.agent`, `.skills`) by default.
2. **Antigravity** and other agentic tools often expect configuration in specific dot-folders at the workspace root to enable specialized features (Knowledge, Browser, etc.).
3. We need a structure that is both syncable and tool-compatible.

## Decision
We use a **Symlink Proxy Strategy**:

1. **Source of Truth (Syncable)**:
   All actual configuration files are stored in standard, non-dot folders at the root:
   - `/agent/`: Agent instructions (e.g., `GEMINI.md`)
   - `/skills/`: Specialized skill logic
   - `/workflows/`: Process definitions
   - `/rules/`: System rules and watch triggers
   - `/.openspec/`: SDD data (specs, proposals, archive)

2. **Tool Compatibility (Local)**:
   Local symbolic links (dot-folders pointing to the non-dot folders) are created on each machine to satisfy Antigravity's requirements:
   - `.agent` -> `agent`
   - `.skills` -> `skills`
   - `.workflows` -> `workflows`
   - `.rules` -> `rules`
   - `.openspec` -> `openspec`

## Impact
- **Sync**: Changes made to the non-dot folders are synced across all devices via Obsidian Sync.
- **Antigravity**: The tool finds the necessary configuration via the local symlinks.
- **Maintenance**: When setting up a new machine, the symlinks must be created manually (or via an automated setup script).

## OpenSpec Structure
We distinguish between **logic** and **data**:
- `/skills/.openspec/`: Contains the technical skill logic/scripts.
- `/.openspec/`: Contains the system state and change history (the "Source of Truth" for the project).
