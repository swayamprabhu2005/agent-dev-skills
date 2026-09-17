# Contributing to Project Blueprint

Thank you for your interest in improving **Project Blueprint**! This guide outlines how to contribute to the skill, its reference documentation, platform integrations, and validation scripts.

---

## 1. Project Stewardship & Author Attribution

* **Maintainer & Creator**: Swayam Kiran Prabhu
* **Copyright**: © 2026 Swayam Kiran Prabhu
* **License**: MIT License

All contributions will be licensed under the project's MIT License. Please ensure your contributions preserve the maintainer copyright notices and author attributions.

---

## 2. Core Philosophy & Design Principles

When modifying or proposing changes to Project Blueprint, adhere strictly to these principles:

1. **Standalone & Zero External Dependencies**:
   * All Python scripts in `skill/scripts/` MUST run on Python 3.8+ using strictly the standard library.
   * Do NOT add dependencies like `pyyaml`, `click`, `rich`, or `pydantic`.
   * Standard output MUST explicitly handle UTF-8 encoding safely on POSIX and Windows (`sys.stdout.reconfigure(encoding="utf-8", errors="replace")`).

2. **Progressive Disclosure**:
   * Keep `skill/SKILL.md` concise, action-oriented, and focused on operational lifecycle rules.
   * Place deep explanations, syntax tables, and detailed patterns in `skill/references/*.md`.

3. **Vendor Neutrality**:
   * The canonical core in `skill/` must not contain proprietary API keys, platform-specific hooks, or vendor-locked syntax.
   * Platform-specific configurations belong solely in `integrations/<platform>/`.

4. **Approval Gate Rigor**:
   * Never weaken or bypass the explicit human approval requirement.
   * The transition from planning to implementation MUST remain blocked until explicit approval is recorded.

---

## 3. Repository Structure

```
project-blueprint/
├── skill/                     # Canonical Agent Skill
│   ├── SKILL.md               # Main skill manifest (Open Agent Skills standard)
│   ├── references/            # Deep reference manuals (progressive disclosure)
│   └── scripts/               # Standalone Python verification scripts
├── integrations/              # Platform integration adapters
│   ├── antigravity/
│   ├── claude-code/
│   ├── cursor/
│   ├── codex/
│   └── generic/
├── examples/                  # Real-world walkthroughs and case studies
├── docs/                      # Architectural and maintainer documentation
├── LICENSE                    # MIT License
├── AUTHORS                    # Maintainer attribution
├── NOTICE                     # Legal notices and disclaimers
└── README.md                  # Comprehensive root project documentation
```

---

## 4. Development & Testing Workflow

Before submitting a change, run the suite of verification scripts against the sample blueprints:

```bash
# 1. Validate document structure and mermaid diagrams
python skill/scripts/validate-blueprint.py --dir examples/a-new-saas-app

# 2. Audit cross-document requirement consistency
python skill/scripts/check-consistency.py --dir examples/a-new-saas-app

# 3. Test state machine transitions
python skill/scripts/blueprint-state.py status --dir examples/a-new-saas-app
```

Ensure that:
* All 3 scripts exit with code `0`.
* Output is clean, formatted, and readable without Unicode encode errors on both Windows cmd/pwsh and Linux/macOS bash.

---

## 5. Commit Guidelines

We practice what we preach! Contributions should follow the atomic slicing and semantic commit standards championed by our sibling skill, **Commit Architect**:

* Use semantic prefixes: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`.
* Slice commits logically (e.g., separate documentation changes from script enhancements).
* Include clear problem-solution context in commit descriptions.
