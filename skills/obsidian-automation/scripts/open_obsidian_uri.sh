#!/bin/bash

# Hjælpe-script til at åbne Obsidian URI'er på macOS
# Anvendelse: ./open_obsidian_uri.sh "obsidian://open?vault=brain&file=Welcome"

URI=$1

if [ -z "$URI" ]; then
    echo "Fejl: Ingen URI angivet."
    echo "Anvendelse: $0 \"obsidian://...\""
    exit 1
fi

echo "Åbner Obsidian URI: $URI"
open "$URI"
