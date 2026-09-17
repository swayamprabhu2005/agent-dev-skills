# Google Antigravity Integration

This integration connects the canonical Project Sync skill to Google Antigravity (AGY).

---

## Verified Capabilities in Antigravity

* **Skill Discovery:** Discovered via `.agents/skills/<skill-name>/SKILL.md` (project-local) or `~/.gemini/config/skills/<skill-name>/SKILL.md` (global).
* **Progressive Disclosure:** Antigravity indexes `name` and `description` from YAML frontmatter on startup and loads the full instructions when triggered.
* **Plugin Packaging:** Can be installed as a bundled plugin inside `.agents/plugins/project-sync/` or `~/.gemini/config/plugins/project-sync/` containing `plugin.json`, `hooks.json`, and `skills/project-sync/`.
* **Ambient Guidelines:** Can be complemented with instructions in `AGENTS.md` or `GEMINI.md` to guarantee end-of-iteration execution.

---

## Installation Options

### Option 1: Direct Project Skill
Link or copy the canonical `skill/` directory into your project's `.agents/skills/project-sync/` directory:

```bash
mkdir -p .agents/skills
# Linux/macOS:
ln -s /path/to/project-sync/skill .agents/skills/project-sync
# Or copy:
cp -r /path/to/project-sync/skill .agents/skills/project-sync
```

### Option 2: Global Skill (Applies to all workspaces)
Copy the skill into your Antigravity user configuration directory:

* **Linux / macOS:** `~/.gemini/config/skills/project-sync/`
* **Windows:** `%USERPROFILE%\.gemini\config\skills\project-sync\`

```bash
mkdir -p ~/.gemini/config/skills/project-sync
cp -r /path/to/project-sync/skill/* ~/.gemini/config/skills/project-sync/
```

### Option 3: Plugin Bundle with Hooks
To package as an Antigravity plugin:
1. Create plugin directory:
   ```bash
   mkdir -p ~/.gemini/config/plugins/project-sync/skills/project-sync
   ```
2. Copy `plugin.json` and `hooks.json`:
   ```bash
   cp integrations/antigravity/plugin.json ~/.gemini/config/plugins/project-sync/
   cp integrations/antigravity/hooks.json ~/.gemini/config/plugins/project-sync/
   ```
3. Copy skill files:
   ```bash
   cp -r skill/* ~/.gemini/config/plugins/project-sync/skills/project-sync/
   ```
