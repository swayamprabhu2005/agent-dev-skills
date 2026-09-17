# Contributing to Project Sync

We welcome contributions to Project Sync from the developer and agent engineering community!

---

## 1. Core Contribution Guidelines

1. **One Canonical Methodology:**
   All core methodology must live in `skill/SKILL.md` and `skill/references/`. Platform integrations in `integrations/` must remain thin adapters.
2. **Minimal Diff Discipline:**
   The skill's primary philosophy is surgical, minimal targeted edits. Any proposed modifications to rules or heuristics must reinforce this principle.
3. **Deterministic Scripts:**
   Scripts in `skill/scripts/` must rely strictly on standard Python 3.8+ with no external `pip` dependencies.
4. **Transparent Authorship:**
   Project Sync is licensed under the **MIT License** with copyright held by **SWAYAM KIRAN PRABHU**.
