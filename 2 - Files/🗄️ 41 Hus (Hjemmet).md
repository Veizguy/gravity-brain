---
created: 2026-02-26 09:10
modified: 2026-02-26 12:44
taxonomy: ["[[🗄️ 40-49 AKTIVER]]"]
type:
  - taksonomi
keywords: ["hus", "hjem", "realkredit", "forsikring", "forsyning", "vedligehold", "have"]
---

## 📝 Beskrivelse

Realkredit, forsikring, forsyning (el/vand/varme) og vedligehold/have.

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
