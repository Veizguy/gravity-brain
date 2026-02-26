---
created: 2026-02-26 09:10
modified: 2026-02-26 09:10
taxonomy: ["[[🗄️ 00-09 SYSTEM OG MIG SELV]]"]
type:
  - taksonomi
keywords: ["lægejournaler", "briller", "linser", "sundhedssikring", "træning"]
---
## 📝 Beskrivelse

Lægejournaler, briller/linser, sundhedssikring og træning.

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
