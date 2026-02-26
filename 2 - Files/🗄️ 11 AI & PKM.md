---
created: 2026-02-26 09:10
modified: 2026-02-26 09:10
taxonomy: ["[[🗄️ 10-19 INTERESSER]]"]
type:
  - taksonomi
keywords: ["ai", "pkm", "forskning", "llm", "obsidian", "anytype"]
---
## 📝 Beskrivelse

AI-forskning, LLM-værktøjer, Obsidian/Anytype og vidensstyring.

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
