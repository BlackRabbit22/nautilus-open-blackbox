#!/usr/bin/env bash
# Installs the "Open in Black Box" extension for Nautilus.

DEST=~/.local/share/nautilus-python/extensions
REPO="https://raw.githubusercontent.com/BlackRabbit22/nautilus-open-blackbox/main"

# Make the extensions folder (if it doesn't exist yet)
mkdir -p "$DEST"

if [ -f "$(dirname "$0")/open_blackbox.py" ]; then
    # You cloned the repo -> use the local file
    cp "$(dirname "$0")/open_blackbox.py" "$DEST/"
else
    # You ran this via curl -> download the file
    curl -fsSL -o "$DEST/open_blackbox.py" "$REPO/open_blackbox.py"
fi

# Restart Nautilus so it loads the extension
nautilus -q

echo "Done! Right-click a folder in Nautilus -> 'Open in Black Box'."
