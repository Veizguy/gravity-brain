---
name: obsidian-automation
description: "Værktøjer til at styre Obsidian via kommandolinjen (CLI) og URI-links. Giver agenter mulighed for at åbne noter, søge, og administrere plugins direkte i Obsidian UI."
---

# Obsidian Automation (CLI & URI)

Denne skill giver dig adgang til at styre Obsidian-applikationen direkte.

## 1. Obsidian CLI
Brug `obsidian` kommandoen til direkte interaktion.

### Vigtige Kommandoer
- `obsidian help`: Vis alle tilgængelige kommandoer.
- `obsidian daily`: Åbn dagens note.
- `obsidian daily:append content="- [ ] Ny opgave"`: Tilføj indhold til dagens note.
- `obsidian open "Min Note"`: Åbn en specifik note.
- `obsidian search "søgeord"`: Start en søgning i Obsidian.
- `obsidian reload-plugins`: Genindlæs alle plugins (nyttigt efter ændringer i `data.json`).

## 2. Obsidian URI
Brug URI'er til at navigere eller trigge handlinger via URL'er. Vault-navnet er `brain`.

### Format
`obsidian://[action]?[parameters]`

### Eksempler
- **Åbn note**: `obsidian://open?vault=brain&file=Welcome`
- **Søg**: `obsidian://search?vault=brain&query=todo`
- **Opret note**: `obsidian://new?vault=brain&name=NyNote&content=Hej`

## 3. Hjælpe-scripts
Brug `scripts/open_obsidian_uri.sh` til at kalde URI'er sikkert fra terminalen.

```bash
./scripts/open_obsidian_uri.sh "obsidian://open?vault=brain&file=01.01%20Test%20Record"
```

> [!IMPORTANT]
> Obsidian skal køre for at CLI og URI fungerer. CLI skal aktiveres i Obsidian indstillingerne.
