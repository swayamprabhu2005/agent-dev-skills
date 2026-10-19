# Context Matrix

> **An open-standard Agent Skill that orchestrates eight specialized prompt-engineering frameworks to construct precise, context-aware, and testable instructions for AI coding assistants.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Specification: Agent Skills](https://img.shields.io/badge/Spec-agentskills.io-blue.svg)](https://agentskills.io)
[![Frameworks: 8 Modules](https://img.shields.io/badge/Frameworks-8%20Specialized-green.svg)](skill/references/framework-selection.md)

---

## What is Context Matrix?

**Context Matrix** is not merely a static collection of eight prompt templates. It is an intelligent prompt-engineering system and framework selector designed for disciplined software engineering with AI coding assistants.

When tasked with complex engineering, architecture, debugging, research, or content creation requests, an assistant equipped with Context Matrix does not respond with generic, unconstrained completions or dump random templates.

Instead, it:
1. **Audits Intent & Task Archetype:** Evaluates whether the request is core coding, system design, forensic debugging, empirical research, educational training, situational advisory, everyday communication, or creative storytelling.
2. **Inspects Grounded Repository Context:** Scans active repository configurations, dependencies, architectural patterns, and existing specifications without dumping irrelevant files.
3. **Selects the Optimal Framework:** Routes the request to one of eight specialized frameworks, or orchestrates a multi-framework combination when justified.
4. **Enforces Negative Constraints & Boundaries:** Formulates explicit boundaries, input assumptions, and testable deliverable contracts.
5. **Audits Prompt Quality:** Applies the 10-point Quality Checklist to guarantee high signal-to-noise ratio and empirical verification criteria.

---

## Why Does It Exist?

AI coding assistants are capable of generating impressive code, but their output quality is severely degraded by predictable prompt-engineering pathologies:

* **The Underspecified One-Liner:** Prompts like *"Add authentication"* or *"Make it faster"* leave security parameters, token lifetimes, and database trade-offs to stochastic chance.
* **Template Inflexibility:** Forcing every request into the same rigid acronym template bloats simple requests and starves complex architectural problems of deep reasoning.
* **Hallucinated Grounding:** Generating synthetic citations, non-existent library APIs, or fictional benchmark numbers without evidence.
* **Unbounded Modifications:** Agents modifying critical production files or introducing unvetted third-party packages because negative constraints ("what NOT to touch") were omitted.
* **Lack of Verification Protocol:** Accepting generated code without automated test assertions, reproduction tests, or failure verification.

**Context Matrix solves this by providing a unified, context-aware framework selection engine and prompt orchestration workflow.**

---

## The Eight Prompt Frameworks

Context Matrix organizes prompt engineering into eight distinct, specialized modules:

| Framework | Acronym Expansion | Primary Objective | Reference Guide |
| :--- | :--- | :--- | :--- |
| **CLARITY** | **C**ontext, **L**ook & Feel, **A**sk, **R**ules, **I**nput, **T**arget, **Y**ou | General software engineering, feature implementation, and functional specifications | [`references/clarity.md`](skill/references/clarity.md) |
| **SOCRATES** | **S**ituation, **O**bjective, **C**onstraints, **R**ole, **A**ction, **T**hinking, **E**valuation, **S**ummary | System architecture, feasibility analysis, hardware limits, and trade-off exploration | [`references/socrates.md`](skill/references/socrates.md) |
| **ANTICIPATE** | **A**udience, **N**eed, **T**ask, **I**nformation, **C**onstraints, **I**llustrate, **P**lan, **A**ct, **T**est, **E**nhance | Developer onboarding, technical tutorials, courseware, and comprehension exercises | [`references/anticipate.md`](skill/references/anticipate.md) |
| **PARTNER** | **P**urpose, **A**udience, **R**esearch, **T**hink, **N**arrow, **E**xecute, **R**eview | Competitive tool evaluations, empirical research, benchmarks, and proof-of-concept tests | [`references/partner.md`](skill/references/partner.md) |
| **TRUST** | **T**ask, **R**eason, **U**nderstand, **S**tructure, **T**ailor | Tailored decision support, situational advisory, and targeted recommendations | [`references/trust.md`](skill/references/trust.md) |
| **RIPPLE** | **R**ole, **I**nput, **P**rocess, **P**oints, **L**ayout, **E**valuate | Forensic code reviews, root-cause debugging, dataset quality audits, and security reviews | [`references/ripple.md`](skill/references/ripple.md) |
| **CATCH** | **C**ontext, **A**im, **T**one, **C**riteria, **H**elp | Everyday team communications, release notes, concise announcements, and short scripts | [`references/catch.md`](skill/references/catch.md) |
| **MAGIC** | **M**otivation, **A**udience, **G**oal, **I**nput, **C**reate | Creative deliverables, narrative storytelling, comic scripts, and marketing concepts | [`references/magic.md`](skill/references/magic.md) |

---

## Framework Selection Decision Engine

```text
Incoming Task / Request
       │
       ▼
Explicit Framework Requested? ──(Yes)──► Honor explicit selection (validate appropriateness)
       │
      (No / Auto)
       │
       ├── Creative storytelling, comic scripts, marketing copy? ─► MAGIC
       ├── Concise, everyday communication or short script? ──────► CATCH
       ├── Code review, debugging, dataset audit, or diagnostics? ─► RIPPLE
       ├── Educational tutorial, onboarding, or training? ────────► ANTICIPATE
       ├── Deep research, competitive tool comparison, PoC? ─────► PARTNER
       ├── High-stakes decision support or tailored advice? ──────► TRUST
       ├── Architecture planning, feasibility, or trade-offs? ────► SOCRATES
       └── Core coding, functional specs, or technical tasks? ────► CLARITY
```

### Multi-Framework Combinations
When tasks span multiple domains, Context Matrix combines complementary frameworks without redundancy:
* **SOCRATES + RIPPLE:** SOCRATES weighs architectural trade-offs; RIPPLE audits candidate implementations.
* **CLARITY + RIPPLE:** RIPPLE diagnoses the bug; CLARITY specifies the precise bug-fix patch and contracts.
* **ANTICIPATE + MAGIC:** ANTICIPATE structures the pedagogical flow; MAGIC authors the creative comic/story.
* **PARTNER + SOCRATES:** PARTNER gathers empirical research; SOCRATES evaluates hardware/scale limits.
* **CATCH + CLARITY:** CATCH maintains concise speed; CLARITY enforces strict output boundaries.

---

## Supported Command Modes (`/context-matrix`)

Context Matrix is invoked via `/context-matrix`. The skill interprets trailing arguments to execute the requested interaction mode:

| Mode | Invocation Pattern | Purpose |
| :--- | :--- | :--- |
| **Auto Mode** | `/context-matrix [task]` or `/context-matrix` | Automatically selects optimal framework and executes task |
| **Explicit Framework** | `/context-matrix [framework] [task]` | Forces a designated framework (e.g. `/context-matrix clarity ...`) |
| **Explicit Auto** | `/context-matrix auto [task]` | Explicit request for framework routing analysis |
| **Explain Mode** | `/context-matrix explain [framework]` | Explains framework components and practical usage without executing tasks |
| **Generate Prompt** | `/context-matrix prompt [task]` | Creates a copyable, standalone prompt for external AI models |
| **Improve Prompt** | `/context-matrix improve [prompt]` | Hardens an ambiguous draft prompt into an unambiguous specification |
| **Evaluate Prompt** | `/context-matrix evaluate [prompt]` | Scores prompt against the 10-point checklist (`READY` / `NEEDS_CLARIFICATION`) |
| **Combine Mode** | `/context-matrix combine [fw1] [fw2] [task]` | Orchestrates multi-framework phased workflows |
| **Help** | `/context-matrix help` | Displays concise cheat sheet with copyable examples |

---

## Project-Aware Context Grounding

When invoked inside a software repository, Context Matrix grounds prompts in real project context:

1. **Audit Project Anatomy:** Inspects project configurations (`package.json`, `Cargo.toml`, `pyproject.toml`) and relevant source files.
2. **Respect Existing Specifications:** Detects pre-implementation artifacts (e.g., `.blueprint/state.yaml`, `PRD.md`) and enforces human approval gates.
3. **Execution Boundaries:**
   * `/context-matrix prompt ...` generates prompts only. Never touches codebase files.
   * `/context-matrix explain ...` explains methodology. Never touches codebase files.
   * `/context-matrix [framework] Implement ...` executes tasks, verifies tests, and respects version control safety.
4. **Anti-Hallucination Mandate:** Never fabricates mock APIs, synthetic test results, or unsupported citations.

---

## Cross-Platform Compatibility Matrix

| Platform | Core Methodology | Native Skill Discovery | Native Rules Support | Status |
| :--- | :---: | :---: | :---: | :--- |
| **Google Antigravity** | ✅ Supported | `.agents/skills/context-matrix/` or `~/.gemini/config/skills/context-matrix/` | `AGENTS.md` / `GEMINI.md` | **Verified Support** |
| **Claude Code** | ✅ Supported | `.claude/skills/context-matrix/` or `~/.claude/skills/context-matrix/` | `CLAUDE.md` | **Verified Support** |
| **Cursor** | ✅ Supported | `.cursor/skills/context-matrix/` or `~/.cursor/skills/context-matrix/` | `.cursor/rules/*.mdc` | **Verified Support** |
| **OpenAI Codex** | ✅ Supported | `.codex/skills/context-matrix/` or `.agents/skills/context-matrix/` | `AGENTS.md` | **Verified Support** |
| **Generic Agent Runtimes** | ✅ Supported | Varies (`.skills/context-matrix/`) | Platform dependent | **Standards-Compatible** |

---

## Installation & Usage

Every skill in the `agent-dev-skills` collection can be installed at the **project level** (for a specific repository) or at the **global level** (for all projects on your workstation).

### Option 1: Install into a Target Project (Recommended)
```bash
# In your target repository:
mkdir -p .agents/skills/context-matrix
cp -r /path/to/agent-dev-skills/context-matrix/skill/* .agents/skills/context-matrix/
```

### Option 2: Install Globally (All Workspaces)
* **Linux / macOS:** `~/.gemini/config/skills/context-matrix/`
* **Windows:** `%USERPROFILE%\.gemini\config\skills\cats\`

```bash
mkdir -p ~/.gemini/config/skills/context-matrix
cp -r /path/to/agent-dev-skills/context-matrix/skill/* ~/.gemini/config/skills/context-matrix/
```

---

## Verification & Testing

Context Matrix includes pure Python standard-library validation scripts:

```bash
# Run complete verification test suite:
python context-matrix/skill/scripts/test-context-matrix.py

# Test framework selection:
python context-matrix/skill/scripts/select-framework.py --task "Implement a distributed lock in TypeScript"

# Test prompt quality evaluator:
python context-matrix/skill/scripts/evaluate-prompt.py --prompt "Make a website"
```

---

## Authorship & Attribution

Context Matrix is created and maintained by **SWAYAM KIRAN PRABHU**.
Licensed under the [MIT License](LICENSE).
See [NOTICE](NOTICE) for trademark disclaimers.
