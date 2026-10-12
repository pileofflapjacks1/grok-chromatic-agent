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
2. Scaffold a GB Studio project:
   - Preferred: `python scripts/generate_basic_project.py <Name> <ParentFolder> --type topdown|platform`
   - Or recommend starting from GB Studio's official Sample Project and remixing.
   - See `docs/scaffolding.md` and `templates/README.md`.
3. Iterate: add scenes, actors, triggers, dialogue, palettes. Check hardware limits before heavy art.
4. Build: guide GUI export or `gb-studio-cli make:rom`.
5. Test: emulator first, then (if device available) `chromatic-cli live-demo`.
6. Flash only after explicit confirmation: `chromatic-cli write-homebrew` (warn about overwrite). Fallback: ChroMagic.

## Key References (load as needed)

- Hardware limits and common failure modes: `references/hardware-limits.md`
- Chromatic CLI commands and safety: `references/chromatic-cli.md`
- GB Studio project basics and scene types: `references/gbstudio-basics.md`
- Scaffolding details: `docs/scaffolding.md`

## Constraints

- Prefer GB Studio over raw GBDK/RGBDS unless low-level control is required.
- Never generate copyrighted Nintendo assets or code.
- Always warn before any cartridge flash.
- Start small; stay within GBC limits.

## Output Style

Give concrete next commands or file structures. Offer the scaffolding script when the user has a target path.
