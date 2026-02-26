# Chat Log: Knowledge Items Setup & Arkitektur

**Dato:** 2026-02-26
**Agent:** Antigravity (Mac Workstation)
**Emne:** Etablering af 'Tacit Knowledge' loop via Knowledge Items (KI)

## Resumé af beslutninger
1.  **Struktur:** Vi har opdelt hukommelsen i `Rule-KIs` (regler/adfærd i `rules/knowledge-items/`) og `Factual-KIs` (fakta i flad struktur i `2 - Files/`).
2.  **Identifikation:** Factual KIs identificeres via property `type: Knowledge Item`.
3.  **Log-Loop:** Alle agenter tvinges til at logge detaljeret i `3 - Daily logs/YYYY-MM-DD.md`.
4.  **Chat Arkiv:** Alle samtaler gemmes fremover i `agent/chats/` som MD-filer for at give Bibliotekaren fuld kontekst.
5.  **Bibliotekarens Rolle:** Bibliotekaren kører hver aften kl 23:30, gennemser dagens logs og chats, og opretter/opdaterer automatisk KIs baseret på denne "Tacit Knowledge".

## Diskuterede emner i denne session
*   Analyse af "Syntese af agentisk PKM" rapporten.
*   Synkronisering mellem Mac (Antigravity) og Brian-VM (Stateless).
*   Vigtigheden af at gemme hele chat-historikken for at undgå videnstab.

## Handlinger udført
*   Oprettelse af mapper: `rules/knowledge-items/`, `skills/pkm-bibliotek/ki-ekstraktion/`, `agent/chats/`.
*   Oprettelse af Index (`KI-000`) og Tone/Skrivestil (`KI-001`).
*   Opdatering af `obsidian-pkm` skill, `gravity-brain-watch` regel og `Agenter_og_Skills.md`.
*   Konfiguration af Bibliotekarens nye `ki-ekstraktion` skill.
