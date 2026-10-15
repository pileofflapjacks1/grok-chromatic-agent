# Platformer Starter

A minimal side-scrolling platformer loop for Chromatic / GB Studio.

**Core loop:** Run, jump, collect power-ups/coins, avoid or defeat simple enemies, reach the goal.

Ideal starting point for the Grok Bot platformer concept (customizable shape/color, fun eyes, 9 levels + boss later).

## How to Start

### Option A — Scaffolder (recommended)
```bash
python scripts/generate_basic_project.py GrokBot ~/Games --type platform
```
Open the generated `.gbsproj` in GB Studio and let it initialize.

### Option B — GB Studio Sample
Create a new project with the Sample template, then switch scenes to Platform type and strip unused content.

## Suggested First Level Structure

- **Scene type:** PLATFORM
- **Player:** Default or simple custom sprite with clear eyes
- **Collectibles:** 3–5 coins or power-ups
- **Enemy:** One simple patrolling or stationary hazard
- **Goal:** Flag or door at the end
- **Variable:** `coins` (optional score)

## First Playable Checklist

- [ ] Platform scene builds and runs
- [ ] Player can run and jump
- [ ] At least one collectible works
- [ ] One enemy or hazard is present
- [ ] Goal/exit is reachable
- [ ] Tested in emulator
- [ ] (Optional) Streamed to Chromatic

## Expanding Toward 9 Levels + Boss

1. Prove the core loop in Level 1.
2. Duplicate the scene for Levels 2–3 with small variations.
3. Add a simple power-up (temporary speed or jump boost).
4. Introduce a second enemy type.
5. Build a short boss encounter once the basic combat/avoidance feels good.
6. Keep each level short (Chromatic-friendly sessions).

## Tips

- Start with high-contrast colors so the character reads well on the Chromatic screen.
- Audit sprites and tiles early (`python scripts/audit_checklist.py`).
- Prefer simple animations at first.
- Use the Grok Chromatic skill to iterate on scripts and structure.
