#!/bin/bash
# Cronjob setup for Brian (Agent VM)
# Dette script opsætter den daglige kørsel af /reception kl 21:00.

COMMAND="cd /home/brian/brain/vault && antigravity run reception"
CRON_ENTRY="0 6,9,12,15,18,21 * * * $COMMAND >> /home/brian/brain/cron_reception.log 2>&1"

# Check if entry already exists
if crontab -l 2>/dev/null | grep -q "/workflows/reception"; then
    echo "Cronjob for Reception findes allerede."
else
    # Append the new cron entry
    (crontab -l 2>/dev/null; echo "$CRON_ENTRY") | crontab -
    echo "Cronjob tilføjet: Reception (/process-inbox) kører nu hver dag kl. 6, 9, 12, 15, 18, 21."
fi
