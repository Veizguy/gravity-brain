---
name: access-brian
description: "Giver agenter adgang til Brian VM via SSH eller web interface (agent-desktop.veis.dk). Brug denne skill når du skal: (1) Tilgå Brians desktop miljø, (2) Udføre kommandoer via SSH på VM'en, (3) Tjekke forbindelsesdetaljer for Brian."
---

# Access Brian Skill

Denne skill gør det muligt for agenter at interagere direkte med den underliggende infrastruktur for Brian (Agent VM).

## Triggere

Aktiveres når:
- Brugeren beder om at "tilgå brian", "ssh til brian" eller "åbne agent-desktop".
- Der er behov for at udrulle filer til VM'en.
- Der skal tjekkes status på processer kørende på Brian.

## SSH Adgang

Brug hjælper-scriptet:
`scripts/brian_ssh.sh [tailscale|vpn|ip|<custom-host>]`

Standard target er `tailscale` (`vm-p-agent-01.elk-eel.ts.net`).

## Web Interface

- **URL**: [https://agent-desktop.veis.dk](https://agent-desktop.veis.dk)
- **Login**: `mikkel`

## Ressourcer

- [[references/access_guide|Access Guide]] - Detaljeret oversigt over forbindelsesmuligheder.
- `scripts/brian_ssh.sh` - SSH hjælper.
