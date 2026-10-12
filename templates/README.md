# Starter Templates

## Available Starters

| Template | Best for | Start with |
|----------|----------|------------|
| [platformer](platformer/README.md) | Run/jump, collect, enemies, goal (Grok Bot style) | `--type platform` |
| [seed-collector](seed-collector/README.md) | Top-down collect-3-items loop | `--type topdown` |

## Recommended Approaches

### 1. Scaffolder + template README
```bash
python scripts/generate_basic_project.py GrokBot ~/Games --type platform
```
Then follow the matching template README.

### 2. Official GB Studio Sample
Create a new project with the Sample template inside GB Studio, then adapt it. Fastest path to a fully initialized project.

### 3. Remix
Copy any existing GB Studio project and modify scenes.

## After Scaffolding

- Open the `.gbsproj` and let GB Studio finish initialization.
- Create/set the starting scene.
- Add player + one core interaction.
- Build and test early.
- Run `python scripts/audit_checklist.py` before adding heavy art.

Contributions of additional complete templates are welcome (see CONTRIBUTING.md).
