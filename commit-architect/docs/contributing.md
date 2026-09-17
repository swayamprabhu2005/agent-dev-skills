# Contributing to Commit Architect

Thank you for your interest in improving Commit Architect! We welcome contributions that refine our Git methodology, expand platform integrations, enhance verification scripts, or add real-world scenarios.

---

## 1. Core Contribution Principles

1. **One Canonical Methodology:**
   Never maintain separate, competing copies of the commit architecture philosophy. All core methodology must live in `skill/SKILL.md` and `skill/references/`. Platform integrations in `integrations/` must remain thin adapters.
2. **Deterministic Scripts vs. Skill Reasoning:**
   Keep scripts purely factual and deterministic (e.g., parsing git output, detecting secrets). Do not attempt to replace LLM contextual reasoning with brittle heuristics.
3. **Natural Developer Language:**
   Preserve Commit Architect's commitment to natural, professional developer commit phrasing as the primary default.
4. **Accuracy and Honesty in Platform Claims:**
   Never claim that a platform supports native skills unless verified against current official documentation. Clearly distinguish *Verified*, *Standards-Compatible*, and *Experimental*.

---

## 2. How to Contribute

### Adding or Updating a Platform Adapter
1. Create a directory in `integrations/<platform-name>/`.
2. Provide a `README.md` documenting verified discovery paths, installation steps, and configuration options.
3. If the platform supports rules or manifest files (e.g., `.mdc` or `plugin.json`), provide thin wrappers pointing back to the canonical skill.
4. Update `docs/portability.md` and the compatibility table in `README.md`.

### Adding a New Example Scenario
1. Add a new markdown document in `examples/XX-scenario-name.md`.
2. Follow the established structure:
   * The Task
   * Repository State & Discovery
   * Discovered Work
   * Dependencies Between Work Units
   * Proposed Commit Plan
   * Implementation Sequence
   * Final Commit Messages
   * Why Boundaries Make Sense
   * What the Agent Should Avoid
3. Add the scenario to the summary table in `skill/references/examples.md`.

### Improving Verification Scripts
* Scripts in `skill/scripts/` must run on vanilla Python 3.8+ using only standard library modules.
* Scripts must support both `--json` output for programmatic consumption and human-friendly terminal formatting.
* Test scripts on both Windows and POSIX environments.

---

## 3. Authorship and Licensing

Commit Architect is licensed under the **MIT License**.

All contributions become part of the open-source repository under the terms of the MIT License, with copyright and maintenance stewardship held by **SWAYAM KIRAN PRABHU**.
