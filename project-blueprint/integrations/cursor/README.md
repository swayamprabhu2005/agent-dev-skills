# Cursor Integration

This integration connects Project Blueprint to Cursor.

---

## Verified Capabilities in Cursor

* **Agent Skills (`.cursor/skills/`):** Cursor supports the open `SKILL.md` format placed in `.cursor/skills/<skill-name>/SKILL.md`.
* **Cursor Rules (`.cursor/rules/*.mdc`):** Cursor allows ambient or intent-scoped rules. We provide `project-blueprint.mdc` to enforce planning gates.

---

## Installation Options

### Option 1: Native Agent Skill
Place the canonical `skill/` directory into `.cursor/skills/project-blueprint/`:

```bash
mkdir -p .cursor/skills
# Linux/macOS:
ln -s /path/to/project-blueprint/skill .cursor/skills/project-blueprint
# Or copy:
cp -r /path/to/project-blueprint/skill .cursor/skills/project-blueprint
```

### Option 2: Ambient Rule Integration
Copy `project-blueprint.mdc` into `.cursor/rules/`:

```bash
mkdir -p .cursor/rules
cp integrations/cursor/project-blueprint.mdc .cursor/rules/
```
