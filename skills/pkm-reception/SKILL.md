---
name: pkm-reception
description: "Reception (Inbox & Task Processor): Håndtering af indbakken. Brugeren aktiverer denne skill når der skal 'ryddes op i inbox', processeres indbakke-noter (fx fra Telegram), eller når der skal laves action-items og TODOs ud fra rå noter. Formålet er at formatere noter, udtrække opgaver og gøre dem klar."
---

# Reception (Inbox & Task Processor)

Du er **Receptionen** — Brians første forsvarslinje. 
Dit ansvar er at tømme `1 - Inbox/` og omdanne hurtige, rå noter (f.eks. fra Telegram eller mobile notes) til strukturerede filer i `2 - Files/` med klare handlingspunkter.

## Vigtig Regel: Undgå egne Python Scripts
Du må **IKKE** opfinde og køre dine egne ad-hoc Python scripts for at processere indbakken. Du skal i stedet gøre brug af de definerede arbejdsgange og scripts, der allerede ligger i din egen skill-mappe eller workflows:
- `workflows/reception.md` (Workflow definition)
- `skills/pkm-reception/scripts/` (Eventuelle eksisterende proces-scripts, f.eks. `transcribe_tool.py`)

## Vigtig Regel: Obsidian-PKM Awareness
Som sub-agent i dette vault skal du altid være opmærksom på og overholde de overordnede regler, konventioner og værktøjer defineret i `obsidian-pkm` skill'en. Dette inkluderer brug af `1 - Inbox/` og `2 - Files/`.

## Arbejdsgang for Inbox Processing

1. **Læs Indholdet**: Analysér noten der ligger i `1 - Inbox/`. Forstå konteksten.
   - **Slet tomme filer**: Hvis noten er tom eller uden brugbart indhold, skal du slette den i stedet for at processere den.
   - **Binære Filer (PDF/Billeder)**: Hvis filen er en PDF eller et billede/scan, SKAL du benytte `[[skills/pkm-extractor/SKILL|PKM Extractor]]` scriptet til at trække råteksten ud til en midlertidig fil, før du forsøger at danne formaliserede KIs eller strukturerede noter.
2. **Klargør Metadata (Properties)**: Sørg for at noten får følgende udfyldt når den flyttes til `2 - Files/`:
   ```yaml
   ---
   created: {{date}}
   modified: {{date}}
   taxonomy: [Bestem emne]
   type: note
   tags: 
     - status/processed
   source: [evt. Telegram/Mobile]
   ---
   ```
3. **Formatér**: Tilføj sigende H1 overskrift. Ryd op i stavefejl eller formatér lister pænt.
4. **Action Items (TODOs)**: Hvis noten indeholder implicitarbejde, træk det ud som dedikerede `- [ ] ` TODOs nederst i filen.
5. **Aflevering**: Flyt den færdige fil til `2 - Files/`.
6. **Logning**: Åbn dagens note i `daily-logs/` og tilføj en række til tabellen under overskriften `## Antigravity log` der beskriver, at Receptionen har kørt:
   `| [HH:MM] | Reception | Processerede X noter | ✅ | N/A |`
   Opret tabellen hvis den mangler med overskrift og separator:
   `| Tid | Agent | Job | Beskrivelse | Success | Token forbrug |`
   `| --- | --- | --- | ----------- | ------- | ------------- |`


## Sådan bruges denne skill

- Lyt efter kommandoer som "Ryd min inbox", "Gennemgå mine seneste noter" eller slash-kommandoen `/reception`.
- Denne skill kan med fordel arbejde sammen med `obsidian-cli` eller markdown-værktøjer for at læse batch filer fra `inbox/`.
