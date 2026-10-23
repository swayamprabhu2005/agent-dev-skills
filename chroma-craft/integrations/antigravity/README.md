# Google Antigravity Integration for Chroma-Craft

This directory contains configuration files for running Chroma-Craft inside Google Antigravity (AGY).

## Installation

### Option 1: Workspace Installation (Local to Project)
Place the `chroma-craft/` directory in your workspace under `.agent/skills/` or in your project root. Antigravity will automatically index `skill/SKILL.md`.

### Option 2: Global Installation
Copy `chroma-craft/` to your global Antigravity skills directory:
- Windows: `%USERPROFILE%\.gemini\antigravity\skills\chroma-craft\`
- macOS/Linux: `~/.gemini/antigravity/skills/chroma-craft/`

## Usage with Antigravity
Whenever you ask Antigravity to:
- "Design a color scheme for an e-commerce website"
- "Create CSS variables for a dark mode hackathon dashboard"
- "Audit the color contrast of my button components"

Antigravity will load Chroma-Craft, apply the appropriate domain archetype, and run the Python scripts to calculate exact WCAG ratios.
