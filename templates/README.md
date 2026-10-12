# Starter Templates

GB Studio works best when you start from its official Sample Project (or a clean GUI-created project) and then remix. Fully valid projects contain many generated resource IDs and default assets that are easiest to let the editor create.

## Recommended Starting Approaches

### 1. Official Sample (easiest)
1. Open GB Studio → New Project → choose **Sample Project**.
2. Name it and save.
3. Delete or modify the example scenes, then build your game on top.
4. This gives you working player, palettes, and example scripts immediately.

### 2. Scaffolded Project (this repo)
Use the improved scaffolder:

```bash
python scripts/generate_basic_project.py MyGame ~/Games --type topdown
# or
python scripts/generate_basic_project.py JumpMan ~/Games --type platform
```

Then open the generated `.gbsproj` in GB Studio. The editor will complete initialization on first load.

### 3. Remix an Existing Game
If you have the Codex "Wrecklight" example or any other GB Studio project, copy the folder and start modifying scenes.

## After Scaffolding

- Create at least one scene and set it as the starting scene.
- Place the player actor.
- Add one simple interaction (dialogue or collectible) so you can test the loop.
- Build early and often.
- Audit tile/sprite/palette usage before adding heavy art.

## Future Templates

Contributions welcome for complete minimal playable projects (top-down seed collector, simple platformer, etc.) that open and build cleanly.
