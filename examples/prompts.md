# Example Prompts

Copy these into Grok (with the Chromatic skill loaded) or adapt them.

## New Game

```
Create a new GB Studio project called MoonGarden.
Make a small top-down exploration game where a gardener collects three seeds
and plants them to unlock a gate. Include a starting outdoor scene and a simple
player character. Generate the project structure and list the next steps.
```

## Remix / Expand

```
I have a GB Studio project at ./MyGame.
Add a village scene with three houses, a central fountain, and one NPC
I can talk to. Connect it to the starting area with a trigger.
Also give the village a cool blue moonlit palette.
```

## Asset Audit

```
Audit the sprites and backgrounds in my current GB Studio project
for Game Boy Color hardware limits. List any problems and suggest fixes.
```

## Device Testing

```
I just built game.gbc. Give me the exact chromatic-cli commands
to stream it to my connected Chromatic for a 2-minute test,
then flash it to the cartridge if the test looks good.
```

## Platformer Starter

```
Scaffold a simple platformer for Chromatic: player can run and jump,
collect coins, avoid one type of enemy, reach a goal flag.
Keep it to 2-3 short levels. Use GB Studio platformer scene type.
```
