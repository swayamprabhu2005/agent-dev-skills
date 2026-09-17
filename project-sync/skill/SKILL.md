---
name: project-sync
description: >-
  Synchronize human-facing documentation (README.md) and Git ignore rules (.gitignore)
  with meaningful software implementation changes. Trigger after completing a coding
  iteration or milestone to reconcile setup, features, configuration, and repository hygiene,
  then present a concise completion summary.
license: MIT
metadata:
  author: SWAYAM KIRAN PRABHU
  version: 0.1.0
---

# Project Sync

Project Sync teaches an AI coding agent how to automatically reconcile a software repository's
human-facing documentation (`README.md`) and Git ignore configuration (`.gitignore`) after completing
a meaningful implementation iteration, concluding with a concise, transparent completion summary.

> **Central Purpose:** After the agent completes a meaningful implementation iteration, reconcile
> the repository's `README.md` and `.gitignore` with what actually changed, then provide a concise
> completion summary.

---

## 1. When to Use This Skill

### Trigger Conditions (Meaningful Implementation Iteration)
Activate this skill **after** completing and validating a meaningful unit of coding work:
* Adding or removing a feature or public capability.
* Changing installation, build steps, or prerequisites.
* Adding, removing, or renaming environment variables or configuration files.
* Changing available CLI commands, scripts, or API endpoints.
* Introducing third-party services, databases, or external integrations.
* Generating persistent build outputs, local cache directories, or machine-specific artifacts.
* Initializing a brand-new repository that lacks a `README.md` or `.gitignore`.

### Silent / Inactive Conditions (Do Nothing)
Do **NOT** run or force changes when:
* Merely conversing with the user or answering architectural/investigatory questions.
* Making purely internal code tweaks (e.g., refactoring a private helper, fixing a variable typo, optimizing an internal loop) that have zero effect on user-facing behavior, setup, or ignore rules.
* The session ends without any code or filesystem modifications.

**Core Rule:** Automatic when useful, silent when unnecessary, and transparent when changing files.

---

## 2. End-of-Iteration Synchronization Workflow

```text
Implementation & Validation Complete
                 ↓
      [ 1. Inspect Git Changes ]
      git status --porcelain
      git diff HEAD (or diff against iteration base)
                 ↓
      [ 2. Detect Semantic Impact ]
      Did features, setup, config, commands, or integrations change?
      Did new untracked/generated artifacts appear?
                 ↓
      ┌──────────────────────────┴──────────────────────────┐
      ▼                                                     ▼
[ 3. README Assessment ]                              [ 4. .gitignore Assessment ]
Does README become inaccurate?                        Are new files generated/local-only?
Does a new capability need setup docs?                Are they already covered by existing rules?
Make minimal, targeted edits                          Add precise, non-broad rules if needed
(Preserve manual structure & style)                   (Never use as a trash can)
      └──────────────────────────┬──────────────────────────┘
                                 ↓
      [ 5. Review Diff of Sync Edits ]
      git diff -- README.md .gitignore
                 ↓
      [ 6. Deliver Completion Summary ]
      Factual, structured report to user
```

---

## 3. Responsibility A: README Synchronization

### Accuracy Over Completeness
The goal is **not** to document every changed line or internal function. The goal is to ensure the `README.md` accurately represents the project as it currently exists.

### Change Categories to Evaluate:
1. **Features:** New user-facing capabilities or deprecated/removed features.
2. **Setup & Prerequisites:** Changed runtimes (e.g., Node version bump), system libraries, or installation commands.
3. **Configuration:** New `.env` variables, changed config files, or modified default ports/flags.
4. **Usage & Commands:** New CLI flags, renamed npm/make scripts, or altered invocation workflows.
5. **Integrations:** New authentication providers (e.g., Google OAuth), payment gateways, databases, or cloud services.
6. **Project Structure:** Only if the README intentionally maintains a high-level architectural file tree.

### Editing Rules:
* **Minimal Targeted Edits:** Update only the specific paragraph, table row, or code block affected.
* **Preserve Voice & Style:** Match the repository's existing tone, heading conventions, and formatting.
* **No Unsolicited Rewrites:** Do not rephrase well-written human prose merely because you can.
* **Generated Sections:** If a section is demarcated as tool-generated (e.g., `<!-- BEGIN API DOCS -->`), follow the project's generator script rather than editing manually.

---

## 4. Responsibility B: `.gitignore` Synchronization

### Legitimate Ignore Criteria
Add an entry to `.gitignore` **only** if the item meets all of the following:
1. It is created by a build tool, compiler, package manager, test runner, or IDE.
2. It is machine-specific, sensitive (credentials, local `.env`), or temporary cache.
3. It is **not** already ignored by an existing glob pattern.
4. It is **not** an intentional project source, configuration, test, or documentation file.

### Safety Rules & Quarantine Protocol:
* **Never Silently Delete Files:** Never silently delete files from the working tree merely because you believe they are temporary scratchpads, logs, or diagnostic dumps. Project Sync is not a destructive cleanup utility; destroying files risks deleting human work.
* **Quarantine Protocol for Temporary Agent Artifacts:**
  1. *Identify:* Recognize genuinely temporary agent-generated scratchpads (e.g. ad-hoc query scripts, debug dumps).
  2. *Quarantine:* Move temporary artifacts into a dedicated project quarantine directory: `.agent/scratch/` (do not leave them in source roots).
  3. *Ignore Quarantine Directory:* Ensure `.agent/scratch/` is ignored in `.gitignore`. This maintains repository hygiene with a single, clean pattern rather than polluting `.gitignore` with individual file names.
  4. *Report:* List all quarantined files explicitly in the completion summary so the human user can inspect, retain, or delete them at their discretion.
* **No Trash Can for Loose Files:** Never append loose file names directly to `.gitignore` to hide unknown or misplaced files.
* **Precise Patterns:** Prefer narrow, explicit rules (e.g., `.agent/scratch/` or `coverage/`) over dangerous broad wildcards (e.g., `*.json` or `tmp*`).
* **Tool-Managed Blocks:** If `.gitignore` contains comments indicating a section is managed by an external tool (e.g., `# created by create-react-app`), do not modify those lines.

---

## 5. Preserving Manual User Edits

Never assume `README.md` or `.gitignore` is agent-owned. Human developers often maintain hand-crafted deployment guides, badges, sponsor links, or specific ignore groupings.

Before modifying either file:
1. Check `git diff -- README.md .gitignore` to see if the user has unstaged manual edits.
2. If uncommitted user edits exist, merge your synchronization cleanly into the appropriate section without clobbering their additions.
3. If a conflict is detected, pause and report it transparently.

---

## 6. Transparent Completion Summary

Every completed iteration must conclude with a clear, factual completion summary distinguishing:
* `Updated`: File was modified, accompanied by a one-line summary of what changed.
* `No changes required`: File was evaluated and confirmed to be accurate as-is.
* `Not applicable`: File does not apply to this project type.
* `Unable to verify`: Ambiguity prevented automated confirmation without user clarification.
* `Quarantined artifacts` (if applicable): Explicit list of files moved to `.agent/scratch/` for human review.

### Standard Template:
```text
Implementation complete.

Implemented:
- Added Google OAuth2 authentication flow
- Added token refresh handler in auth service
- Exposed GET/POST /auth/google endpoints

Project synchronization:
- README.md — Updated authentication and setup sections with Google OAuth variables
- .gitignore — No changes required (all generated tokens and caches already ignored)

Quarantined artifacts:
- .agent/scratch/scratch_auth_test.js (temporary debug script quarantined for review)

Validation:
- Tests: 14 passed (npm test)
- Build: Successful (npm run build)

Iteration complete.
```

---

## 7. Relationship with Sibling Skill (Commit Architect)

Project Sync and Commit Architect are complementary, non-overlapping sibling skills:

| Capability | Project Sync | Commit Architect |
| :--- | :---: | :---: |
| **Documentation Reconciliation** | ✅ Primary Responsibility | ❌ Does not handle |
| **`.gitignore` Hygiene** | ✅ Primary Responsibility | ❌ Does not handle |
| **Completion Summary** | ✅ Primary Responsibility | ❌ Does not handle |
| **Commit Slicing & Planning** | ❌ Defers to Commit Architect | ✅ Primary Responsibility |
| **Staged Diff Safety Review** | ❌ Defers to Commit Architect | ✅ Primary Responsibility |
| **Commit Message Authoring** | ❌ Defers to Commit Architect | ✅ Primary Responsibility |

Project Sync synchronizes the project files; Commit Architect subsequently architects how those files are staged and committed into Git history.

---

## 8. Progressive Disclosure References

Consult the in-depth reference manuals for detailed procedures:
* [README Synchronization Guide](references/readme-synchronization.md) - Impact heuristics, minimal diffing, and structure preservation.
* [Gitignore Synchronization Guide](references/gitignore-synchronization.md) - Exact pattern selection, avoiding wildcards, and clean categorization.
* [Semantic Impact Detection](references/impact-detection.md) - Heuristics for mapping code diffs to documentation needs.
* [First-Time Repository Initialization](references/first-time-initialization.md) - Bootstrapping README and .gitignore for fresh repos.
* [Safety & Preservation Rules](references/safety-rules.md) - Preserving user comments, custom blocks, and merge conflict safety.
* [Worked Scenarios and Examples](references/examples.md) - 17 exhaustive real-world examples.

---

## 9. Helper Scripts

Deterministic utilities are available in `scripts/`:
* `python scripts/detect-readme-impact.py`: Scans recent git diffs for changes affecting configuration, environment variables, commands, and dependencies.
* `python scripts/audit-gitignore.py`: Audits untracked files against current `.gitignore` and recommends precise, safe additions.
* `python scripts/generate-sync-summary.py`: Generates the standardized completion summary for user reporting.
