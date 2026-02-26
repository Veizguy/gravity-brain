# Access Guide for Brian

Denne guide beskriver hvordan man får adgang til Brian-miljøet.

## Web Interface (Agent Desktop)

- **URL**: [https://agent-desktop.veis.dk](https://agent-desktop.veis.dk)
- **Bruger**: `mikkel`
- **Beskrivelse**: Dette er den primære web-baserede interface til Brians desktop-miljø.

## SSH Adgang

Agenter kan bruge SSH til at udrulle scripts eller tjekke status direkte på VM'en.

### SSH Targets
- **Tailscale (Anbefalet)**: `vm-p-agent-01.elk-eel.ts.net`
- **Internal VPN**: `agent-desktop.veis.dk`
- **Internal IP**: `10.0.40.101`

### Brug af hjælper-script
Der findes et script i `scripts/brian_ssh.sh` som kan bruges til hurtig adgang:
```bash
# Standard (Tailscale)
./scripts/brian_ssh.sh

# Specifik IP
./scripts/brian_ssh.sh ip
```

## Systemdetaljer
- **OS**: Linux (Ubuntu-baseret)
- **Rolle**: Agent Desktop VM (Brian)
