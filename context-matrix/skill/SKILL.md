---
name: context-matrix
description: >-
  Context Matrix orchestrates 8 prompt-engineering frameworks
  (CLARITY, SOCRATES, ANTICIPATE, PARTNER, TRUST, RIPPLE, CATCH, MAGIC) for software
  development, system architecture, debugging, research, and prompt optimization.
  Use to select optimal prompt frameworks, generate high-fidelity prompts, evaluate prompt
  quality, or execute context-aware workflows via /context-matrix.
license: MIT
metadata:
  author: SWAYAM KIRAN PRABHU
  version: 0.1.0
---

# Context Matrix

Context Matrix is a production-grade, reusable agent skill and intelligent prompt-engineering system built around eight specialized prompt frameworks.

> **Central Purpose:** Rather than relying on rigid, one-size-fits-all prompts or shallow templates, Context Matrix evaluates a task's intent, inspects repository context, selects the optimal prompt framework, and crafts high-fidelity, testable instructions.

---

## 1. When to Use This Skill

Activate this skill whenever:
* You are formulating complex coding requests, architecture plans, or technical explanations.
* You need to select the most effective prompt-engineering framework for a challenging task.
* You want to generate a reusable, copyable prompt for an external LLM or agent (`/context-matrix prompt ...`).
* You are auditing, improving, or evaluating draft prompts for clarity and testability (`/context-matrix improve ...` or `/context-matrix evaluate ...`).
* You are reviewing code, debugging tricky issues, or auditing datasets using structured analytical workflows (`/context-matrix ripple ...`).
* You are designing tutorials, educational guides, or onboarding documentation (`/context-matrix anticipate ...`).
* You are conducting evidence-based technology evaluations or research comparisons (`/context-matrix partner ...`).
* You are designing system architectures under strict resource trade-offs (`/context-matrix socrates ...`).

Do NOT use this skill to:
* Mechanically dump all eight framework templates into a single prompt.
* Bypass human approval gates or pre-implementation architecture specifications (e.g. Project Blueprint gates).
* Fabricate benchmarks, citations, pricing, or repository capabilities that do not exist.
* Execute destructive code changes when the user only asked for a prompt.

---

## 2. The Eight Internal Frameworks

Context Matrix organizes prompt engineering into eight distinct, specialized modules:

| Framework | Acronym Expansion | Primary Objective | Reference Guide |
| :--- | :--- | :--- | :--- |
| **CLARITY** | **C**ontext, **L**ook & Feel, **A**sk, **R**ules, **I**nput, **T**arget, **Y**ou | General engineering, feature implementation, and technical specs | [references/clarity.md](references/clarity.md) |
| **SOCRATES** | **S**ituation, **O**bjective, **C**onstraints, **R**ole, **A**ction, **T**hinking, **E**valuation, **S**ummary | System architecture, feasibility analysis, and resource trade-offs | [references/socrates.md](references/socrates.md) |
| **ANTICIPATE** | **A**udience, **N**eed, **T**ask, **I**nformation, **C**onstraints, **I**llustrate, **P**lan, **A**ct, **T**est, **E**nhance | Tutorials, educational resources, and onboarding documentation | [references/anticipate.md](references/anticipate.md) |
| **PARTNER** | **P**urpose, **A**udience, **R**esearch, **T**hink, **N**arrow, **E**xecute, **R**eview | Technology evaluation, research comparisons, and empirical benchmarks | [references/partner.md](references/partner.md) |
| **TRUST** | **T**ask, **R**eason, **U**nderstand, **S**tructure, **T**ailor | Tailored decision support, situational advisory, and targeted recommendations | [references/trust.md](references/trust.md) |
| **RIPPLE** | **R**ole, **I**nput, **P**rocess, **P**oints, **L**ayout, **E**valuate | Forensic code reviews, debugging, dataset audits, and security scans | [references/ripple.md](references/ripple.md) |
| **CATCH** | **C**ontext, **A**im, **T**one, **C**riteria, **H**elp | Everyday communications, concise release notes, and short technical requests | [references/catch.md](references/catch.md) |
| **MAGIC** | **M**otivation, **A**udience, **G**oal, **I**nput, **C**reate | Creative deliverables, narrative scripts, comic storyboards, and marketing copy | [references/magic.md](references/magic.md) |

---

## 3. Framework Selection Engine

When invoked without an explicit framework, Context Matrix evaluates task intent using the following routing defaults:

```text
Incoming Task / Request
       │
       ├── Creative, storytelling, visual concepts? ──────────────► MAGIC
       ├── Concise, everyday communication or short script? ──────► CATCH
       ├── Code review, debugging, dataset audit, or diagnostics? ─► RIPPLE
       ├── Educational tutorial, onboarding, or training? ────────► ANTICIPATE
       ├── Deep research, competitive tool comparison, PoC? ─────► PARTNER
       ├── High-stakes decision support or tailored advice? ──────► TRUST
       ├── Architecture planning, feasibility, or trade-offs? ────► SOCRATES
       └── Core coding, functional specs, or technical tasks? ────► CLARITY
```

### Multi-Framework Combinations
When a task spans complementary domains, Context Matrix combines at most two frameworks, assigning each a distinct role:
* **SOCRATES + RIPPLE:** SOCRATES weighs architectural trade-offs; RIPPLE executes structured inspection of candidate implementations.
* **CLARITY + RIPPLE:** RIPPLE diagnoses the bug; CLARITY specifies the precise bug-fix requirements and test contracts.
* **ANTICIPATE + MAGIC:** ANTICIPATE structures the pedagogical flow; MAGIC authors the creative narrative or comic layout.
* **PARTNER + SOCRATES:** PARTNER gathers empirical ecosystem research; SOCRATES analyzes technical feasibility and resource limits.
* **CATCH + CLARITY:** CATCH maintains concise speed; CLARITY enforces strict output boundaries.

For detailed routing mechanics, see [references/framework-selection.md](references/framework-selection.md).

---

## 4. Supported Command Modes (`/context-matrix`)

Context Matrix is invoked through `/context-matrix`. The skill interprets the trailing arguments to trigger one of nine interaction modes:

```text
/context-matrix [optional arguments]
```

1. **Auto Selection (`/context-matrix [task]` or `/context-matrix`):** Automatically determines the best framework, executes the task, and briefly states the framework chosen. If invoked empty, displays an overview and example commands.
2. **Explicit Framework (`/context-matrix [framework] [task]`):** Honors the user's chosen framework (`clarity`, `socrates`, `anticipate`, `partner`, `trust`, `ripple`, `catch`, `magic`).
3. **Explicit Auto (`/context-matrix auto [task]`):** Runs the automatic selection engine and reports the routing decision.
4. **Explain Framework (`/context-matrix explain [framework]`):** Explains framework components and use cases with an illustrative example without altering code.
5. **Generate Prompt (`/context-matrix prompt [task]`):** Produces a copyable, standalone prompt formatted for external AI models without modifying repository files.
6. **Improve Prompt (`/context-matrix improve [prompt]`):** Audits and refines a draft prompt, adding missing constraints and structure while preserving intent.
7. **Evaluate Prompt (`/context-matrix evaluate [prompt]`):** Evaluates a prompt against the 10-point Quality Checklist, returning a qualitative rating (`Ready to Use`, `Ready with Assumptions`, or `Needs Clarification`).
8. **Combine Frameworks (`/context-matrix combine [fw1] [fw2] [task]`):** Executes a phased workflow orchestrating two frameworks.
9. **Help (`/context-matrix help`):** Prints a concise command cheat sheet.

For complete mode specifications, see [references/usage-modes.md](references/usage-modes.md).

---

## 5. Project-Aware Context Grounding

Context Matrix adapts to the actual software project in which it is invoked:

1. **Audit Relevant Project Assets:** Inspect directory structure, language configs (`package.json`, `Cargo.toml`, `pyproject.toml`), and active source files relevant to the task.
2. **Respect Existing Specifications:** Check for pre-implementation artifacts (e.g. `.blueprint/state.yaml`, `PRD.md`, `TRD.md`). Treat approved specifications as binding constraints.
3. **Grounding Categories:**
   * **Verified Facts:** Code, configurations, and test outcomes directly verified in the workspace.
   * **User Requirements:** Explicit parameters given in the prompt.
   * **Stated Assumptions:** Sensible default engineering choices, clearly identified.
   * **Targeted Questions:** At most 1–2 prioritized questions with defaults when critical information is missing.
4. **Strict Anti-Hallucination:** Never fabricate non-existent files, mock APIs, synthetic test results, or citations.

---

## 6. Execution Boundaries & Approval Discipline

Context Matrix enforces three distinct execution boundaries:

1. **Prompt Mode (`/context-matrix prompt ...`):** Generates prompt text only. Never touches codebase files.
2. **Advice Mode (`/context-matrix explain ...` / `/context-matrix evaluate ...`):** Delivers analytical feedback and methodology. Never alters codebase files.
3. **Execution Mode (`/context-matrix [framework] Implement ...`):**
   * Verifies existing project approval gates before writing code.
   * Runs local unit tests and compilers when available.
   * Preserves uncommitted human edits.
   * Never runs destructive Git commands (`git reset --hard`, `git clean -fd`).

---

## 7. Quality Evaluation Checklist

Before finalizing any prompt or task output, evaluate it against the 10-Point Checklist:
* Goal clarity, context completeness, task specificity, negative constraints, input sufficiency, deliverable definition, feasibility, verification protocol, signal-to-noise ratio, and clear fact/assumption boundaries.

For the complete rubric, see [references/prompt-quality-checklist.md](references/prompt-quality-checklist.md).

---

## 8. Deterministic Helper Scripts

Pure Python standard-library utilities support validation and routing:

* `python skill/scripts/select-framework.py --task "..."`: Evaluates a task description and returns recommended framework(s) as JSON.
* `python skill/scripts/evaluate-prompt.py --prompt "..."`: Audits a draft prompt against the 10-point checklist and outputs qualitative readiness status.
* `python skill/scripts/test-context-matrix.py`: Automated test suite verifying routing, framework modules, and structural integrity.
