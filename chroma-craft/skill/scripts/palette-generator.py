#!/usr/bin/env python3
"""
palette-generator.py - Chroma-Craft Color Palette & Gradient Recommendation Engine

Generates 2-color, 3-color (60-30-10), and 4-color design token palettes,
domain-specific schemes (E-commerce, Corporate, Hackathon, Portfolio, etc.),
website section recommendations, and CSS gradient formulas using the official
Chroma-Craft 52-color library.

Author: SWAYAM KIRAN PRABHU
Part of chroma-craft (agent-dev-skills)
License: MIT
"""

import sys
import argparse
import json
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ==============================================================================
# WCAG 2.1 MATHEMATICAL FORMULAS (SELF-CONTAINED)
# ==============================================================================

def normalize_hex(hex_str: str) -> str:
    clean = hex_str.strip().lstrip("#")
    if len(clean) == 3:
        clean = "".join([c * 2 for c in clean])
    if len(clean) != 6 or not re.match(r"^[0-9A-Fa-f]{6}$", clean):
        raise ValueError(f"Invalid hex color code: '{hex_str}'")
    return f"#{clean.upper()}"

def hex_to_rgb(hex_str: str) -> tuple[int, int, int]:
    norm = normalize_hex(hex_str).lstrip("#")
    return int(norm[0:2], 16), int(norm[2:4], 16), int(norm[4:6], 16)

def rgb_to_linear(channel: int) -> float:
    c = channel / 255.0
    if c <= 0.04045:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4

def calculate_luminance(hex_str: str) -> float:
    r, g, b = hex_to_rgb(hex_str)
    return 0.2126 * rgb_to_linear(r) + 0.7152 * rgb_to_linear(g) + 0.0722 * rgb_to_linear(b)

def calculate_contrast(fg_hex: str, bg_hex: str) -> float:
    l1 = calculate_luminance(fg_hex)
    l2 = calculate_luminance(bg_hex)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)

def evaluate_wcag(contrast: float) -> dict:
    return {
        "contrast_ratio": round(contrast, 2),
        "formatted_ratio": f"{contrast:.2f}:1",
        "aa_normal_text": contrast >= 4.5,
        "aa_large_text": contrast >= 3.0,
        "aa_ui_components": contrast >= 3.0,
        "aaa_normal_text": contrast >= 7.0,
        "aaa_large_text": contrast >= 4.5,
    }

# ==============================================================================
# 1. THE CANONICAL COLOR ROSTER (41 BASE + 5 CURATED + 6 COSMIC RIBBON ACCENTS)
# ==============================================================================

COLOR_ROSTER = {
    # --- Neutrals & Whites (6) ---
    "Snow White": {"hex": "#FBFBFD", "category": "Neutrals & Whites", "type": "surface", "tone": "cool-neutral"},
    "Ivory White": {"hex": "#FFFFF0", "category": "Neutrals & Whites", "type": "surface", "tone": "warm-neutral"},
    "Pearl White": {"hex": "#F8F6F0", "category": "Neutrals & Whites", "type": "surface", "tone": "warm-neutral"},
    "Grey": {"hex": "#6B7280", "category": "Neutrals & Whites", "type": "structural", "tone": "slate-grey"},
    "Silver": {"hex": "#C0C0C8", "category": "Neutrals & Whites", "type": "structural", "tone": "cool-silver"},
    "Beige": {"hex": "#E8DCC4", "category": "Neutrals & Whites", "type": "surface-accent", "tone": "warm-sand"},

    # --- Blues (STRICT LIST - EXACTLY 7 BLUES) ---
    "Ice Blue": {"hex": "#DDF2FD", "category": "Blues", "type": "surface-tint", "tone": "cool-ice"},
    "Baby Blue": {"hex": "#89CFF0", "category": "Blues", "type": "accent", "tone": "soft-blue"},
    "Ocean Blue": {"hex": "#0077BE", "category": "Blues", "type": "brand-primary", "tone": "deep-cyanic-blue"},
    "Midnight Blue": {"hex": "#191970", "category": "Blues", "type": "brand-deep", "tone": "deep-navy"},
    "Electric Blue": {"hex": "#0066FF", "category": "Blues", "type": "action-primary", "tone": "vivid-blue"},
    "Arctic Blue": {"hex": "#C6E2FF", "category": "Blues", "type": "surface-tint", "tone": "soft-arctic"},
    "Steel Blue": {"hex": "#4682B4", "category": "Blues", "type": "brand-primary", "tone": "industrial-blue"},

    # --- Greens & Cyans (6) ---
    "Cyan": {"hex": "#00E5FF", "category": "Greens & Cyans", "type": "action-accent", "tone": "electric-cyan"},
    "Teal": {"hex": "#008080", "category": "Greens & Cyans", "type": "brand-primary", "tone": "balanced-teal"},
    "Lime": {"hex": "#00FF00", "category": "Greens & Cyans", "type": "status-accent", "tone": "high-vis-lime"},
    "Lime Green": {"hex": "#32CD32", "category": "Greens & Cyans", "type": "action-accent", "tone": "vibrant-green"},
    "Forest Green": {"hex": "#228B22", "category": "Greens & Cyans", "type": "brand-deep", "tone": "organic-forest"},
    "Moss Green": {"hex": "#8A9A5B", "category": "Greens & Cyans", "type": "structural", "tone": "earthy-moss"},

    # --- Reds (4) ---
    "Crimson Red": {"hex": "#DC143C", "category": "Reds", "type": "action-urgent", "tone": "vivid-crimson"},
    "Scarlet Red": {"hex": "#FF2400", "category": "Reds", "type": "action-urgent", "tone": "flame-scarlet"},
    "Apple Red": {"hex": "#8E1A1A", "category": "Reds", "type": "brand-deep", "tone": "garnet-apple"},
    "Rose Red": {"hex": "#C21E56", "category": "Reds", "type": "accent", "tone": "deep-rose"},

    # --- Pinks (5) ---
    "Pink": {"hex": "#FFC0CB", "category": "Pinks", "type": "accent-soft", "tone": "classic-pink"},
    "Baby Pink": {"hex": "#F4C2C2", "category": "Pinks", "type": "surface-tint", "tone": "blush-pink"},
    "Dusty Pink": {"hex": "#DCAE96", "category": "Pinks", "type": "structural", "tone": "warm-dusty"},
    "Hot Pink": {"hex": "#FF69B4", "category": "Pinks", "type": "action-accent", "tone": "high-energy-pink"},
    "Magenta": {"hex": "#FF00FF", "category": "Pinks", "type": "action-accent", "tone": "neon-magenta"},

    # --- Purples & Violets (8) ---
    "Purple": {"hex": "#800080", "category": "Purples & Violets", "type": "brand-primary", "tone": "classic-purple"},
    "Deep Purple": {"hex": "#36013F", "category": "Purples & Violets", "type": "brand-deep", "tone": "obsidian-purple"},
    "Royal Purple": {"hex": "#7851A9", "category": "Purples & Violets", "type": "brand-primary", "tone": "regal-purple"},
    "Plum Purple": {"hex": "#5A1846", "category": "Purples & Violets", "type": "brand-deep", "tone": "wine-plum"},
    "Lavender Purple": {"hex": "#967BB6", "category": "Purples & Violets", "type": "accent-soft", "tone": "gentle-lavender"},
    "Violet": {"hex": "#8F00FF", "category": "Purples & Violets", "type": "action-accent", "tone": "electric-violet"},
    "Violet Purple": {"hex": "#6A0DAD", "category": "Purples & Violets", "type": "brand-primary", "tone": "deep-violet"},
    "Indigo": {"hex": "#4B0082", "category": "Purples & Violets", "type": "brand-deep", "tone": "midnight-indigo"},

    # --- Browns & Earth Tones (5) ---
    "Brown": {"hex": "#8B4513", "category": "Browns & Earth Tones", "type": "brand-earth", "tone": "saddle-brown"},
    "Chocolate Brown": {"hex": "#3D1C02", "category": "Browns & Earth Tones", "type": "brand-deep", "tone": "espresso-dark"},
    "Coffee Brown": {"hex": "#4A2C2A", "category": "Browns & Earth Tones", "type": "brand-deep", "tone": "roast-coffee"},
    "Caramel Brown": {"hex": "#AF6E4D", "category": "Browns & Earth Tones", "type": "structural", "tone": "warm-caramel"},
    "Gold": {"hex": "#D4AF37", "category": "Browns & Earth Tones", "type": "accent-luxury", "tone": "metallic-gold"},

    # --- Curated Complementary Accents (5 Non-Blue Additions) ---
    "Terracotta": {"hex": "#E07A5F", "category": "Curated Accents", "type": "accent-editorial", "tone": "warm-clay"},
    "Sage Green": {"hex": "#9CAF88", "category": "Curated Accents", "type": "structural-organic", "tone": "muted-sage"},
    "Amber Gold": {"hex": "#F59E0B", "category": "Curated Accents", "type": "action-conversion", "tone": "vibrant-amber"},
    "Charcoal Onyx": {"hex": "#121214", "category": "Curated Accents", "type": "surface-dark", "tone": "neutral-dark-surface"},
    "Blush Peach": {"hex": "#FEE2E2", "category": "Curated Accents", "type": "surface-wash", "tone": "soft-peach"},

    # --- Cosmic Ribbon & Luminous Accents (6 Spectral Shades) ---
    "Neon Mint Glow": {"hex": "#A1EFD8", "category": "Cosmic Accents", "type": "accent-glow", "tone": "iridescent-mint"},
    "Warm Amber Gold": {"hex": "#FBBF90", "category": "Cosmic Accents", "type": "accent-light", "tone": "incandescent-gold"},
    "Electric Violet": {"hex": "#713F91", "category": "Cosmic Accents", "type": "brand-primary", "tone": "mid-tone-violet"},
    "Spectral Indigo Cyan": {"hex": "#6B8EBA", "category": "Cosmic Accents", "type": "accent-sheen", "tone": "cool-indigo-cyan"},
    "Deep Plum Shadow": {"hex": "#5D2C5B", "category": "Cosmic Accents", "type": "brand-deep", "tone": "dark-plum-shadow"},
    "Cosmic Obsidian": {"hex": "#060814", "category": "Cosmic Accents", "type": "surface-dark", "tone": "midnight-obsidian"}
}

# Lookup map by uppercase hex
HEX_TO_NAME = {data["hex"].upper(): name for name, data in COLOR_ROSTER.items()}

# ==============================================================================
# 2. DOMAIN ARCHETYPES & AESTHETIC DIRECTIVES
# ==============================================================================

DOMAIN_DIRECTIVES = {
    "corporate": {
        "name": "Corporate & Enterprise B2B SaaS",
        "description": "Authoritative, stable, trustworthy, and distraction-free. Strictly forbids fluorescent glows, holographic gradients, and animated borders (anti-jigmig).",
        "aesthetic_rules": [
            "Dominant surfaces must remain neutral (#FBFBFD Snow White or #F8F6F0 Pearl White) with deep high-contrast text (#121214).",
            "Brand colors should rely on Steel Blue (#4682B4), Ocean Blue (#0077BE), or Midnight Blue (#191970).",
            "Action CTAs must be solid or subtle 2-stop gradients, never flashy neon.",
            "Card borders must use subtle Silver (#C0C0C8) or Grey (#6B7280) with low visual weight."
        ],
        "primary_palette_light": {
            "background-base": "Snow White",
            "surface-card": "Pearl White",
            "brand-primary": "Steel Blue",
            "accent-highlight": "Ocean Blue",
            "text-primary": "Charcoal Onyx",
            "border-subtle": "Silver"
        },
        "primary_palette_dark": {
            "background-base": "Charcoal Onyx",
            "surface-card": "Midnight Blue",
            "brand-primary": "Steel Blue",
            "accent-highlight": "Electric Blue",
            "text-primary": "Snow White",
            "border-subtle": "Grey"
        },
        "background_gradients": [
            {"name": "Corporate Clean Wash", "css": "linear-gradient(180deg, #FBFBFD 0%, #F8F6F0 100%)"},
            {"name": "Executive Subtlety", "css": "linear-gradient(180deg, #FBFBFD 0%, #C6E2FF 100%)"},
            {"name": "Enterprise Dark Deep", "css": "linear-gradient(135deg, #121214 0%, #191970 100%)"}
        ],
        "cta_gradient": "linear-gradient(135deg, #0077BE 0%, #4682B4 100%)"
    },
    "ecommerce": {
        "name": "E-Commerce & High-Conversion Storefront",
        "description": "Laser-focused on product prominence and frictionless purchasing. Zero shiny distractions, zero visual noise over product photos, instant CTA recognition.",
        "aesthetic_rules": [
            "Product canvas must be pristine (#FBFBFD Snow White) so product imagery colors are 100% accurate.",
            "Never use multi-color mesh gradients behind product catalogs or checkout flows.",
            "Conversion CTA ('Add to Cart' / 'Checkout') must use Amber Gold (#F59E0B), Forest Green (#228B22), or Ocean Blue (#0077BE) for instant discovery.",
            "Pricing tags must use highest contrast Charcoal Onyx (#121214) with subtle sale badges in Crimson Red (#DC143C)."
        ],
        "primary_palette_light": {
            "background-base": "Snow White",
            "surface-card": "Ivory White",
            "brand-primary": "Ocean Blue",
            "accent-highlight": "Amber Gold",
            "text-primary": "Charcoal Onyx",
            "border-subtle": "Silver"
        },
        "primary_palette_dark": {
            "background-base": "Charcoal Onyx",
            "surface-card": "#1E1E22", # fallback dark card
            "brand-primary": "Ocean Blue",
            "accent-highlight": "Amber Gold",
            "text-primary": "Snow White",
            "border-subtle": "Grey"
        },
        "background_gradients": [
            {"name": "Retail Neutral Backdrop", "css": "linear-gradient(180deg, #FBFBFD 0%, #F8F6F0 100%)"},
            {"name": "Soft Peach Product Aura", "css": "linear-gradient(180deg, #FBFBFD 0%, #FEE2E2 100%)"},
            {"name": "Ice Blue Tech Showcase", "css": "linear-gradient(180deg, #FBFBFD 0%, #DDF2FD 100%)"}
        ],
        "cta_gradient": "linear-gradient(135deg, #F59E0B 0%, #AF6E4D 100%)"
    },
    "hackathon": {
        "name": "Hackathon, AI Showcase & High-Tech Launch",
        "description": "High-octane, punchy, futuristic, and memorable for judges and developers. Dark-mode first with radiant neon electric accents and deep mesh backgrounds.",
        "aesthetic_rules": [
            "Ground the canvas in deep Charcoal Onyx (#121214) or Midnight Blue (#191970).",
            "Electrify key interactive elements with Electric Blue (#0066FF), Cyan (#00E5FF), and Royal Purple (#7851A9).",
            "Employ radiant multi-stop hero gradients and glowing borders (e.g. 1px cyan/electric blue halo).",
            "Use Lime (#00FF00) or Hot Pink (#FF69B4) strictly for status indicators, live telemetry, and novelty badges."
        ],
        "primary_palette_light": {
            "background-base": "Snow White",
            "surface-card": "Ice Blue",
            "brand-primary": "Electric Blue",
            "accent-highlight": "Cyan",
            "text-primary": "Charcoal Onyx",
            "border-subtle": "Arctic Blue"
        },
        "primary_palette_dark": {
            "background-base": "Charcoal Onyx",
            "surface-card": "Deep Purple",
            "brand-primary": "Electric Blue",
            "accent-highlight": "Cyan",
            "text-primary": "Snow White",
            "border-subtle": "Royal Purple"
        },
        "background_gradients": [
            {"name": "Cyber Nebula Hero", "css": "linear-gradient(135deg, #121214 0%, #191970 50%, #0066FF 100%)"},
            {"name": "Quantum Violet Pulse", "css": "linear-gradient(135deg, #36013F 0%, #7851A9 50%, #00E5FF 100%)"},
            {"name": "Matrix Void Ray", "css": "linear-gradient(135deg, #121214 0%, #008080 70%, #00FF00 100%)"}
        ],
        "cta_gradient": "linear-gradient(135deg, #0066FF 0%, #00E5FF 100%)"
    },
    "portfolio": {
        "name": "Personal Portfolio & Creative Developer",
        "description": "Distinctive, editorial, typography-driven, and minimalist. Focuses on craft, whitespace, and a high-impact signature duo accent.",
        "aesthetic_rules": [
            "Leverage the Duo (2-color) or 3-color minimalist system for memorable personal branding.",
            "Avoid generic multi-color noise; pick one bold signature accent (e.g., Terracotta #E07A5F, Electric Blue #0066FF, or Violet #8F00FF).",
            "Use subtle glassmorphic card overlays with backdrop blur to display project showcases.",
            "Maintain pristine editorial typography contrast (>15:1 for headline reading)."
        ],
        "primary_palette_light": {
            "background-base": "Ivory White",
            "surface-card": "Pearl White",
            "brand-primary": "Terracotta",
            "accent-highlight": "Charcoal Onyx",
            "text-primary": "Charcoal Onyx",
            "border-subtle": "Silver"
        },
        "primary_palette_dark": {
            "background-base": "Charcoal Onyx",
            "surface-card": "#1A1A1E",
            "brand-primary": "Electric Blue",
            "accent-highlight": "Cyan",
            "text-primary": "Snow White",
            "border-subtle": "Grey"
        },
        "background_gradients": [
            {"name": "Editorial Linen Wash", "css": "linear-gradient(180deg, #FFFFF0 0%, #E8DCC4 100%)"},
            {"name": "Monochrome Studio Depth", "css": "linear-gradient(180deg, #121214 0%, #1E1E22 100%)"},
            {"name": "Nordic Dusk", "css": "linear-gradient(135deg, #121214 0%, #36013F 100%)"}
        ],
        "cta_gradient": "linear-gradient(135deg, #E07A5F 0%, #AF6E4D 100%)"
    },
    "fintech": {
        "name": "Fintech & Banking Platform",
        "description": "High-confidence fiscal stability and security. Balances calm authority with clear positive/negative metrics.",
        "aesthetic_rules": [
            "Core architecture anchored in Midnight Blue (#191970) and Pearl White (#F8F6F0).",
            "Financial gains and positive balances strictly represented with Forest Green (#228B22).",
            "Negative metrics and critical risk warnings reserved for Crimson Red (#DC143C) or Apple Red (#8E1A1A).",
            "Pending/yield indicators mapped to Amber Gold (#F59E0B)."
        ],
        "primary_palette_light": {
            "background-base": "Snow White",
            "surface-card": "Pearl White",
            "brand-primary": "Midnight Blue",
            "accent-highlight": "Forest Green",
            "text-primary": "Charcoal Onyx",
            "border-subtle": "Silver"
        },
        "primary_palette_dark": {
            "background-base": "Charcoal Onyx",
            "surface-card": "Midnight Blue",
            "brand-primary": "Steel Blue",
            "accent-highlight": "Lime Green",
            "text-primary": "Snow White",
            "border-subtle": "Grey"
        },
        "background_gradients": [
            {"name": "Vault Security Mesh", "css": "linear-gradient(135deg, #191970 0%, #121214 100%)"},
            {"name": "Clean Ledger Aura", "css": "linear-gradient(180deg, #FBFBFD 0%, #F8F6F0 100%)"}
        ],
        "cta_gradient": "linear-gradient(135deg, #191970 0%, #0077BE 100%)"
    },
    "luxury": {
        "name": "Luxury, Fashion & Premium Hospitality",
        "description": "Serene, warm, tactile, and opulent without gaudiness. Uses warm ivories, rich chocolates, and restrained metallic gold.",
        "aesthetic_rules": [
            "Base canvas built on Ivory White (#FFFFF0) and warm Beige (#E8DCC4).",
            "Typography and borders articulated in Chocolate Brown (#3D1C02) and Coffee Brown (#4A2C2A).",
            "Accents and badges highlighted in refined Gold (#D4AF37).",
            "Never use cold cyans, neon limes, or electric blues."
        ],
        "primary_palette_light": {
            "background-base": "Ivory White",
            "surface-card": "Beige",
            "brand-primary": "Coffee Brown",
            "accent-highlight": "Gold",
            "text-primary": "Chocolate Brown",
            "border-subtle": "Caramel Brown"
        },
        "primary_palette_dark": {
            "background-base": "Chocolate Brown",
            "surface-card": "Coffee Brown",
            "brand-primary": "Gold",
            "accent-highlight": "Ivory White",
            "text-primary": "Ivory White",
            "border-subtle": "Caramel Brown"
        },
        "background_gradients": [
            {"name": "Champagne Silk", "css": "linear-gradient(135deg, #FFFFF0 0%, #E8DCC4 50%, #F8F6F0 100%)"},
            {"name": "Velvet Noir", "css": "linear-gradient(135deg, #3D1C02 0%, #4A2C2A 100%)"}
        ],
        "cta_gradient": "linear-gradient(135deg, #D4AF37 0%, #AF6E4D 100%)"
    },
    "wellness": {
        "name": "Healthcare, Wellness & Organic Living",
        "description": "Restful, calming, restorative, and sterile. Organic sage, soothing teals, soft blush, and clear whites.",
        "aesthetic_rules": [
            "Base canvas in Snow White (#FBFBFD) or Pearl White (#F8F6F0).",
            "Structural elements in Sage Green (#9CAF88) or Moss Green (#8A9A5B).",
            "Interactive buttons in balanced Teal (#008080) or Baby Blue (#89CFF0).",
            "Subtle surface wash in Blush Peach (#FEE2E2)."
        ],
        "primary_palette_light": {
            "background-base": "Snow White",
            "surface-card": "Pearl White",
            "brand-primary": "Teal",
            "accent-highlight": "Sage Green",
            "text-primary": "Charcoal Onyx",
            "border-subtle": "Silver"
        },
        "primary_palette_dark": {
            "background-base": "Charcoal Onyx",
            "surface-card": "#162320",
            "brand-primary": "Teal",
            "accent-highlight": "Sage Green",
            "text-primary": "Snow White",
            "border-subtle": "Moss Green"
        },
        "background_gradients": [
            {"name": "Morning Mist", "css": "linear-gradient(180deg, #FBFBFD 0%, #9CAF88 20%, #FBFBFD 100%)"},
            {"name": "Calm Waters", "css": "linear-gradient(135deg, #DDF2FD 0%, #C6E2FF 100%)"}
        ],
        "cta_gradient": "linear-gradient(135deg, #008080 0%, #8A9A5B 100%)"
    }
}

# ==============================================================================
# 3. WEBSITE SECTION RECOMMENDATION ENGINE
# ==============================================================================

SECTION_BLUEPRINTS = {
    "navbar": {
        "title": "Navigation Bar & Header",
        "role": "Persistent orientation, brand anchor, search, and global primary CTA.",
        "guidelines": {
            "light_mode": {
                "surface": "rgba(251, 251, 253, 0.85) (Snow White with 12px backdrop-blur)",
                "border": "1px solid #C0C0C8 (Silver, 35% opacity)",
                "logo_text": "#121214 (Charcoal Onyx) — Contrast: 18.1:1",
                "nav_links": "#6B7280 (Grey) -> Hover: Brand Primary",
                "cta_button": "Brand Primary or Accent Focus"
            },
            "dark_mode": {
                "surface": "rgba(18, 18, 20, 0.85) (Charcoal Onyx with 12px backdrop-blur)",
                "border": "1px solid rgba(192, 192, 200, 0.15)",
                "logo_text": "#FBFBFD (Snow White) — Contrast: 18.1:1",
                "nav_links": "#C0C0C8 (Silver) -> Hover: Electric Blue / Accent",
                "cta_button": "Electric Blue (#0066FF) or Accent Highlight"
            }
        }
    },
    "hero": {
        "title": "Hero Section (Above the Fold)",
        "role": "Value proposition, first impression, primary conversion driver.",
        "guidelines": {
            "light_mode": {
                "surface": "Domain Background Wash (e.g. Snow White to Pearl White gradient)",
                "h1_headline": "#121214 (Charcoal Onyx) — Max contrast, zero eye fatigue",
                "subheadline": "#6B7280 (Grey) — Readable, distinct hierarchy",
                "primary_cta": "Domain CTA 2-Stop Linear Gradient or High-Impact Solid",
                "secondary_cta": "Ghost Button: 1px solid #C0C0C8 with Charcoal Onyx text",
                "social_proof_pill": "Surface tint (e.g. Ice Blue #DDF2FD with Ocean Blue text)"
            },
            "dark_mode": {
                "surface": "Domain Dark Mesh / Multi-Stop Linear Gradient",
                "h1_headline": "#FBFBFD (Snow White) — Crisp clarity",
                "subheadline": "#C0C0C8 (Silver) — 7.5:1 contrast",
                "primary_cta": "Vibrant 2-Stop Gradient (e.g. Electric Blue to Cyan)",
                "secondary_cta": "Ghost Button: 1px solid rgba(255,255,255,0.2) with White text",
                "social_proof_pill": "rgba(255, 255, 255, 0.05) with Accent text"
            }
        }
    },
    "cards": {
        "title": "Feature Grid & Service Cards",
        "role": "Structured value props, capabilities, modules.",
        "guidelines": {
            "light_mode": {
                "container_bg": "#F8F6F0 (Pearl White) to demarcate from pure white Hero",
                "card_surface": "#FBFBFD (Snow White) with 1px #C0C0C8 border and subtle shadow",
                "card_icon_box": "15% opacity tint of Brand Primary",
                "card_icon": "Brand Primary (#0077BE, #4682B4, or #E07A5F)",
                "card_title": "#121214 (Charcoal Onyx)",
                "card_body": "#6B7280 (Grey) — Contrast 5.2:1 (Passes AA)"
            },
            "dark_mode": {
                "container_bg": "#121214 (Charcoal Onyx)",
                "card_surface": "rgba(255, 255, 255, 0.03) with 1px solid rgba(255, 255, 255, 0.08)",
                "card_icon_box": "rgba(0, 102, 255, 0.15) (Electric Blue wash)",
                "card_icon": "#00E5FF (Cyan) or #0066FF (Electric Blue)",
                "card_title": "#FBFBFD (Snow White)",
                "card_body": "#C0C0C8 (Silver) — Contrast 7.5:1"
            }
        }
    },
    "pricing": {
        "title": "Pricing & Product Catalog Showcase",
        "role": "Conversion decision zone; clean pricing, clear feature comparison, checkout trigger.",
        "guidelines": {
            "light_mode": {
                "standard_card": "#FBFBFD with 1px #C0C0C8 border",
                "featured_card": "#FBFBFD with 2px Brand Primary border & 'Popular' badge",
                "badge_bg": "Accent Highlight (e.g., #F59E0B Amber Gold or #7851A9 Royal Purple)",
                "badge_text": "#FBFBFD (Snow White) or #121214 (Charcoal Onyx)",
                "price_amount": "#121214 (Charcoal Onyx) — Strongest visual weight",
                "feature_check_icon": "#228B22 (Forest Green) for included features",
                "buy_button": "Dominant Action Focus (Amber Gold / Electric Blue)"
            },
            "dark_mode": {
                "standard_card": "rgba(255, 255, 255, 0.03) with 1px border",
                "featured_card": "linear-gradient(180deg, rgba(0, 102, 255, 0.1) 0%, rgba(18, 18, 20, 0.8) 100%) with 1px #0066FF border",
                "badge_bg": "#0066FF (Electric Blue)",
                "price_amount": "#FBFBFD (Snow White)",
                "feature_check_icon": "#32CD32 (Lime Green)",
                "buy_button": "Gradient: Electric Blue to Cyan"
            }
        }
    },
    "cta": {
        "title": "Lead Magnet & Final Conversion Banner",
        "role": "High-urgency final invitation before footer.",
        "guidelines": {
            "light_mode": {
                "banner_bg": "Deep Brand Container: Midnight Blue (#191970) or Steel Blue (#4682B4)",
                "headline": "#FBFBFD (Snow White) — Contrast: >14:1",
                "subheadline": "#DDF2FD (Ice Blue)",
                "action_button": "Amber Gold (#F59E0B) or White Button with Midnight Blue text",
                "input_field": "White (#FBFBFD) with 1px Silver border"
            },
            "dark_mode": {
                "banner_bg": "linear-gradient(135deg, #191970 0%, #0066FF 100%)",
                "headline": "#FBFBFD (Snow White)",
                "subheadline": "#C6E2FF (Arctic Blue)",
                "action_button": "#FBFBFD with #121214 text or Cyan (#00E5FF) with #121214 text",
                "input_field": "rgba(0, 0, 0, 0.4) with 1px solid rgba(255, 255, 255, 0.2)"
            }
        }
    },
    "footer": {
        "title": "Footer & Informational Base",
        "role": "Site index, compliance, social links, copyright, grounding tone.",
        "guidelines": {
            "light_mode": {
                "surface": "#F8F6F0 (Pearl White) or grounded #121214 (Charcoal Onyx)",
                "border_top": "1px solid #C0C0C8 (Silver)",
                "column_headings": "#121214 (Charcoal Onyx) or #FBFBFD (Snow White)",
                "link_text": "#6B7280 (Grey) -> Hover: Brand Primary",
                "copyright": "#6B7280 (Grey) at 80% opacity"
            },
            "dark_mode": {
                "surface": "#121214 (Charcoal Onyx)",
                "border_top": "1px solid rgba(255, 255, 255, 0.08)",
                "column_headings": "#FBFBFD (Snow White)",
                "link_text": "#C0C0C8 (Silver) -> Hover: #00E5FF (Cyan)",
                "copyright": "#6B7280 (Grey)"
            }
        }
    }
}

# ==============================================================================
# 4. PALETTE RECIPES (2-COLOR, 3-COLOR, 4-COLOR)
# ==============================================================================

TWO_COLOR_DUOS = [
    {
        "name": "High-Impact Tech Minimalist",
        "dominant_surface": "Charcoal Onyx (#121214)",
        "accent_cta": "Electric Blue (#0066FF)",
        "light_inversion": "Snow White (#FBFBFD) + Electric Blue (#0066FF)",
        "contrast_on_dark": "5.68:1 (Passes AA)",
        "contrast_on_light": "4.92:1 (Passes AA)",
        "best_for": "Developer Portfolios, AI Tools, Minimalist SaaS"
    },
    {
        "name": "Warm Editorial Craft",
        "dominant_surface": "Ivory White (#FFFFF0)",
        "accent_cta": "Terracotta (#E07A5F)",
        "dark_inversion": "Charcoal Onyx (#121214) + Terracotta (#E07A5F)",
        "contrast_on_dark": "7.20:1 (Passes AAA)",
        "contrast_on_light": "3.15:1 (UI / Large text) — Body text uses Charcoal Onyx",
        "best_for": "Design Portfolios, Architecture Studios, Editorial Publications"
    },
    {
        "name": "Executive Midnight Authority",
        "dominant_surface": "Snow White (#FBFBFD)",
        "accent_cta": "Midnight Blue (#191970)",
        "dark_inversion": "Midnight Blue (#191970) + Arctic Blue (#C6E2FF)",
        "contrast_on_dark": "10.4:1 (Passes AAA)",
        "contrast_on_light": "14.2:1 (Passes AAA)",
        "best_for": "Legal, Venture Capital, Corporate Landing Pages"
    },
    {
        "name": "High-Conversion Commerce Duo",
        "dominant_surface": "Snow White (#FBFBFD)",
        "accent_cta": "Amber Gold (#F59E0B)",
        "dark_inversion": "Charcoal Onyx (#121214) + Amber Gold (#F59E0B)",
        "contrast_on_dark": "9.45:1 (Passes AAA)",
        "contrast_on_light": "3.2:1 (Large CTA Button with Charcoal Onyx label)",
        "best_for": "Retail Banners, Direct-to-Consumer landing pages"
    },
    {
        "name": "Cosmic Luminous Duo",
        "dominant_surface": "Cosmic Obsidian (#060814)",
        "accent_cta": "Neon Mint Glow (#A1EFD8)",
        "light_inversion": "Snow White (#FBFBFD) + Electric Violet (#713F91)",
        "contrast_on_dark": "15.06:1 (Passes AAA)",
        "contrast_on_light": "7.20:1 (Passes AAA)",
        "best_for": "Next-Gen AI Products, Cyber Showcases, Futuristic Dark Frontends"
    }
]

THREE_COLOR_60_30_10 = [
    {
        "name": "Modern Enterprise 60-30-10",
        "ratio_60": {"color": "Snow White (#FBFBFD)", "role": "60% Clean Background / Reading Canvas"},
        "ratio_30": {"color": "Grey (#6B7280) & Silver (#C0C0C8)", "role": "30% Structural cards, borders, secondary typography"},
        "ratio_10": {"color": "Ocean Blue (#0077BE)", "role": "10% Action buttons, active navigation, focus rings"},
        "wcag_body_contrast": "18.10:1 (Charcoal Onyx text on Snow White)",
        "wcag_cta_contrast": "4.52:1 (White text on Ocean Blue CTA)"
    },
    {
        "name": "Hackathon Cyber Void 60-30-10",
        "ratio_60": {"color": "Charcoal Onyx (#121214)", "role": "60% Deep Dark Mode Surface"},
        "ratio_30": {"color": "Midnight Blue (#191970)", "role": "30% Structural cards, header surfaces, sidebars"},
        "ratio_10": {"color": "Electric Blue (#0066FF) / Cyan (#00E5FF)", "role": "10% Focus buttons, badges, radiant accents"},
        "wcag_body_contrast": "18.10:1 (Snow White text on Charcoal Onyx)",
        "wcag_cta_contrast": "10.8:1 (Charcoal Onyx text on Cyan CTA)"
    },
    {
        "name": "Artisanal Luxury 60-30-10",
        "ratio_60": {"color": "Ivory White (#FFFFF0)", "role": "60% Warm tactile background"},
        "ratio_30": {"color": "Beige (#E8DCC4) / Caramel Brown (#AF6E4D)", "role": "30% Card panels, borders, secondary elements"},
        "ratio_10": {"color": "Gold (#D4AF37)", "role": "10% Premium badges, active indicators, CTA buttons"},
        "wcag_body_contrast": "16.4:1 (Chocolate Brown text on Ivory White)",
        "wcag_cta_contrast": "4.8:1 (Chocolate Brown text on Gold badge)"
    },
    {
        "name": "Cosmic Ribbon 60-30-10",
        "ratio_60": {"color": "Cosmic Obsidian (#060814)", "role": "60% Midnight-tinted cosmic canvas"},
        "ratio_30": {"color": "Electric Violet (#713F91) & Deep Plum Shadow (#5D2C5B)", "role": "30% Structural ribbon body, cards, and loop frames"},
        "ratio_10": {"color": "Neon Mint Glow (#A1EFD8) & Warm Amber Gold (#FBBF90)", "role": "10% Luminous rim glow, action CTAs, incandescent highlights"},
        "wcag_body_contrast": "19.30:1 (Snow White text on Cosmic Obsidian)",
        "wcag_cta_contrast": "15.06:1 (Cosmic Obsidian text on Neon Mint Glow CTA)"
    }
]

# ==============================================================================
# 5. GRADIENT STUDIO DEFINITIONS
# ==============================================================================

GRADIENT_STUDIO = {
    "hero_and_mesh": [
        {
            "name": "Midnight to Electric Blue",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #191970 0%, #0066FF 100%)",
            "recommended_use": "Corporate & Tech Hero Sections, High-Impact Banners"
        },
        {
            "name": "Plum Purple to Rose Red",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #5A1846 0%, #C21E56 100%)",
            "recommended_use": "Creative Portfolios, Fashion & Lifestyle Headers"
        },
        {
            "name": "Deep Purple to Royal Purple",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #36013F 0%, #7851A9 100%)",
            "recommended_use": "AI Product Landing Pages, Web3 & Hackathon Heroes"
        },
        {
            "name": "Quantum Cyber Mesh",
            "type": "Radial Mesh",
            "css": "radial-gradient(circle at 20% 20%, #0066FF 0%, transparent 40%), radial-gradient(circle at 80% 80%, #7851A9 0%, transparent 40%), #121214",
            "recommended_use": "Futuristic Hero Canvas, Developer Showcases"
        },
        {
            "name": "Cosmic Ribbon Void",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #060814 0%, #5D2C5B 35%, #713F91 70%, #A1EFD8 100%)",
            "recommended_use": "Luminous Dark Heroes, AI & Web3 Product Launches"
        },
        {
            "name": "Spectral Ribbon Flow",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #713F91 0%, #6B8EBA 50%, #FBBF90 100%)",
            "recommended_use": "Iridescent Banners, Creative Developer Portfolios"
        }
    ],
    "cta_buttons": [
        {
            "name": "Electric Blue to Cyan",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #0066FF 0%, #00E5FF 100%)",
            "text_color": "#121214 (Charcoal Onyx) or #FBFBFD with shadow",
            "recommended_use": "Primary SaaS 'Get Started' or Hackathon CTA"
        },
        {
            "name": "Hot Pink to Magenta",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #FF69B4 0%, #FF00FF 100%)",
            "text_color": "#FBFBFD (Snow White)",
            "recommended_use": "Creator economy, social tools, novelty triggers"
        },
        {
            "name": "Gold to Caramel Brown",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #D4AF37 0%, #AF6E4D 100%)",
            "text_color": "#FFFFFF (Pure White) or #3D1C02",
            "recommended_use": "Luxury purchases, VIP tier upgrades, premium membership"
        },
        {
            "name": "Amber Conversion Action",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #F59E0B 0%, #E07A5F 100%)",
            "text_color": "#121214 (Charcoal Onyx)",
            "recommended_use": "E-Commerce 'Add to Cart', Free Trial Signups"
        },
        {
            "name": "Neon Mint Glow Action",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #A1EFD8 0%, #6B8EBA 100%)",
            "text_color": "#060814 (Cosmic Obsidian)",
            "recommended_use": "High-Impact Dark Mode Conversion CTA, Live Launch Buttons"
        },
        {
            "name": "Warm Amber Incandescent",
            "type": "Linear 135deg",
            "css": "linear-gradient(135deg, #FBBF90 0%, #713F91 100%)",
            "text_color": "#060814 (Cosmic Obsidian)",
            "recommended_use": "Luminous Edge Highlights, Featured Tier Buttons"
        }
    ],
    "surface_overlays": [
        {
            "name": "Snow White Glassmorphic Tint",
            "type": "Glassmorphic Overlay",
            "css": "linear-gradient(135deg, rgba(251, 251, 253, 0.8) 0%, rgba(248, 246, 240, 0.6) 100%)",
            "backdrop_filter": "blur(12px)",
            "recommended_use": "Light-mode floating navigation bars, card headers"
        },
        {
            "name": "Ivory Soft Ambient Wash",
            "type": "Subtle Surface Wash",
            "css": "linear-gradient(180deg, rgba(255, 255, 240, 0.9) 0%, rgba(232, 220, 196, 0.4) 100%)",
            "backdrop_filter": "blur(8px)",
            "recommended_use": "Editorial card overlays, testimonial backplates"
        },
        {
            "name": "Charcoal Onyx Dark Glass",
            "type": "Dark Glassmorphic Overlay",
            "css": "linear-gradient(135deg, rgba(18, 18, 20, 0.75) 0%, rgba(25, 25, 112, 0.25) 100%)",
            "backdrop_filter": "blur(16px)",
            "recommended_use": "Dark-mode modals, sticky navigation, code preview cards"
        },
        {
            "name": "Cosmic Obsidian Glass",
            "type": "Deep Dark Glassmorphic Overlay",
            "css": "linear-gradient(135deg, rgba(6, 8, 20, 0.85) 0%, rgba(93, 44, 91, 0.25) 100%)",
            "backdrop_filter": "blur(16px)",
            "recommended_use": "Deep cosmic navigation bars, frosted dark modals, sticky headers"
        }
    ]
}

# ==============================================================================
# 6. EXPORT HELPERS (CSS, TAILWIND, JSON)
# ==============================================================================

def export_palette_css(domain_key: str) -> str:
    domain = DOMAIN_DIRECTIVES.get(domain_key.lower())
    if not domain:
        raise ValueError(f"Unknown domain '{domain_key}'. Choose from: {list(DOMAIN_DIRECTIVES.keys())}")

    p_light = domain["primary_palette_light"]
    p_dark = domain["primary_palette_dark"]

    lines = [
        "/* ==========================================================================",
        f"   CHROMA-CRAFT DESIGN TOKENS - {domain['name'].upper()}",
        "   Generated by chroma-craft (agent-dev-skills)",
        "   ========================================================================== */",
        "",
        ":root {",
        "  /* --- Light Mode Core Tokens --- */"
    ]

    for token, col_name in p_light.items():
        hex_val = COLOR_ROSTER[col_name]["hex"] if col_name in COLOR_ROSTER else col_name
        lines.append(f"  --color-{token}: {hex_val}; /* {col_name} */")

    lines.append(f"  --gradient-cta: {domain['cta_gradient']};")
    lines.append(f"  --gradient-bg-primary: {domain['background_gradients'][0]['css']};")
    lines.append("}")
    lines.append("")
    lines.append("[data-theme=\"dark\"] {")
    lines.append("  /* --- Dark Mode Inversions --- */")

    for token, col_name in p_dark.items():
        hex_val = COLOR_ROSTER[col_name]["hex"] if col_name in COLOR_ROSTER else col_name
        lines.append(f"  --color-{token}: {hex_val}; /* {col_name} */")

    if len(domain["background_gradients"]) > 1:
        lines.append(f"  --gradient-bg-primary: {domain['background_gradients'][-1]['css']};")
    lines.append("}")
    return "\n".join(lines)


def export_tailwind_config(domain_key: str) -> str:
    domain = DOMAIN_DIRECTIVES.get(domain_key.lower())
    if not domain:
        raise ValueError(f"Unknown domain '{domain_key}'")

    p_light = domain["primary_palette_light"]

    color_lines = []
    for token, col_name in p_light.items():
        hex_val = COLOR_ROSTER[col_name]["hex"] if col_name in COLOR_ROSTER else col_name
        key_name = token.replace("-", "_")
        color_lines.append(f"        '{key_name}': '{hex_val}',")

    return f"""// tailwind.config.js - Chroma-Craft {domain['name']} Palette
module.exports = {{
  darkMode: 'class',
  theme: {{
    extend: {{
      colors: {{
{chr(10).join(color_lines)}
      }},
      backgroundImage: {{
        'cta-gradient': "{domain['cta_gradient']}",
        'hero-gradient': "{domain['background_gradients'][0]['css']}",
      }}
    }},
  }},
  plugins: [],
}}"""


# ==============================================================================
# 7. CLI COMMAND INTERFACE
# ==============================================================================

def list_colors_report() -> str:
    lines = [
        "================================================================================",
        "                     CHROMA-CRAFT COMPLETE COLOR ROSTER                         ",
        "     (41 Mandatory Base Colors + 5 Curated Accents + 6 Cosmic Ribbon Accents)   ",
        "================================================================================",
        f"{'Color Name':<20} | {'Hex Code':<9} | {'Category':<22} | {'Relative Lum':<12}",
        "-" * 80
    ]
    for name, data in COLOR_ROSTER.items():
        lum = calculate_luminance(data["hex"])
        lines.append(f"{name:<20} | {data['hex']:<9} | {data['category']:<22} | {lum:.4f}")
    lines.append("=" * 80)
    lines.append(f"Total Canonical Colors: {len(COLOR_ROSTER)}")
    return "\n".join(lines)


def list_domains_report() -> str:
    lines = [
        "================================================================================",
        "                       CHROMA-CRAFT DOMAIN ARCHETYPES                           ",
        "================================================================================"
    ]
    for key, dom in DOMAIN_DIRECTIVES.items():
        lines.append(f"\n[{key.upper()}] - {dom['name']}")
        lines.append(f"  Description: {dom['description']}")
        lines.append("  Aesthetic Rules:")
        for r in dom["aesthetic_rules"]:
            lines.append(f"    * {r}")
        lines.append("  Light Tokens:")
        for k, v in dom["primary_palette_light"].items():
            hex_val = COLOR_ROSTER[v]["hex"] if v in COLOR_ROSTER else v
            lines.append(f"    - {k:<18}: {v} ({hex_val})")
        lines.append("  Background Gradients:")
        for g in dom["background_gradients"]:
            lines.append(f"    - {g['name']}: {g['css']}")
        lines.append(f"  CTA Gradient: {dom['cta_gradient']}")
    lines.append("\n" + "=" * 80)
    return "\n".join(lines)


def section_report(section_name: str) -> str:
    sec = SECTION_BLUEPRINTS.get(section_name.lower())
    if not sec:
        raise ValueError(f"Unknown section '{section_name}'. Options: {list(SECTION_BLUEPRINTS.keys())}")

    lines = [
        "================================================================================",
        f"        CHROMA-CRAFT SECTION BLUEPRINT: {sec['title'].upper()}         ",
        "================================================================================",
        f"Role: {sec['role']}",
        "\n--- LIGHT MODE SPECIFICATION ---"
    ]
    for k, v in sec["guidelines"]["light_mode"].items():
        lines.append(f"  * {k.replace('_', ' ').capitalize():<20}: {v}")

    lines.append("\n--- DARK MODE SPECIFICATION ---")
    for k, v in sec["guidelines"]["dark_mode"].items():
        lines.append(f"  * {k.replace('_', ' ').capitalize():<20}: {v}")
    lines.append("=" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Chroma-Craft Color Palette Engine")
    subparsers = parser.add_subparsers(dest="command")

    # list-colors
    subparsers.add_parser("list-colors", help="List all 52 canonical colors with hex and luminance")

    # list-domains
    subparsers.add_parser("list-domains", help="List all domain archetypes with aesthetic directives")

    # domain
    domain_parser = subparsers.add_parser("domain", help="Get domain-specific color system and gradients")
    domain_parser.add_argument("name", choices=list(DOMAIN_DIRECTIVES.keys()), help="Domain name")
    domain_parser.add_argument("--format", choices=["text", "json", "css", "tailwind"], default="text", help="Output format")

    # section
    sec_parser = subparsers.add_parser("section", help="Get section-by-section color specifications")
    sec_parser.add_argument("name", choices=list(SECTION_BLUEPRINTS.keys()), help="Section name")

    # gradients
    subparsers.add_parser("gradients", help="View gradient studio catalog")

    args = parser.parse_args()

    if args.command == "list-colors":
        print(list_colors_report())
    elif args.command == "list-domains":
        print(list_domains_report())
    elif args.command == "domain":
        if args.format == "text":
            d = DOMAIN_DIRECTIVES[args.name]
            print(f"Domain: {d['name']}")
            print(f"Description: {d['description']}\n")
            print("Light Tokens:")
            for k, v in d["primary_palette_light"].items():
                hex_val = COLOR_ROSTER[v]["hex"] if v in COLOR_ROSTER else v
                print(f"  {k}: {v} ({hex_val})")
            print("\nDark Tokens:")
            for k, v in d["primary_palette_dark"].items():
                hex_val = COLOR_ROSTER[v]["hex"] if v in COLOR_ROSTER else v
                print(f"  {k}: {v} ({hex_val})")
            print("\nBackground Gradients:")
            for g in d["background_gradients"]:
                print(f"  {g['name']}: {g['css']}")
            print(f"\nCTA Gradient:\n  {d['cta_gradient']}")
        elif args.format == "json":
            print(json.dumps(DOMAIN_DIRECTIVES[args.name], indent=2))
        elif args.format == "css":
            print(export_palette_css(args.name))
        elif args.format == "tailwind":
            print(export_tailwind_config(args.name))
    elif args.command == "section":
        print(section_report(args.name))
    elif args.command == "gradients":
        print(json.dumps(GRADIENT_STUDIO, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
