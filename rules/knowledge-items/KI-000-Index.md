---
name: Knowledge Items (KI) Index
description: Dokumentation og regler for systemets brug af Knowledge Items til opsamling af 'Tacit Knowledge' og fakta.
---

# Knowledge Items (KI) - Systemets Hukommelse

Dette dokument definerer, hvordan systemet (og alle dets agenter) gemmer og genanvender "Tacit Knowledge" — altså underforstået viden om brugerens præferencer, arbejdsgange, og specifikke opsamlede fakta over tid.

Ved at formalisere dette, undgår vi at gentage de samme fejl, og over tid tilpasser agenterne sig brugerens naturlige flow. Målet er at flytte alt, der plejede at ligge glemt i historik, over i denne formaliserede struktur.

## De to KI-Typer

Systemet opererer med to forskellige typer af Knowledge Items, afhængigt af formålet:

### 1. Regelsæt KIs (Rule-KIs)
* **Placering:** `rules/knowledge-items/`
* **Formål:** Beskriver systemets *adfærd*. Hvordan vil brugeren kontaktes? Hvilket sprog bruges? Hvordan formateres output bedst muligt? 
* **Brug:** Disse KIs forventes løbende at blive læst og evalueret af agenter for at kalibrere deres tone og metodik, før en opgave udføres.
* **Eksempler:** `KI-001-Skrivestil-og-Tone.md`

### 2. Faktuelle KIs (Factual-KIs)
* **Placering:** Den flade stuktur direkte i `2 - Files/`
* **Formål:** Konkrete vidensobjekter, fakta-ark, koncepter og opsamlet baggrundsviden, som opstår i forlængelse af arbejdet.
* **Metadata Standard:** Disse filer SKAL anvende brugerens eksisterende frontmatter konventioner (skal indeholde `taxonomy:` property). Særligt bemærkelsesværdigt er, at deres type defineres som `type: Knowledge Item`.

#### Eksempel på Factual KI YAML
```yaml
---
created: {{date}}
modified: {{date}}
taxonomy: [Relevant Emne]
type: Knowledge Item
tags:
  - status/processed
---
```

## Agenternes Pligt (Lokal Indlæring)
Alle agenter (via deres underliggende *obsidian-pkm* regelsæt) er ansvarlige for at vedligeholde dette system. 

1. **Den Daglige Log (The Source):** For at opsamle Tacit Knowledge i det daglige, dokumenterer alle agenter deres handlinger og indsigter grundigt i `daily-logs/` (Under sektionen "Antigravity log"). De logfører diskussioner om arbejdsgange, samt nye formelle koncepter.
2. **Bibliotekarens Udvindelse (The Synthesis):** Hver aften kl 23:30 gennemgår **Bibliotekaren** (via `pkm-bibliotek/ki-ekstraktion` skill'en) dagens "Antigravity log" samt alle ubehandlede chat-logs. Bibliotekaren identificerer mønstre, nye præferencer og formelle fakta, og opbygger/opdaterer automatisk filerne i KI-systemet i overensstemmelse med de definerede KI-typer ovenfor.
