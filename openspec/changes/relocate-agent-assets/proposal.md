# Proposal: Relocate Agent Assets to 00 The Brain

## Goal
Move all agent-related system folders and visibility symlinks into the `00 The Brain` folder to declutter the root of the Obsidian vault.

## Background
The vault contains several folders and symlinks that manage the AI agent's behavior (rules, skills, workflows). Currently, these are scattered in the root directory. Since they are symlinked to "dot-folders" (like `.agent`), moving the visibility links into a subfolder should not break the agent's functionality as long as the underlying structure is preserved.

## Proposed Changes

### [Root Directory]
#### [MOVE] `agent/` -> `00 The Brain/agent/`
#### [MOVE] `rules/` -> `00 The Brain/rules/`
#### [MOVE] `skills/` -> `00 The Brain/skills/`
#### [MOVE] `workflows/` -> `00 The Brain/workflows/`
#### [MOVE] `openspec/` -> `00 The Brain/openspec/`
#### [MOVE] `.agent/` -> `00 The Brain/.agent/`
#### [MOVE] `.rules/` -> `00 The Brain/.rules/`
#### [MOVE] `.skills/` -> `00 The Brain/.skills/`
#### [MOVE] `.workflows/` -> `00 The Brain/.workflows/`
#### [MOVE] `.openspec/` -> `00 The Brain/.openspec/`

## Verification Plan
1. Check that all moved folders are still accessible.
2. Verify that symlinks still point to the correct relative paths.
3. Confirm that the agent (Brian) can still read its own rules and skills.
