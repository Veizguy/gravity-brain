---
created: 2026-02-26 09:10
modified: 2026-02-26 09:10
taxonomy: ["[[🗄️ 40-49 AKTIVER]]"]
type:
  - taksonomi
keywords: ["lån", "investering", "pension", "nordnet", "frie midler", "skat"]
---
## 📝 Beskrivelse

Pension, Nordnet, frie midler (reserver), renter og skatteforhold.

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
