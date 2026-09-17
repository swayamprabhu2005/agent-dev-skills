# Commit Architect

> **An open-standard Agent Skill that teaches AI coding assistants how to intelligently plan, divide, implement, validate, and organize software work into clean, logical Git commit histories.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Specification: Agent Skills](https://img.shields.io/badge/Spec-agentskills.io-blue.svg)](https://agentskills.io)
[![Standard: Natural Developer Commits](https://img.shields.io/badge/Commit%20Style-Natural%20Developer-green.svg)](skill/references/natural-commit-messages.md)

---

## What is Commit Architect?

**Commit Architect** is not merely a commit-message generator. It is an agentic engineering methodology that equips AI pair programmers to act as thoughtful Git architects.

When given a non-trivial software task, an AI agent equipped with Commit Architect does not dump all edits into a single massive, unreviewable commit at the end. Nor does it scatter work across dozens of meaningless single-line micro-commits.

Instead, it:
1. Audits existing repository and working-tree state.
2. Identifies coherent logical work units.
3. Maps architectural dependencies and designs an intentional commit sequence.
4. Implements, tests, and stages each logical slice progressively.
5. Reviews staged diffs (`git diff --cached`) against strict safety checklists.
6. Authors concise, natural developer commit messages in ordinary programmer language.

---

## Why Does It Exist?

AI coding agents are remarkably proficient at writing code, but notoriously poor at managing version control history. Typical agentic workflows suffer from chronic Git anti-patterns:

* **The Monolithic Megacommit:** The agent modifies 30 files across backend APIs, database migrations, frontend views, dependencies, and docs, and commits everything with `Implement feature X`. Code review becomes a nightmare, and `git bisect` is rendered useless.
* **The Micro-Commit Storm:** The agent creates a new commit for every single file edit, variable rename, or typo fix (`Add import`, `Rename foo to bar`, `Fix syntax error`), cluttering the Git log with noise.
* **Smuggled Refactoring & Opportunistic Edits:** While fixing a bug, the agent quietly reformats unrelated files or rewires unrelated abstractions, obscuring the actual fix and breaking `git blame`.
* **The Robotic Conventional Commit Trap:** Blindly prefixing every commit with `feat(scope):` or `chore(deps):`—even in projects whose human maintainers communicate in standard Git prose.
* **AI Fluff and Hallucinated Attribution:** Filling commit messages with hyperbolic buzzwords (`Implemented robust and comprehensive pipeline`) or injecting unrequested `Co-authored-by: AI` footers.
* **Accidental Staging of Secrets and Artifacts:** Blindly executing `git add .` and accidentally committing `.env` files, build directories, or temporary scratchpads.

**Commit Architect solves this by embedding true version-control craftsmanship directly into the agent's decision-making loop.**

---

## How It Works

Commit Architect guides the agent through an intentional 12-step engineering lifecycle:

```text
User Request
     ↓
Understand Complete Task Requirements
     ↓
Audit Working Tree & Git State (git status, git branch, git log)
     ↓
Inspect Project Architecture & Commit Conventions
     ↓
Identify Logical Work Units
     ↓
Determine Dependency Order (Foundations → Core → API → UI → Tests)
     ↓
Design Progressive Commit Sequence
     ↓
Implement First Logical Unit
     ↓
Validate (Build & Tests Pass)
     ↓
Review Staged Diff (git diff --cached)
     ↓
Commit with Natural Developer Phrasing
     ↓
Verify Commit (git log -1)
     ↓
Implement Next Logical Unit...
     ↓
Review Final Branch Git History
```

---

## Core Commit Philosophy

### Split by Logical Intent, Not by Edit Count
A commit should represent **one coherent conceptual milestone**. Sizing commits requires balancing seven architectural principles:

1. **Atomicity:** The commit addresses one specific goal completely.
2. **Cohesion:** All changes directly serving that goal (code, schemas, directly coupled tests) are bundled together.
3. **Reviewability:** A human engineer can understand the diff in a single reading pass.
4. **Dependency Order:** Foundational changes precede the consumers that depend on them.
5. **Repository Stability:** Every intermediate commit builds and passes tests (preserving `git bisect`).
6. **Reversibility:** An individual change can be cleanly reverted with `git revert` without collateral breakage.
7. **Meaningful Granularity:** Avoiding both micro-commit noise and monolithic bloat.

### Natural Developer Phrasing (The Default Standard)
Commit Architect establishes natural, concise developer language as the universal default:
* Write in the imperative mood (`Add Google login support`, `Handle expired tokens`).
* Capitalize the subject line, omit trailing periods, and keep subjects under 72 characters.
* **DO NOT automatically use Conventional Commits** (`feat:`, `fix:`, etc.) unless the repository explicitly mandates them in `CONTRIBUTING.md` or via automated tools like `commitlint`.

---

## Cross-Platform Compatibility Matrix

Commit Architect features a **single canonical methodology** (`skill/SKILL.md`) wrapped in thin platform-specific adapters:

| Platform | Core Methodology | Native Skill Discovery | Native Rules Support | Status |
| :--- | :---: | :---: | :---: | :--- |
| **Google Antigravity** | ✅ Supported | `.agents/skills/` or `~/.gemini/config/` | `AGENTS.md` / `GEMINI.md` | **Verified Support** |
| **Claude Code** | ✅ Supported | `.claude/skills/` or `~/.claude/skills/` | `CLAUDE.md` | **Verified Support** |
| **Cursor** | ✅ Supported | `.cursor/skills/` or `~/.cursor/skills/` | `.cursor/rules/*.mdc` | **Verified Support** |
| **OpenAI Codex** | ✅ Supported | `.codex/skills/` or `.agents/skills/` | `AGENTS.md` | **Verified Support** |
| **Generic Agent Systems** | ✅ Supported | Runtime dependent (`.skills/`) | Platform dependent | **Standards-Compatible** |

---

## Repository Structure

```text
commit-architect/
│
├── README.md                 # Project documentation and guide
├── LICENSE                   # MIT License
├── AUTHORS                   # Project authorship and maintainers
├── NOTICE                    # Trademark disclaimers and legal notices
├── .gitignore                # Git ignore configuration
│
├── skill/                    # CANONICAL CORE SKILL (Vendor-Neutral)
│   ├── SKILL.md              # Open Agent Skills manifest and core workflow
│   │
│   ├── references/           # In-depth progressive disclosure manuals
│   │   ├── commit-boundaries.md        # Boundary rules and sizing heuristics
│   │   ├── natural-commit-messages.md  # Tone, structure, and phrasing guide
│   │   ├── commit-anti-patterns.md     # Catalog of AI-specific commit mistakes
│   │   ├── dependency-ordering.md      # Sequencing foundations, code, and tests
│   │   ├── working-tree-safety.md      # Dirty trees, staging, and diff review
│   │   └── examples.md                 # Worked scenario index
│   │
│   └── scripts/              # Deterministic verification tools (Python 3)
│       ├── inspect-working-tree.py     # Working-tree status and secrets audit
│       ├── validate-staged-diff.py     # 5-point staged diff validator
│       └── verify-commit.py            # Commit message style verifier
│
├── integrations/             # Thin platform-specific adapters
│   ├── antigravity/          # Google Antigravity setup & plugin.json
│   ├── claude-code/          # Claude Code setup guide
│   ├── cursor/               # Cursor setup & commit-architect.mdc rule
│   ├── codex/                # OpenAI Codex setup & AGENTS.md instructions
│   └── generic/              # Generic Agent Skills runtime instructions
│
├── examples/                 # 12 Comprehensive real-world case studies
│   ├── 01-new-feature.md               # Large feature slicing (OAuth)
│   ├── 02-bug-fix.md                   # Coupling regression test with fix
│   ├── 03-database-migration.md        # Live schema migration ordering
│   ├── 04-backend-frontend.md          # Full-stack monorepo separation
│   ├── 05-refactoring.md               # Preparatory refactoring vs. feature
│   ├── 06-unrelated-changes.md         # Preserving user edits safely
│   ├── 07-tests.md                     # Companion tests vs. separate suites
│   ├── 08-documentation.md           # Inline docs vs. dedicated docs
│   ├── 09-configuration.md             # Environment variables and Docker
│   ├── 10-dependency-update.md         # Breaking dependency version bumps
│   ├── 11-conventional-commit-repo.md  # Handling explicit Conventional Commit repos
│   └── 12-non-conventional-repo.md     # Handling standard developer prose repos
│
└── docs/                     # Architectural and developer documentation
    ├── architecture.md       # Decoupled core and progressive disclosure
    ├── portability.md        # Cross-platform compatibility analysis
    └── contributing.md       # Guidelines for community contributors
```

---

## Installation & Distribution Note

> [!IMPORTANT]
> **This repository is the source and distribution hub.** Cloning this repository alone does not automatically configure every agent on your workstation unless you install or link the skill into your target project or global agent directory.

Follow the instructions below for your specific development platform:

### 1. Google Antigravity
To install in a project repository:
```bash
mkdir -p .agents/skills
cp -r /path/to/commit-architect/skill .agents/skills/commit-architect
```
Or install globally for all Antigravity projects on your machine:
* **Linux / macOS:** `cp -r /path/to/commit-architect/skill ~/.gemini/config/skills/commit-architect`
* **Windows:** Copy `skill` to `%USERPROFILE%\.gemini\config\skills\commit-architect`

See [integrations/antigravity/README.md](integrations/antigravity/README.md) for plugin packaging options.

### 2. Claude Code
Install locally in your project:
```bash
mkdir -p .claude/skills
cp -r /path/to/commit-architect/skill .claude/skills/commit-architect
```
Or install globally:
```bash
mkdir -p ~/.claude/skills
cp -r /path/to/commit-architect/skill ~/.claude/skills/commit-architect
```
See [integrations/claude-code/README.md](integrations/claude-code/README.md).

### 3. Cursor
Place the skill into your project's Cursor skills folder:
```bash
mkdir -p .cursor/skills
cp -r /path/to/commit-architect/skill .cursor/skills/commit-architect
```
Optionally copy the companion `.mdc` rule for persistent ambient enforcement:
```bash
mkdir -p .cursor/rules
cp integrations/cursor/commit-architect.mdc .cursor/rules/
```
See [integrations/cursor/README.md](integrations/cursor/README.md).

### 4. OpenAI Codex
Install into `.codex/skills/` or append the rules block from [integrations/codex/agents-instructions.md](integrations/codex/agents-instructions.md) into your project's `AGENTS.md`.

---

## Deterministic Verification Scripts

Commit Architect includes three zero-dependency Python 3 scripts in `skill/scripts/` to assist agents and developers in automated verification:

```bash
# 1. Audit current working tree, detect untracked files and potential secret leaks
python skill/scripts/inspect-working-tree.py

# 2. Validate staged diff for leftover debug code, large diff sizes, and sensitive files
python skill/scripts/validate-staged-diff.py

# 3. Verify a commit message against natural developer standards and repo rules
python skill/scripts/verify-commit.py -m "Add Google OAuth2 login support"

# Or verify against Conventional Commits if the repo mandates it:
python skill/scripts/verify-commit.py --conventional -m "feat(auth): add google oauth2 login"
```

All scripts support the `--json` flag for automated integration into agent tool pipelines or git hooks.

---

## Configuration & Precedence

Commit Architect is designed to respect repository culture above all else. When deciding commit format, the agent follows this strict hierarchy:

1. **Repository Rules File:** Explicit instructions in `AGENTS.md`, `CLAUDE.md`, or `.cursor/rules/`.
2. **Contributor Guidelines:** Explicit commit conventions in `CONTRIBUTING.md` or `DEVELOPMENT.md`.
3. **Automated Commit Linting:** Active `commitlint.config.js` or `.commitlintrc` configurations.
4. **Recent Git Log Precedent:** Uniform conventions observable in `git log -n 10 --oneline`.
5. **Default Fallback:** Natural, concise developer prose (Commit Architect default).

---

## License

Commit Architect is distributed under the terms of the **MIT License**.
See the [LICENSE](LICENSE) file for full details.

---

## Authorship and Trademarks

**Author and Copyright Owner:**
**SWAYAM KIRAN PRABHU**

```text
Copyright (c) 2026 SWAYAM KIRAN PRABHU

Commit Architect is an independent open-source project and is not affiliated with,
endorsed by, sponsored by, or officially associated with Google LLC, Alphabet Inc.,
Anthropic PBC, Cursor / Anysphere Inc., OpenAI OpCo LLC, or any other platform
vendors unless explicitly stated otherwise.
```
