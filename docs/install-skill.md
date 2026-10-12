# Installing the Grok Skill

## Method 1 — Copy into skills folder (preferred if supported)

1. Locate your Grok skills directory (often something like `~/.grok/skills/` or the path shown in your Grok settings).
2. Create a folder named `grok-chromatic-agent`.
3. Copy these into it:
   - `SKILL.md`
   - `references/` (entire folder)
   - Optionally `evals/`
4. Restart or refresh Grok so it picks up the new skill.

The skill should now trigger on Chromatic, GB Studio, or ModRetro game-development requests.

## Method 2 — Paste in any chat (always works)

1. Open `SKILL.md` from this repo.
2. Copy its full contents.
3. In a new Grok chat, paste it and say:

```
Use the following skill for this conversation:

[paste SKILL.md here]

Now help me scaffold a platformer called GrokBot.
```

## Method 3 — Reference the raw URL

Tell Grok:

```
Read and follow the skill at:
https://raw.githubusercontent.com/pileofflapjacks1/grok-chromatic-agent/main/SKILL.md

Then help me build a short platformer.
```

## Verifying It Works

Ask: “Scaffold a simple platformer for Chromatic.”

You should see references to GB Studio, the `--type platform` scaffolder, hardware limits, and concrete next steps.
