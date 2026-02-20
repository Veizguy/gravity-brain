# Change Proposal: Housekeeping Skill for Antigravity

## Baggrund & Motivation
Brugeren ønsker at automatisere vedligeholdelse ("housekeeping") af deres inbox i Obsidian vaulten. Systemet skal løbende behandle nye filer i mappen `vault/inbox/raw` og sortere dem korrekt baseret på deres indhold.

For at gøre løsningen elegant og drage nytte af LLM-kapabiliteter, skal Antigravity-agenten selv læse filernes indhold og ud fra kontekst vurdere, om en fil er en "Opgave" eller en "Note", frem for at forlade sig på hardcodede regler som et præfiks.

## Kriterier for Sortering
Når agenten aktiveres for at udføre Housekeeping, skal den:
1. Skimtes alle markdown filer (`.md`) i mappen `vault/inbox/raw`.
2. Læse og analysere indholdet af hver enkelt fil.
3. Bruge sin dømmekraft til at skelne mellem:
   - **Opgave (Task):** Noter, der beskriver handlinger, todos eller forpligtelser (f.eks. "Husk at købe ind", "Ring til X", indeholder checkbokse `- [ ]`, eller starter eksplicit med `_t `). Disse flyttes til mappen `vault/tasks/`.
   - **Note (Daily Log):** Generel information, logbog-notater, tanker, referater o.l., som ikke er handlingsorienterede. Disse flyttes til mappen `vault/daily/`.

## Aktuel Tilstand
Filer samles op i `vault/inbox/raw` og en tidligere teknisk plan foreslog et fastlåst Python script. Dette er nu forkastet til fordel for en fuld agent-styret løsning.

## Forslag til Løsning
Vi opretter/opdaterer Antigravity skillen **"housekeeping"**.
Denne skill vil bestå af et enkelt `SKILL.md` dokument med klare, pædagogiske instruktioner til, hvordan Antigravity agenten:
- Finder filerne frem.
- Vurderer dem én for én.
- Bruger terminal-kommandoer (som `mv` via sine agent-tools) til at flytte filerne og håndtere evt. navnekonflikter.

Derudover udskiftes cronjob-scriptet (`setup_cron.sh`), så det automatisk kalder Antigravity's CLI til at køre "housekeeping" målet hver time i 'headless' mode (uden brugerinteraktion).

## Impact & Risici
- **Tokenforbrug & Tid:** Da agenten skal aktiveres en gang i timen, indlæse filerne og foretage vurderinger, kræver dette opkald til LLM-API'et. Dette er et forventet og bevidst trade-off for en smartere, mere kapabel model.
- **Konteksthåndtering:** Agenten skal huske at den kører i baggrunden, så den skal blot udføre opgaven, bekræfte filerne er flyttet, og stoppe - uden at afvente bruger-svar midt i processen.

## Næste Skridt (Klar til Implementering)
- Opdatere `SKILL.md` til at spejle den rent prompt-baserede tilgang.
- Slette det forældede Python script.
- Opdatere det planlagte bash-trigger script, så det starter Agenten.
