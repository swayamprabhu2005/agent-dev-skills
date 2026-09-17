# Commit Anti-Patterns

This document catalogs common pitfalls that AI agents produce when creating Git commits, along with direct remediation guidance.

---

## 1. The Robotic Conventional Commit Anti-Pattern

### The Flaw
Applying `feat(...)`, `fix(...)`, `chore(...)`, `refactor(...)` indiscriminately to repositories that do not use Conventional Commits.

### Why It Harms the Repository
* Clutters `git log` with redundant prefixes.
* Invents artificial scopes (e.g., `feat(database-models-user-entity): ...`) that do not exist in the project taxonomy.
* Violates project culture when human developers use standard Git prose.

### Remediation
Check `git log -n 10 --oneline` and `CONTRIBUTING.md`. If Conventional Commits are not standard in the repo, drop the prefixes entirely and write direct, active verbs:
* Instead of `feat(auth): implement google login` → `Add Google login flow`
* Instead of `fix(cart): resolve null reference error in checkout` → `Prevent null reference in checkout cart calculator`

---

## 2. The AI Buzzword and Fluff Anti-Pattern

### The Flaw
Generating pompous, repetitive, or hyperbolic prose to make a routine commit sound monumental.

### Examples of AI Tropes to Eliminate:
* ❌ `Implement comprehensive and robust authentication framework across multiple services`
* ❌ `Seamlessly enhance user experience by optimizing database interaction pipelines`
* ❌ `Elevate code quality with meticulous refactoring of payment processing logic`

### Remediation
Be direct, humble, and concrete:
* ✅ `Add Google OAuth2 login and token validation`
* ✅ `Index user_id column on transactions table`
* ✅ `Extract payment retry logic into PaymentGateway class`

---

## 3. The Unrequested AI Attribution Trailer Anti-Pattern

### The Flaw
Automatically appending metadata footers to commit messages:
```text
Add user profile page

Co-authored-by: AI Assistant <assistant@example.com>
Generated with Antigravity AI
```

### Why It Harms the Repository
* Many enterprise and open-source projects have strict policies regarding commit trailers, legal contributor agreements (DCO / CLA), and automated git hook validation.
* Fabricating co-authorship trailers can cause CI or CLA bots to fail.

### Remediation
**Never inject AI attribution footers unless:**
1. The repository's documentation explicitly requires them (e.g., in `CONTRIBUTING.md`), OR
2. The user explicitly requests them in their prompt.

Otherwise, author the commit cleanly without automated disclaimers.

---

## 4. The Fabricated Identity Anti-Pattern

### The Flaw
Falsely inventing human names, false cryptographic signatures, fake PGP keys, or fictitious Jira/GitHub issue numbers (e.g., `Fixes PROJ-9999`).

### Remediation
* Never fabricate issue identifiers. Only reference tickets or issues if they were explicitly provided in the user's task or branch name.
* Never forge GPG or SSH signatures.
* Never invent fictitious human co-authors.

---

## 5. The Vague Commit Anti-Pattern

### The Flaw
Writing ultra-terse, uninformative commit titles:
* ❌ `Update files`
* ❌ `Fix bug`
* ❌ `WIP`
* ❌ `Changes`
* ❌ `Refactor code`
* ❌ `More fixes`

### Remediation
A commit title must answer: **"What did this commit change, specifically?"**
* ✅ `Fix off-by-one error in pagination calculation`
* ✅ `Allow empty string for optional middle name field`

---

## 6. The Sneak Refactor (Opportunistic Cleanup)

### The Flaw
While fixing a simple bug in `order_service.py`, the agent notices some poorly formatted code or an old method, and decides to rename variables, reformat spacing, and restructure classes throughout the entire file.

### Why It Harms the Repository
* Distorts `git blame`, making it appear that the bug-fixer wrote all the reformatted lines.
* Obscures the actual fix during code review, forcing human reviewers to hunt through 200 lines of stylistic diff for the 3 lines of actual logic change.
* Increases the risk of merge conflicts for teammates working on concurrent branches.

### Remediation
Keep the bug fix minimal and focused. If a refactoring is genuinely necessary, do it in a **separate, dedicated commit** either immediately before or after the fix.

---

## 7. The Micro-Commit Storm

### The Flaw
Creating a commit for every single file edit or syntax change:
* Commit 1: `Import os module`
* Commit 2: `Add get_env function`
* Commit 3: `Call get_env in main`
* Commit 4: `Fix typo in get_env`

### Remediation
Group interconnected changes that form one working unit into a single commit:
* `Add environment variable helper for configuration loading`

---

## 8. Staging Accidental Artifacts and Secrets

### The Flaw
Running `git add .` blindly and committing:
* Secrets: `.env`, credentials, private keys, API tokens.
* Build directories: `dist/`, `build/`, `target/`, `node_modules/`, `__pycache__/`.
* IDE clutter: `.idea/`, `.vscode/`, `.DS_Store`, `Thumbs.db`.
* Temporary test artifacts: `test.log`, `coverage.html`, SQLite dev databases.

### Remediation
Always run `python scripts/inspect-working-tree.py` or `git status --porcelain` and selectively stage only tracked, intentional source files. Ensure generated files are recorded in `.gitignore`.
