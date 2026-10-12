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
   - `python scripts/generate_basic_project.py <Name> <Parent> --type topdown|platform`
   - Or start from GB Studio Sample Project.
   - For a concrete first game, follow `templates/seed-collector/README.md`.
3. Iterate on scenes, actors, triggers, and scripts. Run `python scripts/audit_checklist.py` or check `references/hardware-limits.md` before heavy art.
4. Build (GUI or `gb-studio-cli make:rom`).
5. Test in emulator, then optionally `chromatic-cli live-demo`.
6. Flash only after explicit confirmation (`chromatic-cli write-homebrew`). Always warn about overwrite. Fallback: ChroMagic.

## Key References (load as needed)

- Hardware limits: `references/hardware-limits.md`
- Chromatic CLI: `references/chromatic-cli.md`
- GB Studio basics: `references/gbstudio-basics.md`
- Scaffolding: `docs/scaffolding.md`
- Seed-collector starter: `templates/seed-collector/README.md`

## Constraints

- Prefer GB Studio over raw GBDK/RGBDS unless low-level control is required.
- Never generate copyrighted Nintendo assets or code.
- Always warn before any cartridge flash.
- Start small; stay within GBC limits.

## Output Style

Give concrete commands and next steps. Prefer the scaffolder or seed-collector template when starting fresh.
