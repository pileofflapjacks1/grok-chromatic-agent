# Example Prompts

Copy these into Grok (with the Chromatic skill loaded) or adapt them.

## New Exploration Game

```
Create a new GB Studio project called MoonGarden.
Make a small top-down exploration game where a gardener collects three seeds
and plants them to unlock a gate. Include a starting outdoor scene and a simple
player character. Generate the project structure and list the next steps.
```

## Platformer / Grok Bot Starter

```
Scaffold a platformer called GrokBot for Chromatic.
Player can run and jump, has fun customizable eyes, collects power-ups,
and avoids or defeats simple enemies. Start with one short level and a goal flag.
Use --type platform. Give me the exact commands and first-playable checklist.
```

## Add a Power-up

```
In my platformer, add a power-up that temporarily increases jump height.
Show me the GB Studio variable + script approach and where to place the actor.
```

## Enemy

```
Add a simple patrolling enemy to my platform level that hurts the player on touch.
Keep it hardware-friendly and suggest a basic sprite size.
```

## Level Progression

```
I have a working Level 1 platformer. Help me plan Levels 2–3 and a path toward
9 short levels + a boss while staying within GBC limits.
```

## Asset Audit

```
Audit the sprites and backgrounds in my current GB Studio project
for Game Boy Color hardware limits. List any problems and suggest fixes.
```

## Device Testing

```
I just built game.gbc. Give me the exact chromatic-cli commands
to stream it to my connected Chromatic for a short test,
then the safe steps if I later want to flash it.
```

## Remix / Expand

```
I have a GB Studio project at ./MyGame.
Add a second scene with a different palette, connect it with a trigger,
and add one NPC or enemy. Keep everything Chromatic-friendly.
```
