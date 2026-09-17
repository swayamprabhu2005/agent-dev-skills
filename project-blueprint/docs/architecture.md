# Project Blueprint System Architecture

Project Blueprint separates canonical specification methodology from platform delivery mechanisms.

---

## 1. Decoupled Core Philosophy

```text
                   PROJECT BLUEPRINT
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
* **Platform Adapters (`integrations/`):** Thin manifests and command configurations tailored to specific agent environments.

---

## 2. Progressive Disclosure

1. **Discovery Layer:** At startup, the agent reads only `name` and `description` from `SKILL.md` (~30 tokens).
2. **Activation Layer:** When a substantial planning task begins, the agent loads `SKILL.md`.
3. **Reference Layer:** Detailed guidance for specific tasks (e.g. Mermaid syntax or conflict resolution) is loaded on demand from `references/`.

---

## 3. Division of Labor: Skill vs. Scripts

* **Skill Reasoning:** Interactive questioning, architectural synthesis, cross-document alignment, and drafting specifications.
* **Deterministic Scripts:** Managing `.blueprint/state.yaml`, parsing requirement tags (`REQ-xxx`), and validating Mermaid diagram syntax.
