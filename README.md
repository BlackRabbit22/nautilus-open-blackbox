# Nautilus Black Box Extension
Extension for Nautilus file manager that opens a Black Box terminal in your current working directory.

- Right-click a folder → opens Black Box in that folder
- Right-click empty space → opens Black Box in the folder you're in

## Requirements

- Nautilus with `nautilus-python`
- [Black Box](https://flathub.org/apps/com.raggesilver.BlackBox) installed as a Flatpak

## Installation

### Automated install

```bash
curl -fsSL https://raw.githubusercontent.com/BlackRabbit22/nautilus-open-blackbox/main/install.sh | bash
```

### Manual install

```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp open_blackbox.py ~/.local/share/nautilus-python/extensions/
nautilus -q
```

## Uninstall

```bash
rm ~/.local/share/nautilus-python/extensions/open_blackbox.py
nautilus -q
```
