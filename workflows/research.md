---
description: Start Research sub-agenten (The Researcher) for dybdegående indsamling af viden.
---

# `Research` Workflow

Kør denne for at foretage et Deep Dive på et valgt emne med Brians Research-subagent.

1. **Afklar Spørgsmål**: Læs The prompt (emnet for din søgning).
2. **Søgning**: Brug Perplexity MCP eller Web Search værktøjet til at indhente nyeste information om emnet. Find minimum tre pålidelige kilder.
3. **Kildekritik**: Bekræft evt. uoverensstemmelser.
4. **Syntese**: Saml al viden til en velstruktureret, Markdown-baseret note.
5. **Output**: Opret noten i Brians Vault i `inbox/` eller send teksten tilbage til brugeren ifølge skabelonen til Research Notes.
6. **Logning**: Åbn dagens note i `daily-logs/` og find sektionen `## Antigravity log`.
- **Tilføj ny række øverst** i tabellen (nyeste først):
  `| [HH:MM] | Research | Deep Dive | Undersøgte [Emne] | ✅ | N/A |`
