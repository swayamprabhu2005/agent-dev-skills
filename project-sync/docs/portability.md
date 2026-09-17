# Cross-Platform Portability & Compatibility Guide

Project Sync is engineered to run portably across modern agentic development environments.

---

## 1. Platform Capability Matrix

| Platform | Core Methodology | Native Skill Discovery | Native Rules Support | Lifecycle Hooks | Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Google Antigravity** | ✅ Supported | `.agents/skills/` or `~/.gemini/config/` | `AGENTS.md` / `GEMINI.md` | Supported (`hooks.json`) | **Verified Support** |
| **Claude Code** | ✅ Supported | `.claude/skills/` or `~/.claude/skills/` | `CLAUDE.md` | Via `CLAUDE.md` rules | **Verified Support** |
| **Cursor** | ✅ Supported | `.cursor/skills/` or `~/.cursor/skills/` | `.cursor/rules/*.mdc` | Via `.mdc` rules | **Verified Support** |
| **OpenAI Codex** | ✅ Supported | `.codex/skills/` or `.agents/skills/` | `AGENTS.md` | Via `AGENTS.md` instructions | **Verified Support** |
| **Generic Agent Skills** | ✅ Supported | Runtime dependent (`.skills/`) | Platform dependent | Platform dependent | **Standards-Compatible** |

---

## 2. Directory Conventions Comparison

| Platform | Project Skills Directory | User Skills Directory | Ambient Rules |
| :--- | :--- | :--- | :--- |
| **Google Antigravity** | `.agents/skills/project-sync/` | `~/.gemini/config/skills/project-sync/` | `AGENTS.md` / `GEMINI.md` |
| **Claude Code** | `.claude/skills/project-sync/` | `~/.claude/skills/project-sync/` | `CLAUDE.md` |
| **Cursor** | `.cursor/skills/project-sync/` | `~/.cursor/skills/project-sync/` | `.cursor/rules/project-sync.mdc` |
| **OpenAI Codex** | `.codex/skills/project-sync/` | `~/.codex/skills/project-sync/` | `AGENTS.md` |
