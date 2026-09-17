# Claude Code Integration

This integration provides setup instructions for loading Project Sync into Claude Code.

---

## Verified Capabilities in Claude Code

* **Skill Discovery:** Discovered via `.claude/skills/<skill-name>/SKILL.md` (project-local) or `~/.claude/skills/<skill-name>/SKILL.md` (global/personal).
* **Progressive Disclosure:** Reads YAML frontmatter at session startup and activates when tasks involve completing an implementation iteration, updating documentation, or managing repository ignore rules.
* **Standard Conformance:** Follows the open `agentskills.io` standard.

---

## Installation Options

### Option 1: Project-Specific Skill
```bash
mkdir -p .claude/skills
# Linux/macOS:
ln -s /path/to/project-sync/skill .claude/skills/project-sync
# Or copy:
cp -r /path/to/project-sync/skill .claude/skills/project-sync
```

### Option 2: Global Personal Skill
```bash
mkdir -p ~/.claude/skills/project-sync
cp -r /path/to/project-sync/skill/* ~/.claude/skills/project-sync/
```

### Option 3: Complementary `CLAUDE.md` Instruction (Recommended)
To ensure Claude Code automatically remembers to invoke Project Sync after completing meaningful implementation milestones, add this note to your project's `CLAUDE.md`:

```markdown
## Post-Implementation Hygiene
After completing and validating a meaningful coding milestone, invoke Project Sync (.claude/skills/project-sync/SKILL.md) to reconcile README.md and .gitignore, and provide the structured completion summary.
```
