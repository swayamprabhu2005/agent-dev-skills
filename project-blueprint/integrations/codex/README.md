# OpenAI Codex Integration

This integration provides setup instructions for OpenAI Codex and Codex-based agent environments.

---

## Verified Capabilities in Codex

* **Agent Skills:** Supports modular skills following the `agentskills.io` standard invoked on-demand or via `$project-blueprint`.
* **Hierarchical Instructions (`AGENTS.md`):** Allows persistent enforcement of the pre-implementation approval gate across all repository interactions.

---

## Installation Options

### Option 1: Native Agent Skill
Install into `.codex/skills/` or `.agents/skills/`:

```bash
mkdir -p .codex/skills
# Linux/macOS:
ln -s /path/to/project-blueprint/skill .codex/skills/project-blueprint
# Or copy:
cp -r /path/to/project-blueprint/skill .codex/skills/project-blueprint
```

### Option 2: Persistent Instructions via `AGENTS.md`
Append `integrations/codex/agents-instructions.md` to your repository's `AGENTS.md`:

```bash
cat integrations/codex/agents-instructions.md >> AGENTS.md
```
