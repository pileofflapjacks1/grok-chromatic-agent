# Advanced Topics

## MCP Server Mode (future / community)

The community project [eoinjordan/gb-studio-agent](https://github.com/eoinjordan/gb-studio-agent) already provides an MCP server so Claude and other agents can create/modify GB Studio projects programmatically.

To extend this repo in that direction:
- Wrap the existing scaffolder and references as MCP tools.
- Add Chromatic CLI commands (`live-demo`, `write-homebrew`) as optional tools with confirmation gates.
- Reuse the hardware-limits checks.

A full MCP implementation is left as a contribution opportunity.

## GBDK-2020 Path

GB Studio is the recommended starting point. When you need lower-level control (custom engines, tight timing, unusual effects):

- Switch to [GBDK-2020](https://github.com/gbdk-2020/gbdk-2020).
- Keep the same Chromatic testing flow (`chromatic-cli live-demo` / `write-homebrew`).
- Hardware limits still apply.

This repo focuses on the GB Studio workflow; GBDK projects can still use the CLI references and audit checklist.

## Automated Playtest Notes

Current practical approach:
1. Build ROM in GB Studio.
2. Test manually in emulator.
3. Run `python scripts/audit_checklist.py`.
4. Optionally stream to device.

Future ideas: simple ROM header checks, screenshot diffs, or scripted input via an emulator. Not implemented yet.
