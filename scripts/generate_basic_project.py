#!/usr/bin/env python3
"""
Minimal GB Studio project scaffolder.
Generates a bare-bones .gbsproj and folder structure that you can open in GB Studio.

Usage:
    python scripts/generate_basic_project.py MyGame /path/to/parent/folder
"""

import json
import os
import sys
import uuid
from pathlib import Path

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_basic_project.py <ProjectName> <ParentFolder>")
        sys.exit(1)

    name = sys.argv[1]
    parent = Path(sys.argv[2]).expanduser().resolve()
    project_dir = parent / name
    project_dir.mkdir(parents=True, exist_ok=True)

    # Basic .gbsproj (simplified — open in GB Studio to fully initialize)
    project = {
        "_resourceType": "project",
        "name": name,
        "author": "",
        "sceneTypes": ["TOPDOWN"],
        "startSceneId": "",
        "startX": 0,
        "startY": 0,
        "startDirection": "down",
        "startMoveSpeed": 1,
        "startAnimSpeed": 15,
        "colorMode": "color",
        "defaultPlayerSpritesheetId": "",
        "defaultPlayerPaletteId": "",
        "defaultBackgroundPaletteIds": [],
        "defaultSpritePaletteIds": [],
        "musicDriver": "gbtplayer",
        "engineFields": {},
        "variables": [],
        "constants": [],
        "prefabs": [],
        "scenes": [],
        "backgrounds": [],
        "spriteSheets": [],
        "tilesets": [],
        "fonts": [],
        "avatars": [],
        "emotes": [],
        "sounds": [],
        "music": [],
        "palettes": [],
        "scriptEvents": [],
        "customEvents": []
    }

    gbsproj_path = project_dir / f"{name}.gbsproj"
    with open(gbsproj_path, "w") as f:
        json.dump(project, f, indent=2)

    # Minimal folder structure GB Studio expects
    for folder in ["assets", "project", "build"]:
        (project_dir / folder).mkdir(exist_ok=True)

    print(f"Created basic project at: {project_dir}")
    print(f"Open {gbsproj_path} in GB Studio to finish initialization and start building.")
    print("Then use Grok + the Chromatic skill to add scenes, actors, and logic.")

if __name__ == "__main__":
    main()
