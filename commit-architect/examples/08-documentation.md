# Example 08: Documentation (Accompanying vs. Dedicated Commits)

This example provides guidance on when documentation changes should accompany code and when they warrant a separate commit.

---

## 1. The Core Rule

* **Accompanying Docs (Same Commit):** Documentation that describes a specific API method, function docstrings, internal comments, or minor parameter updates in a README should accompany the code change directly.
* **Dedicated Docs (Separate Commit):** Comprehensive user manuals, standalone architecture design records (ADRs), major API reference rewrites, or site-wide documentation overhaul belong in their own commit.

---

## 2. Case A: Accompanying Documentation
* **Task:** "Add `--format=json` flag to the CLI tool."
* **Changes:**
  * `src/cli.ts` (parses `--format` flag)
  * `README.md` (adds `--format=json` to the usage command table)
  * `tests/cli.test.ts` (tests JSON serialization)
* **Decision:** Keep in ONE commit.
* **Commit Message:**
  ```text
  Support JSON output format in CLI export command

  Add --format flag accepting 'json' or 'table' (default). Update command-line
  reference in README with JSON output examples.
  ```
* **Rationale:** A reviewer inspecting the new CLI flag benefits from seeing the updated CLI help text and README table right in the same diff.

---

## 3. Case B: Dedicated Documentation Commit
* **Task:** "Write an architectural guide and deployment runbook for the new multi-region Kubernetes cluster."
* **Changes:**
  * `docs/architecture/multi-region-failover.md` (300 lines of architecture diagrams and failure recovery steps)
  * `docs/runbooks/database-failover.md`
  * `mkdocs.yml` (navigation updates)
* **Decision:** Dedicated Documentation Commit.
* **Commit Message:**
  ```text
  Add multi-region failover architecture guide and database runbook

  Document DNS failover topology, database replication lag thresholds,
  and step-by-step operational runbook for manual regional evacuation.
  ```
* **Rationale:** This is an independent knowledge artifact with no coupled application code. Isolating it allows technical writers and system architects to review the prose without clutter.

---

## 4. What the Agent Should Avoid
* ❌ Making a separate micro-commit for a 2-line typo fix in a README that was modified in the preceding feature commit.
* ❌ Putting 400 lines of unrelated documentation updates inside a core bug-fix commit.
