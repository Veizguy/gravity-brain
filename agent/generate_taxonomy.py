import os

template = """---
created: {date}
modified: {date}
taxonomy: {parent}
type:
  - taksonomi
keywords: {keywords}
---
## 📝 Beskrivelse

{description}

## 📂 Records

```base
filters:
  and:
    - type.contains("record")
    - taxonomy == this.file
views:
  - type: table
    name: Records i denne Taksonomi
    order:
      - file.name
      - keywords
      - modified
      - created
    sort:
      - property: file.name
        direction: ASC
      - property: keywords
        direction: ASC
    columnSize:
      file.name: 199
      note.keywords: 590
```
"""

categories = [
    {
        "name": "🗄️ 00-09 SYSTEM OG MIG SELV",
        "parent": "",
        "keywords": "[\"system\", \"mig selv\", \"pkm\", \"personlig\"]",
        "description": "Systemets fundament og mine personlige dokumenter.",
        "subs": [
            {"name": "🗄️ 01 System", "keywords": "[\"index\", \"retningslinjer\", \"pkm\", \"templates\", \"workflows\"]", "description": "Index, retningslinjer for PKM, templates og workflows."},
            {"name": "🗄️ 02 Personlige papirer", "keywords": "[\"cv\", \"pas\", \"kørekort\", \"id\", \"log\"]", "description": "CV, pas, kørekort, ID-dokumenter og personlig log."},
            {"name": "🗄️ 03 Sundhed", "keywords": "[\"lægejournaler\", \"briller\", \"linser\", \"sundhedssikring\", \"træning\"]", "description": "Lægejournaler, briller/linser, sundhedssikring og træning."},
        ]
    },
    {
        "name": "🗄️ 10-19 INTERESSER",
        "parent": "",
        "keywords": "[\"interesser\", \"viden\", \"teknik\", \"hobby\"]",
        "description": "Mine vidensområder og tekniske nørderier.",
        "subs": [
            {"name": "🗄️ 11 AI & PKM", "keywords": "[\"ai\", \"pkm\", \"forskning\", \"llm\", \"obsidian\", \"anytype\"]", "description": "AI-forskning, LLM-værktøjer, Obsidian/Anytype og vidensstyring."},
            {"name": "🗄️ 12 Homelab", "keywords": "[\"homelab\", \"netværk\", \"server\", \"hardware\", \"proxmox\"]", "description": "Netværksdokumentation, server-setup og hardware-lister."},
            {"name": "🗄️ 13 Andre interesser", "keywords": "[\"interesser\", \"projekter\"]", "description": "Plads til nye emner eller kortere projekter."},
        ]
    },
    {
        "name": "🗄️ 20-29 ARBEJDE OG KARRIERE",
        "parent": "",
        "keywords": "[\"arbejde\", \"karriere\", \"professionel\"]",
        "description": "Alt professionelt indhold og karriere-administration.",
        "subs": [
            {"name": "🗄️ 21 Netcompany", "keywords": "[\"netcompany\", \"projekter\", \"kontrakter\", \"tidsregistrering\", \"udlæg\"]", "description": "Projekter, kontrakter, tidsregistrering og arbejdsrelaterede udlæg."},
            {"name": "🗄️ 22 MFeld", "keywords": "[\"mfeld\", \"arkiv\", \"admin\", \"firma\"]", "description": "Arkiv, administrative opgaver og firma-dokumentation."},
            {"name": "🗄️ 23 Tidligere jobs", "keywords": "[\"tidligere jobs\", \"reference\", \"erfaring\"]", "description": "Reference-materiale og erfaring fra tidligere ansættelser."},
            {"name": "🗄️ 24 Karriereudvikling", "keywords": "[\"karriereudvikling\", \"kurser\", \"certificeringer\", \"fagforening\", \"akasse\"]", "description": "Kurser, certificeringer, fagforening og A-kasse."},
        ]
    },
    {
        "name": "🗄️ 30-39 FAMILIE",
        "parent": "",
        "keywords": "[\"familie\", \"relationer\", \"privatliv\", \"opleverser\"]",
        "description": "Relationer, privatlivet og de fælles oplevelser.",
        "subs": [
            {"name": "🗄️ 31 Trine", "keywords": "[\"trine\", \"personlig\", \"fælles\"]", "description": "Personlige dokumenter og fælles projekter."},
            {"name": "🗄️ 32 Børnene", "keywords": "[\"børn\", \"bertil\", \"arthur\", \"kamma\", \"opsparing\", \"skole\", \"lommepenge\"]", "description": "Opsparinger, skole, lommepenge og projekter (f.eks. Kammas kørekort)."},
            {"name": "🗄️ 33 Den brede familie", "keywords": "[\"familie\", \"kontaktinfo\", \"slægtsforskning\", \"mærkedage\"]", "description": "Kontaktinfo, slægtsforskning og store mærkedage (f.eks. Mikkel 50 år)."},
            {"name": "🗄️ 34 Ferier", "keywords": "[\"ferie\", \"rejser\", \"planlægning\", \"billetter\", \"sommerferie\", \"vinterferie\"]", "description": "Planlægning, billetter og minder fra sommerferie, vinterferie og øvrige rejser."},
            {"name": "🗄️ 35 Husholdningsdrift", "keywords": "[\"husholdning\", \"dagligvarer\", \"tøj\", \"kæledyr\", \"forbrug\"]", "description": "Dagligvarer, tøj/sko, kæledyr og diverse privatforbrug."},
        ]
    },
    {
        "name": "🗄️ 40-49 AKTIVER",
        "parent": "",
        "keywords": "[\"aktiver\", \"formue\", \"hus\", \"transport\"]",
        "description": "Hus, sommerhus, transport og den overordnede formuepleje.",
        "subs": [
            {"name": "🗄️ 41 Hus (Hjemmet)", "keywords": "[\"hus\", \"hjem\", \"realkredit\", \"forsikring\", \"forsyning\", \"vedligehold\", \"have\"]", "description": "Realkredit, forsikring, forsyning (el/vand/varme) og vedligehold/have."},
            {"name": "🗄️ 42 Sommerhus", "keywords": "[\"sommerhus\", \"leje\", \"realkredit\", \"drift\", \"istandsættelse\", \"carport\", \"anneks\"]", "description": "Lejeindtægter, realkredit, drift og de store istandsættelsesprojekter (Carport, Anneks)."},
            {"name": "🗄️ 43 Biler & Transport", "keywords": "[\"bil\", \"transport\", \"tesla\", \"passat\", \"lån\", \"forsikring\", \"brændstof\", \"el\"]", "description": "Tesla & Passat (lån, forsikring, afgifter), brændstof/el og øvrig transport (taxi/tog)."},
            {"name": "🗄️ 44 Lån og investeringer", "keywords": "[\"lån\", \"investering\", \"pension\", \"nordnet\", \"frie midler\", \"skat\"]", "description": "Pension, Nordnet, frie midler (reserver), renter og skatteforhold."},
        ]
    }
]

dir_path = "/Users/mikkelfeld/obsidian/brain/2 - Files"
date_str = "2026-02-26 09:10"

for cat in categories:
    parent_name = cat["name"]
    content = template.format(
        date=date_str, 
        parent="", 
        keywords=cat["keywords"], 
        description=cat["description"]
    )
    with open(os.path.join(dir_path, f"{parent_name}.md"), "w") as f:
        f.write(content)
        
    for sub in cat["subs"]:
        sub_name = sub["name"]
        content = template.format(
            date=date_str, 
            parent=f"[\"[[{parent_name}]]\"]", 
            keywords=sub["keywords"], 
            description=sub["description"]
        )
        with open(os.path.join(dir_path, f"{sub_name}.md"), "w") as f:
            f.write(content)

print("Taxonomy files created successfully.")
