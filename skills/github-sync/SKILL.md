# GitHub Sync Skill

Denne skill muliggør automatiseret synkronisering af Antigravity opsætningen og vaultens indhold til GitHub. Den er designet til at fungere sammen med Obsidian Sync.

## Koncept
Da Obsidian Sync allerede udveksler fil-indhold mellem Brian og Mac, bruger denne skill `git rebase` for at samle commit-historikken uden at skabe unødvendige merge-commits. Dette resulterer i en ren, lineær og konsolideret changelog.

## Kommandoer
- **Synkroniser**: Kører `agent/scripts/git-sync.py <AgentNavn>`

## Steps i synkronisering
1.  **Stage**: Alle ændringer addes (`git add .`).
2.  **Commit**: Ændringer committes med agentens navn (f.eks. `chore: updates by Brian`).
3.  **Fetch**: Henter nyeste commits fra GitHub.
4.  **Rebase**: Flytter lokale commits til at ligge efter commits fra remote.
5.  **Push**: Pusher den opdaterede historik til GitHub.

## Best Practices
- Kør denne skill efter større ændringer i systemet eller som en del af aften-rutinen.
- Undgå at manuelt rette i `.git` mappen, da Obsidian Sync IKKE synkroniserer denne (og det skal den heller ikke).

## Fejlfinding
Hvis rebasing fejler (merge conflicts), skyldes det sandsynligvis at to agenter har ændret den præcis samme linje før Obsidian Sync nåede at synkronisere den.
I så fald:
1.  Løs konflikten manuelt i Obsidian.
2.  Kør `git rebase --continue` eller `git commit` igen.
