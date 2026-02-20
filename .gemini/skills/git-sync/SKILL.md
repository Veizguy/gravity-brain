---
name: Brian Git Sync
description: Lader dig (Brian) uploade og synkronisere de ændringer du har lavet i dine egne filer (.gemini, skills etc.) til dit GitHub repository.
---

# Brian Git Sync

## Formål
Når din bruger beder dig om at "opdatere dine egne regler", "lave et nyt flow", eller "skrive dine egne filer", foretager du ændringerne lokalt på Agent VM'en i dit `/home/brian/gravity-brain` workspace.
For at holde disse ændringer sikre, skal de "skubbes" op til GitHub, så brugeren kan godkende dem. 
Du må ALDRIG forsøge at pushe direkte til `main` eller `master` branchen. Du skal bruge dette specifikke sync-script.

## Hvordan du bruger the Sync Command

Når du har ændret eller oprettet de nødvendige filer i dit workspace (og valideret at de fungerer), skal du eksekvere følgende bash kommando i din Agent-terminal:

```bash
bash /home/brian/gravity-brain/.agent/workflows/brian-git-sync.sh
```

### Scriptets opførsel
Dette script tager automatisk alle dine lokale ændringer (`git add .`), opretter en helt ny branch med et tidsstempel, og skubber denne nye branch op til repository'et (GitHub).
Til sidst skifter scriptet dig automatisk tilbage til `main` branchen.

## Når scriptet er færdigt
Hvis scriptet rapporterer "Succes!", skal du stoppe arbejdet og informere brugeren (via Telegram eller i chatten) med en besked á la:
*"Jeg har gemt mine ændringer! De ligger nu i GitHub. Du kan oprette og godkende min Pull Request for branchen `brian-updates-...` inde i dit gravity-brain repository, og derefter trække dem ned på din Mac."*
