#!/usr/bin/env python3
"""
wcag-checker.py - WCAG 2.1 Color Contrast & Accessibility Engine

Calculates relative luminance and contrast ratio between foreground and
background colors according to the W3C WCAG 2.1 specification.

Formulas:
  sRGB to Linear:
    C_linear = C_srgb / 12.92 if C_srgb <= 0.04045 else ((C_srgb + 0.055) / 1.055) ** 2.4
  Relative Luminance:
    L = 0.2126 * R_linear + 0.7152 * G_linear + 0.0722 * B_linear
  Contrast Ratio:
    (L1 + 0.05) / (L2 + 0.05) where L1 is the lighter of the two

Author: SWAYAM KIRAN PRABHU
Part of chroma-craft (agent-dev-skills)
License: MIT
"""

import sys
import argparse
import re
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def normalize_hex(hex_str: str) -> str:
    """Normalize hex code to 6-character uppercase format with leading hash."""
    clean = hex_str.strip().lstrip("#")
    if len(clean) == 3:
        clean = "".join([c * 2 for c in clean])
    if len(clean) != 6 or not re.match(r"^[0-9A-Fa-f]{6}$", clean):
        raise ValueError(f"Invalid hex color code: '{hex_str}'")
    return f"#{clean.upper()}"


def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    """Convert normalized hex string to (r, g, b) tuple in 0..255."""
    norm = normalize_hex(hex_str).lstrip("#")
    return int(norm[0:2], 16), int(norm[2:4], 16), int(norm[4:6], 16)


def rgb_to_linear(channel: int) -> float:
    """Convert an 8-bit sRGB channel to linear gamma value (0.0 .. 1.0)."""
    c = channel / 255.0
    if c <= 0.04045:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def calculate_luminance(hex_str: str) -> float:
    """Calculate relative luminance according to WCAG 2.1 (0.0 to 1.0)."""
    r, g, b = hex_to_rgb(hex_str)
    r_lin = rgb_to_linear(r)
    g_lin = rgb_to_linear(g)
    b_lin = rgb_to_linear(b)
    return 0.2126 * r_lin + 0.7152 * g_lin + 0.0722 * b_lin


def calculate_contrast(fg_hex: str, bg_hex: str) -> float:
    """Calculate contrast ratio between two hex colors (1.0:1 to 21.0:1)."""
    l1 = calculate_luminance(fg_hex)
    l2 = calculate_luminance(bg_hex)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def evaluate_wcag(contrast: float) -> dict:
    """Evaluate contrast ratio against WCAG 2.1 AA and AAA thresholds."""
    return {
        "contrast_ratio": round(contrast, 2),
        "formatted_ratio": f"{contrast:.2f}:1",
        "aa_normal_text": contrast >= 4.5,      # 4.5:1 for body / normal text (< 18pt or < 14pt bold)
        "aa_large_text": contrast >= 3.0,       # 3.0:1 for large text (>= 18pt or >= 14pt bold)
        "aa_ui_components": contrast >= 3.0,    # 3.0:1 for UI borders, controls, focus rings
        "aaa_normal_text": contrast >= 7.0,     # 7.0:1 for enhanced body text
        "aaa_large_text": contrast >= 4.5,      # 4.5:1 for enhanced large text
    }


def analyze_pair(fg: str, bg: str) -> dict:
    fg_norm = normalize_hex(fg)
    bg_norm = normalize_hex(bg)
    lum_fg = calculate_luminance(fg_norm)
    lum_bg = calculate_luminance(bg_norm)
    cr = calculate_contrast(fg_norm, bg_norm)
    eval_data = evaluate_wcag(cr)
    return {
        "foreground": fg_norm,
        "foreground_luminance": round(lum_fg, 4),
        "background": bg_norm,
        "background_luminance": round(lum_bg, 4),
        **eval_data
    }


def format_cli_report(res: dict) -> str:
    lines = [
        "============================================================",
        "        CHROMA-CRAFT WCAG 2.1 ACCESSIBILITY AUDIT          ",
        "============================================================",
        f" Foreground : {res['foreground']} (Relative Luminance: {res['foreground_luminance']:.4f})",
        f" Background : {res['background']} (Relative Luminance: {res['background_luminance']:.4f})",
        f" Contrast   : {res['formatted_ratio']}",
        "------------------------------------------------------------",
        f" Level AA  - Normal Body Text (<18pt)   : {'[PASS]' if res['aa_normal_text'] else '[FAIL]'} (req 4.5:1)",
        f" Level AA  - Large Text / Headings      : {'[PASS]' if res['aa_large_text'] else '[FAIL]'} (req 3.0:1)",
        f" Level AA  - UI Components & Borders    : {'[PASS]' if res['aa_ui_components'] else '[FAIL]'} (req 3.0:1)",
        f" Level AAA - Normal Body Text (Enhanced): {'[PASS]' if res['aaa_normal_text'] else '[FAIL]'} (req 7.0:1)",
        f" Level AAA - Large Text / Headings      : {'[PASS]' if res['aaa_large_text'] else '[FAIL]'} (req 4.5:1)",
        "============================================================"
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Chroma-Craft WCAG 2.1 Color Contrast Checker")
    parser.add_argument("foreground", help="Foreground / Text hex code (e.g., '#121214' or '121214')")
    parser.add_argument("background", help="Background / Surface hex code (e.g., '#FBFBFD' or 'FBFBFD')")
    parser.add_argument("--json", action="store_true", help="Output result as JSON")
    args = parser.parse_args()

    try:
        result = analyze_pair(args.foreground, args.background)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_cli_report(result))
            if not result["aa_normal_text"]:
                sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
