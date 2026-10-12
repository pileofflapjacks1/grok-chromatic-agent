---
name: grok-chromatic-agent
description: "Build and iterate Game Boy Color games for ModRetro Chromatic using GB Studio. Use when creating, scaffolding, auditing, building, or flashing Chromatic/GBC homebrew, or when the user mentions Chromatic, GB Studio, or ModRetro game development."
type: workflow
lifecycle: active
---

# Grok Chromatic Agent

Create and iterate Game Boy Color games that run on the ModRetro Chromatic (and any GB/GBC hardware or emulator). Prefer GB Studio. Keep games small and hardware-aware.

## When to Use

- User wants a new GBC / Chromatic game
- Scaffold or expand a GB Studio project
- Audit assets for hardware limits
- Build a ROM or export for web/Pocket
- Stream or flash to a Chromatic device

## Core Workflow

1. Clarify the core loop, genre, and session length (prefer short).
2. Scaffold:
   - Platformer: `python scripts/generate_basic_project.py <Name> <Parent> --type platform` then follow `templates/platformer/README.md`
   - Exploration: `--type topdown` + `templates/seed-collector/README.md`
   - Or start from GB Studio Sample Project.
3. Iterate on scenes, actors, triggers, and scripts. Run `python scripts/audit_checklist.py` or check `references/hardware-limits.md` before heavy art.
4. Build (GUI or `gb-studio-cli make:rom`).
5. Test in emulator, then optionally use helpers:
   - `python scripts/chromatic_helpers.py live-demo path/to/game.gbc`
6. Flash only after explicit confirmation. Use:
   - `python scripts/chromatic_helpers.py flash path/to/game.gbc`
   Always warn about overwrite. Fallback: ChroMagic.

## Key References (load as needed)

- Hardware limits: `references/hardware-limits.md`
- Chromatic CLI: `references/chromatic-cli.md`
- GB Studio basics: `references/gbstudio-basics.md`
- Scaffolding: `docs/scaffolding.md`
- Platformer starter: `templates/platformer/README.md`
- Seed-collector starter: `templates/seed-collector/README.md`
- Troubleshooting: `docs/troubleshooting.md`
- Skill install: `docs/install-skill.md`

## Constraints

- Prefer GB Studio over raw GBDK/RGBDS unless low-level control is required.
- Never generate copyrighted Nintendo assets or code.
- Always warn before any cartridge flash.
- Start small; stay within GBC limits.

## Output Style

Give concrete commands and next steps. Prefer the scaffolder + matching template when starting fresh.
