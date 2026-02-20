---
name: SDD Workflow
description: Specification-Driven Design workflow regler der gælder for alle projekter.
---

# SDD Workflow Regler

## Opgave-Klassificering

Før du starter, klassificér opgaven:

| Størrelse | Eksempler | SDD Omfang |
|-----------|-----------|------------|
| **Triviel** | Fix typo, svar på spørgsmål, enkelt config-ændring | Kun Specify + Implement |
| **Lille** | Ny feature, stack deployment, vault-reorganisering | Specify + Plan + Implement + Verify |
| **Medium** | Multi-komponent ændring, ny integration, arkitekturændring | Fuld SDD med OpenSpec change proposal |
| **Stor** | Nyt projekt, migration, platform-ændring | Fuld SDD med project.md + architecture.md |

## Agent Attribution Policy

SDD kræver eksplicit angivelse af ansvarlige agenter i planlægnings- og afslutningsfasen.

### Implementation Plan (Planlægning)
Hver sektion eller opgavegruppe i `implementation_plan.md` SKAL angive den **forventede agent**:
```markdown
### [Sektion Navn] [Agent: Arkitekt]
- [ ] Opgave 1
- [ ] Opgave 2
```

### Walkthrough (Afslutning)
Hver sektion i `walkthrough.md` SKAL angive den **faktiske agent** der udførte arbejdet:
```markdown
### [Sektion Navn] [Agent: Udvikler]
| Fil | Ændring |
|-----|---------|
| ... | ... |
```

## OpenSpec Change Proposal Format

For medium+ opgaver, opret `openspec/changes/<feature>/proposal.md`:

```markdown
# Proposal: [Feature Navn]

## Motivation
[Hvilket problem løser dette?]

## Impact Assessment
- **Berørte systemer**: [liste]
- **Risici**: [liste]
- **Estimeret kompleksitet**: Lav / Medium / Høj

## Proposed Changes
[Beskrivelse af ændringer med ADDED/MODIFIED/REMOVED delta specs]

## Acceptance Criteria
- [ ] [Kriterium 1]
- [ ] [Kriterium 2]
```

## Task Dekomponering

Opret `openspec/changes/<feature>/tasks.md`:

```markdown
# Tasks: [Feature Navn]

## Rækkefølge
1. [ ] **[Task titel]** [Agent: Udvikler] — [Kort beskrivelse]
   - Acceptkriterium: [Hvad validerer succces?]
   - Fil(er): [Berørte filer]
2. [ ] **[Task titel]** [Agent: Tester] — ...
```

## Apply & Archive

Når alle tasks er implementeret og verificeret:
1. Opdatér berørte specs i `openspec/specs/`
2. Flyt change folder til `openspec/archive/`
3. Dokumentér hvad der ændrede sig

## Workflow for Obsidian Vaults

Obsidian vaults bruger en letere version:
1. **Research**: Indsaml og validér information (Perplexity, browser)
2. **Organize**: Strukturér i vault med links og tags
3. **Document**: Skriv notes med klar metadata og kontekst
4. **Review**: Verificér noter for korrekthed og komplethed
