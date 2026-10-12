# Seed Collector Starter

A minimal top-down exploration loop ideal for Chromatic / GB Studio.

**Core loop:** Explore a small outdoor area, collect 3 seeds, plant them (or reach a gate), unlock the exit.

## How to Start

### Option A — Recommended (fastest to playable)
1. Open GB Studio → New Project → **Sample Project**.
2. Name it `SeedCollector` (or whatever you like).
3. Delete the example scenes you don’t need.
4. Create one outdoor scene (160×144 or slightly larger).
5. Place the player, 3 collectible actors (seeds), and one exit trigger or gate actor.
6. Add simple scripts: on collect → increment variable; when variable == 3 → enable exit.

### Option B — Use the scaffolder
```bash
python scripts/generate_basic_project.py SeedCollector ~/Games --type topdown
```
Open the generated `.gbsproj` in GB Studio, let it initialize, then follow the steps above.

## Suggested Structure

- **Scene 1: Garden** — starting outdoor area with 3 seed pickups
- **Variable:** `seeds_collected` (0–3)
- **Exit:** A door or path that only activates when `seeds_collected == 3`
- **Player:** Default GB Studio player sprite is fine for the first version

## First Playable Checklist

- [ ] One scene that builds and runs
- [ ] Player can move
- [ ] At least one collectible works
- [ ] Variable increments
- [ ] Exit/gate reacts to the variable
- [ ] Tested in emulator
- [ ] (Optional) Streamed to Chromatic with `chromatic-cli live-demo`

## Tips for Chromatic

- Keep the first version to 1 scene and simple art.
- Use high-contrast palettes so it reads well on the Chromatic screen.
- Audit tile count before adding many unique graphics (see `references/hardware-limits.md`).
- Build and test early.

Once the loop feels good, expand with a second scene or more polish.
