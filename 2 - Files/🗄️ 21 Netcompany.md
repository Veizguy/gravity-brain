---
created: 2026-02-26 09:10
modified: 2026-02-26 09:10
taxonomy: ["[[🗄️ 20-29 ARBEJDE OG KARRIERE]]"]
type:
  - taksonomi
keywords: ["netcompany", "projekter", "kontrakter", "tidsregistrering", "udlæg"]
---
## 📝 Beskrivelse

Projekter, kontrakter, tidsregistrering og arbejdsrelaterede udlæg.

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
