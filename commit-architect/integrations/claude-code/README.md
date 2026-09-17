# Claude Code Integration

This integration provides instructions for loading Commit Architect into Claude Code.

---

## Verified Capabilities in Claude Code

* **Skill Discovery:** Discovered via `.claude/skills/<skill-name>/SKILL.md` (project-local) or `~/.claude/skills/<skill-name>/SKILL.md` (global/personal).
* **Progressive Disclosure:** Reads YAML frontmatter (`name` and `description`) at startup, loading the full `SKILL.md` and referenced files only when triggered by matching user prompts.
* **Standard Compatibility:** Claude Code natively supports the open Agent Skills standard (`agentskills.io`).
* **Session Reloading:** Note that Claude Code reads skills on startup; restart the session after adding or modifying skill files.

---

## Installation Options

### Option 1: Project-Specific Skill
To enable Commit Architect for a specific repository:

```bash
# In your target repository:
mkdir -p .claude/skills
# On Linux/macOS:
ln -s /path/to/commit-architect/skill .claude/skills/commit-architect
# Or copy:
cp -r /path/to/commit-architect/skill .claude/skills/commit-architect
```

### Option 2: Global Personal Skill
To make Commit Architect available across all Claude Code sessions on your machine:

```bash
mkdir -p ~/.claude/skills/commit-architect
cp -r /path/to/commit-architect/skill/* ~/.claude/skills/commit-architect/
```

### Option 3: Complementary `CLAUDE.md` Hint (Optional)
If you want Claude Code to always keep Git architecture top-of-mind during broad tasks, add this concise line to your project's `CLAUDE.md`:

```markdown
## Git Workflow
Follow the Commit Architect skill (.claude/skills/commit-architect/SKILL.md) for planning, staging, and committing changes into clean, atomic, logical commits with natural developer messages.
```
