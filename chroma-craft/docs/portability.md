# Chroma-Craft Cross-Platform Portability

> **How Chroma-Craft runs seamlessly across Google Antigravity, Claude Code, OpenAI Codex, and Cursor.**

---

## 1. Universal Agent Skills Compliance

Chroma-Craft strictly adheres to the open [Agent Skills Specification](https://agentskills.io). It is vendor-neutral, zero-dependency, and works across modern AI coding environments without proprietary lock-in.

---

## 2. Integration Adapters

### A. Google Antigravity (AGY)
- **Plugin Manifest:** Located in `integrations/antigravity/plugin.json`.
- **Loading:** Discovered automatically when placed in the workspace or global skills directory (`~/.gemini/antigravity/skills/chroma-craft/`).
- **Tools:** Agents invoke `palette-generator.py`, `wcag-checker.py`, and `token-exporter.py` via native bash/PowerShell tool calls.

### B. Claude Code
- **Skill Discovery:** Discovered in `.claude/skills/chroma-craft/` or referenced directly from the project root.
- **Workflow:** Claude Code loads `skill/SKILL.md` when asked to create or style frontends and automatically runs CLI scripts for contrast checks.

### C. OpenAI Codex / ChatGPT Agent
- **Instructions:** Located in `integrations/codex/agents-instructions.md`.
- **Integration:** Imported as system instructions or project rules for code generation runs.

### D. Cursor
- **Rule File:** Standard MDC rule file located in `integrations/cursor/chroma-craft.mdc`.
- **Trigger:** Applies whenever CSS, Tailwind, or frontend components (`.tsx`, `.jsx`, `.vue`, `.svelte`, `.css`) are being edited.

---

## 3. Zero External Dependencies

All Chroma-Craft scripts (`palette-generator.py`, `wcag-checker.py`, `token-exporter.py`, `test-chroma-craft.py`) are implemented strictly using the Python standard library:
- No `pip install` required.
- Compatible with Python 3.9+.
- Cross-platform path handling (`pathlib.Path`).
- Safe UTF-8 console output reconfiguring across Windows PowerShell, macOS zsh, and Linux bash.
