# OpenAI Codex / AGENTS.md Integration

This integration connects the canonical Context Matrix skill to OpenAI Codex and agents utilizing the `AGENTS.md` open convention.

---

## Installation

### Project-Level Installation
Copy the canonical `skill/` directory into your project's `.agents/skills/context-matrix/` (or `.codex/skills/context-matrix/`):

```bash
mkdir -p .agents/skills/context-matrix
cp -r /path/to/agent-dev-skills/context-matrix/skill/* .agents/skills/context-matrix/
```

### AGENTS.md Configuration
Append the contents of `agents-instructions.md` to your workspace root `AGENTS.md` to ensure automatic framework awareness.
