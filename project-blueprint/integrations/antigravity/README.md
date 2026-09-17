# Google Antigravity Integration

This integration connects the canonical Project Blueprint skill to Google Antigravity (AGY).

---

## Verified Capabilities in Antigravity

* **Skill Discovery:** Discovered via `.agents/skills/<skill-name>/SKILL.md` (project-local) or `~/.gemini/config/skills/<skill-name>/SKILL.md` (global).
* **Progressive Disclosure:** Antigravity indexes `name` and `description` from YAML frontmatter on startup and injects full instructions upon activation.
* **Slash Command Registration:** Once registered as a skill, users can trigger Project Blueprint by typing `/project-blueprint` in the Antigravity chat interface.
* **Artifact Review Panel:** Project Blueprint artifacts generated in `docs/project-blueprint/` render directly in Antigravity's rich artifact viewing interface with clickable links and native Mermaid rendering.

---

## Installation Options

### Option 1: Direct Project Skill
Link or copy the canonical `skill/` directory into your project's `.agents/skills/project-blueprint/` directory:

```bash
mkdir -p .agents/skills
# Linux/macOS:
ln -s /path/to/project-blueprint/skill .agents/skills/project-blueprint
# Or copy:
cp -r /path/to/project-blueprint/skill .agents/skills/project-blueprint
```

### Option 2: Global Skill (Applies to all workspaces)
Copy the skill into your Antigravity user configuration directory:

* **Linux / macOS:** `~/.gemini/config/skills/project-blueprint/`
* **Windows:** `%USERPROFILE%\.gemini\config\skills\project-blueprint\`

```bash
mkdir -p ~/.gemini/config/skills/project-blueprint
cp -r /path/to/project-blueprint/skill/* ~/.gemini/config/skills/project-blueprint/
```

### Option 3: Antigravity Plugin Bundle
```bash
mkdir -p ~/.gemini/config/plugins/project-blueprint/skills/project-blueprint
cp integrations/antigravity/plugin.json ~/.gemini/config/plugins/project-blueprint/
cp -r skill/* ~/.gemini/config/plugins/project-blueprint/skills/project-blueprint/
```
