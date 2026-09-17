# Working-Tree Safety and Diff Inspection Protocol

This guide establishes the non-negotiable safety guardrails for managing Git state, inspecting working directories, and safely staging modifications.

---

## 1. Initial State Audit

Before editing any file, creating branches, or staging changes, the agent must perform a complete audit of the repository state:

```bash
# 1. Identify current branch and upstream tracking
git branch -vv

# 2. Inspect porcelain status for modified, deleted, or untracked files
git status --porcelain

# 3. Inspect recent commit style and branch head
git log -n 5 --oneline

# 4. Check for existing unstaged or staged diffs
git diff
git diff --cached
```

### Categorization Matrix
Every modified or untracked file detected in the repository falls into one of three categories:

| Category | Description | Action Required |
| :--- | :--- | :--- |
| **Pre-existing User Changes** | Edits made by the human developer prior to invoking the agent. | **PRESERVE UNCONDITIONALLY.** Never stage, overwrite, or discard without explicit user consent. |
| **Agent-Created Changes** | Edits made intentionally by the agent to fulfill the user's prompt. | Stage selectively for the designated commit. |
| **Transient / Generated Files** | Build outputs, logs, `.cache`, `.DS_Store`, SQLite databases. | Add to `.gitignore` or exclude from staging. Never commit. |

---

## 2. Strict Prohibition on Destructive Operations

The following commands can destroy uncommitted work or unpushed history. **They are strictly forbidden unless the user explicitly commands them in their prompt:**

* ❌ `git reset --hard`
* ❌ `git clean -fd` / `git clean -fx`
* ❌ `git checkout -- .` / `git restore .`
* ❌ `git branch -D`
* ❌ `git push --force` / `git push -f`
* ❌ Rewriting existing commits belonging to other contributors (`git rebase -i` on shared branches).

If an agent needs a clean tree to test something, it must use `git stash` with a clear message:
```bash
git stash push -m "antigravity-pre-task-backup" --include-untracked
```
And restore it when appropriate:
```bash
git stash pop
```

---

## 3. Staging Discipline: No Blind `git add .`

Running `git add .` or `git add -A` blindly is the leading cause of accidental secrets exposure, bloated commits, and broken builds.

### Golden Rule of Staging:
> **Stage files by exact path or explicit pattern.**

```bash
# Good: Explicit file staging
git add src/services/auth_service.py tests/test_auth_service.py

# Bad: Staging everything including scratch files and secrets
git add .
```

---

## 4. The 5-Point Staged Diff Review

Once files are staged, the agent must inspect the exact diff that will be committed:

```bash
git diff --cached
```

Review against the 5-point checklist:
1. **Zero Secret Leaks:** Verify no API keys, private tokens, passwords, or `.env` credentials are in the diff.
2. **Zero Transient Artifacts:** Verify no build artifacts (`dist/`, `.pyc`), IDE files, or log files are staged.
3. **Diff-to-Intent Match:** Does every single line addition or deletion directly support the current commit objective?
4. **No Smuggled Cleanups:** Did you accidentally stage reformatting or whitespace changes in unrelated functions?
5. **Compilation Verification:** Does the project build and pass unit tests with this staged index?

---

## 5. Handling Pre-Existing Dirty Trees

If the user's workspace already has unstaged changes before you begin work:
1. Do not blend your work with their pre-existing edits.
2. Work only on the files required for your task.
3. If their edits conflict with your task, ask for clarification or propose stashing their changes temporarily.
4. Stage only your modified files explicitly.
