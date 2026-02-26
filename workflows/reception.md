---
description: Start Reception sub-agenten (Inbox & Tasks Processor)
---

# `Reception` Workflow

Kør denne for at processere indbakken i din Brian PKM vault. Denne proces fungerer nu som din "process-inbox" rutine.

## 1. Hent og Processér Gmail
- Kør Gmail Monitor skill'en for at hente dagens emails.
- **Map Taxonomy**: Identificér relevant `record` (et overordnet projekt, interesseområde eller person, fx `📂 Navn`) og tilføj til frontmatter som `taxonomy: [[📂 Record Navn]]`. Indkomne noter og filer er **items**, som lægges under en record.
- **Log**: Tilføj række til indbakke-tabellen i `daily-logs/YYYY-MM-DD.md`.

## 2. Scan Indbakke (Filer)
- Find alle filer i `1 - Inbox`.
- **Ekstrahér data (Binære filer)**: Hvis en fil i indbakken er en PDF eller et billede, SKAL du bruge `[[skills/pkm-extractor/SKILL|PKM Extractor]]` scriptet til først at udtrække teksten til en midlertidig fil. Byg dine KIs/formaterede noter ud fra dette udtræk.
- **Slet tomme filer**: Hvis en fil er tom (0 bytes eller kun indeholder tom frontmatter), skal den slettes med det samme.

## 3. Processerings-logik (Mapping & Metadata)
For hver fil:
- **Standardisér Titel**: Sørg for at filnavnet følger standarden `[Emoji] [ID] [Navn]`. Hvis titlen er mangelfuld (fx bare "Record Navn"), skal du tilføje den korrekte emoji (📂 for records, 🗄️ for taksonomier) og ID hvis muligt.
- **Emoji-Awareness**: Husk at records (projekter, personer, områder) bruger 📂 og taksonomier bruger 🗄️. Filer/noter (items) oprettes som almindelige filer men knyttes til en record/taksonomi via properties.

## 4. Flytning og Arkivering
- Flyt alle processerede filer fra `1 - Inbox` til `2 - Files`.
- **VIGTIGT**: Filerne skal ligge **fladt** i `2 - Files`. Der må **IKKE** oprettes undermapper.

## 6. Logning og Afrapportering
- Tilføj række øverst i `## Antigravity log` i dagens note:
  `| [HH:MM] | Reception | Gmail Monitor | Processerede [Antal] emails | ✅ | N/A |`
  `| [HH:MM] | Reception | Process-Inbox | Processerede [Antal] noter | ✅ | N/A |`
