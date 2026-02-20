---
name: Obsidian PKM
description: Obsidian vault management, videnorganisering, note-linking og research workflows.
---

# Obsidian PKM Skill

## Formål

Denne skill guider arbejde i Obsidian vaults — fra research og kilde-kuration til note-organisering og videnstrukturer.

## Vault-Detektion

Når workspace indeholder `.obsidian/`, aktivér denne skill automatisk.

## Kerneworkflow

```
Research → Capture → Process → Connect → Review
```

### 1. Research (Indsamling)
- Brug Perplexity MCP til bred emne-mapping
- Brug browser til at læse og validere kilder
- Dokumentér kilder med URL, dato og relevans-score

### 2. Capture (Fangst)
- Opret rå noter i `00-Inbox/`
- Brug templates for konsistent formatering
- Inkludér metadata: `created`, `source`, `tags`

### 3. Process (Bearbejdning)
- Omskriv til egne ord (undgå copy-paste)
- Tilføj kontekst og egne refleksioner
- Klassificér med tags og læg i korrekt folder

### 4. Connect (Linking)
- Opret `[[wikilinks]]` til relaterede noter
- Byg MOC'er (Maps of Content) for emnegrupper
- Brug backlinks aktivt til at opdage relationer

### 5. Review (Gennemgang)
- Verificér noter for korrekthed
- Opdatér forældede noter
- Ryd op i `00-Inbox/` regelmæssigt

## Note Metadata

Brug YAML frontmatter i alle noter:

```yaml
---
created: 2026-02-18
tags:
  - type/research
  - area/homelab
  - status/draft
source: https://example.com
---
```

### Standard Tags

| Prefix | Formål | Eksempler |
|--------|--------|-----------|
| `type/` | Note-type | `type/research`, `type/guide`, `type/log` |
| `area/` | Ansvarsområde | `area/homelab`, `area/career` |
| `status/` | Bearbejdningsstatus | `status/draft`, `status/reviewed`, `status/archive` |
| `project/` | Projekt-tilknytning | `project/ns58`, `project/sdd` |

## Templates

### Research Note

```markdown
---
created: {{date}}
tags:
  - type/research
  - status/draft
source: [URL]
---

# [Emne]

## Resumé
[Kort opsummering i egne ord]

## Nøglepunkter
- [punkt 1]
- [punkt 2]

## Egne Refleksioner
[Hvordan relaterer dette til eksisterende viden?]

## Relaterede Noter
- [[relateret-note-1]]
- [[relateret-note-2]]
```

### Projekt Note

```markdown
---
created: {{date}}
tags:
  - type/project
  - status/active
---

# [Projekt Navn]

## Mål
[Hvad vil du opnå?]

## Status
- [ ] [opgave 1]
- [ ] [opgave 2]

## Noter
- [[relateret-research]]

## Log
### {{date}}
- [hvad skete der i dag?]
```

## OpenSpec Integration

For større vault-ændringer (reorganisering, ny struktur, migration):
1. Opret `openspec/changes/<ændring>/proposal.md`
2. Beskriv hvad der ændres og hvorfor
3. Opret `tasks.md` med konkrete trin
4. Gennemfør ændringer systematisk
5. Arkivér change folder

## Best Practices

1. **Skriv for dit fremtidige jeg** — Kontekst der er oplagt nu, er glemt om 6 måneder
2. **Én idé per note** — Atomare noter er lettere at linke og genbruge
3. **Link aggressivt** — Jo flere links, jo mere værdi skaber netværket
4. **Undgå perfektionisme** — En ufuldstændig note er bedre end ingen note
5. **Inbox zero** — Bearbejd inbox regelmæssigt, arkivér eller slet
