---
name: "Housekeeping"
description: "Læser, vurderer og sorterer automatisk filer i indbakken (vault/inbox/raw). Opgaver flyttes til 'tasks/', noter flyttes til 'daily/'. KØRES KUN ON-DEMAND."
---

> [!IMPORTANT]
> **SUPERSEDED**: Denne skill er ved at blive erstattet af workflowet `/process-inbox.md`. Brug venligst workflowet i stedet for denne skill direkte for at sikre den nyeste logik.

# Housekeeping Skill (On-Demand Only)

Denne skill bruges til intelligent at sortere noter og opgaver i dit Obsidian vault. Du (agenten) skal læse indholdet og bruge din dømmekraft til at bestemme destinationen.

> [!NOTE]
> Denne skill skal kun køres når brugeren eksplicit anmoder om det. Baggrunds-automatisering er deaktiveret for at spare tokens.

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

4.  **Rapportér & Log:**
    - Afslut opgaven med en kort, præcis status på hvor mange filer du læste.
    - **Log til Daily Log:** Find dagens log og tilføj en række til `# Antigravity log`:
        - **Job**: `Housekeeping`
        - **Beskrivelse**: `Sorterede X filer til tasks/ og daily/`.
        - **Success**: `Ja`.
        - **Token forbrug**: Estimat (f.eks. `~1.500 tokens`).
