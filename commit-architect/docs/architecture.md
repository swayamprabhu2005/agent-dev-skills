# Commit Architect System Architecture

Commit Architect is structured around a single canonical methodology decoupled from platform-specific delivery formats.

---

## 1. Architectural Philosophy: The Decoupled Core

To prevent ecosystem fragmentation and avoid maintaining multiple diverging copies of Git methodology, Commit Architect separates the **instructional core** from **platform delivery adapters**:

```text
                    COMMIT ARCHITECT
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

* **Canonical Core (`skill/`):** Contains the vendor-neutral `SKILL.md`, detailed operational manuals in `references/`, and deterministic verification tools in `scripts/`.
* **Platform Adapters (`integrations/`):** Thin shims, manifests (e.g., `plugin.json`), and discovery instructions tailored to specific agent environments.

---

## 2. Progressive Disclosure

AI coding agents operate under finite context windows and high inference costs. Dumping hundreds of lines of Git advice into every prompt degrades agent focus and exhausts tokens.

Commit Architect uses **progressive disclosure**:

1. **Discovery Layer (Frontmatter):**
   * At session startup, the agent reads only `name` and `description` from `SKILL.md` (approximately 30 tokens).
2. **Activation Layer (`SKILL.md` Body):**
   * When the agent identifies a commit-related task, it loads the core workflow and central rules from `SKILL.md`.
3. **Reference Layer (`references/`):**
   * If the agent encounters a complex scenario (e.g., an intricate database migration or an explicit Conventional Commit repository), it loads only the relevant reference file from `references/`.

---

## 3. Division of Labor: Reasoning vs. Deterministic Scripts

Commit Architect draws a strict boundary between agent reasoning and deterministic code:

| Component | Responsibility | Examples |
| :--- | :--- | :--- |
| **Agent Reasoning (Skill)** | Architectural planning, identifying logical boundaries, balancing cohesion, deciding commit order, drafting natural messages. | "Split this into a migration commit and an application service commit." |
| **Deterministic Scripts (Python)** | Inspecting git porcelain status, parsing diffs, identifying unignored secrets, checking line count thresholds, syntax validation. | `inspect-working-tree.py`, `validate-staged-diff.py`, `verify-commit.py` |

Scripts never make architectural decisions on behalf of the agent; they provide factual guardrails and audits to keep the agent safe.
