# Project Sync System Architecture

Project Sync is designed to serve as the post-implementation reconciliation engine for AI coding workflows.

---

## 1. Decoupled Core Architecture

```text
                      PROJECT SYNC
                           │
                           │
                  Canonical Core Skill
                 [skill/SKILL.md & references/]
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

* **Canonical Methodology (`skill/`):** Contains the vendor-neutral `SKILL.md`, operational manuals in `references/`, and deterministic audit scripts in `scripts/`.
* **Platform Adapters (`integrations/`):** Thin manifests and discovery configurations tailored to specific agent environments.

---

## 2. Progressive Disclosure

1. **Discovery Layer:** The agent reads only `name` and `description` from `SKILL.md` at session startup (~30 tokens).
2. **Activation Layer:** When a meaningful implementation iteration concludes, the agent loads `SKILL.md`.
3. **Reference Layer:** Detailed guidance for edge cases (e.g. tool-generated documentation or pre-existing uncommitted user changes) is loaded on-demand from `references/`.

---

## 3. The Division of Labor

* **Skill Reasoning:** Contextual evaluation of whether a feature deserves mention in the README, tone matching, and human summary phrasing.
* **Deterministic Scripts:** Parsing `git diff`, detecting modified config templates, checking `git check-ignore`, and auditing for sensitive files.
