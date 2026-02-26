---
created: 2026-02-26 09:10
modified: 2026-02-26 09:10
taxonomy: ["[[🗄️ 00-09 SYSTEM OG MIG SELV]]"]
type:
  - taksonomi
keywords: ["cv", "pas", "kørekort", "id", "log"]
---
## 📝 Beskrivelse

CV, pas, kørekort, ID-dokumenter og personlig log.

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
