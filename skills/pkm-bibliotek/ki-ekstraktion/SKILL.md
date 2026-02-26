---
name: KI-Ekstraktion
description: Bibliotekarens aftenvagt til at udvinde og formalisere Tacit Knowledge (KI's) fra logfiler og chats.
---

# KI-Ekstraktion (Aftenvagt)

## Formål
At sikre, at systemet lærer over tid. Denne skill køres af Bibliotekaren for at gennemgå dagens opsamlede logs og chats, destillere værdifuld underforstået viden (Tacit Knowledge), og persistére det i Knowledge Items (KI) strukturen.

## Trigger
- **Tidspunkt:** Kører automatisk hver aften kl. 23:30 sammen med andre vedligeholdelsesopgaver (jf. `[[rules/gravity-brain-watch]]`).

## Workflow (Execution Steps)

1. **Læs Dagens Log:**
   - Åbn filen `3 - Daily logs/YYYY-MM-DD.md` for dags dato.
   - Gennemlæs alle log-entries under `## Antigravity log`.
2. **Læs Chat-Historik:**
   - Gennemgå mapper med dagens direkte interaktioner, herunder **`agent/chats/`** for fulde sessioner, Telegram chat-logs i `inbox/processed/archive/json/` eller andre steder, hvor systemet deponerer chathistorik.
   - Fokusér på prompt-rettelser, konklusioner på diskussioner, nye facts, eller fejl agenten har lavet og som brugeren har rettet.
3. **Identificer Tacit Knowledge:**
   - Findes der viden her, som er vigtig for fremtiden, og som ikke allerede eksisterer i systemet?
   - Kategorisér viden i:
     - **Regler/Adfærd:** Instruktioner til agent-adfærd, tone-of-voice, skabeloner (Rule-KI).
     - **Fakta:** Konkrete data, beskrivelser af personer/systemer, teori (Factual-KI).
4. **Opret / Opdater Knowledge Items (KI):**
   - For **Rule-KIs:** Opret eller opdater MD-filen i `rules/knowledge-items/` (f.eks. `KI-002-...`). Følg formatet beskrevet i `[[rules/knowledge-items/KI-000-Index]]`.
   - For **Factual-KIs:** Opret en ny flad MD-fil direkte i `2 - Files/`.
     - Filen *skal* indeholde YAML frontmatter med `type: Knowledge Item` og relevant `taxonomy: [emne]`.
     - Indholdet skrives formelt, genbrugeligt og struktureret (helst undgå the "jeg" / agent format i selve filen).
5. **Afslut:**
   - Logfør evt. oprettede Knowledge Items i dagens log, så brugeren kan se, at "systemet blev klogere i løbet af natten".
