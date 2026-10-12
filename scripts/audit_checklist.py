#!/usr/bin/env python3
"""
Simple hardware audit checklist for GB Studio / Chromatic projects.
Prints the key limits and common failure modes so you (or an agent) can review before a build.

Usage:
    python scripts/audit_checklist.py
"""

def main():
    print("=" * 60)
    print("GB Studio / Chromatic Hardware Audit Checklist")
    print("=" * 60)
    print()
    print("Screen")
    print("  • 160 × 144 pixels — design for short, readable scenes")
    print()
    print("Graphics")
    print("  • Unique background tiles per scene: keep well under ~256")
    print("  • Sprites: watch 40 on-screen / 10 per scanline limits")
    print("  • Sprite size: 8×8 or 8×16 preferred")
    print("  • Palettes: 8 BG + 8 sprite (4 colors each) on GBC")
    print("  • High contrast is important on the Chromatic screen")
    print()
    print("Common Failure Modes")
    print("  • Too many unique tiles → build warnings or failure")
    print("  • Sprite overflow on a line → flickering")
    print("  • Low-contrast palettes → hard to read on device")
    print("  • Too many actors/scripts → slowdowns")
    print()
    print("Before a serious build:")
    print("  1. Count unique tiles in the busiest scene")
    print("  2. Check sprite sizes and count per line")
    print("  3. Verify palette contrast")
    print("  4. Test in an emulator first")
    print("  5. Then (optionally) live-demo on Chromatic")
    print()
    print("See references/hardware-limits.md for more detail.")
    print("=" * 60)

if __name__ == "__main__":
    main()
