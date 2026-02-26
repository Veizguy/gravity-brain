---
name: pkm-reception-telegram-chat
description: "Håndterer tovejs-chat via en dedikeret Telegram bot. Modtager beskeder i inbox/chat-in og sender svar fra outbox/chat-out."
---

# Telegram Chat (Reception Sub-agent)

Denne skill muliggør interaktiv tovejs-kommunikation med Brian via Telegram. 

## Mappe-struktur
- `1 - Inbox/`: Her lander alle indkommende beskeder (JSON) og filer fra Telegram.
- `outbox/chat-out/raw/`: Her skal Brian lægge sine svar (f.eks. `.txt` eller `.json`).
- `outbox/chat-out/processed/`: Arkiv over afsendte beskeder.

## Bridge Script
Selve logikken mod Telegram kører via `scripts/telegram_chat_bridge.py`. Dette script skal køre som en service på Brian-VM.

## Arbejdsgang
1. **Modtagelse**: Beskeder fra Telegram gemmes som JSON i `inbox/chat-in/`.
2. **Behandling**: Brian (eller en anden agent) læser filerne, formulerer et svar, og lægger det i `outbox/chat-out/raw/`.
3. **Afsendelse**: Bridge-scriptet opdager filen, sender den til brugerens Telegram-chat, og flytter filen til `processed/`.
