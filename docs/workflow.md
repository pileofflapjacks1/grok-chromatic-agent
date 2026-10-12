# Recommended Workflow

1. **Describe the game** to Grok (using the SKILL.md).
2. **Scaffold the project** — create the folder, `.gbsproj`, and initial scenes.
3. **Open in GB Studio** and refine visually (or continue iterating via agent).
4. **Build ROM**:
   - GUI: Export → Export ROM
   - CLI: `gb-studio-cli make:rom path/to/project.gbsproj out/game.gbc`
5. **Test in emulator**.
6. **Stream to Chromatic** (if device connected and activated):
   ```bash
   chromatic-cli live-demo out/game.gbc
   ```
7. **Flash to cartridge** when ready:
   ```bash
   chromatic-cli write-homebrew out/game.gbc
   ```
   Always back up the cart first if it contains anything you want to keep.

## Hardware Limits Cheat Sheet

- Screen: 160 × 144 pixels
- Background tiles: limited unique tiles per scene (typically ~256 or less depending on mode)
- Sprites: 40 max on screen, 10 per line (classic GB limits; GBC has more flexibility but still constrained)
- Palettes: 8 background + 8 sprite palettes on GBC (4 colors each)
- ROM size: start with 32KB or 128KB; larger requires banking

Always audit assets before a final build.
