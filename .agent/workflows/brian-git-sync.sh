#!/bin/bash
# brian-git-sync.sh
# Dette script tillader Brian (Agent VM) at synkronisere sine egne filændringer 
# fra /home/brian/gravity-brain op til GitHub ved at oprette en ny branch.

REPO_DIR="/home/brian/gravity-brain"

# Tjek om vi er i mappen
if [ ! -d "$REPO_DIR" ]; then
    echo "Fejl: $REPO_DIR findes ikke."
    exit 1
fi

cd "$REPO_DIR" || exit 1

# Er der overhovedet ændringer?
if [ -z "$(git status --porcelain)" ]; then
    echo "Ingen nye ændringer at synkronisere."
    exit 0
fi

# Konfigurer Git if fald det mangler
git config user.name "Brian AI"
git config user.email "brian@ns58.veis.dk"

# Opret ny unik branch
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
BRANCH_NAME="brian-updates-$TIMESTAMP"
echo "Opretter og skifter til branch: $BRANCH_NAME"
git checkout -b "$BRANCH_NAME"

# Tilføj og commit alle ændringer
git add .
COMMIT_MSG="Brian AI Auto-Sync: Opdaterede regler/agenter ($TIMESTAMP)"
git commit -m "$COMMIT_MSG"

# Skub til GitHub
echo "Skubber branch $BRANCH_NAME til GitHub (origin)..."
if git push -u origin "$BRANCH_NAME"; then
    echo "Succes! Dine ændringer er skubbet til GitHub. Bed Mikkel om at godkende din Pull Request for branch '$BRANCH_NAME'."
    
    # Valgfrit: Skift tilbage til main for at undgå at hænge fast i dev branchen
    git checkout main
else
    echo "Fejl under 'git push'. Sikr dig at deploy-nøglen eller authentication fungerer for brian-brugeren."
    # Rydder lidt op ved push fejl
    git reset HEAD~1
    git checkout main
    git branch -D "$BRANCH_NAME"
    exit 1
fi
