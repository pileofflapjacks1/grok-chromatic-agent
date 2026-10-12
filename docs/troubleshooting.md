# Troubleshooting

## GB Studio won’t open the generated .gbsproj
- Make sure you are opening the `.gbsproj` file itself, not the folder.
- Let GB Studio fully initialize on first open (it adds default player, palettes, etc.).
- If it still fails, create a new project inside GB Studio using the Sample template and copy your ideas across.

## Scaffold script errors
- Confirm you are running Python 3.
- Usage: `python scripts/generate_basic_project.py MyGame ~/Games --type platform`
- The parent folder must be writable.

## chromatic-cli issues
- Run `chromatic-cli install-drivers` once (may need admin/sudo).
- Reconnect the Chromatic after driver install.
- `chromatic-cli list-devices` should show the device.
- Activation (`chromatic-cli activate CODE`) is only needed for official flashing; DevDay units had codes. Regular units may need ChroMagic instead.

## Build failures or tile warnings in GB Studio
- Too many unique tiles in one scene → simplify art or split the scene.
- Sprite overflow → reduce simultaneous sprites or size.
- Run `python scripts/audit_checklist.py` and review `references/hardware-limits.md`.

## Live demo or flash doesn’t work
- Test the ROM in an emulator first.
- Confirm the file is `.gbc` or `.gb`.
- For flashing, always back up the cart first (see safer helpers).
- If no activation code, use [ChroMagic](https://chromagic.org/).

## Skill doesn’t trigger
- Use the paste method from `docs/install-skill.md`.
- Explicitly say “use the Chromatic / GB Studio skill.”
