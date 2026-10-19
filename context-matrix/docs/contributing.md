# Contributing to Context Matrix

Thank you for your interest in contributing to Context Matrix. We welcome contributions from prompt engineers, software architects, and agent developers.

---

## Code of Conduct & Standards

1. **Vendor Neutrality:** Do not tie framework definitions or core instructions to proprietary features of a single vendor.
2. **Minimal Dependencies:** All helper scripts must use pure Python 3.8+ standard library modules. No third-party package dependencies.
3. **Decoupled Architecture:** Context Matrix must not depend on external skills or require other skills to be installed at runtime.
4. **Comprehensive Testing:** Any addition or modification to the 8 frameworks must include test cases in `skill/scripts/test-context-matrix.py`.

---

## Development Workflow

1. Fork or clone the repository.
2. Make your edits in `context-matrix/skill/SKILL.md`, `context-matrix/skill/references/`, or `context-matrix/skill/scripts/`.
3. Run the automated verification suite:
   ```bash
   python context-matrix/skill/scripts/test-context-matrix.py
   ```
4. Verify cross-platform compatibility across Windows PowerShell and Unix shells.
5. Submit a pull request with a concise, natural developer description of your changes.
