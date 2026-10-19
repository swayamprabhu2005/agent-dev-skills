# Generic Agent Skills Specification Integration

This integration allows Context Matrix to run in any agent runtime conforming to the open [Agent Skills Specification](https://agentskills.io).

---

## Standard Installation

Most Agent Skills runtimes search for skills inside a `.skills/` or `.agents/skills/` directory at the project root:

```bash
mkdir -p .agents/skills/context-matrix
cp -r /path/to/agent-dev-skills/context-matrix/skill/* .agents/skills/context-matrix/
```

The runtime will parse `SKILL.md` frontmatter and make the skill available to the agent dynamically.
