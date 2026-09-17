# OpenAI Codex Integration

This integration provides setup instructions for OpenAI Codex and Codex-based agent environments.

---

## Verified Capabilities in Codex

* **Agent Skills:** Supports modular skills conformant to `agentskills.io` invoked on-demand or with `$project-sync`.
* **Instruction Systems (`AGENTS.md`):** Supports persistent, hierarchical instructions in project root or global `~/.codex/AGENTS.md`.

---

## Installation Options

### Option 1: Native Agent Skill
Install the skill into your project's `.codex/skills/` or `.agents/skills/` directory:

```bash
mkdir -p .codex/skills
# Linux/macOS:
ln -s /path/to/project-sync/skill .codex/skills/project-sync
# Or copy:
cp -r /path/to/project-sync/skill .codex/skills/project-sync
```

### Option 2: Persistent Instructions via `AGENTS.md`
Append the contents of `integrations/codex/agents-instructions.md` to your repository's root `AGENTS.md`:

```bash
cat integrations/codex/agents-instructions.md >> AGENTS.md
```
