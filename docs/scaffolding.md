# Scaffolding a New Project

## Quick Command

```bash
python scripts/generate_basic_project.py MoonGarden ~/Games --type topdown
```

Supported types: `topdown` (default), `platform`.

## What You Get

- Clean project folder
- Starter `.gbsproj` with the chosen scene type
- Asset subfolders (`backgrounds`, `sprites`, `ui`, `music`, `sounds`)
- `project/` and `build/` directories
- A local `README.md` with next steps

## After Generation

1. Open the `.gbsproj` in GB Studio.
2. Allow the editor to finish setup (default player sprite, palettes, etc.).
3. Create your first scene and mark it as the start scene.
4. Add the player and one core interaction.
5. Playtest in the GB Studio window or an emulator.
6. Optionally stream or flash to Chromatic using the commands in `references/chromatic-cli.md`.

## Alternative: Official Sample

For the fastest path to a playable base, create a new project in GB Studio using the built-in **Sample Project** template, then delete the example content and rebuild. This is often faster than starting completely empty.
