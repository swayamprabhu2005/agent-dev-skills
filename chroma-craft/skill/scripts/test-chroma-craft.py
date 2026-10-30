#!/usr/bin/env python3
"""
test-chroma-craft.py - Comprehensive Chroma-Craft Test Suite

Validates:
1. Canonical 52-color roster (41 base + 5 curated accents + 6 cosmic ribbon accents) with strict hex codes.
2. Strict blue roster integrity (only the 7 permitted blues).
3. WCAG 2.1 relative luminance and contrast ratio mathematical accuracy.
4. Domain archetypes and aesthetic directives integrity.
5. Section-by-section specification mappings.
6. Design token exports (CSS, Tailwind, DTCG JSON, SCSS).

Author: SWAYAM KIRAN PRABHU
Part of chroma-craft (agent-dev-skills)
License: MIT
"""

import sys
import os
import json
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import importlib.util
palette_gen_path = Path(__file__).parent / "palette-generator.py"
spec = importlib.util.spec_from_file_location("palette_generator", str(palette_gen_path))
palette_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(palette_mod)

wcag_checker_path = Path(__file__).parent / "wcag-checker.py"
spec_wcag = importlib.util.spec_from_file_location("wcag_checker", str(wcag_checker_path))
wcag_mod = importlib.util.module_from_spec(spec_wcag)
spec_wcag.loader.exec_module(wcag_mod)

token_exp_path = Path(__file__).parent / "token-exporter.py"
spec_token = importlib.util.spec_from_file_location("token_exporter", str(token_exp_path))
token_mod = importlib.util.module_from_spec(spec_token)
spec_token.loader.exec_module(token_mod)


def test_color_roster_exactness():
    roster = palette_mod.COLOR_ROSTER
    assert len(roster) == 52, f"Expected exactly 52 colors, got {len(roster)}"

    expected_colors = {
        # Neutrals (6)
        "Snow White": "#FBFBFD",
        "Ivory White": "#FFFFF0",
        "Pearl White": "#F8F6F0",
        "Grey": "#6B7280",
        "Silver": "#C0C0C8",
        "Beige": "#E8DCC4",
        # Blues (7 STRICT)
        "Ice Blue": "#DDF2FD",
        "Baby Blue": "#89CFF0",
        "Ocean Blue": "#0077BE",
        "Midnight Blue": "#191970",
        "Electric Blue": "#0066FF",
        "Arctic Blue": "#C6E2FF",
        "Steel Blue": "#4682B4",
        # Greens & Cyans (6)
        "Cyan": "#00E5FF",
        "Teal": "#008080",
        "Lime": "#00FF00",
        "Lime Green": "#32CD32",
        "Forest Green": "#228B22",
        "Moss Green": "#8A9A5B",
        # Reds (4)
        "Crimson Red": "#DC143C",
        "Scarlet Red": "#FF2400",
        "Apple Red": "#8E1A1A",
        "Rose Red": "#C21E56",
        # Pinks (5)
        "Pink": "#FFC0CB",
        "Baby Pink": "#F4C2C2",
        "Dusty Pink": "#DCAE96",
        "Hot Pink": "#FF69B4",
        "Magenta": "#FF00FF",
        # Purples & Violets (8)
        "Purple": "#800080",
        "Deep Purple": "#36013F",
        "Royal Purple": "#7851A9",
        "Plum Purple": "#5A1846",
        "Lavender Purple": "#967BB6",
        "Violet": "#8F00FF",
        "Violet Purple": "#6A0DAD",
        "Indigo": "#4B0082",
        # Browns & Earth Tones (5)
        "Brown": "#8B4513",
        "Chocolate Brown": "#3D1C02",
        "Coffee Brown": "#4A2C2A",
        "Caramel Brown": "#AF6E4D",
        "Gold": "#D4AF37",
        # Curated Complementary Accents (5)
        "Terracotta": "#E07A5F",
        "Sage Green": "#9CAF88",
        "Amber Gold": "#F59E0B",
        "Charcoal Onyx": "#121214",
        "Blush Peach": "#FEE2E2",
        # Cosmic Ribbon & Luminous Accents (6)
        "Neon Mint Glow": "#A1EFD8",
        "Warm Amber Gold": "#FBBF90",
        "Electric Violet": "#713F91",
        "Spectral Indigo Cyan": "#6B8EBA",
        "Deep Plum Shadow": "#5D2C5B",
        "Cosmic Obsidian": "#060814"
    }

    for name, hex_code in expected_colors.items():
        assert name in roster, f"Missing color: {name}"
        assert roster[name]["hex"].upper() == hex_code.upper(), f"Hex mismatch for {name}: expected {hex_code}, got {roster[name]['hex']}"

    # Strict blue check: ensure no unexpected blues are in the blues category
    blues_in_roster = [name for name, data in roster.items() if data["category"] == "Blues"]
    assert len(blues_in_roster) == 7, f"Blues list must have strictly 7 colors, found {len(blues_in_roster)}"
    print("  [PASS] Canonical 52-color roster and strict blue list verified.")


def test_wcag_mathematics():
    # Pure white vs pure black test
    white_lum = wcag_mod.calculate_luminance("#FFFFFF")
    black_lum = wcag_mod.calculate_luminance("#000000")
    assert abs(white_lum - 1.0) < 0.001
    assert abs(black_lum - 0.0) < 0.001

    cr_max = wcag_mod.calculate_contrast("#FFFFFF", "#000000")
    assert abs(cr_max - 21.0) < 0.01

    # Charcoal Onyx vs Snow White
    cr = wcag_mod.calculate_contrast("#121214", "#FBFBFD")
    assert cr > 18.0, f"Expected >18:1 contrast, got {cr}"

    # Cosmic Obsidian vs Neon Mint Glow
    cr_cosmic = wcag_mod.calculate_contrast("#060814", "#A1EFD8")
    assert cr_cosmic > 15.0, f"Expected >15:1 contrast, got {cr_cosmic}"

    eval_data = wcag_mod.evaluate_wcag(cr)
    assert eval_data["aa_normal_text"] is True
    assert eval_data["aaa_normal_text"] is True
    assert eval_data["aa_large_text"] is True

    # Low contrast pair (e.g. Silver on Snow White)
    cr_low = wcag_mod.calculate_contrast("#C0C0C8", "#FBFBFD")
    assert cr_low < 3.0
    eval_low = wcag_mod.evaluate_wcag(cr_low)
    assert eval_low["aa_normal_text"] is False
    print("  [PASS] WCAG 2.1 relative luminance and contrast calculations verified.")


def test_domain_archetypes():
    domains = palette_mod.DOMAIN_DIRECTIVES
    expected_domains = ["corporate", "ecommerce", "hackathon", "portfolio", "fintech", "luxury", "wellness"]

    for d in expected_domains:
        assert d in domains, f"Missing domain directive: {d}"
        data = domains[d]
        assert "aesthetic_rules" in data and len(data["aesthetic_rules"]) > 0
        assert "primary_palette_light" in data
        assert "primary_palette_dark" in data
        assert "background_gradients" in data and len(data["background_gradients"]) > 0
        assert "cta_gradient" in data

        # Check that light mode text-primary against background-base has AA contrast
        p_light = data["primary_palette_light"]
        bg_name = p_light["background-base"]
        text_name = p_light.get("text-primary", "Charcoal Onyx")
        bg_hex = palette_mod.COLOR_ROSTER[bg_name]["hex"] if bg_name in palette_mod.COLOR_ROSTER else bg_name
        text_hex = palette_mod.COLOR_ROSTER[text_name]["hex"] if text_name in palette_mod.COLOR_ROSTER else text_name
        cr = wcag_mod.calculate_contrast(text_hex, bg_hex)
        assert cr >= 4.5, f"Domain {d} fails WCAG AA text contrast: {cr:.2f}:1"

    print("  [PASS] All 7 domain archetypes and text contrasts verified.")


def test_section_blueprints():
    sections = palette_mod.SECTION_BLUEPRINTS
    expected_sections = ["navbar", "hero", "cards", "pricing", "cta", "footer"]
    for s in expected_sections:
        assert s in sections, f"Missing section blueprint: {s}"
        sec = sections[s]
        assert "light_mode" in sec["guidelines"]
        assert "dark_mode" in sec["guidelines"]
    print("  [PASS] All 6 website section blueprints verified.")


def test_token_exporters():
    for d in ["corporate", "ecommerce", "hackathon"]:
        css = palette_mod.export_palette_css(d)
        assert ":root {" in css
        assert "[data-theme=\"dark\"] {" in css
        assert "--color-background-base:" in css

        tailwind = palette_mod.export_tailwind_config(d)
        assert "module.exports" in tailwind
        assert "backgroundImage:" in tailwind

        dtcg = token_mod.export_dtcg_json(d)
        dtcg_obj = json.loads(dtcg)
        assert "color" in dtcg_obj
        assert "global" in dtcg_obj["color"]
        assert "theme" in dtcg_obj["color"]

        scss = token_mod.export_scss(d)
        assert "$background-base:" in scss

    print("  [PASS] Token exporters (CSS, Tailwind, DTCG JSON, SCSS) verified.")


def main():
    print("Running Chroma-Craft Skill Verification Suite...")
    test_color_roster_exactness()
    test_wcag_mathematics()
    test_domain_archetypes()
    test_section_blueprints()
    test_token_exporters()
    print("\nALL 5 TEST SUITES PASSED PERFECTLY (100% SUCCESS)!")


if __name__ == "__main__":
    main()
