# Chromatic CLI Reference

Package: `@modretro/chromatic-cli`

## Setup
```bash
npm install --global @modretro/chromatic-cli
chromatic-cli install-drivers   # once per machine
```

## Activation (if you have a code)
```bash
chromatic-cli activate YOUR_CODE
```
DevDay units included codes. Regular Chromatics may not.

## Useful Commands
| Command | Purpose |
|---------|---------|
| `chromatic-cli list-devices` | Show connected Chromatics |
| `chromatic-cli detect-cart` | Inspect cartridge |
| `chromatic-cli live-demo path/to/game.gbc` | Stream ROM for testing |
| `chromatic-cli write-homebrew path/to/game.gbc` | Flash ROM to cart |
| `chromatic-cli reset-device` | Reset |

## Safety
- Always back up the cartridge first if it contains a game you want to keep.
- Confirm with the user before any `write-homebrew`.
- If activation is unavailable, recommend ChroMagic (https://chromagic.org/) as an alternative flashing path.

## Live Demo Tips
- Test in an emulator first.
- Use a short duration for initial checks.
- Verify controls, audio, and video on the physical device.
