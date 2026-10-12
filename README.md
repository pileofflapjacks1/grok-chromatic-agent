# grok-chromatic-agent

Grok-friendly agent / skill for building **Game Boy Color** games that run on the **ModRetro Chromatic** (and any GB/GBC-compatible hardware or emulator).

This is an open reverse-engineering of the software features provided by the official **ModRetro Chromatic plugin** for OpenAI Codex. It uses the same public toolchain:

- **GB Studio** (open source) for project creation, scenes, actors, scripts, and ROM builds
- **`@modretro/chromatic-cli`** for device interaction (live demo streaming + homebrew flashing)
- Hardware-aware constraints for Game Boy / GBC limits

## What you can do

- Describe a game in natural language and get a GB Studio project skeleton + guidance
- Validate assets against real hardware limits (tiles, sprites, palettes)
- Build ROMs with the GB Studio CLI
- Stream a live demo to a connected Chromatic
- Flash homebrew to a writable Chromatic cartridge (when developer mode is activated)
- Use alternative flashing methods (ChroMagic, etc.) if you don't have an official activation code

## Quick Start

1. Install [GB Studio](https://www.gbstudio.dev/) (latest stable).
2. Install the Chromatic CLI:
   ```bash
   npm install --global @modretro/chromatic-cli
   chromatic-cli install-drivers   # once, platform-specific
   ```
3. (Optional) Activate developer mode if you have a code from a DevDay Chromatic or ModRetro:
   ```bash
   chromatic-cli activate YOUR_CODE
   ```
4. Use this repo with Grok (see `SKILL.md`) or follow the guides in `docs/`.

## Key Commands (chromatic-cli)

| Command | Purpose |
|---------|---------|
| `chromatic-cli list-devices` | List connected Chromatics |
| `chromatic-cli detect-cart` | Inspect the cartridge |
| `chromatic-cli live-demo path/to/game.gbc` | Stream ROM to Chromatic for testing |
| `chromatic-cli write-homebrew path/to/game.gbc` | Flash ROM to cartridge |

## Project Structure

- `SKILL.md` — Drop this into your Grok skills folder for native agent behavior
- `docs/` — Detailed setup, workflows, and hardware notes
- `examples/` — Sample prompts and project ideas
- `scripts/` — Helper scripts (basic project scaffolding)

## Related Projects

- Official Codex plugin: ModRetro Chromatic (requires Codex desktop)
- Community MCP server for Claude: [eoinjordan/gb-studio-agent](https://github.com/eoinjordan/gb-studio-agent)
- Custom firmware / alternative flashing: [ChroMagic](https://chromagic.org/)

## Disclaimer

This is an independent community project. It is not affiliated with ModRetro or OpenAI. Use developer mode and cartridge flashing at your own risk. Only flash original homebrew you created.

## License

MIT
