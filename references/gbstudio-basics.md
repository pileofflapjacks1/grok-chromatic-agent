# GB Studio Basics

## Project Structure
- `.gbsproj` — main project file (JSON)
- `assets/` — images, sounds, music
- `project/` — generated resource JSON
- `build/` — output ROMs and web exports

## Scene Types
- `TOPDOWN` — exploration, RPGs, adventure
- `PLATFORM` — side-scrolling platformers
- Others available (shooter, etc.) depending on version and settings

## Typical Workflow
1. Create or open project in GB Studio
2. Add scenes, set backgrounds, place actors and triggers
3. Add scripts (dialogue, movement, collectibles, scene changes)
4. Set color palettes
5. Play / Export ROM

## CLI (optional)
If built from source:
```bash
gb-studio-cli make:rom path/to/project.gbsproj out/game.gbc
gb-studio-cli make:web path/to/project.gbsproj out/
```

## Tips for Agents
- Prefer generating a minimal project then letting the user open it in the GUI for visual editing.
- Recommend the sample/Wrecklight-style remix approach when possible.
- Keep the first playable version to 1–3 scenes.
