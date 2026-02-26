---
created: 2026-02-26 09:10
modified: 2026-02-26 09:10
taxonomy: 
type:
  - taksonomi
keywords: ["interesser", "viden", "teknik", "hobby"]
---
## 📝 Beskrivelse

Mine vidensområder og tekniske nørderier.

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
