# Context Matrix System Architecture

Context Matrix is structured around a single canonical prompt-engineering engine decoupled from platform-specific delivery formats.

---

## 1. Architectural Philosophy: The Decoupled Core

To prevent ecosystem fragmentation and ensure seamless cross-platform operation, Context Matrix separates the **canonical instructional core** from **platform delivery adapters**:

```text
                        Context Matrix SYSTEM
                             │
                             │
                    Canonical Core Skill
                   (skill/SKILL.md & references)
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
       Antigravity      Claude Code        Cursor
       Integration      Integration      Integration
            │                │                │
            └────────────────┼────────────────┘
                             │
                             ▼
                        Codex / Other
                     Agent Skills Runtimes
```

* **Canonical Core (`skill/`):** Contains the vendor-neutral `SKILL.md`, detailed operational manuals for each framework in `references/`, and deterministic routing utilities in `scripts/`.
* **Platform Adapters (`integrations/`):** Thin manifests (e.g. `plugin.json`), prompt rules (`.mdc`), and discovery instructions tailored to specific AI agent runtimes.

---

## 2. Progressive Disclosure

Large language models and AI coding assistants operate under finite context windows and high inference latency. Injecting hundreds of lines of prompt templates into every session degrades focus and exhausts tokens.

Context Matrix implements **progressive disclosure**:

1. **Discovery Layer (Frontmatter):**
   * At session startup, the agent reads only `name` and `description` from `SKILL.md` (~40 tokens).
2. **Activation Layer (`SKILL.md` Body):**
   * When the agent detects a prompt engineering or complex orchestration task, it loads the core workflow and routing decision tree from `SKILL.md`.
3. **Reference Layer (`references/`):**
   * The agent dynamically loads *only* the specific framework module needed for the task (e.g., `references/ripple.md` for a code review or `references/socrates.md` for architecture planning). Unrelated framework references are never loaded into context.

---

## 3. Division of Labor: Reasoning vs. Deterministic Tooling

Context Matrix maintains a strict boundary between model reasoning and deterministic code:

| Component | Responsibility | Examples |
| :--- | :--- | :--- |
| **Agent Reasoning (Skill)** | Identifying user intent, evaluating codebase architecture, selecting frameworks, crafting tailored prompt specifications. | "This task involves both hardware constraints and trade-offs; route to SOCRATES." |
| **Deterministic Scripts (Python)** | Auditing keyword intent, calculating readiness states, validating manifest frontmatter, unit testing. | `select-framework.py`, `evaluate-prompt.py`, `test-context-matrix.py` |

Scripts never restrict the agent's creativity; they provide factual guardrails and objective scoring.
