#!/bin/bash
# Start OCR Watcher for Brian

VAULT_PATH="/Users/mikkelfeld/obsidian/brain"
EXTRACTOR_DIR="$VAULT_PATH/skills/pkm-extractor"
PYTHON_BIN="/Users/mikkelfeld/.brian/envs/extractor/bin/python3"
WATCHER_SCRIPT="$EXTRACTOR_DIR/scripts/watch_inbox.py"
LOG_FILE="$VAULT_PATH/agent/ocr_watcher.log"

echo "Starter OCR Watcher på Brian..."

# Tjek om processen allerede kører
if pgrep -f "$WATCHER_SCRIPT" > /dev/null; then
    echo "OCR Watcher kører allerede."
else
    nohup "$PYTHON_BIN" "$WATCHER_SCRIPT" >> "$LOG_FILE" 2>&1 &
    echo "OCR Watcher startet i baggrunden (PID: $!)."
    echo "Log: $LOG_FILE"
fi
