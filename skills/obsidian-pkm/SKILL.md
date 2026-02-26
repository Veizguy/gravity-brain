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
- Opret rå noter i `1 - Inbox/`
- Brug templates for konsistent formatering
- Inkludér metadata: `created`, `source`, `tags`

### 3. Process (Bearbejdning)
- Omskriv til egne ord (undgå copy-paste)
- Tilføj kontekst og egne refleksioner
- Klassificér med tags og læg i `2 - Files/`
- Sørg for at opdatere metadata (se nedenfor)

### 4. Connect (Linking)
- Opret `[[wikilinks]]` til relaterede noter
- Byg MOC'er (Maps of Content) for emnegrupper
- Brug backlinks aktivt til at opdage relationer

### 5. Review (Gennemgang)
- Verificér noter for korrekthed
- Opdatér forældede noter
- Ryd op i `1 - Inbox/` regelmæssigt (Inbox Zero)

## Note Metadata

Brug YAML frontmatter i alle noter. For processed noter i `2 - Files/` bør du tilstræbe følgende properties:

```yaml
---
created: 2026-02-18
modified: 2026-02-25
taxonomy: [Emne fra Taksonomi]
type: note # daily-note, note, file, moc
tags:
  - type/research
  - status/processed
---
```

### Standard Tags og Properties

| Property | Formål | Eksempler |
|----------|--------|-----------|
| `created` | Oprettelsesdato | `2026-02-25` |
| `modified` | Sidst ændret | `2026-02-25` |
| `taxonomy` | Emne-kategorisering | `Homelab`, `AI`, `Productivity` |
| `type` | Note-kategori | `daily-note`, `note`, `file`, `moc` |
| `status/` | Bearbejdningsstatus | `status/draft`, `status/processed`, `status/archive` |

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
1. Opret `.openspec/changes/<ændring>/proposal.md`
2. Beskriv hvad der ændres og hvorfor
3. Opret `tasks.md` med konkrete trin
4. Gennemfør ændringer systematisk
5. Arkivér change folder

## Agent Logning (Obligatorisk)

> [!IMPORTANT]
> Entry'et skal beskrive handlingen og opsummere enhver ny viden. 
> 
> **VIGTIGT:** Logning skal ske i tabelformat med en separator-linje for at renderes korrekt. **Nyeste handlinger skal stå øverst i tabellen.**
> Format: `| Tid | Agent | Job | Beskrivelse | Success | Token forbrug |`
> Separator: `| --- | --- | --- | ----------- | ------- | ------------- |`
> 
> **Script-optimering:** Hvis en agent opdager fejl eller uhensigtsmæssigheder i et script, skal dette rettes proaktivt. Ændringen skal logges tydeligt i daily-log, så det er klart hvilken optimering der er foretaget til næste kørsel.
> **Chat-Arkivering:** For at give Bibliotekaren fuld kontekst, SKAL hver agent-session (især komplekse research- eller arkitekturopgaver) afsluttes med at gemme en .md fil i `agent/chats/YYYY-MM-DD-Opgave-Navn.md`. **Hver log entry i daily-log SKAL indeholde et link til denne chat-fil.** Filen skal indeholde de vigtigste dele af samtalen, der førte til beslutninger eller ny viden. **Der SKAL desuden altid inkluderes direkte `[[wikilinks]]` i chat-loggen til de faktiske artefakter (fx KIs, noter eller scripts), som agenten har produceret under sessionen.**
>
> Agenter bør desuden læse relaterede `[[rules/knowledge-items/KI-000-Index|Rule-KIs]]` før løsning af opgaven for at kalibrere sig selv.

## Best Practices

1. **Skriv for dit fremtidige jeg** — Kontekst der er oplagt nu, er glemt om 6 måneder
2. **Én idé per note** — Atomare noter er lettere at linke og genbruge
3. **Link aggressivt** — Jo flere links, jo mere værdi skaber netværket
4. **Undgå perfektionisme** — En ufuldstændig note er bedre end ingen note
5. **Inbox zero** — Bearbejd inbox regelmæssigt, arkivér eller slet
