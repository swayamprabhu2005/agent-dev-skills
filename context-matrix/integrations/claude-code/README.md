# Claude Code Integration

This integration connects the canonical Context Matrix skill to Anthropic Claude Code.

---

## Installation

### Project-Level Installation
Copy the canonical `skill/` directory into your project's `.claude/skills/context-matrix/` directory:

```bash
mkdir -p .claude/skills/context-matrix
cp -r /path/to/agent-dev-skills/context-matrix/skill/* .claude/skills/context-matrix/
```

### Global Installation
Copy into your global Claude configuration directory:

* **Linux / macOS:** `~/.claude/skills/context-matrix/`
* **Windows:** `%USERPROFILE%\.claude\skills\cats\`

```bash
mkdir -p ~/.claude/skills/context-matrix
cp -r /path/to/agent-dev-skills/context-matrix/skill/* ~/.claude/skills/context-matrix/
```

---

## CLAUDE.md Rules Snippet

To activate prompt engineering discipline ambiently in Claude Code, add the following to your project's `CLAUDE.md`:

```markdown
## Prompt Engineering & Framework Selection
When formulating complex tasks, architecture plans, educational guides, or prompt designs:
- Reference the Context Matrix skill located in `.claude/skills/context-matrix/SKILL.md`.
- Select from the 8 frameworks: CLARITY (coding), SOCRATES (architecture), ANTICIPATE (tutorials), PARTNER (research), TRUST (advisory), RIPPLE (code review), CATCH (concise), MAGIC (creative).
- Adhere to the 10-point Quality Checklist before finalizing prompts.
```
