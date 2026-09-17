---
name: commit-architect
description: >-
  Architect clean, logical Git commit histories for software engineering tasks.
  Use when planning, implementing, validating, staging, and committing code changes,
  preventing giant monolithic commits, avoiding meaningless micro-commits, and
  authoring concise, natural developer commit messages.
license: MIT
metadata:
  author: SWAYAM KIRAN PRABHU
  version: 0.1.0
---

# Commit Architect

Commit Architect teaches an AI coding agent how to intelligently plan, divide, implement,
validate, and organize software work into a clean, logical Git commit history.

> **Central Purpose:** Commit Architect helps an AI coding agent architect the Git history of its work.
> Commit planning is an integral part of software engineering, not merely post-hoc formatting.

---

## 1. When to Use This Skill

Activate this skill whenever:
* You are starting a multi-step software implementation, refactor, bug fix, or feature.
* You are preparing to stage and commit changes to a Git repository.
* You need to break down complex tasks into atomic, reviewable work units.
* You need to format natural, professional developer commit messages.
* You are inspecting existing working-tree changes before undertaking new work.

Do NOT use this skill to:
* Mechanically generate a single commit message for an unreviewed, massive diff without inspecting boundaries.
* Force artificial Conventional Commit tags (`feat:`, `chore:`, etc.) when the repository does not mandate them.
* Rewrite Git history belonging to other contributors.

---

## 2. The Core Philosophy

A software repository's Git history is a communication tool for human engineers. Every commit should represent **one coherent conceptual change** that leaves the repository in a compiling, testable, and stable state whenever practical.

```text
User Request
     ↓
Understand the Complete Task
     ↓
Inspect Working-Tree & Git State
     ↓
Understand Project Architecture & Conventions
     ↓
Identify Logical Work Units
     ↓
Determine Dependency Order
     ↓
Design Commit Sequence Plan
     ↓
Implement First Logical Unit
     ↓
Validate (Build & Tests)
     ↓
Review Staged Diff (git diff --cached)
     ↓
Commit with Natural Developer Message
     ↓
Verify Commit (git log -1, git status)
     ↓
Implement Next Logical Unit
     ↓
...
     ↓
Review Final Git History (git log)
```

---

## 3. The Central Rule: Logical Intent

> **Split work by logical intent, not by file, function, or edit count.**

A commit represents one meaningful conceptual milestone. Balancing commit boundaries requires weighing seven key factors:

1. **Atomicity:** The commit does one thing completely. It does not mix unrelated concerns.
2. **Cohesion:** All modifications directly supporting that single concern live together (code, configuration, directly coupled tests).
3. **Reviewability:** A human reviewer can understand the diff in a single reading pass without context-switching between disparate topics.
4. **Dependency Order:** Dependent changes are committed after the foundational changes they rely upon.
5. **Repository Stability:** The project compiles, runs, and passes tests at each logical milestone wherever possible (bisectability).
6. **Reversibility:** If a feature or fix needs to be rolled back with `git revert`, it can be undone cleanly without collateral damage to unrelated features.
7. **Meaningful Granularity:** Avoid both over-splitting (micro-commits) and under-splitting (monolithic commits).

---

## 4. Boundary Discipline: Avoid Over-Splitting and Under-Splitting

### Anti-Micro-Commit Rule (Do Not Over-Split)
Do not commit trivial single-line changes or syntax fragments in isolation.
* **Bad:** 5 separate commits: `Add import`, `Rename variable`, `Add helper`, `Update test`, `Fix formatting`.
* **Good:** 1 coherent commit: `Add token refresh helper and validation tests`.

**One logical change does not equal one file or one function. More commits do not automatically mean better history.**

### Anti-Giant-Commit Rule (Do Not Under-Split)
Do not bundle dependencies, database schema migrations, backend controllers, frontend UI components, tests, and documentation into a single catch-all commit like `Implement authentication`.
* Split into focused, sequentially buildable slices:
  1. Add authentication configuration and token dependencies
  2. Add authentication service and cryptographic token handler
  3. Expose authentication endpoints in API router
  4. Connect frontend login form to authentication API
  5. Add end-to-end authentication tests and update setup documentation

---

## 5. Pre-Work Inspection: Working-Tree Safety

Before modifying any file, inspect the environment:

```bash
git status
git branch --show-current
git log -n 3 --oneline
git diff
```

The agent must distinguish:
* **Pre-existing changes:** Uncommitted modifications made by the user before the agent was invoked. **Never overwrite or destroy existing user work.**
* **Agent-created changes:** Modifications made intentionally for the current task.
* **Generated / temporary files:** Build outputs, coverage reports, `.DS_Store`, or logs. These belong in `.gitignore`, not in commits.

**Strict Prohibition:** Never run `git add .` or `git add -A` blindly. Always stage selectively by path (`git add path/to/file`) or inspect `git diff --cached` before committing.

---

## 6. Staged-Diff Review Protocol

Before running `git commit`, the agent must execute and inspect:

```bash
git diff --cached
```

Perform the **5-Point Diff Review Checklist**:
1. **Scope:** Does every staged line belong strictly to the single intended logical unit?
2. **Exclusion:** Are all unrelated files, leftover debugging prints, scratch files, and temporary artifacts excluded?
3. **Accuracy:** Does the proposed commit message accurately describe the staged diff?
4. **Completeness:** Are any required companion files (e.g., config updates or companion tests) missing from the staging index?
5. **Integrity:** Does the code compile, build, and pass tests in this exact staged state?

---

## 7. Natural Developer Commit Messages (Default Policy)

Commit Architect establishes a **natural programmer-style message policy** as the universal default:

* Use concise, ordinary, professional developer language in the imperative mood.
* Capitalize the subject line. Do not end the subject with a period. Keep it under 72 characters.
* **DO NOT automatically use Conventional Commits** (`feat:`, `fix:`, `chore:`, `refactor:`, `test:`) or scoped tags (`feat(auth):`) unless the repository's rules explicitly mandate them.

### Examples of Preferred Natural Messages:
* `Add Google login support`
* `Handle expired authentication tokens`
* `Add tests for token refresh`
* `Update authentication setup instructions`
* `Remove unused API client`
* `Handle missing request parameters in order search`
* `Move database configuration into the service container`

### Anti-Patterns to Avoid:
* Vague subjects: `Update files`, `Fix stuff`, `WIP`, `Various improvements`, `Bug fixes`.
* AI fluff: `Implement comprehensive and robust authentication mechanisms across backend`.
* Fabricated scopes: `feat(core-security-auth-module): Add login`.
* Automatic trailers: Never add `Generated by AI` or `Co-authored-by: AI` unless explicitly configured by the repository or user.

---

## 8. Repository-Specific Rules Precedence

Always inspect repository documentation and configuration before finalizing commit styles:
1. `AGENTS.md` / `GEMINI.md` / `CLAUDE.md` / `.cursor/rules/`
2. `CONTRIBUTING.md` / `DEVELOPMENT.md`
3. Commit lint configuration (`commitlint.config.js`, `.commitlintrc`, etc.)
4. Recent Git log style (`git log -n 10 --oneline`)

**Precedence Order:**
If the repository explicitly requires Conventional Commits (e.g., in `CONTRIBUTING.md` or enforced by commitlint hooks), **follow the repository's convention**. Otherwise, default to natural developer language.

---

## 9. Progressive Disclosure References

For in-depth guidance on specific scenarios, read the companion reference manuals:

* [Commit Boundaries Reference](references/commit-boundaries.md) - Rules for sizing, splitting, and bundling logical changes.
* [Natural Commit Messages Reference](references/natural-commit-messages.md) - Style guide, phrasing patterns, and body structure.
* [Commit Anti-Patterns Reference](references/commit-anti-patterns.md) - Catalog of anti-patterns (micro-commits, megacommit, AI tropes).
* [Dependency Ordering Reference](references/dependency-ordering.md) - How to sequence schemas, configs, services, UI, tests, and docs.
* [Working-Tree Safety Reference](references/working-tree-safety.md) - Handling dirty trees, untracked files, and destructive operation guardrails.
* [Worked Scenarios and Examples](references/examples.md) - 12 real-world scenarios illustrating complete planning and execution.

---

## 10. Helper Scripts

Deterministic command-line tools are available in `scripts/`:

* `python scripts/inspect-working-tree.py`: Audits current Git working tree, uncommitted files, branches, and untracked changes.
* `python scripts/validate-staged-diff.py`: Checks staged diff for common safety violations (accidental files, debug prints, oversized diffs).
* `python scripts/verify-commit.py`: Validates a proposed commit message against natural style rules and repository requirements.
