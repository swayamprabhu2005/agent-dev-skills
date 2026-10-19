# agent-dev-skills

> **A curated collection of independent, cross-platform Agent Skills for disciplined software engineering with AI coding assistants.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Specification: Agent Skills](https://img.shields.io/badge/Spec-agentskills.io-purple.svg)](https://agentskills.io)
[![Author: Swayam Kiran Prabhu](https://img.shields.io/badge/Author-Swayam%20Kiran%20Prabhu-green.svg)](#authorship)
[![Status: Production](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)](#)

---

## Overview

**agent-dev-skills** is an open personal collection of specialized **Agent Skills** designed to teach AI pair programmers and autonomous coding agents professional software engineering discipline.

Typical AI coding agents suffer from predictable behavioral pathologies:
* **Vague prompt engineering:** Formulating ambiguous requests without negative constraints, proper context grounding, or testable verification criteria.
* **Premature implementation:** Rushing into code generation on ambiguous instructions without architecture or user approval.
* **Documentation rot:** Leaving human-facing `README.md` files and repository ignore configurations (`.gitignore`) out of date after implementing features.
* **Chaotic version control:** Creating giant, unreviewable monolithic commits or noisy, single-line micro-commits with robotic conventional prefixes.

The skills in this collection solve these challenges by providing modular, vendor-neutral workflows adhering to the open [Agent Skills Specification](https://agentskills.io).

---

## The Skills Collection

| Skill | Primary Responsibility | Key Output | Status | Repository |
| :--- | :--- | :--- | :---: | :--- |
| **[Context Matrix](./context-matrix/)** | Context-aware prompt design, framework selection (8 frameworks), prompt construction, and quality evaluation | Tailored, testable prompts, framework routing rationale, qualitative readiness score | **Production** | [`context-matrix/`](./context-matrix/README.md) |
| **[Project Blueprint](./project-blueprint/)** | Pre-implementation planning, architectural clarification, and human approval gating | 5 core specs (`PRD`, `TRD`, `UI_UX`, `BACKEND_SCHEMA`, `APP_FLOW`) + `.blueprint/state.yaml` | **Production** | [`project-blueprint/`](./project-blueprint/README.md) |
| **[Project Sync](./project-sync/)** | Synchronizing `README.md` and `.gitignore` after meaningful implementation iterations | Reconciled documentation, quarantine of temporary artifacts, factual completion summary | **Production** | [`project-sync/`](./project-sync/README.md) |
| **[Commit Architect](./commit-architect/)** | Planning, slicing, dependency-ordering, diff-reviewing, and authoring natural Git commits | Cohesive atomic Git commits, clean history, natural programmer commit messages | **Production** | [`commit-architect/`](./commit-architect/README.md) |

---

## How the Skills Relate

The four skills are **completely independent and decoupled**. There are no runtime dependencies, hardcoded links, or required couplings between them. You can install and use any single skill on its own without installing the others.

When used together across a larger project lifecycle, they form a natural, closed-loop development pipeline:

```mermaid
flowchart LR
    CM["🎯 Context Matrix\n(Prompt & Task Architecture)\n8 Frameworks • Selection Engine • Quality Rubric"] -->|"Grounded Task Specification\n& Context-Aware Prompt"| A["📐 Project Blueprint\n(Planning & Approval Gate)\nPRD • TRD • UI/UX • Schema • Flow"]
    A -->|"Approved Specifications\n& Implementation Roadmap"| Dev["⚙️ Implementation Phase\n(Agent Code Execution)"]
    Dev -->|"Completed Milestone\n& Verified Codebase"| B["🔄 Project Sync\n(Documentation Reconciliation)\nDocs • README • Gitignore"]
    B -->|"Synchronized Files\n& Clean Working Tree"| C["🏗️ Commit Architect\n(History Architecture & Slicing)\nAtomic Commits • Logical History"]

    style CM fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    style A fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    style Dev fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    style B fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style C fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
```

* **Step 0 (Prompt & Framework Architecture):** **Context Matrix** inspects repository context, selects the optimal prompt framework from 8 modules (CLARITY, SOCRATES, ANTICIPATE, PARTNER, TRUST, RIPPLE, CATCH, MAGIC), bounds negative constraints, and constructs a testable, high-fidelity prompt.
* **Step 1 (Before Implementation):** **Project Blueprint** conducts targeted clarification, drafts synchronized architectural specifications with Mermaid diagrams, audits cross-document consistency, and enforces human sign-off before coding starts.
* **Step 2 (During/After Implementation):** The agent writes and tests the software.
* **Step 3 (Post-Implementation Reconciliation):** **Project Sync** inspects changed files, updates relevant `README.md` sections, updates `.gitignore`, quarantines temporary scratchpads into `.agent/scratch/`, and outputs a factual completion report.
* **Step 4 (Version Control Architecture):** **Commit Architect** reviews the working tree, partitions the completed work into dependency-ordered atomic slices, validates staged diffs, and records clean commits with natural developer messages.

---

## Detailed Skill Profiles

### 1. Project Blueprint 📐

* **Core Purpose:** Stops agents from diving blindly into implementation. Establishes a formal pre-implementation planning and human approval gate.
* **Key Mechanisms:**
  * **Targeted Clarification:** Interrogates vague prompts asking 1–2 prioritized questions at a time with opinionated defaults.
  * **5-Document Specification Suite:** Produces synchronized specifications: `PRD.md` (requirements), `TRD.md` (technical architecture), `UI_UX.md` (interface and ASCII layouts), `BACKEND_SCHEMA.md` (data models and endpoints), and `APP_FLOW.md` (user and state journeys).
  * **First-Class Visual Architecture:** Standardized Mermaid.js diagrams embedded directly in specifications (`flowchart`, `erDiagram`, `sequenceDiagram`).
  * **Cross-Document Consistency:** Audits requirement IDs (`REQ-xxx`) across documents and halts immediately upon detecting contradictions.
  * **Approval Gate & Version Invalidation:** Tracks lifecycle state in `.blueprint/state.yaml`. Strictly blocks code generation until explicit human approval is given. Changing requirements invalidates prior approval.
* **Verification Scripting:** Pure Python stdlib tools: `blueprint-state.py`, `check-consistency.py`, `validate-blueprint.py`.
* **Deep Dive:** Read the [Project Blueprint Guide](./project-blueprint/README.md).

### 2. Project Sync 🔄

* **Core Purpose:** Eliminates documentation drift by reconciling `README.md` and `.gitignore` after meaningful implementation iterations.
* **Key Mechanisms:**
  * **Meaningful-Iteration Trigger:** Evaluates changes only when public features, CLI commands, prerequisites, dependencies, or environment variables are altered. Remains silent on pure internal refactors.
  * **Surgical Documentation Edits:** Updates only the specific lines, tables, or sections affected by the change without rewriting unrelated human-authored prose.
  * **Safe Temporary Artifact Quarantine:** Prohibits silent file deletion. Quarantines genuine agent scratchpads into `.agent/scratch/`, adds the quarantine pattern to `.gitignore`, and reports them for human review.
  * **Preserving Manual Edits:** Detects uncommitted user edits in `README.md` or `.gitignore` and performs safe additive merges without clobbering.
  * **Transparent Completion Summary:** Concludes iterations with a four-state report (`Updated`, `No changes required`, `Not applicable`, `Unable to verify`) and lists quarantined items.
* **Verification Scripting:** Pure Python stdlib tools: `detect-readme-impact.py`, `audit-gitignore.py`, `generate-sync-summary.py`.
* **Deep Dive:** Read the [Project Sync Guide](./project-sync/README.md).

### 3. Commit Architect 🏗️

* **Core Purpose:** Teaches AI coding agents to plan, divide, stage, validate, and record clean, logical Git commit histories.
* **Key Mechanisms:**
  * **Logical Boundaries:** Splits commits by conceptual milestone rather than by file count or lines edited.
  * **Anti-Micro-Commit & Anti-Monolith:** Forbids trivial single-line noise commits while preventing 30-file catch-all megacomcommits.
  * **Dependency-Aware Ordering:** Sequences changes logically (foundations → data migrations → core logic → endpoints → UI → tests).
  * **Working-Tree Safety:** Audits dirty trees, protects pre-existing human edits, and bans destructive Git commands (`reset --hard`, `clean -fd`, `push -f`).
  * **Staged-Diff Review:** Enforces a 5-point diff checklist via `git diff --cached` before committing.
  * **Natural Developer Commit Messages:** Defaults to ordinary, professional programmer English (imperative mood, concise, no artificial prefixes). Follows Conventional Commits only if the repository explicitly mandates them.
* **Verification Scripting:** Pure Python stdlib tools: `inspect-working-tree.py`, `validate-staged-diff.py`, `verify-commit.py`.
* **Deep Dive:** Read the [Commit Architect Guide](./commit-architect/README.md).

### 4. Context Matrix 🎯

* **Core Purpose:** Teaches AI coding agents disciplined prompt engineering, framework selection, and prompt-quality evaluation across eight specialized methodologies.
* **Key Mechanisms:**
  * **Framework Selection Engine:** Dynamically routes tasks to the optimal framework: `CLARITY` (functional specs/coding), `SOCRATES` (architecture/trade-offs), `ANTICIPATE` (tutorials/pedagogy), `PARTNER` (research/benchmarks), `TRUST` (tailored advisory), `RIPPLE` (code reviews/debugging/audits), `CATCH` (concise communications), or `MAGIC` (creative narrative).
  * **Multi-Framework Orchestration:** Combines complementary frameworks for complex workflows without boilerplate redundancy (e.g. `SOCRATES + RIPPLE`, `CLARITY + RIPPLE`).
  * **Project-Aware Context Grounding:** Inspects active repository dependencies, configurations, and existing specifications (`.blueprint/state.yaml`) to inject verified facts and enforce negative constraints.
  * **Prompt Quality Rubric:** Evaluates prompts against a 10-point Quality Checklist, returning actionable qualitative readiness states (`Ready to Use`, `Ready with Assumptions`, or `Needs Clarification`).
  * **9 Operating Modes:** Supports `/context-matrix [task]`, explicit framework invocation, prompt generation (`/context-matrix prompt ...`), prompt improvement (`/context-matrix improve ...`), evaluation, explanation, and combinations.
* **Verification Scripting:** Pure Python stdlib tools: `select-framework.py`, `evaluate-prompt.py`, `test-context-matrix.py`.
* **Deep Dive:** Read the [Context Matrix Guide](./context-matrix/README.md).

---

## Independent Usage & Installation

Every skill in this collection is self-contained and adheres to the open [Agent Skills Specification](https://agentskills.io). You can install a single skill or all four skills together, either at the **project level** (for a specific codebase) or at the **global level** (workstation-wide across all projects).

---

### Direct Slash Command Invocation

When installed in your project's `.agents/skills/` directory (or globally), Google Antigravity automatically registers each skill directory as a native slash command:

```text
/context-matrix [task]       # Context-aware prompt design, 8 frameworks, prompt evaluation
/project-blueprint [feature] # Pre-implementation planning, 5 specifications, human approval gate
/project-sync [iteration]    # Reconciles README.md and .gitignore, quarantines scratchpads
/commit-architect [work]     # Plans, validates staged diffs, and creates atomic Git commits
```

Arguments following the command are passed directly to the skill instructions. For example:
* `/context-matrix socrates Evaluate database partitioning for 10TB scale`
* `/context-matrix prompt Build an idempotent payment webhook in Go`
* `/project-blueprint Design an email invitation system for team administrators`
* `/project-sync Reconcile documentation after implementing Redis rate limiting`
* `/commit-architect Create atomic commits for the authentication overhaul`

---

### Method 1: Direct GitHub ZIP Download & Unzip (No Git Clone Required)

If `agent-dev-skills` is hosted on GitHub, you can download and use any skill in your active project **without cloning the repository, without touching submodules, and without risking Git conflicts**:

1. **Download the Repository ZIP from GitHub:**
   * Go to the GitHub repository page (`https://github.com/swayamprabhu2005/agent-dev-skills`).
   * Click **Code** → **Download ZIP**, and extract it locally.
2. **Create the `.agents/skills` Folder in Your Working Project:**
   ```bash
   # In your working project root:
   mkdir -p .agents/skills
   ```
3. **Copy / Unzip the Desired Skill's `skill/` Subfolder:**
   * Each skill folder contains a canonical `skill/` subfolder (which holds `SKILL.md`, `references/`, and `scripts/`).
   * Copy or unzip that `skill/` directory into `.agents/skills/<skill-name>/`.
   * **Verification Rule:** Ensure `SKILL.md` resides directly at `.agents/skills/<skill-name>/SKILL.md`.

#### Windows Example (PowerShell):
```powershell
# In your target working project:
New-Item -ItemType Directory -Force -Path .agents\skills\commit-architect

# Extract or copy the canonical skill/ folder files:
Copy-Item -Recurse -Force C:\Downloads\agent-dev-skills-main\commit-architect\skill\* .agents\skills\commit-architect\
```

#### macOS / Linux Example (Bash):
```bash
# In your target working project:
mkdir -p .agents/skills/commit-architect
cp -r ~/Downloads/agent-dev-skills-main/commit-architect/skill/* .agents/skills/commit-architect/
```

Once unzipped, restart or open your AI assistant session in your project. The skill and its `/slash-command` are immediately discovered.

---

### Method 2: Scripted Copy from Local Clone (For Developers)

If you have cloned `agent-dev-skills` locally, use these copy commands to install skills into any target project:

#### Option A: Install ONLY Context Matrix
```bash
# In your target repository root:
mkdir -p .agents/skills/context-matrix
cp -r /path/to/agent-dev-skills/context-matrix/skill/* .agents/skills/context-matrix/

# Or for Claude Code:
mkdir -p .claude/skills/context-matrix
cp -r /path/to/agent-dev-skills/context-matrix/skill/* .claude/skills/context-matrix/

# Or for Cursor:
mkdir -p .cursor/skills/context-matrix .cursor/rules
cp -r /path/to/agent-dev-skills/context-matrix/skill/* .cursor/skills/context-matrix/
cp /path/to/agent-dev-skills/context-matrix/integrations/cursor/context-matrix.mdc .cursor/rules/
```

#### Option B: Install ONLY Project Blueprint
```bash
# In your target repository root:
mkdir -p .agents/skills/project-blueprint
cp -r /path/to/agent-dev-skills/project-blueprint/skill/* .agents/skills/project-blueprint/

# Or for Claude Code:
mkdir -p .claude/skills/project-blueprint
cp -r /path/to/agent-dev-skills/project-blueprint/skill/* .claude/skills/project-blueprint/

# Or for Cursor:
mkdir -p .cursor/skills/project-blueprint .cursor/rules
cp -r /path/to/agent-dev-skills/project-blueprint/skill/* .cursor/skills/project-blueprint/
cp /path/to/agent-dev-skills/project-blueprint/integrations/cursor/project-blueprint.mdc .cursor/rules/
```

#### Option C: Install ONLY Project Sync
```bash
# In your target repository root:
mkdir -p .agents/skills/project-sync
cp -r /path/to/agent-dev-skills/project-sync/skill/* .agents/skills/project-sync/

# Or for Claude Code:
mkdir -p .claude/skills/project-sync
cp -r /path/to/agent-dev-skills/project-sync/skill/* .claude/skills/project-sync/

# Or for Cursor:
mkdir -p .cursor/skills/project-sync .cursor/rules
cp -r /path/to/agent-dev-skills/project-sync/skill/* .cursor/skills/project-sync/
cp /path/to/agent-dev-skills/project-sync/integrations/cursor/project-sync.mdc .cursor/rules/
```

#### Option D: Install ONLY Commit Architect
```bash
# In your target repository root:
mkdir -p .agents/skills/commit-architect
cp -r /path/to/agent-dev-skills/commit-architect/skill/* .agents/skills/commit-architect/

# Or for Claude Code:
mkdir -p .claude/skills/commit-architect
cp -r /path/to/agent-dev-skills/commit-architect/skill/* .claude/skills/commit-architect/

# Or for Cursor:
mkdir -p .cursor/skills/commit-architect .cursor/rules
cp -r /path/to/agent-dev-skills/commit-architect/skill/* .cursor/skills/commit-architect/
cp /path/to/agent-dev-skills/commit-architect/integrations/cursor/commit-architect.mdc .cursor/rules/
```

#### Option E: Install ALL Four Skills in One Step
```bash
# In your target repository root (for Google Antigravity):
mkdir -p .agents/skills
for skill in context-matrix project-blueprint project-sync commit-architect; do
  mkdir -p .agents/skills/$skill
  cp -r /path/to/agent-dev-skills/$skill/skill/* .agents/skills/$skill/
done

# Or for Claude Code:
mkdir -p .claude/skills
for skill in context-matrix project-blueprint project-sync commit-architect; do
  mkdir -p .claude/skills/$skill
  cp -r /path/to/agent-dev-skills/$skill/skill/* .claude/skills/$skill/
done

# Or for Cursor:
mkdir -p .cursor/skills .cursor/rules
for skill in context-matrix project-blueprint project-sync commit-architect; do
  mkdir -p .cursor/skills/$skill
  cp -r /path/to/agent-dev-skills/$skill/skill/* .cursor/skills/$skill/
done
cp /path/to/agent-dev-skills/*/integrations/cursor/*.mdc .cursor/rules/
```

---

### Global / Workstation Installation (Available Across All Projects)

If you prefer having all four skills available across **every workspace on your machine** without copying files into every repository:

* **Google Antigravity:**
  * **Windows:** `%USERPROFILE%\.gemini\config\skills\<skill-name>\`
  * **Linux / macOS:** `~/.gemini/config/skills/<skill-name>/`
  ```bash
  mkdir -p ~/.gemini/config/skills
  for skill in context-matrix project-blueprint project-sync commit-architect; do
    mkdir -p ~/.gemini/config/skills/$skill
    cp -r /path/to/agent-dev-skills/$skill/skill/* ~/.gemini/config/skills/$skill/
  done
  ```

* **Claude Code:**
  ```bash
  mkdir -p ~/.claude/skills
  for skill in context-matrix project-blueprint project-sync commit-architect; do
    mkdir -p ~/.claude/skills/$skill
    cp -r /path/to/agent-dev-skills/$skill/skill/* ~/.claude/skills/$skill/
  done
  ```

* **Cursor:**
  ```bash
  mkdir -p ~/.cursor/skills
  for skill in context-matrix project-blueprint project-sync commit-architect; do
    mkdir -p ~/.cursor/skills/$skill
    cp -r /path/to/agent-dev-skills/$skill/skill/* ~/.cursor/skills/$skill/
  done
  ```


---

## Platform Compatibility Matrix

All four skills adhere to the open [Agent Skills Specification](https://agentskills.io). Support across major platforms has been audited and verified against official upstream conventions:

| Platform | Skill Discovery Convention | Invocation Mode | Compatibility Level | Notes |
| :--- | :--- | :--- | :---: | :--- |
| **Google Antigravity** | `.agents/skills/<name>/SKILL.md`<br>`~/.gemini/config/skills/<name>/` | Model-Driven (Progressive Disclosure) / Direct Prompt / Slash Commands (`/context-matrix`, etc.) | **Verified** | Full support for YAML metadata indexing, on-demand reference loading, and slash commands. |
| **Claude Code** | `.claude/skills/<name>/SKILL.md`<br>`~/.claude/skills/<name>/` | Model-Driven / Prompt | **Verified** | Native support for standard Agent Skills format. Optional hint in `CLAUDE.md`. |
| **Cursor** | `.cursor/skills/<name>/SKILL.md`<br>`.cursor/rules/*.mdc` | Model-Driven / Composer Chat | **Verified** | Full support for `SKILL.md` coupled with lightweight `.mdc` rules for ambient enforcement. |
| **OpenAI Codex** | `.codex/skills/<name>/SKILL.md`<br>`AGENTS.md` | Model-Driven / Direct `$command` | **Verified** | Standard `SKILL.md` loading supported, with persistent instructions in `AGENTS.md`. |
| **Generic Agent Systems** | Runtime dependent (`.skills/`) | System dependent | **Standards-Compatible** | Follows open `agentskills.io` standard with zero proprietary dependencies. |

### Compatibility Level Definitions:
* **Verified:** Formally tested and validated against current official platform directories, runtime behaviors, and discovery mechanisms.
* **Standards-Compatible:** Fully compliant with the vendor-neutral `agentskills.io` specification.
* **Experimental:** Upstream platform mechanism is in active alpha/beta or subject to breaking changes.
* **Unsupported:** Platform lacks local filesystem access, tool execution, or skill discovery mechanisms.

---

## Practical Examples

### Example 1: Project Blueprint in Action
**User Prompt:**
> *"Build an invitation system so team admins can invite new members by email."*

**Agent Flow:**
1. **Clarifies:** Asks 2 focused questions (role permissions and token expiration duration).
2. **Drafts Specs:** Generates `PRD.md`, `TRD.md`, `UI_UX.md`, `BACKEND_SCHEMA.md`, and `APP_FLOW.md` with Mermaid sequence and ER diagrams.
3. **Audits Consistency:** Runs `check-consistency.py` to confirm `REQ-001` is covered across all technical artifacts.
4. **Gates Implementation:** Initializes state in `.blueprint/state.yaml` as `READY_FOR_REVIEW`. Blocks code execution until user says *"Approved"*.

### Example 2: Project Sync in Action
**User Prompt:**
> *"Implement rate limiting on the public API using Redis."*

**Agent Flow:**
1. **Implements & Tests:** Implements Redis rate-limiting middleware and verifies unit tests pass.
2. **Detects Impact:** Runs `detect-readme-impact.py`, identifying new `REDIS_URL` and `RATE_LIMIT_RPM` environment variables.
3. **Surgically Reconciles:** Updates the Environment Variables table in `README.md`.
4. **Quarantines Scratch:** Moves ad-hoc load test script `stress_test.py` into `.agent/scratch/stress_test.py` and verifies `.agent/scratch/` is ignored in `.gitignore`.
5. **Summarizes:** Delivers transparent completion report itemizing README updates and quarantined files.

### Example 3: Commit Architect in Action
**User Prompt:**
> *"Connect the signup page to the authentication endpoint, handle network errors, and add tests."*

**Agent Flow:**
1. **Inspects Working Tree:** Runs `inspect-working-tree.py` to verify no unrelated edits are staged.
2. **Plans Sequence:** Designs two logical commits:
   - Commit 1: Core API client authentication method and unit tests.
   - Commit 2: Signup form submission UI, loading states, and error handling.
3. **Executes & Reviews Diff:** Implements Unit 1, reviews `git diff --cached`, and commits with:
   `Add user authentication client and token handling`
4. **Repeats for Unit 2:** Implements UI integration, tests, reviews diff, and commits with:
   `Handle signup form submission and network error display`

### Example 4: Context Matrix in Action
**User Prompt:**
> *"/context-matrix Evaluate architecture trade-offs between monolith and microservices under 8GB memory limits."*

**Agent Flow:**
1. **Routes Framework:** Automatic selection engine selects `SOCRATES` (System Architecture & Trade-Offs).
2. **Inspects Grounded Context:** Gathers memory constraints, team size parameters, and operational boundaries.
3. **Enforces Boundaries:** Keeps planning separate from code generation; systematically compares bounded options.
4. **Delivers Tailored Plan:** Outputs trade-off matrix, failure modes, SLA evaluation criteria, and phased roadmap.

---

## Repository Structure

The actual structure of the `agent-dev-skills` collection is organized as four standalone sibling skills:

```text
agent-dev-skills/
│
├── README.md                      # Central collection landing page & catalog (this document)
│
├── context-matrix/                # Independent Skill: Prompt Architecture & Framework Engine
│   ├── README.md                  # Comprehensive skill documentation
│   ├── LICENSE                    # MIT License
│   ├── AUTHORS                    # Authorship attribution
│   ├── NOTICE                     # Legal disclaimers & trademark notices
│   ├── skill/                     # Canonical Open Agent Skill
│   │   ├── SKILL.md               # Main skill manifest with YAML frontmatter
│   │   ├── references/            # 8 framework reference manuals & quality checklists
│   │   └── scripts/               # Pure Python stdlib verification tools
│   ├── integrations/              # Multi-platform adapters (Antigravity, Claude, Cursor, Codex)
│   ├── examples/                  # 10 real-world case study walkthroughs
│   └── docs/                      # Architecture, portability, and contribution guides
│
├── commit-architect/              # Independent Skill: Commit Architecture
│   ├── README.md                  # Comprehensive skill documentation
│   ├── LICENSE                    # MIT License
│   ├── AUTHORS                    # Authorship attribution
│   ├── NOTICE                     # Legal disclaimers & trademark notices
│   ├── skill/                     # Canonical Open Agent Skill
│   │   ├── SKILL.md               # Main skill manifest with YAML frontmatter
│   │   ├── references/            # Deep reference manuals (progressive disclosure)
│   │   └── scripts/               # Pure Python stdlib verification tools
│   ├── integrations/              # Multi-platform adapters (Antigravity, Claude, Cursor, Codex)
│   ├── examples/                  # 12 real-world case study walkthroughs
│   └── docs/                      # Architecture, portability, and contribution guides
│
├── project-sync/                  # Independent Skill: Project Synchronization
│   ├── README.md                  # Comprehensive skill documentation
│   ├── LICENSE                    # MIT License
│   ├── AUTHORS                    # Authorship attribution
│   ├── NOTICE                     # Legal disclaimers & trademark notices
│   ├── skill/                     # Canonical Open Agent Skill
│   │   ├── SKILL.md               # Main skill manifest with YAML frontmatter
│   │   ├── references/            # Deep reference manuals (progressive disclosure)
│   │   └── scripts/               # Pure Python stdlib verification tools
│   ├── integrations/              # Multi-platform adapters (Antigravity, Claude, Cursor, Codex)
│   ├── examples/                  # 17 real-world case study walkthroughs
│   └── docs/                      # Architecture, portability, and contribution guides
│
└── project-blueprint/             # Independent Skill: Pre-Implementation Planning
    ├── README.md                  # Comprehensive skill documentation
    ├── LICENSE                    # MIT License
    ├── AUTHORS                    # Authorship attribution
    ├── NOTICE                     # Legal disclaimers & trademark notices
    ├── skill/                     # Canonical Open Agent Skill
    │   ├── SKILL.md               # Main skill manifest with YAML frontmatter
    │   ├── references/            # Deep reference manuals (progressive disclosure)
    │   └── scripts/               # Pure Python stdlib verification tools
    ├── integrations/              # Multi-platform adapters (Antigravity, Claude, Cursor, Codex)
    ├── examples/                  # 6 real-world reference blueprints & case studies
    └── docs/                      # Architecture, portability, and contribution guides
```

---

## Development & Contributing

Each skill is developed and maintained independently within its own directory:
1. **Canonical Standard:** Changes to core methodology belong in `skill/SKILL.md` and `skill/references/`.
2. **Zero Dependencies:** Helper scripts in `skill/scripts/` must run on Python 3.8+ using strictly the standard library. No third-party packages (`pip`) are permitted.
3. **Cross-Platform Encodings:** All scripts must explicitly configure UTF-8 output streams (`sys.stdout.reconfigure(encoding="utf-8", errors="replace")`) to run cleanly on Windows consoles as well as POSIX systems.
4. **Dogfooding:** Contributions should follow the Commit Architect standard for atomic commit slicing and Project Sync standards for documentation updates.

For specific contribution guidelines, see:
* [Context Matrix Contributing Guide](./context-matrix/docs/contributing.md)
* [Commit Architect Contributing Guide](./commit-architect/docs/contributing.md)
* [Project Sync Contributing Guide](./project-sync/docs/contributing.md)
* [Project Blueprint Contributing Guide](./project-blueprint/docs/contributing.md)

---

## Licensing

All repositories and artifacts within agent-dev-skills are distributed under the terms of the **MIT License**.

```text
MIT License

Copyright (c) 2026 SWAYAM KIRAN PRABHU

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

See individual repository license files:
* [Context Matrix License](./context-matrix/LICENSE)
* [Commit Architect License](./commit-architect/LICENSE)
* [Project Sync License](./project-sync/LICENSE)
* [Project Blueprint License](./project-blueprint/LICENSE)

---

## Authorship & Disclaimers

* **Creator and Copyright Owner:** **SWAYAM KIRAN PRABHU** (2026)
* **Project Status:** Independent Open-Source Software

### Third-Party Disclaimers
agent-dev-skills is an independent open-source developer toolchain. It is not affiliated with, sponsored by, endorsed by, or officially associated with:
* Google LLC or Alphabet Inc. (*Google Antigravity, Gemini*)
* Anthropic PBC (*Claude, Claude Code*)
* Anysphere Inc. (*Cursor*)
* OpenAI OpCo LLC (*OpenAI, ChatGPT, Codex*)

All product names, trademarks, and registered trademarks are property of their respective owners.

---

## Reference Links & Documentation

### agent-dev-skills Repositories
* [Context Matrix Repository Guide](./context-matrix/README.md)
* [Commit Architect Repository Guide](./commit-architect/README.md)
* [Project Sync Repository Guide](./project-sync/README.md)
* [Project Blueprint Repository Guide](./project-blueprint/README.md)

### Standards & Official Upstream Documentation
* [Agent Skills Specification](https://agentskills.io)
* [Google Antigravity Customization Documentation](https://antigravity.google)
* [Anthropic Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
* [Cursor AI Rules Documentation](https://docs.cursor.com/context/rules-for-ai)
* [OpenAI Custom Instructions & AGENTS.md](https://platform.openai.com)
