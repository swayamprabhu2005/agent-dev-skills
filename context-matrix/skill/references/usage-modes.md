# Context Matrix Command & Usage Modes

Context Matrix is accessed through the primary slash command `/context-matrix`. The skill interprets the arguments that follow `/context-matrix` to dynamically invoke the appropriate operating mode.

> **Important Platform Note:**
> Antigravity derives slash commands directly from the installed skill directory name. With Context Matrix installed at `.agents/skills/context-matrix/SKILL.md`, `/context-matrix` is registered natively. Arguments such as `clarity`, `prompt`, or `auto` are handled inside the skill's instructions.

---

## 1. Summary of Supported Argument Modes

| Mode | Invocation Syntax | Purpose | Output Deliverable |
| :--- | :--- | :--- | :--- |
| **Mode A: Auto Task** | `/context-matrix [task]` or `/context-matrix` | Automatically selects optimal framework and executes | Formulated result + brief framework rationale |
| **Mode B: Explicit Framework** | `/context-matrix [framework] [task]` | Forces a specific framework (e.g. `/context-matrix clarity ...`) | Execution using the designated framework |
| **Mode C: Explicit Auto** | `/context-matrix auto [task]` | Explicit request for framework routing | Selected framework + rationale + task result |
| **Mode D: Explain** | `/context-matrix explain [framework]` | Explains a framework without running tasks | Framework components, purpose, and examples |
| **Mode E: Generate Prompt** | `/context-matrix prompt [task]` | Creates a copyable prompt for external LLMs | Ready-to-use prompt string + metadata |
| **Mode F: Improve Prompt** | `/context-matrix improve [prompt]` | Hardens and refines an existing prompt | Revised prompt + summary of key improvements |
| **Mode G: Evaluate Prompt** | `/context-matrix evaluate [prompt]` | Scores prompt quality across 10 dimensions | Qualitative status + actionable gap checklist |
| **Mode H: Combine Frameworks** | `/context-matrix combine [fw1] [fw2] [task]` | Orchestrates multi-framework workflows | Phased execution leveraging both frameworks |
| **Mode I: Help & Guidance** | `/context-matrix help` | Displays available commands and frameworks | Quick-reference manual with copyable examples |

---

## 2. Detailed Mode Specifications

### Mode A: Automatic Selection (`/context-matrix [task]`)
* **Trigger:** User types `/context-matrix` with or without a task description.
* **Behavior:**
  * If no task is supplied: Outputs a brief welcome explaining Context Matrix, the 8 frameworks, and copyable example invocations.
  * If a task is supplied: Inspects repository context, runs the framework selection engine, picks the primary framework, executes the task, and mentions the chosen framework in 1 sentence.

### Mode B: Explicit Framework Selection (`/context-matrix [framework] [task]`)
* **Supported Framework Keywords (Case-Insensitive):**
  * `clarity`
  * `socrates`
  * `anticipate`
  * `partner`
  * `trust`
  * `ripple`
  * `catch`
  * `magic`
* **Behavior:**
  * Bypasses the auto-selection engine and honors the requested framework.
  * If another framework would offer a complementary advantage, mentions it as an optional enhancement without overriding the user's choice.

### Mode C: Explicit Auto (`/context-matrix auto [task]`)
* **Behavior:**
  * Runs the framework selection engine explicitly.
  * Identifies the primary (and optional secondary) framework.
  * Solves the user's task adhering to the chosen framework.

### Mode D: Explain (`/context-matrix explain [framework]`)
* **Examples:** `/context-matrix explain clarity`, `/context-matrix explain socrates`.
* **Behavior:**
  * Explains the framework acronym, core philosophy, ideal use cases, and provides 1 concrete prompt example.
  * Does NOT perform codebase modifications or execute unrelated tasks.

### Mode E: Generate Reusable Prompt (`/context-matrix prompt [task]`)
* **Example:** `/context-matrix prompt Implement JWT authentication with refresh token rotation in Go`.
* **Behavior:**
  * Produces a structured, standalone prompt formatted for copy-pasting into any LLM or AI coding agent.
  * Includes role, context, task requirements, negative constraints, input assumptions, and output expectations.
  * Does NOT execute code changes in the repository.

### Mode F: Improve Existing Prompt (`/context-matrix improve [prompt]`)
* **Example:** `/context-matrix improve Make a website for selling shoes`.
* **Behavior:**
  * Diagnoses ambiguities, missing technical constraints, and unspecified deliverables in the user's draft prompt.
  * Re-engineers the prompt into a high-fidelity specification while strictly preserving original intent.
  * Provides a bulleted summary of key improvements made.

### Mode G: Evaluate Existing Prompt (`/context-matrix evaluate [prompt]`)
* **Example:** `/context-matrix evaluate Review this PR and tell me if it works`.
* **Behavior:**
  * Evaluates the draft prompt against the 10-point Prompt Quality Checklist (Goal clarity, Context, Constraints, Inputs, Target, etc.).
  * Assigns a qualitative readiness status (`Ready to Use`, `Ready with Assumptions`, or `Needs Clarification`).
  * Lists actionable recommendations to elevate the prompt's quality.

### Mode H: Combine Frameworks (`/context-matrix combine [fw1] [fw2] [task]`)
* **Example:** `/context-matrix combine socrates ripple Evaluate and audit our multi-tenant database partitioning logic`.
* **Behavior:**
  * Assigns distinct responsibilities to each framework (e.g. Framework 1 handles architectural trade-offs; Framework 2 handles systematic inspection).
  * Synthesizes the workflow cleanly without redundant repetition.

### Mode I: Help (`/context-matrix help`)
* **Behavior:**
  * Prints a concise cheat sheet listing the 8 frameworks, argument patterns, and copyable examples.
