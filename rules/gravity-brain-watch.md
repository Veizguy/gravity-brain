---
name: Brian Watch Mode
description: Instruerer Brian i hvordan de rå Telegram filer i Inboxen læses og behandles statelessly (uden historik).
---

# Brian Watch Mode (Stateless)

Når brugeren (på Agent-VM eller via en prompt) beder dig om at "Tjek inboxen", "Watch telegram", eller når en `/wake` trigger ("ACTION: WAKE_SYSTEM...") opfanges, anvend disse steps.

Derudover fungerer dette regelsæt som din centrale **Overvågning af faste kørsler**.

## Faste Kørsler (Tidsstyret)
- **Daglige kørsler (kl. 07, 12, 15, 18, 21)**: Du skal automatisk aktivere og køre [[workflows/reception]] workflowet for at rydde op i indbakken.
- **Natlig kørsel (kl. 23:30)**: Du skal aktivere **BÅDE** [[skills/taxonomy-moc/SKILL|Librarian Taxonomy MoC]] skill'en for at vedligeholde taksonomier og MoCs, **OG** [[skills/pkm-bibliotek/ki-ekstraktion/SKILL|KI-Ekstraktion]] skill'en for at destillere dagens viden (fra log og chats) til Knowledge Items.
- **Logning**: Hver kørsel SKAL logges i dagens [[daily-logs/]] som en række i tabellen under `## Antigravity log`. Herunder skal eventuelle script-optimeringer eller fejlretninger fremgå tydeligt.

## The Telegram / Brian Loop (Stateless Mode)

> [!IMPORTANT]
> **Stateless Processing**: Du skal IKKE indlæse eller gemme chathistorik for disse beskeder. Hver kørsel er uafhængig for at spare tokens. Indbakken est blot et dump af filer, der skal behandles én efter én.

1.  **LÆS NYE FILER:** Scan `/home/brian/brain/vault/inbox/raw/files` and `/home/brian/brain/vault/inbox/raw/audio`.
2.  **BEHANDL ÉN AD GANGEN:** Læs JSON payload for hver fil. Ignorer tidligere beskeder eller kontekst.
3.  **FORSTÅ PAYLOADS:** Læs JSON payload. Reelle beskeder har værdier i `"text"` feltet fra "telegram".
    *   *Ad-hoc Wakelocks:* Hvis du ser teksten "ACTION: WAKE_SYSTEM...", slet filen med det samme og stop.
4.  **REPLY TIL BRUGEREN:** Når opgaven er løst, skriv et slutsvar til brugeren i `/home/brian/brain/vault/outbox/raw/` som en simpel tekstfil.
5.  **CLEANUP (VIGTIGT):** Flyt straks den behandlede JSON til `/home/brian/brain/vault/inbox/processed/archive/json/` eller slet den. Lad aldrig filer blive liggende i raw-mappen.
6.  **LOGGING:** Afslut opgaven med at tilføje en detaljeret logning under `## Antigravity log` i `daily-logs/YYYY-MM-DD.md` om hvad der blev gjort. **Nyeste handlinger skal stå øverst i tabellen.**
    *   Format: `| Tid | Agent | Job | Beskrivelse | Success | Token forbrug |`
    *   Separator: `| --- | --- | --- | ----------- | ------- | ------------- |`

## Personlighed og Tone
Da dine svar sendes tilbage som private chatbeskeder:
- Læs regelsættet i **[[rules/knowledge-items/KI-001-Skrivestil-og-Tone]]**.
- Modificér evt. din tone baseret på hvad den KI skriver.
