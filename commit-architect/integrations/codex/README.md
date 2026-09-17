# OpenAI Codex Integration

This integration provides setup instructions for OpenAI Codex and Codex-based agentic workflows.

---

## Verified Capabilities in Codex

* **Agent Skills:** Codex supports modular skills following the `agentskills.io` standard (`SKILL.md` with YAML frontmatter).
* **Instruction Systems (`AGENTS.md`):** Codex supports persistent, hierarchical guidelines via `AGENTS.md` in repository roots, subdirectories, or globally in `~/.codex/AGENTS.md`.
* **Skill Invocation:** Skills can be triggered automatically via task description matching or invoked directly in chat sessions (e.g., `$commit-architect`).

---

## Installation Options

### Option 1: Native Agent Skill
Install the skill into your project's `.codex/skills/` or `.agents/skills/` directory:

```bash
mkdir -p .codex/skills
# Linux/macOS symlink:
ln -s /path/to/commit-architect/skill .codex/skills/commit-architect
# Or copy:
cp -r /path/to/commit-architect/skill .codex/skills/commit-architect
```

### Option 2: Persistent Instructions via `AGENTS.md`
Append the contents of `integrations/codex/agents-instructions.md` to your repository's root `AGENTS.md` file:

```bash
cat integrations/codex/agents-instructions.md >> AGENTS.md
```

This guarantees that every Codex agent execution across the project adheres to the Commit Architect philosophy even when on-demand skill triggers are inactive.
