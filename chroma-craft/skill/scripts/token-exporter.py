#!/usr/bin/env python3
"""
token-exporter.py - Chroma-Craft Multi-Platform Design Token Exporter

Exports Chroma-Craft color palettes and domain token architectures into
industry-standard frontend and design system token formats:
- CSS Custom Properties (CSS variables with dark mode support)
- Tailwind CSS (v3 / v4 theme extension)
- W3C Design Tokens Community Group (DTCG) specification JSON
- SCSS variables
- Swift (iOS Color extension)
- Android XML (res/values/colors.xml)

Author: SWAYAM KIRAN PRABHU
Part of chroma-craft (agent-dev-skills)
License: MIT
"""

import sys
import argparse
import json
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Import definitions from palette_generator safely
import importlib.util
palette_gen_path = Path(__file__).parent / "palette-generator.py"
spec = importlib.util.spec_from_file_location("palette_generator", str(palette_gen_path))
palette_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(palette_mod)

COLOR_ROSTER = palette_mod.COLOR_ROSTER
DOMAIN_DIRECTIVES = palette_mod.DOMAIN_DIRECTIVES


def export_dtcg_json(domain_key: str) -> str:
    """Exports to W3C Design Tokens Community Group JSON format."""
    domain = DOMAIN_DIRECTIVES[domain_key]
    tokens = {
        "$schema": "https://design-tokens.github.io/community-group/format/",
        "color": {
            "global": {},
            "theme": {
                "light": {},
                "dark": {}
            }
        },
        "gradient": {
            "cta": {"$value": domain["cta_gradient"], "$type": "gradient"},
            "background": {"$value": domain["background_gradients"][0]["css"], "$type": "gradient"}
        }
    }

    # Global color primitives
    for name, data in COLOR_ROSTER.items():
        slug = name.lower().replace(" ", "-")
        tokens["color"]["global"][slug] = {
            "$value": data["hex"],
            "$type": "color",
            "$description": f"{data['category']} — {data['tone']}"
        }

    # Semantic aliases
    for mode in ["light", "dark"]:
        source = domain[f"primary_palette_{mode}"]
        for role, color_ref in source.items():
            hex_val = COLOR_ROSTER[color_ref]["hex"] if color_ref in COLOR_ROSTER else color_ref
            tokens["color"]["theme"][mode][role] = {
                "$value": hex_val,
                "$type": "color",
                "$description": f"Semantic token for {role} ({color_ref})"
            }

    return json.dumps(tokens, indent=2)


def export_scss(domain_key: str) -> str:
    """Exports SCSS variables."""
    domain = DOMAIN_DIRECTIVES[domain_key]
    lines = [
        f"// Chroma-Craft SCSS Tokens: {domain['name']}",
        "// Global Palette Primitives"
    ]
    for name, data in COLOR_ROSTER.items():
        slug = name.lower().replace(" ", "-")
        lines.append(f"${slug}: {data['hex']};")

    lines.append("\n// Semantic Tokens (Default Light)")
    for role, col in domain["primary_palette_light"].items():
        hex_val = COLOR_ROSTER[col]["hex"] if col in COLOR_ROSTER else col
        lines.append(f"${role}: {hex_val}; // {col}")

    lines.append(f"\n$gradient-cta: {domain['cta_gradient']};")
    lines.append(f"$gradient-hero: {domain['background_gradients'][0]['css']};")
    return "\n".join(lines)


def export_swift(domain_key: str) -> str:
    """Exports iOS Swift Color extension."""
    domain = DOMAIN_DIRECTIVES[domain_key]
    lines = [
        "import SwiftUI",
        "",
        f"// MARK: - ChromaCraft {domain['name'].replace(' ', '')} Theme",
        "extension Color {",
        "    struct ChromaCraft {"
    ]
    for role, col in domain["primary_palette_light"].items():
        hex_val = (COLOR_ROSTER[col]["hex"] if col in COLOR_ROSTER else col).lstrip("#")
        r = int(hex_val[0:2], 16) / 255.0
        g = int(hex_val[2:4], 16) / 255.0
        b = int(hex_val[4:6], 16) / 255.0
        camel_role = "".join(w.capitalize() if i > 0 else w for i, w in enumerate(role.split("-")))
        lines.append(f"        static let {camel_role} = Color(red: {r:.3f}, green: {g:.3f}, blue: {b:.3f}) // #{hex_val}")
    lines.append("    }")
    lines.append("}")
    return "\n".join(lines)


def export_android_xml(domain_key: str) -> str:
    """Exports Android res/values/colors.xml."""
    domain = DOMAIN_DIRECTIVES[domain_key]
    lines = [
        "<?xml version=\"1.0\" encoding=\"utf-8\"?>",
        f"<!-- Chroma-Craft Tokens: {domain['name']} -->",
        "<resources>"
    ]
    for role, col in domain["primary_palette_light"].items():
        hex_val = COLOR_ROSTER[col]["hex"] if col in COLOR_ROSTER else col
        tag_name = role.replace("-", "_")
        lines.append(f"    <color name=\"{tag_name}\">{hex_val}</color>")
    lines.append("</resources>")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Chroma-Craft Design Token Exporter")
    parser.add_argument("domain", choices=list(DOMAIN_DIRECTIVES.keys()), help="Target domain archetype")
    parser.add_argument("--format", choices=["css", "tailwind", "dtcg", "scss", "swift", "android"], default="css", help="Target export format")
    parser.add_argument("--output", "-o", help="Optional output file path")
    args = parser.parse_args()

    content = ""
    if args.format == "css":
        content = palette_mod.export_palette_css(args.domain)
    elif args.format == "tailwind":
        content = palette_mod.export_tailwind_config(args.domain)
    elif args.format == "dtcg":
        content = export_dtcg_json(args.domain)
    elif args.format == "scss":
        content = export_scss(args.domain)
    elif args.format == "swift":
        content = export_swift(args.domain)
    elif args.format == "android":
        content = export_android_xml(args.domain)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(content + "\n")
        print(f"Exported {args.domain} tokens to {args.output} ({args.format})")
    else:
        print(content)


if __name__ == "__main__":
    main()
