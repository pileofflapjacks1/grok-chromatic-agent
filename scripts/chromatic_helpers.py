#!/usr/bin/env python3
"""
Safer helper reminders and command printers for Chromatic CLI.
Does not run destructive commands; it prints the exact commands and warnings.

Usage:
    python scripts/chromatic_helpers.py live-demo path/to/game.gbc
    python scripts/chromatic_helpers.py flash path/to/game.gbc
    python scripts/chromatic_helpers.py backup-reminder
"""

import sys

def live_demo(rom):
    print("Live demo command (test on device):")
    print(f"  chromatic-cli live-demo {rom}")
    print()
    print("Tips:")
    print("  • Test in an emulator first.")
    print("  • Keep the first session short.")
    print("  • Check controls, video, and audio.")

def flash(rom):
    print("=" * 60)
    print("WARNING: This will overwrite the cartridge!")
    print("=" * 60)
    print()
    print("Before flashing:")
    print("  1. Back up the current cart if it has anything you want to keep.")
    print("  2. Confirm the ROM is your own homebrew.")
    print("  3. Make sure developer mode is activated (or use ChroMagic).")
    print()
    print("Flash command (run only after confirming):")
    print(f"  chromatic-cli write-homebrew {rom}")
    print()
    print("Alternative if you lack an activation code:")
    print("  Use ChroMagic: https://chromagic.org/")

def backup_reminder():
    print("Cartridge backup reminder")
    print("  • Use ChroMagic / ChroMagician to back up before writing.")
    print("  • Or use any other verified cart backup tool you trust.")
    print("  • Never flash over a cart that still contains a game you care about.")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "live-demo" and len(sys.argv) >= 3:
        live_demo(sys.argv[2])
    elif cmd == "flash" and len(sys.argv) >= 3:
        flash(sys.argv[2])
    elif cmd == "backup-reminder":
        backup_reminder()
    else:
        print(__doc__)
        sys.exit(1)

if __name__ == "__main__":
    main()
