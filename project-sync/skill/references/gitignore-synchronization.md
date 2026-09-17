# Gitignore Synchronization Reference Guide

This guide establishes the criteria, precision standards, and safety rules for synchronizing `.gitignore` with repository changes.

---

## 1. The Core Purpose of `.gitignore`

The purpose of `.gitignore` is to declare which untracked files should **never** be checked into version control because they are:
1. Generated build artifacts (e.g., compiled binaries, minified bundles, distribution folders).
2. Machine-specific local state (e.g., SQLite dev databases, IDE workspaces, OS desktop artifacts).
3. Secret or private configuration (e.g., `.env`, private keys, local auth tokens).
4. Package dependencies managed by a lockfile (e.g., `node_modules/`, `vendor/`).

---

## 2. The Strict Non-Negotiable Rules

### Rule 1: Never Use `.gitignore` as a Trash Can
* ❌ An agent creates a temporary test file `test_scratch_123.py` or downloads a data dump in the root folder, doesn't know what to do with it, and appends `test_scratch_123.py` to `.gitignore`.
* **Correction:** If a file is temporary scratch created by the agent, **delete it** before concluding the iteration! `.gitignore` is for persistent, predictable project artifacts, not temporary agent trash.

### Rule 2: Always Check Existing Coverage First
Before adding any new pattern, run:
```bash
git check-ignore -v path/to/untracked/file
```
If this command returns an existing rule (e.g., `dist/` is already covered by `build/` or an existing `.gitignore` line), **do not add a redundant entry**.

### Rule 3: Prefer Precise Rules Over Broad Wildcards
* ❌ Adding `*.log` when only `app-runtime.log` should be ignored (someone might have an intentional `changes.log` or test fixture).
* ❌ Adding `*.json` to ignore a generated report (this ignores `package.json`, `tsconfig.json`, and all project configuration!).
* ❌ Adding `temp*` (might match a valid source file like `templateRenderer.ts`).
* ✅ Add specific paths: `logs/runtime.log`, `.agent-local/`, `coverage/`, `.cache/`.

---

## 3. Standard Categorization and Ordering

When appending new rules to an existing `.gitignore`, match the file's existing structure and categorize under standard headers if sections exist:

```gitignore
# -----------------------------------------------------------------------------
# Dependencies
# -----------------------------------------------------------------------------
node_modules/
vendor/

# -----------------------------------------------------------------------------
# Build Outputs & Distribution
# -----------------------------------------------------------------------------
dist/
build/
*.pyc
__pycache__/

# -----------------------------------------------------------------------------
# Local Environment & Secrets
# -----------------------------------------------------------------------------
.env
.env.local
*.pem
*.key

# -----------------------------------------------------------------------------
# Test Coverage & Tool Caches
# -----------------------------------------------------------------------------
coverage/
.pytest_cache/
.eslintcache
```

If the existing `.gitignore` is unsectioned, append the new rule neatly at the bottom with a concise explanatory comment.

---

## 4. Preserving Tool-Managed Sections

Many CLI tools (e.g., Next.js, Vite, Angular CLI, Create React App) insert tool-demarcated sections:

```gitignore
# Dependencies
/node_modules
/.pnp
.pnp.js

# Testing
/coverage

# Next.js
/.next/
/out/
```

**Guardrail:** Never delete or alter existing tool-managed blocks. Place custom project additions in a dedicated, clearly commented section at the end of the file.
