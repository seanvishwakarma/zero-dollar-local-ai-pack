#!/usr/bin/env bash
# ==========================================================
#  The Zero-Dollar Dev: Local AI Daemon Tuning (Linux/macOS)
#  https://thezerodollardev.blogspot.com/
# ==========================================================

set -euo pipefail

echo "Optimizing Ollama daemon environment for consumer hardware..."

# Detect shell rc file
RC_FILE="$HOME/.bashrc"
if [ -f "$HOME/.zshrc" ]; then
    RC_FILE="$HOME/.zshrc"
fi

cat << 'EOF' >> "$RC_FILE"

# --- The Zero-Dollar Dev: Ollama Optimization ---
export OLLAMA_FLASH_ATTENTION=1
export OLLAMA_KEEP_ALIVE=15m
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_HOST=127.0.0.1:11434
# ------------------------------------------------
EOF

echo "✓ Settings appended to $RC_FILE"
echo "Restart your terminal or run: source $RC_FILE"
echo "Restart Ollama service: systemctl --user restart ollama (Linux) or restart the menu bar app (macOS)."
