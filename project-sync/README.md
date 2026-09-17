# Project Sync

> **An open-standard Agent Skill that automatically reconciles a repository's `README.md` and `.gitignore` with meaningful implementation changes made by an AI coding agent, concluding with a concise, transparent completion summary.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Specification: Agent Skills](https://img.shields.io/badge/Spec-agentskills.io-blue.svg)](https://agentskills.io)
[![Philosophy: Minimal Targeted Diffs](https://img.shields.io/badge/Sync%20Style-Minimal%20Diffs-green.svg)](skill/references/readme-synchronization.md)

---

## What is Project Sync?

**Project Sync** is a post-implementation repository synchronization skill for AI coding assistants.

When an AI agent finishes implementing and validating a non-trivial coding task, Project Sync executes as the final project-hygiene step. It inspects what was actually changed in the codebase, evaluates whether the project's documentation (`README.md`) or Git ignore rules (`.gitignore`) have become out-of-date or incomplete, applies minimal surgical updates, and presents a factual completion summary to the user.

---

## Why Does It Exist?

AI agents frequently introduce new capabilities, add environment variables, or generate local build artifacts without updating documentation or ignore rules:
* **The Stale README Trap:** The agent adds Google OAuth login, but the README still instructs users to configure only email/password authentication.
* **The Missing Environment Variable:** The agent adds `REDIS_URL` to `.env.example` and code, but the README setup instructions never mention it.
* **The Accidental Secrets/Artifacts Leak:** The agent runs tests that create a `coverage/` directory or compiled bundles, which end up staged because `.gitignore` was never updated.
* **The Documentation Destroyer Anti-Pattern:** When asked to update a README, an agent often rewrites the entire document, destroying human badges, re-formatting unrelated sections, and polluting `git blame`.

**Project Sync eliminates this friction by making documentation and ignore-rule reconciliation an automatic, disciplined post-implementation routine.**

---

## The End-of-Iteration Concept

Project Sync operates on the concept of **meaningful implementation iterations**:

```text
User Request
    ↓
Agent Implements & Validates
    ↓
Meaningful Work Complete
    ↓
PROJECT SYNC
    │
    ├── Inspect Git Changes (git diff, git status)
    │
    ├── Evaluate Semantic Impact (Config, Features, Commands, Artifacts)
    │
    ├── Update README.md (Minimal, surgical edits only)
    │
    ├── Update .gitignore (Precise rules only; never as a trash can)
    │
    ├── Verify Diffs (git diff -- README.md .gitignore)
    │
    └── Present Transparent Completion Summary
    ↓
Iteration Complete
```

### What Counts as a Meaningful Iteration?
* ✅ Added or removed a feature or public capability.
* ✅ Changed project setup, prerequisites, or installation steps.
* ✅ Added, changed, or removed environment variables or config keys.
* ✅ Added or changed CLI commands, flags, or npm scripts.
* ✅ Created persistent build outputs or cache directories.

### When Project Sync Remains Silent:
* ⏹️ Answering questions or discussing architectural trade-offs with the user.
* ⏹️ Internal bug fixes or private helper refactorings that have zero user-facing impact.
* ⏹️ Sessions where no code or filesystem changes occurred.

---

## What Project Sync Does NOT Do

* **It is NOT a commit tool:** It does not stage or commit code into Git history. (That is the responsibility of its sibling skill, [Commit Architect](../commit-architect/)).
* **It does NOT rewrite entire documents:** It makes the surgical minimum update to keep documentation accurate.
* **It is NOT a trash can:** It never adds temporary agent scratch files to `.gitignore`. It cleans them up instead.
* **It does NOT invent speculative features:** It documents only what is implemented and verified.

---

## Cross-Platform Compatibility Matrix

| Platform | Core Methodology | Native Skill Discovery | Native Rules Support | Lifecycle Hooks | Status |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Google Antigravity** | ✅ Supported | `.agents/skills/` or `~/.gemini/config/` | `AGENTS.md` / `GEMINI.md` | Supported (`hooks.json`) | **Verified Support** |
| **Claude Code** | ✅ Supported | `.claude/skills/` or `~/.claude/skills/` | `CLAUDE.md` | Via `CLAUDE.md` rules | **Verified Support** |
| **Cursor** | ✅ Supported | `.cursor/skills/` or `~/.cursor/skills/` | `.cursor/rules/*.mdc` | Via `.mdc` rules | **Verified Support** |
| **OpenAI Codex** | ✅ Supported | `.codex/skills/` or `.agents/skills/` | `AGENTS.md` | Via `AGENTS.md` instructions | **Verified Support** |
| **Generic Agent Systems** | ✅ Supported | Runtime dependent (`.skills/`) | Platform dependent | Platform dependent | **Standards-Compatible** |

---

## Repository Structure

```text
project-sync/
│
├── README.md                 # Project documentation and guide
├── LICENSE                   # MIT License
├── AUTHORS                   # Authorship and maintainers
├── NOTICE                    # Trademark disclaimers and legal notices
├── .gitignore                # Git ignore configuration
│
├── skill/                    # CANONICAL CORE SKILL
│   ├── SKILL.md              # Open Agent Skills manifest and core workflow
│   │
│   ├── references/           # Progressive disclosure manuals
│   │   ├── readme-synchronization.md   # Rules for surgical README edits
│   │   ├── gitignore-synchronization.md# Rules for precise .gitignore entries
│   │   ├── impact-detection.md         # Heuristics for mapping diffs to docs
│   │   ├── first-time-initialization.md# Bootstrapping fresh repositories
│   │   ├── safety-rules.md             # Preserving manual user edits
│   │   └── examples.md                 # Worked scenario index
│   │
│   └── scripts/              # Deterministic audit tools (Python 3)
│       ├── detect-readme-impact.py     # Detects config, CLI, and setup diffs
│       ├── audit-gitignore.py          # Audits untracked files for ignore rules
│       └── generate-sync-summary.py    # Formats standardized completion summary
│
├── integrations/             # Thin platform adapters
│   ├── antigravity/          # Google Antigravity plugin.json, hooks.json & guide
│   ├── claude-code/          # Claude Code setup guide
│   ├── cursor/               # Cursor setup & project-sync.mdc rule
│   ├── codex/                # OpenAI Codex setup & AGENTS.md instructions
│   └── generic/              # Generic Agent Skills runtime instructions
│
├── examples/                 # 17 Real-world case studies
│   ├── 01-new-repo-init.md             # Bootstrapping fresh repos
│   ├── 02-existing-repo-readme.md      # Surgical insertions into mature repos
│   ├── 03-feature-addition.md          # CLI feature and usage flags
│   ├── 04-api-change.md                # Updating API query parameter docs
│   ├── 05-auth-change.md               # Documenting Google OAuth2 setup
│   ├── 06-config-change.md             # Documenting Redis connection settings
│   ├── 07-new-generated-artifacts.md   # Ignoring persistent SDK build outputs
│   ├── 08-new-temporary-artifacts.md   # Cleaning up vs. ignoring scratchpads
│   ├── 09-internal-refactor-no-impact.md# Silent execution on internal changes
│   ├── 10-gitignore-only-change.md     # Adding coverage reports to ignore
│   ├── 11-readme-only-change.md        # Documenting new CLI verbose flag
│   ├── 12-readme-and-gitignore-change.md# Local SQLite database zero-config setup
│   ├── 13-neither-requiring-changes.md # Logic bug fix with zero impact
│   ├── 14-preexisting-readme-edits.md  # Preserving uncommitted user README edits
│   ├── 15-preexisting-gitignore-edits.md# Preserving uncommitted user ignore rules
│   ├── 16-generated-readme-section.md  # Handling Swagger/TypeDoc generated blocks
│   └── 17-generated-gitignore-section.md# Handling framework-managed ignore blocks
│
└── docs/                     # Architectural documentation
    ├── architecture.md       # Decoupled core and progressive disclosure
    ├── portability.md        # Cross-platform compatibility analysis
    └── contributing.md       # Contribution guidelines
```

---

## Installation

### 1. Google Antigravity
Copy or link into your project's `.agents/skills/` directory:
```bash
mkdir -p .agents/skills
cp -r /path/to/project-sync/skill .agents/skills/project-sync
```
Or install globally across all workspaces:
* **Linux / macOS:** `cp -r /path/to/project-sync/skill ~/.gemini/config/skills/project-sync`
* **Windows:** Copy `skill` to `%USERPROFILE%\.gemini\config\skills\project-sync`

See [integrations/antigravity/README.md](integrations/antigravity/README.md) for plugin and hook configuration.

### 2. Claude Code
Install into `.claude/skills/project-sync/` or globally in `~/.claude/skills/project-sync/`. Add the completion instruction to `CLAUDE.md`.
See [integrations/claude-code/README.md](integrations/claude-code/README.md).

### 3. Cursor
Install into `.cursor/skills/project-sync/` and copy `integrations/cursor/project-sync.mdc` into `.cursor/rules/`.
See [integrations/cursor/README.md](integrations/cursor/README.md).

### 4. OpenAI Codex
Install into `.codex/skills/project-sync/` or append [integrations/codex/agents-instructions.md](integrations/codex/agents-instructions.md) into `AGENTS.md`.

---

## Deterministic Verification Scripts

Zero-dependency Python 3 scripts in `skill/scripts/` provide automated factual audits:

```bash
# 1. Detect if recent git changes affect configuration, CLI, or dependencies
python skill/scripts/detect-readme-impact.py

# 2. Audit untracked files against current .gitignore
python skill/scripts/audit-gitignore.py

# 3. Format the standardized completion summary
python skill/scripts/generate-sync-summary.py \
  --implemented "Added Google OAuth2 login" \
  --readme-status "Updated" \
  --readme-note "Added GOOGLE_CLIENT_ID environment variable" \
  --gitignore-status "No changes required" \
  --validation "Tests passed (14/14)"
```

All scripts support the `--json` flag for programmatic tool pipelines.

---

## Standard Completion Summary

At the conclusion of each meaningful iteration, Project Sync presents a concise, transparent report:

```text
Implementation complete.

Implemented:
- Added Google OAuth2 authentication flow
- Added token refresh handler in auth service
- Exposed GET/POST /auth/google endpoints

Project synchronization:
- README.md — Updated: Added GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET to Configuration table
- .gitignore — No changes required: All runtime tokens and local caches already ignored

Validation:
- Tests: 14 passed (npm test)
- Build: Successful (npm run build)

Iteration complete.
```

---

## Relationship with Sibling Skill: Commit Architect

Project Sync is designed to operate alongside **Commit Architect** in the same personal skill collection:

```text
MYSKILLS/
├── commit-architect/       # Plans, stages, and authors clean Git commit histories
└── project-sync/           # Reconciles README.md, .gitignore, and completion summaries
```

After an agent implements a feature:
1. **Project Sync** reconciles `README.md` and `.gitignore` to ensure the project files are accurate.
2. **Commit Architect** then plans, inspects staged diffs, and creates atomic commits with natural developer messages.

---

## License

Distributed under the terms of the **MIT License**.
See [LICENSE](LICENSE) for details.

---

## Authorship & Provenance

**Author and Copyright Owner:**
**SWAYAM KIRAN PRABHU**

```text
Copyright (c) 2026 SWAYAM KIRAN PRABHU

Project Sync is an independent open-source project and is not affiliated with,
endorsed by, sponsored by, or officially associated with Google LLC, Alphabet Inc.,
Anthropic PBC, Cursor / Anysphere Inc., OpenAI OpCo LLC, or any other platform
vendors unless explicitly stated otherwise.
```
