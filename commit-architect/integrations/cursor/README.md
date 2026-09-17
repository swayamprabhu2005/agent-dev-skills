# Cursor Integration

This integration provides setup instructions for Cursor Agent workflows.

---

## Verified Capabilities in Cursor

* **Agent Skills (`.cursor/skills/`):** Cursor supports the open `SKILL.md` format placed in `.cursor/skills/<skill-name>/SKILL.md` (project-local) or `~/.cursor/skills/` (global).
* **Cursor Rules (`.cursor/rules/*.mdc`):** Cursor's native rule engine allows defining persistent or intent-triggered instructions. We provide `commit-architect.mdc` as a lightweight companion rule.
* **Legacy Compatibility:** For older Cursor workspaces relying on `.cursorrules`, a rule snippet can be appended directly.

---

## Installation Options

### Option 1: Native Agent Skill (Recommended)
Place the canonical `skill/` directory into `.cursor/skills/commit-architect/`:

```bash
mkdir -p .cursor/skills
# Linux/macOS symlink:
ln -s /path/to/commit-architect/skill .cursor/skills/commit-architect
# Or copy:
cp -r /path/to/commit-architect/skill .cursor/skills/commit-architect
```

### Option 2: Cursor Rule Integration
Copy the companion `.mdc` rule into your project's `.cursor/rules/` folder:

```bash
mkdir -p .cursor/rules
cp integrations/cursor/commit-architect.mdc .cursor/rules/
```

This ensures Cursor's agent keeps the Git safety guardrails and natural commit message conventions active during code generation sessions.
