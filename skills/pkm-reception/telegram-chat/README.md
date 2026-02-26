# Setup & Drift af Telegram Chat Bridge

Dette script skal køre på den maskine, der har adgang til din Obsidian vault (f.eks. din Brian-VM).

## System Dependencies (Linux/VM)

Hvis `pip3` eller `venv` mangler på din VM, skal de installeres først:
```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```

## Installation

1. Gå til mappen:
   `cd skills/pkm-reception/telegram-chat/`

2. Opret virtuelt miljø (valgfrit men anbefalet):
   `python3 -m venv venv`
   `source venv/bin/activate`

3. Installer afhængigheder:
   `pip install -r requirements.txt`

4. Konfigurer miljø-variabler:
   - Kopier `.env.example` til `.env`
   - Indsæt din **nye** bot token og dit chat ID.
   - Indstil `VAULT_PATH` til den absolutte sti på VM'en (f.eks. `/home/brian/brain/vault`).

## Start scriptet

Du kan starte scriptet manuelt med:
`python3 scripts/telegram_chat_bridge.py`

Det anbefales at køre det som en system-service (systemd) eller via `pm2` / `screen` for at sikre at det altid kører.

## Forbindelse til Reception
Dette script dumper JSON filer i `inbox/chat-in/`. Du skal sikre dig at dit `reception` workflow (eller Agent Brian) overvåger denne mappe for at besvare beskederne.
