---
name: "Housekeeping"
description: "Læser, vurderer og sorterer automatisk filer i indbakken (vault/inbox/raw). Opgaver flyttes til 'tasks/', noter flyttes til 'daily/'."
---

# Housekeeping Skill

Denne skill bruges til intelligent at sortere noter og opgaver i dit Obsidian vault. Du (agenten) skal læse indholdet og bruge din dømmekraft til at bestemme destinationen.

## Instruktioner til Agent

Når du bliver bedt om at fuldføre Housekeeping-opgaven, skal du gøre følgende eksakt:

1.  **Find Filer:**
    - Identificer den absolutte sti til `vault/inbox/raw` (det kan være `~/vault/inbox/raw` eller et andet sted, alt efter setup).
    - List alle `.md` filer i denne mappe.

2.  **Læs og Vurder:**
    - Læs indholdet af hver fil én ad gangen.
    - Brug din interne analyse og vurder: Er dette en **opgave** (Task) eller en **note** (Daily Log)?
        - *Opgave:* Beskriver en handling, en to-do liste, indeholder checkboxe (`- [ ]`), præfikset `_t `, refererer til noget der *skal gøres* eller løses.
        - *Note:* Mødereferat, dagbogsnotat, generel information, tanker, links, idéer der ikke eksplicit er tasks.

3.  **Flyt Filerne:**
    - Opret destinationsmapperne `vault/tasks/` og `vault/daily/` hvis de ikke eksisterer.
    - Brug `mv` eller Python internt for at flytte hver fil:
        - **Opgaver** flyttes til `vault/tasks/`.
        - **Noter** flyttes til `vault/daily/`.
    - *Vigtigt:* Før du flytter en fil, tjek om filnavnet allerede findes i destinationen. Er det tilfældet, omdøb filen automatisk (f.eks. tilføj et `_1` suffix) så du ikke overskriver eksisterende data.

4.  **Rapportér:**
    - Afslut opgaven med en kort, præcis status på hvor mange filer du læste, og hvilke der blev vurderet som hhv. opgaver og noter.
