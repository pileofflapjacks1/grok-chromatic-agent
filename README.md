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
   python scripts/generate_basic_project.py MyGame ~/Games --type topdown
   ```
4. Open the `.gbsproj` in GB Studio and start building.
5. Use the skill (`SKILL.md`) with Grok for iteration, auditing, and device commands.

See `templates/seed-collector/README.md` for a concrete first-game loop.

## What You Get

- Proper Grok skill (`SKILL.md`) with frontmatter, evals, and references
- Project scaffolder with `--type topdown|platform`
- Hardware limits reference + audit checklist script
- Chromatic CLI command reference and safety notes
- Example prompts and starter guidance

## Project Structure

```
SKILL.md                  # Grok skill (drop into skills or reference)
CHANGELOG.md
evals/                    # Skill evaluation cases
references/               # Hardware limits, CLI, GB Studio basics
docs/                     # Setup, workflow, scaffolding
templates/                # Starter ideas (seed-collector, etc.)
scripts/                  # generate_basic_project.py, audit_checklist.py
examples/prompts.md
```

## Key Commands

| Tool | Command | Purpose |
|------|---------|---------|
| Scaffolder | `python scripts/generate_basic_project.py Name ~/Games --type topdown` | Create project |
| Audit | `python scripts/audit_checklist.py` | Print hardware checklist |
| Chromatic | `chromatic-cli live-demo game.gbc` | Stream to device |
| Chromatic | `chromatic-cli write-homebrew game.gbc` | Flash (warn first!) |

## Related

- Official Codex plugin: ModRetro Chromatic
- Community Claude MCP: [eoinjordan/gb-studio-agent](https://github.com/eoinjordan/gb-studio-agent)
- Alternative flashing: [ChroMagic](https://chromagic.org/)

## Disclaimer

Independent community project. Not affiliated with ModRetro or OpenAI. Flash only your own homebrew. Use developer mode and cartridge writing at your own risk.

## License

MIT
