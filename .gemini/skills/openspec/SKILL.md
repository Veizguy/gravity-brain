---
name: OpenSpec Framework
description: Specification-Driven Design framework med OpenSpec mappestruktur, spec-skrivning, change proposals og delta specs.
---

# OpenSpec Framework Skill

## Hvad er OpenSpec?

OpenSpec er et Git-native, Markdown-baseret framework for Specification-Driven Design. Det isolerer system-tilstand (specs/) fra foreslåede ændringer (changes/) og bruger en Propose → Apply → Archive workflow.

## Kerneprincipper

1. **Specs er source of truth** — `openspec/specs/` beskriver altid den nuværende tilstand
2. **Ændringer er isolerede** — Forslag lever i `openspec/changes/<feature>/` indtil godkendt
3. **Delta specs** — Beskriv ændringer som `ADDED`, `MODIFIED`, eller `REMOVED`
4. **Load-on-demand** — Kun relevante specs indlæses for en given opgave
5. **Arkivering** — Gennemførte ændringer flyttes til `openspec/archive/`

## Mappestruktur

Se templates for projekttype-specifikke strukturer:
- `templates/git-repo-structure.md` — For Git-baserede projekter
- `templates/obsidian-vault-structure.md` — For Obsidian vaults

## Spec-Skrivning

### project.md (Projekt-konstitution)

```markdown
# [Projekt Navn]

## Formål
[Kort beskrivelse af projektets raison d'être]

## Scope
- **In-scope**: [hvad projektet dækker]
- **Out-of-scope**: [hvad det IKKE dækker]

## Principper
- [Princip 1]
- [Princip 2]

## Tech Stack
| Komponent | Teknologi | Version |
|-----------|-----------|---------|
| [komponent] | [tech] | [version] |

## Boundaries
### ✅ Always
- [regel]

### ⏸️ Ask First
- [regel]

### ❌ Never
- [regel]
```

### architecture.md (System-design)

```markdown
# Arkitektur: [Projekt Navn]

## Overblik
[Mermaid C4-diagram eller flowchart]

## Komponenter
| Komponent | Ansvar | Afhængigheder |
|-----------|--------|---------------|
| [komp] | [ansvar] | [deps] |

## Dataflow
[Mermaid sequence-diagram]

## Deployments
[Deployment-strategi og miljøer]
```

### Feature Specs

```markdown
# Feature: [Navn]

## Beskrivelse
[Hvad featuren gør]

## Krav
### Funktionelle
- FR-001: [krav]
  - Acceptkriterium: [Gherkin format]

### Non-funktionelle
- NFR-001: [krav]

## Afhængigheder
- [afhængighed]
```

## Change Proposal Workflow

### 1. Opret change folder

```bash
mkdir -p openspec/changes/<feature-name>/deltas
```

### 2. Skriv proposal.md

```markdown
# Proposal: [Feature Navn]

## Motivation
[Hvilket problem løser dette?]

## Impact Assessment
- **Berørte specs**: [liste over specs der ændres]
- **Nye specs**: [liste over nye specs]
- **Risici**: [identificerede risici]

## Proposed Changes
[Overordnet beskrivelse]

## Acceptance Criteria
- [ ] [kriterium]
```

### 3. Opret delta specs (i `deltas/`)

```markdown
<!-- Status: ADDED | MODIFIED | REMOVED -->
<!-- Target: openspec/specs/features/new-feature.md -->

# ADDED: new-feature.md

[Indhold af den nye spec]
```

### 4. Dekomponér til tasks.md

```markdown
# Tasks: [Feature Navn]

Baseret på: proposal.md
Status: IN PROGRESS | COMPLETE

## Opgaver
1. [ ] **[Titel]** [Agent: AgentNavn] — [Beskrivelse]
   - Acceptkriterium: [hvad der validerer success]
   - Berørte filer: [liste]
2. [ ] **[Titel]** [Agent: AgentNavn] — ...
```

### 5. Apply (efter implementering)
1. Kopiér/merge delta specs ind i `openspec/specs/`
2. Flyt hele change folderen til `openspec/archive/<dato>-<feature>/`
3. Opdatér evt. `project.md` eller `architecture.md`

## Tre-Tier Boundary System

Brug disse markører i specs:

| Markør | Betydning | Eksempel |
|--------|-----------|---------|
| ✅ Always | Agent gør dette uden at spørge | "Altid brug VirtIO-FS paths" |
| ⏸️ Ask First | Agent spørger før handling | "Spørg før production deployment" |
| ❌ Never | Agent må aldrig gøre dette | "Aldrig hardcode credentials" |

## Best Practices

1. **Hold specs fokuserede** — Én spec per feature/komponent
2. **Undgå overspecificering** — Specs skal guide, ikke diktere
3. **Versionér med Git** — Specs er code, behandl dem som code
4. **Referér, duplikér ikke** — Link til andre specs i stedet for at kopiere
5. **Opdatér specs med koden** — Specs der drifter fra virkeligheden er værdiløse
