# Claude Code Integration for Chroma-Craft

This directory documents how to utilize Chroma-Craft within Anthropic's Claude Code CLI.

## Installation

Link or copy `chroma-craft/` into your project's `.claude/skills/` folder:

```bash
mkdir -p .claude/skills
cp -r path/to/chroma-craft .claude/skills/chroma-craft
```

Or add the following instruction to your project's `CLAUDE.md`:

```markdown
## Design & Color System
When creating, styling, or auditing web UI, consult the Chroma-Craft skill in `chroma-craft/skill/SKILL.md`. Always adhere to the 46-color canonical library, strict blue rules, and domain archetypes.
```

## CLI Verification
Claude Code will automatically invoke the Python scripts:
```bash
python chroma-craft/skill/scripts/palette-generator.py domain ecommerce --format css
python chroma-craft/skill/scripts/wcag-checker.py "#121214" "#FBFBFD"
```
