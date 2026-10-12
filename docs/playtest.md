# Playtest Notes

## Manual Playtest Flow (current)

1. Build the ROM in GB Studio (Play button or Export ROM).
2. Test core loop in the built-in player or an external emulator (mGBA, BGB, SameBoy).
3. Run the hardware checklist:
   ```bash
   python scripts/audit_checklist.py
   ```
4. If you have a Chromatic:
   ```bash
   python scripts/chromatic_helpers.py live-demo path/to/game.gbc
   # then run the printed command
   ```
5. Only after the loop feels good, consider flashing (with backup).

## What to Verify

- Player movement feels responsive
- Collectibles register
- Hazards/enemies behave as expected
- Goal/exit works
- No obvious sprite flicker or tile corruption
- Audio (if any) is audible
- Session length is short and satisfying

## Future Automation Ideas

- ROM header / size sanity check
- Emulator screenshot comparison
- Scripted input sequences

These are not yet implemented.
