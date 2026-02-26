#!/bin/bash

# SSH Helper for Brian VM
# Usage: ./brian_ssh.sh [target]
# Targets: tailscale, vpn, ip

TARGET=${1:-tailscale}
USER="mikkel"

case $TARGET in
  tailscale)
    HOST="vm-p-agent-01.elk-eel.ts.net"
    ;;
  vpn)
    HOST="agent-desktop.veis.dk"
    ;;
  ip)
    HOST="10.0.40.101"
    ;;
  *)
    HOST=$TARGET
    ;;
esac

echo "Connecting to $HOST as $USER..."
ssh "$USER@$HOST"
