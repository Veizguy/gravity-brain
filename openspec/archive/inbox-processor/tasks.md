# Implementation Tasks: Housekeeping Skill (Agentisk)

## Opgavebeskrivelse
Implementering af Antigravity skill "housekeeping" med agent-baseret intelligent dokument-sortering. Agenten skal selv læse alle filer i `vault/inbox/raw` og vurdere ud fra indhold, om de hører til i `vault/tasks/` eller `vault/daily/`.

## Tasks

- [x] 1. Opret Mappestruktur for Skill.
- [x] 2. Implementér det nye `SKILL.md`.
  - Tilføj systemprompts/instruktioner, der lærer agenten at vurdere indhold og bruge shell-kommandoer til fil-opsætning og omdøbning.
- [ ] 3. Opret Automatisering (Cron). **[FUTURE TODO]**
  - Udskudt: Afventer at Antigravity får ægte CLI support for "headless" skill-kørsel via cronjob.
- [x] 4. Kør og Test.
  - Skill er bygget og klar til interaktiv agent-kørsel.
