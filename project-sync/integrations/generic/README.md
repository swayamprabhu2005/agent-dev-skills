# Generic Agent Skills Integration

Project Sync complies with the open **Agent Skills** specification ([agentskills.io](https://agentskills.io)).

Any AI coding tool, IDE extension, or agent runtime that implements the open specification can discover and execute Project Sync without vendor lock-in.

---

## Universal Installation

```bash
# Link or copy the canonical skill folder into your agent's configured skills path:
mkdir -p .skills
ln -s /path/to/project-sync/skill .skills/project-sync
```

If your agent runtime relies on system prompt instructions, configure it to load `skill/SKILL.md` after implementation iterations.
