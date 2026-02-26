---
created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
modified: <% tp.file.last_modified_date("YYYY-MM-DD HH:mm") %>
taxonomy: 
type:
  - record
keywords: 
---
## 📝 Beskrivelse

(En kort beskrivelse af recorden)

## 📄 Items (Noter, Filer og KIs)

```base
filters:
  and:
    - taxonomy == this.file
    - not:
        type.contains("record")
    - not:
        type.contains("taksonomi")
views:
  - type: table
    name: Items knyttet til denne Record
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
