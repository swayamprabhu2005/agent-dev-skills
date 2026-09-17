# Generic Agent Skills Integration

Project Blueprint is fully compliant with the open **Agent Skills** specification ([agentskills.io](https://agentskills.io)).

Any AI coding tool, IDE extension, or agent runtime implementing the open specification can execute Project Blueprint without vendor-proprietary plugins.

---

## Universal Installation

```bash
# Link or copy the canonical skill folder into your agent's configured skills path:
mkdir -p .skills
ln -s /path/to/project-blueprint/skill .skills/project-blueprint
```

If your platform relies on system prompt instructions, configure it to load `skill/SKILL.md` before undertaking major coding initiatives.
