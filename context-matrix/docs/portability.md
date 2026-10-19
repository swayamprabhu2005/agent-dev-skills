# Cross-Platform Portability & Compatibility Guide

Context Matrix is engineered to operate seamlessly across modern agentic development environments adhering to the open Agent Skills Specification.

---

## 1. Platform Capability Matrix

| Platform | Core Methodology | Native Skill Discovery | Native Rules Support | Status |
| :--- | :---: | :---: | :---: | :--- |
| **Google Antigravity** | ✅ Supported | `.agents/skills/context-matrix/` or `~/.gemini/config/skills/context-matrix/` | `AGENTS.md` / `GEMINI.md` | **Verified Support** |
| **Claude Code** | ✅ Supported | `.claude/skills/context-matrix/` or `~/.claude/skills/context-matrix/` | `CLAUDE.md` | **Verified Support** |
| **Cursor** | ✅ Supported | `.cursor/skills/context-matrix/` or `~/.cursor/skills/context-matrix/` | `.cursor/rules/*.mdc` | **Verified Support** |
| **OpenAI Codex** | ✅ Supported | `.codex/skills/context-matrix/` or `.agents/skills/context-matrix/` | `AGENTS.md` | **Verified Support** |
| **Generic Agent Runtimes** | ✅ Supported | Varies (`.skills/context-matrix/`) | Platform dependent | **Standards-Compatible** |
| **Vanilla Chat LLMs** | ✅ Supported (Manual) | ❌ No native discovery | ❌ System prompt only | **Manual / Unsupported** |

---

## 2. Directory Conventions Comparison

| Platform | Project-Level Skills Directory | Global / Workstation Directory | Ambient Rules File |
| :--- | :--- | :--- | :--- |
| **Google Antigravity** | `.agents/skills/<name>/` | `~/.gemini/config/skills/<name>/` | `AGENTS.md` / `GEMINI.md` |
| **Claude Code** | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` | `CLAUDE.md` |
| **Cursor** | `.cursor/skills/<name>/` | `~/.cursor/skills/<name>/` | `.cursor/rules/*.mdc` |
| **OpenAI Codex** | `.codex/skills/<name>/` | `~/.codex/skills/<name>/` | `AGENTS.md` |

---

## 3. Portability Principles

### 1. Frontmatter Neutrality
The YAML frontmatter in `context-matrix/skill/SKILL.md` conforms to the intersection of the open Agent Skills standard:
* `name`: Lowercase string `cats`.
* `description`: Action-oriented third-person summary used by agent routers for semantic triggering.
* `license` & `metadata`: Conforms to standard YAML syntax without vendor lock-in.

### 2. Relative Forward-Slash Paths
All links within `SKILL.md` to reference documents (`references/clarity.md`) and scripts (`scripts/select-framework.py`) use relative POSIX forward slashes, ensuring identical resolution on Windows, macOS, and Linux.

### 3. Pure Python Standard Library
All helper scripts in `skill/scripts/` require only standard Python 3.8+ with zero third-party `pip` dependencies.
