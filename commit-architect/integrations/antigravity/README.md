# Google Antigravity Integration

This integration connects the canonical Commit Architect skill to Google Antigravity (AGY).

---

## Verified Capabilities in Antigravity

* **Skill Discovery:** Discovered via `.agents/skills/<skill-name>/SKILL.md` (project-local) or `~/.gemini/config/skills/<skill-name>/SKILL.md` (global).
* **Progressive Disclosure:** Antigravity indexes `name` and `description` from YAML frontmatter on startup and only injects the full `SKILL.md` body when activated.
* **Plugin Packaging:** Can be installed as a bundle inside `.agents/plugins/commit-architect/` or `~/.gemini/config/plugins/commit-architect/` containing `plugin.json` and `skills/commit-architect/`.
* **Rules Integration:** Ambient guidelines can also be mirrored in `AGENTS.md` or `GEMINI.md`.

---

## Installation Options

### Option 1: Direct Project Skill (Recommended for Repositories)
Link or copy the canonical `skill/` directory into your project's `.agents/skills/commit-architect/` directory:

```bash
# In your target project repository root:
mkdir -p .agents/skills
# On Linux/macOS:
ln -s /path/to/commit-architect/skill .agents/skills/commit-architect
# On Windows (PowerShell Administrator):
# New-Item -ItemType SymbolicLink -Path .agents\skills\commit-architect -Target \path\to\commit-architect\skill
```

Or copy the directory directly:
```bash
cp -r /path/to/commit-architect/skill .agents/skills/commit-architect
```

### Option 2: Global Skill (Applies to all your Antigravity workspaces)
Copy the skill into your Antigravity user configuration directory:

* **Linux / macOS:** `~/.gemini/config/skills/commit-architect/`
* **Windows:** `%USERPROFILE%\.gemini\config\skills\commit-architect\`

```bash
mkdir -p ~/.gemini/config/skills/commit-architect
cp -r /path/to/commit-architect/skill/* ~/.gemini/config/skills/commit-architect/
```

### Option 3: Antigravity Plugin Bundle
To install as a packaged plugin in your global Antigravity plugins directory:

1. Create plugin folder:
   ```bash
   mkdir -p ~/.gemini/config/plugins/commit-architect/skills/commit-architect
   ```
2. Copy `plugin.json`:
   ```bash
   cp integrations/antigravity/plugin.json ~/.gemini/config/plugins/commit-architect/
   ```
3. Copy skill files:
   ```bash
   cp -r skill/* ~/.gemini/config/plugins/commit-architect/skills/commit-architect/
   ```

Antigravity will automatically detect the plugin and enable it on the next session.
