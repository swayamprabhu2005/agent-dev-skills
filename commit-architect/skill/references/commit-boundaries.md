# Commit Boundaries and Logical Units

This guide provides deep architectural rules for determining where a commit begins and ends.

---

## 1. What is a Logical Unit of Work?

A logical unit of work is the smallest set of changes that accomplishes one self-contained, reviewable intention without leaving the repository in a broken intermediate state.

A logical unit:
* **Has a singular purpose:** Can be described cleanly in one sentence without conjunctions like "and also", "plus", or "additionally".
* **Is functionally coherent:** Contains all the files directly required to fulfill that purpose.
* **Preserves buildability and testability:** Checking out this commit allows the codebase to compile and pass the test suite (vital for `git bisect`).
* **Is reversible:** Can be reverted via `git revert <hash>` without breaking unrelated features.

---

## 2. The Three Human Review Tests

Before staging and committing, the agent must pass three mental checks:

### Test 1: The Git Log Test
> *"If another experienced software engineer browses `git log --oneline` six months from today, will this commit title and summary clearly tell them what changed and why?"*

If the commit message requires someone to inspect 50 lines of diff across four disparate modules just to guess what was being attempted, the commit boundary is wrong.

### Test 2: The Diff Test
> *"Does the staged diff (`git diff --cached`) contain only changes that directly serve the commit message?"*

If the commit title says `Add token expiration handling`, but the diff also contains an unrelated import cleanup in `user_profile.py` or a CSS fix in the footer, the Diff Test fails.

### Test 3: The Boundary Test
> *"Do all modified files in this diff share the exact same conceptual lifecycle?"*

If reverting this commit would undo two unrelated decisions, they do not share the same lifecycle and must be separated.

---

## 3. When Changes MUST Stay Together

Do not split changes mechanically. Slicing too thin creates broken intermediate states that damage bisectability and introduce friction for reviewers.

Keep changes together when:
1. **Coupled Code and Schema:** An application change depends on a database migration file, and running the application without the migration causes an immediate crash or syntax error.
2. **Implementation and Immediate Unit Tests:** A new calculation function or data model and the unit tests that exercise its core edge cases should be committed together. (A reviewer needs to see the tests alongside the code to verify correctness).
3. **Renaming or Refactoring Call Sites:** Renaming an internal symbol, method, or file and updating all immediate call sites across the project must happen in one commit so the project compiles cleanly.
4. **Configuration and Bootstrapping:** Introducing a new configuration variable in `.env.example` and consuming it in `config.py` belong in the same commit.

---

## 4. When Changes MUST Be Separated

Split changes into distinct sequential commits when:
1. **Foundational Pre-work vs. Feature Consumer:**
   * Commit 1: Add new library dependency and base configuration.
   * Commit 2: Implement the core domain service using that dependency.
2. **Backend API vs. Frontend Client:**
   * Commit 1: Implement API endpoint, schema serialization, and server-side tests.
   * Commit 2: Implement UI component that queries the API endpoint.
   * *Rationale:* Allows independent deployment, separate code review by domain specialists, and cleaner rollbacks.
3. **Necessary Refactoring vs. Feature Addition:**
   * If implementing feature X requires first refactoring existing messy module Y:
     * Commit 1: Refactor module Y (without changing existing behavior or adding new features).
     * Commit 2: Add feature X on top of the clean module Y.
   * *Rationale:* Never mix behavioral changes with structural refactorings. Mixing them obscures bugs and makes diff reviews twice as difficult.
4. **Unrelated Bug Fixes or Cleanups:**
   * If you spot an existing bug or typo while working on an assigned feature, do not smuggle it into your feature commit. Create a dedicated commit or keep it untouched.

---

## 5. Granularity Spectrum: Finding the Balance

```text
[ Micro-Commit Chaos ] <────────── [ The Sweet Spot ] ──────────> [ Monolithic Megacommit ]
- 1 file per commit                - 1 logical intent             - Entire multi-day task
- "Fix typo in variable"           - Compiles & passes tests      - "Implemented auth system"
- "Add missing import"             - Includes coupled tests       - 47 files across 5 domains
- Cannot be reviewed cleanly       - Cleanly reviewable diff      - Impossible to bisect/revert
```

### Self-Check Questions for Sizing:
* *Is this commit too small?* If you find yourself writing a commit message like `Update import` or `Add parameter to function signature`, ask: "What feature or fix is this parameter for?" Bundle it with that actual change.
* *Is this commit too big?* If your commit touches backend routes, frontend views, build scripts, and documentation simultaneously, ask: "Can this be split into two or three independently working stages?"
