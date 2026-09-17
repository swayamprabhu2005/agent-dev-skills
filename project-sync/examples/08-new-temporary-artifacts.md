# Example 08: New Temporary Artifacts (Quarantine vs. Silent Deletion)

This example demonstrates the safe quarantine protocol for temporary agent scratch files: never silently delete files, and never misuse `.gitignore` as a trash can for loose filenames.

---

## 1. Implementation Change
While debugging a complex SQL join for an order reporting feature, the agent created:
* `scratch_test_query.py` in the root directory.
* `query_dump.json` containing 10,000 raw output rows.

The agent verified the query, integrated the fix into `src/reports/orders.py`, and validated the feature.

## 2. Determination of Documentation Impact
* The order query fix was an internal performance optimization.
* No CLI flags, setup steps, or configurations changed.
* **Decision:** No changes required for `README.md`.

## 3. Determination of Ignore-Rule & Quarantine Impact
* Inspecting `git status` shows:
  ```text
  ?? query_dump.json
  ?? scratch_test_query.py
  ```
* **Critical Evaluation:**
  * Are these files persistent build artifacts created by the application? **NO.**
  * Are they machine-specific environment configurations? **NO.**
  * Are they temporary scratchpad files created by the agent during debugging? **YES.**
* **Anti-Pattern 1 (Trash Can):** Adding `scratch_test_query.py` and `query_dump.json` to `.gitignore`.
* **Anti-Pattern 2 (Silent Deletion):** Silently running `rm` on the files without user knowledge, destroying investigation artifacts.
* **Correct Protocol:**
  1. Quarantine temporary artifacts by moving them to `.agent/scratch/`:
     - `.agent/scratch/scratch_test_query.py`
     - `.agent/scratch/query_dump.json`
  2. Ensure `.agent/scratch/` is in `.gitignore`.
  3. Report quarantined files in the completion summary for human review.

## 4. Resulting Modifications
* Moved temporary debug files to `.agent/scratch/`.
* `README.md`: Unchanged.
* `.gitignore`: Added `.agent/scratch/` rule.

## 5. Completion Summary
```text
Implementation complete.

Implemented:
- Optimized SQL join in OrderReportService to eliminate N+1 query bottleneck

Project synchronization:
- README.md — No changes required: Internal optimization with no user-facing documentation impact
- .gitignore — Updated: Added .agent/scratch/ rule for temporary agent scratchpad quarantine

Quarantined artifacts:
- .agent/scratch/scratch_test_query.py (temporary SQL test script quarantined for review)
- .agent/scratch/query_dump.json (diagnostic data dump quarantined for review)

Validation:
- Tests: 19 passed (pytest tests/test_order_reports.py)

Iteration complete.
```

