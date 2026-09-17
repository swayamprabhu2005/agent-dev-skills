# Claude Code Integration

This integration provides instructions for loading Project Blueprint into Claude Code.

---

## Verified Capabilities in Claude Code

* **Skill Discovery:** Discovered via `.claude/skills/<skill-name>/SKILL.md` (project-local) or `~/.claude/skills/<skill-name>/SKILL.md` (global/personal).
* **Progressive Disclosure:** Reads YAML frontmatter at startup and activates when tasks involve planning new projects, designing architecture, or modeling databases.
* **Standard Conformance:** Follows the open `agentskills.io` standard.

---

## Installation Options

### Option 1: Project-Specific Skill
```bash
mkdir -p .claude/skills
# Linux/macOS:
ln -s /path/to/project-blueprint/skill .claude/skills/project-blueprint
# Or copy:
cp -r /path/to/project-blueprint/skill .claude/skills/project-blueprint
```

### Option 2: Global Personal Skill
```bash
mkdir -p ~/.claude/skills/project-blueprint
cp -r /path/to/project-blueprint/skill/* ~/.claude/skills/project-blueprint/
```

### Option 3: Complementary `CLAUDE.md` Instruction
Add this instruction to your project's `CLAUDE.md` to guarantee that Claude Code invokes Project Blueprint before writing non-trivial new features:

```markdown
## Pre-Implementation Planning Gate
For non-trivial new features or projects, invoke Project Blueprint (.claude/skills/project-blueprint/SKILL.md). You MUST obtain explicit user approval on the generated blueprint documents before writing any production code.
```
