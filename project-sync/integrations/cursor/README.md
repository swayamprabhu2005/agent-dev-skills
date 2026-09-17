# Cursor Integration

This integration provides setup instructions for using Project Sync with Cursor.

---

## Verified Capabilities in Cursor

* **Agent Skills (`.cursor/skills/`):** Cursor supports the open `SKILL.md` format placed in `.cursor/skills/<skill-name>/SKILL.md`.
* **Cursor Rules (`.cursor/rules/*.mdc`):** Cursor's rule system allows defining ambient guidelines. We provide `project-sync.mdc` to guide the agent to perform post-implementation synchronization.

---

## Installation Options

### Option 1: Native Agent Skill
Place the canonical `skill/` directory into `.cursor/skills/project-sync/`:

```bash
mkdir -p .cursor/skills
# Linux/macOS:
ln -s /path/to/project-sync/skill .cursor/skills/project-sync
# Or copy:
cp -r /path/to/project-sync/skill .cursor/skills/project-sync
```

### Option 2: Ambient Rule Integration
Copy the companion `.mdc` rule into your project's `.cursor/rules/` directory:

```bash
mkdir -p .cursor/rules
cp integrations/cursor/project-sync.mdc .cursor/rules/
```
