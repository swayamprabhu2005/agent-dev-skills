# Semantic Impact Detection Reference Guide

This guide provides the reasoning heuristics used by Project Sync to determine whether an implementation change carries semantic impact for `README.md` or `.gitignore`.

---

## 1. The Impact Decision Matrix

Not all code modifications are created equal. Use this matrix to evaluate incoming diffs:

```text
Incoming Git Diff
        │
        ├─► Did dependency manifests change? (package.json, pyproject.toml, Cargo.toml)
        │     └─► YES: Check if install steps, runtime version, or core commands changed.
        │
        ├─► Did environment templates change? (.env.example, config.yaml, settings.py)
        │     └─► YES: README configuration/environment section MUST be updated.
        │
        ├─► Did CLI entrypoints or script blocks change?
        │     └─► YES: README usage/commands section MUST be updated.
        │
        ├─► Did public API routes or major exports change?
        │     └─► YES: If README summarizes high-level endpoints, update them.
        │
        ├─► Did the build or test runner produce new untracked files?
        │     └─► YES: Check if they are persistent generated files. If so, assess .gitignore.
        │
        └─► Were edits confined to internal logic, private functions, or unit tests?
              └─► YES: ZERO IMPACT. Both README and .gitignore remain UNCHANGED.
```

---

## 2. File-by-File Impact Signatures

### 1. Configuration & Secrets Signatures
* **Indicators:** Modifying `.env.example`, `config/default.json`, `src/config.ts`, `settings.py`.
* **Action:** Check if new environment variables were introduced.
* **README Check:** Does `README.md` have a table or code snippet showing required environment variables? If yes, add the new variable with its default or format description.

### 2. Dependency & Tooling Signatures
* **Indicators:** Adding a major library to `package.json` (e.g., `redis`, `stripe`, `@auth/core`), changing `engines` field, or adding a new script (`"test:e2e": "playwright test"`).
* **Action:**
  * If a new external service is required (e.g., Redis), document the prerequisite in README.
  * If a new convenient script is added, add it to the README's "Available Scripts" section.

### 3. Public API & Routing Signatures
* **Indicators:** Adding `@app.get("/api/v1/export")` or modifying GraphQL schema definitions.
* **Action:** If the README contains an API Overview table or quickstart curl commands, ensure the new route or payload contract is accurately represented.

### 4. Untracked Artifact Signatures
* **Indicators:** New items appearing in `git status --porcelain` starting with `??`.
* **Action:**
  * Run `git check-ignore -v <path>`.
  * If untracked and NOT ignored, classify:
    * Is it a source file? (Stage for Git, do NOT ignore).
    * Is it a temporary agent scratchpad? (Delete it immediately).
    * Is it a build output / test cache / local database? (Add to `.gitignore`).

---

## 3. Heuristic Safeguards Against False Positives

To prevent annoying, trivial updates:
1. **The 30-Second Glance Rule:** If a human developer reviewing the PR would not expect the README to change, the agent should not touch it.
2. **No Cosmetic Upgrades:** Do not fix spelling in a paragraph unrelated to the current task.
3. **No Redundant Ignore Entries:** If `*.log` is already in `.gitignore`, never add `debug.log`.
