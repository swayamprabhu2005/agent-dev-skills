# Cross-Platform Portability & Compatibility Guide

Commit Architect is engineered to operate seamlessly across modern agentic development environments. This document outlines platform compatibility levels, discovery mechanisms, and portability considerations.

---

## 1. Platform Capability Matrix

| Platform | Core Methodology | Native Skill Discovery | Native Rules Support | Status |
| :--- | :---: | :---: | :---: | :--- |
| **Google Antigravity** | ✅ Supported | `.agents/skills/` or `~/.gemini/config/` | `AGENTS.md` / `GEMINI.md` | **Verified Support** |
| **Claude Code** | ✅ Supported | `.claude/skills/` or `~/.claude/skills/` | `CLAUDE.md` | **Verified Support** |
| **Cursor** | ✅ Supported | `.cursor/skills/` or `~/.cursor/skills/` | `.cursor/rules/*.mdc` | **Verified Support** |
| **OpenAI Codex** | ✅ Supported | `.codex/skills/` or `.agents/skills/` | `AGENTS.md` | **Verified Support** |
| **Generic Agent Skills** | ✅ Supported | Varies by runtime (`.skills/`) | Platform dependent | **Standards-Compatible** |
| **Vanilla Chat LLMs** | ✅ Supported (Manual) | ❌ No native discovery | ❌ System prompt only | **Manual / Unsupported** |

### Status Definitions:
* **Verified Support:** Officially verified through platform documentation and testing. Native directory conventions and progressive disclosure work as specified.
* **Standards-Compatible:** Conforms to the open `agentskills.io` standard. Works on any platform implementing this specification.
* **Experimental:** Mechanism is subject to upstream beta changes.
* **Unsupported:** Platform lacks native skill discovery or local file system execution capabilities.

---

## 2. Directory Conventions Comparison

| Platform | Project-Level Skills Directory | Global / User Skills Directory | Ambient Rules File |
| :--- | :--- | :--- | :--- |
| **Google Antigravity** | `.agents/skills/<name>/` | `~/.gemini/config/skills/<name>/` | `AGENTS.md` / `GEMINI.md` |
| **Claude Code** | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` | `CLAUDE.md` |
| **Cursor** | `.cursor/skills/<name>/` | `~/.cursor/skills/<name>/` | `.cursor/rules/*.mdc` |
| **OpenAI Codex** | `.codex/skills/<name>/` | `~/.codex/skills/<name>/` | `AGENTS.md` |

---

## 3. Portability Considerations

### 1. Frontmatter Neutrality
All YAML frontmatter fields in Commit Architect conform to the intersection of the open Agent Skills standard:
* `name`: Lowercase, hyphen-delimited string (e.g. `commit-architect`).
* `description`: Action-oriented third-person summary used by agent routers for semantic triggering.
* `license` & `metadata`: Informative metadata that conforms to YAML syntax without breaking strict parsers.

### 2. File Path References
All links within `SKILL.md` to reference documents (`references/commit-boundaries.md`) and scripts (`scripts/inspect-working-tree.py`) use relative POSIX forward slashes. Standard agent runtimes resolve these paths relative to the skill directory across Windows, macOS, and Linux.

### 3. Execution Environment for Scripts
The helper scripts in `skill/scripts/` require only standard Python 3.8+ with no third-party `pip` dependencies. They run identically on Windows PowerShell, bash, and zsh.
