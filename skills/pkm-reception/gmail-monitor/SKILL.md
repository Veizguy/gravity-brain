---
name: Gmail (MCP)
description: Giver Brian on-demand adgang til Gmail via `@mcp-z/mcp-gmail` MCP-serveren. Erstatter det tidligere CRON-baserede monitor script.
---

# Gmail (MCP)

Brian tilgår Gmail **on-demand** via `@mcp-z/mcp-gmail` MCP-serveren, som er konfigureret i Antigravity's `mcp_config.json`. Ingen CRON-jobs eller automatiske dumps til vault'en.

## Arbejdsgang (On-Demand)

Når brugeren beder om at tjekke mails, skal følgende trin følges:

1. **Hent Mails**: Brug `mcp_gmail_list_messages` (eller fallback scripts) til at hente relevante mails.
2. **Opdatér Daily Log**:
   - **Indkomne Emails**: For hver ny eller relevant mail, tilføj en række til tabellen under `# 📨 Indkomne` i dagens note (`daily-logs/YYYY-MM-DD.md`). **Nyeste skal stå øverst i tabellen.**
     - Sørg for at tabellen har overskrift og separator hvis den oprettes på ny:
       `| Tid | Type | Emne | Beskrivelse | Ref. | Status |`
       `| --- | --- | --- | --- | --- | --- |`
     - Brug formatet: `| [Tid] | Email | [Afsender] | [Resumé] | | <!-- msg_id:: [ID] --> |`
   - **Aktivitetslog**: Tilføj en række til tabellen under `# 🤖 Antigravity log` for at dokumentere tjekket. **Nyeste skal stå øverst i tabellen.**
     - Sørg for at tabellen har overskrift og separator hvis den oprettes på ny:
       `| Tid | Job | Beskrivelse | Success | Token forbrug |`
       `| --- | --- | ----------- | ------- | ------------- |`
     - Brug formatet: `| [Tid] | Reception | Gmail Check | Tjekkede emails (on-demand via MCP) | ✅ | [Tokens] |`

## Hvornår bruges dette?

Brian aktiverer Gmail-værktøjerne, når brugeren beder om det, f.eks.:
- "Hvad er de seneste mails fra X?"
- "Hent og opsummér gårsdagens ulæste mails"
- "Skriv et udkast til et svar på den seneste mail fra Y"

## Konfiguration

| Fil | Placering |
|-----|-----------|
| OAuth credentials | `~/.gmail-mcp/gcp-oauth.keys.json` |
| OAuth token | `~/.gmail-mcp/credentials.json` |
| MCP config | `~/.gemini/antigravity/mcp_config.json` |

---
> **DEPPRECATED:** Det tidligere Python-script `scripts/monitor_gmail.py` og dets CRON-job er deaktiveret til fordel for denne MCP-løsning.
