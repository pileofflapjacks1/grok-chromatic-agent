# grok-chromatic-agent

Grok-friendly agent / skill for building **Game Boy Color** games that run on the **ModRetro Chromatic** (and any GB/GBC-compatible hardware or emulator).

Open reverse-engineering of the software features in the official ModRetro Chromatic plugin for OpenAI Codex. Built on public tools:

- **GB Studio** — project creation, scenes, actors, scripts, ROM builds
- **`@modretro/chromatic-cli`** — live demo streaming and homebrew flashing
- Hardware-aware guidance for real Game Boy / GBC limits

## Quick Start

1. Install [GB Studio](https://www.gbstudio.dev/).
2. (Optional) Install the Chromatic CLI:
   ```bash
   npm install --global @modretro/chromatic-cli
   chromatic-cli install-drivers
   ```
3. Scaffold a project:
   ```bash
   python scripts/generate_basic_project.py GrokBot ~/Games --type platform
   # or --type topdown
   ```
4. Open the `.gbsproj` in GB Studio and start building.
5. Install or reference the skill (see `docs/install-skill.md`).

Starter guides:
- Platformer: `templates/platformer/README.md`
- Exploration: `templates/seed-collector/README.md`

## Install the Skill

See **[docs/install-skill.md](docs/install-skill.md)** for copy-to-skills-folder, paste-in-chat, or URL methods.

## What You Get

- Proper Grok skill (`SKILL.md`) with frontmatter, evals, and references
- Project scaffolder with `--type topdown|platform`
- Platformer and seed-collector starter templates
- Hardware limits reference + audit checklist
- Safer Chromatic CLI helpers (warnings + exact commands)
- Troubleshooting, playtest notes, and advanced (MCP/GBDK) guidance
- GitHub Action for basic checks
- Example prompts

## Project Structure

```
SKILL.md
CHANGELOG.md
CONTRIBUTING.md
evals/
references/               # hardware, CLI, GB Studio basics
docs/                     # install-skill, setup, workflow, troubleshooting, advanced, playtest
templates/                # platformer, seed-collector
scripts/                  # generate, audit, chromatic_helpers
examples/prompts.md
.github/workflows/ci.yml
```

## Key Commands

| Tool | Command | Purpose |
|------|---------|---------|
| Scaffolder | `python scripts/generate_basic_project.py Name ~/Games --type platform` | Create project |
| Audit | `python scripts/audit_checklist.py` | Hardware checklist |
| Helpers | `python scripts/chromatic_helpers.py live-demo game.gbc` | Safe command printer |
| Helpers | `python scripts/chromatic_helpers.py flash game.gbc` | Flash warning + command |
| Chromatic | `chromatic-cli live-demo game.gbc` | Stream to device |
| Chromatic | `chromatic-cli write-homebrew game.gbc` | Flash (after confirmation) |

## Related

- Official Codex plugin: ModRetro Chromatic
- Community Claude MCP: [eoinjordan/gb-studio-agent](https://github.com/eoinjordan/gb-studio-agent)
- Alternative flashing: [ChroMagic](https://chromagic.org/)

## Topics to add (manual)

Suggested GitHub topics: `gbstudio` `gameboy` `gameboy-color` `chromatic` `modretro` `grok` `ai-agent` `homebrew`

## Disclaimer

Independent community project. Not affiliated with ModRetro or OpenAI. Flash only your own homebrew. Use developer mode and cartridge writing at your own risk.

## License

MIT
