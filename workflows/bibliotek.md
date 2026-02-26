---
description: Start Bibliotek sub-agenten (Taxonomy & Structure Manager) for at organisere filer i din vault.
---

# `Bibliotek` Workflow

Kør denne for at sikre struktur i Brians PKM vault. Denne proces fungerer nu som din "update-taxonomy" rutine.

## Trin 1: Opdater Records
- Gennemgå alle noter med `type: record` (📂).
- Tjek for nye beskrivelser eller ændringer i de underliggende filer (via Bases).
- Sikr at `taxonomy` feltet er udfyldt korrekt med et link til en taksonomi (🗄️).

## Trin 2: Opdater Taksonomier
- Gennemgå alle noter med `type: taksonomi` (🗄️).
- **Stikords-sync**: Uddrag vigtige keywords fra de tilknyttede records og tilføj dem til taksonomiens `keywords` felt.
- Opdater den centrale `00.01 Taksonomi.md` hvis der er væsentlige ændringer i beskrivelserne.

## Trin 3: Gap Analysis
- Gennemse de nye filer i `2 - Files`.
- Identificér overordnede emner, projekter eller personer, der endnu mangler deres egen **Record** (📂) eller **Taksonomi** (🗄️).
- Foreslå oprettelse af disse nye overordnede enheder ved hjælp af skabelonerne `Taksonomi.md` og `Record.md`. Knyt desuden de fundne *items* (noter/filer) til de rigtige records via taxonomy-feltet.
- **Logning**: Åbn dagens note i `daily-logs/` og find sektionen `## Antigravity log`.
- **Tilføj ny række øverst** i tabellen (nyeste først):
  `| [HH:MM] | Bibliotek | Organisering | Organiserede [Filnavne] | ✅ | N/A |`
