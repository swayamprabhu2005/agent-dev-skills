# Google Antigravity Integration

This integration connects the canonical Context Matrix skill to Google Antigravity (AGY).

---

## Verified Capabilities in Antigravity

* **Native Skill Discovery:** Discovered via `.agents/skills/context-matrix/SKILL.md` (project-local) or `~/.gemini/config/skills/context-matrix/SKILL.md` (global).
* **Native Slash-Command Derivation:** Antigravity CLI and IDE derive slash commands directly from the installed skill directory name. Installing to `cats/` makes `/context-matrix` available natively.
* **Progressive Disclosure:** Antigravity indexes `name` and `description` from YAML frontmatter on startup and dynamically injects `SKILL.md` and referenced files only when invoked.
* **Plugin Packaging:** Can be installed as a bundled plugin in `.agents/plugins/context-matrix/` or `~/.gemini/config/plugins/context-matrix/` containing `plugin.json` and `skills/context-matrix/`.

---

## Installation Options

### Option 1: Direct Project Skill (Recommended for Repositories)
Copy the canonical `skill/` directory into your project's `.agents/skills/context-matrix/` directory:

```bash
# In your target project repository root:
mkdir -p .agents/skills/context-matrix
cp -r /path/to/agent-dev-skills/context-matrix/skill/* .agents/skills/context-matrix/
```

On Windows PowerShell:
```powershell
New-Item -ItemType Directory -Force -Path .agents\skills\cats
Copy-Item -Recurse -Force \path\to\agent-dev-skills\cats\skill\* .agents\skills\cats\
```

### Option 2: Global / Workstation Skill (Available across all projects)
Copy the skill into your Antigravity user configuration directory:

* **Linux / macOS:** `~/.gemini/config/skills/context-matrix/`
* **Windows:** `%USERPROFILE%\.gemini\config\skills\cats\`

```bash
mkdir -p ~/.gemini/config/skills/context-matrix
cp -r /path/to/agent-dev-skills/context-matrix/skill/* ~/.gemini/config/skills/context-matrix/
```

### Option 3: Antigravity Plugin Bundle
To package Context Matrix as an Antigravity plugin:

1. Create plugin directory:
   ```bash
   mkdir -p ~/.gemini/config/plugins/context-matrix/skills/context-matrix
   ```
2. Copy `plugin.json`:
   ```bash
   cp /path/to/agent-dev-skills/context-matrix/integrations/antigravity/plugin.json ~/.gemini/config/plugins/context-matrix/
   ```
3. Copy skill resources:
   ```bash
   cp -r /path/to/agent-dev-skills/context-matrix/skill/* ~/.gemini/config/plugins/context-matrix/skills/context-matrix/
   ```

---

## Verifying Discovery & Invocation

1. Start an Antigravity session.
2. Type `/context-matrix help` to verify native command discovery.
3. Try an automated routing invocation:
   ```text
   /context-matrix Implement a threadpool in Rust
   ```
4. Try an explicit framework:
   ```text
   /context-matrix socrates Evaluate database partitioning strategy for 10TB scale
   ```
5. Try prompt generation:
   ```text
   /context-matrix prompt Build a JWT authentication flow
   ```

---

## Troubleshooting

* **Command `/context-matrix` not found:** Ensure the directory is named `cats` (lowercase) and contains `SKILL.md` with valid YAML frontmatter.
* **Relative paths not resolving:** Ensure `references/` and `scripts/` are copied alongside `SKILL.md` inside `.agents/skills/context-matrix/`.
