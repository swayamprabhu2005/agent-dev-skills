# RIPPLE Framework

> **Purpose:** Perform rigorous, systematic analysis of source code, bug reproductions, data pipelines, datasets, and complex technical artifacts.

The **RIPPLE** framework enforces structured diagnostic and review discipline. Rather than providing subjective or unstructured feedback, RIPPLE decouples the analytical process, inspection points, presentation layout, and empirical validation methods.

---

## 1. The 6 Components of RIPPLE

```text
┌────────────────────────────────────────────────────────────────────────┐
│ R — Role    : Analytical persona (e.g. Security Auditor, Data Scientist)│
│ I — Input   : Source code, stack traces, telemetry logs, or datasets   │
│ P — Process : Step-by-step diagnostic or analytical procedure to follow│
│ P — Points  : Specific dimensions, invariants, or metrics to inspect   │
│ L — Layout  : Presentation structure (severity table, diff, root-cause)│
│ E — Evaluate: Empirical validation methods (unit tests, assertions)    │
└────────────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

1. **R — Role:**
   * Specialized analytical lens: Senior AppSec Auditor, Database Performance DBA, Senior Code Reviewer, Static Analysis Specialist.
2. **I — Input:**
   * Concrete artifacts to inspect: Git diffs, stack traces, schema dumps, CSV data distributions, or memory profiles.
3. **P — Process (Analytical Methodology):**
   * The exact sequence of investigation:
     * Phase 1: Invariant verification.
     * Phase 2: Boundary value testing & edge case scanning.
     * Phase 3: Resource lifecycle & leak inspection.
     * Phase 4: Error propagation and fault recovery.
4. **P — Points (Explicit Inspection Metrics):**
   * Specific categories to audit: Concurrency safety, SQL injection vulnerability, memory allocation in loops, backward compatibility, null-pointer safety, time complexity.
5. **L — Layout:**
   * Formatted deliverable structure:
     * Summary of Findings.
     * Severity Table (Critical, Major, Minor, Informational).
     * Root Cause Analysis with exact line references.
     * Remediated code diff.
6. **E — Evaluate (Empirical Verification):**
   * *Critical Core:* How do we prove the diagnosis is correct?
   * For software: Write a failing reproduction test before patching, run the test suite, verify the patch passes.
   * *Rule:* Never rely solely on model self-assessment; mandate executable verification.

---

## 2. Empirical Verification vs. Speculation

> [!IMPORTANT]
> When debugging software, an AI agent should never merely say "I fixed it" without running tests or verifying the fix against the reproduction input. RIPPLE requires active validation.

```text
1. Inspect Input & Reproduce Defect
           ↓
2. Follow Analytical Process across Inspection Points
           ↓
3. Isolate Exact Failure Mechanism
           ↓
4. Formulate Remediated Patch
           ↓
5. Run Empirical Evaluation (Tests, Compilation, Linters)
           ↓
6. Output Structured Layout (Report + Verified Diff)
```

---

## 3. When to Use RIPPLE

* **Primary Use Cases:**
  * Pull request reviews and code quality audits.
  * Root-cause debugging of crash reports, stack traces, and memory leaks.
  * Dataset sanity audits, missingness checks, and distribution drift analysis.
  * Security vulnerability scanning and threat modeling.
* **When NOT to Use:**
  * Authoring brand new greenfield features from scratch (use **CLARITY**).
  * High-level architectural roadmaps (use **SOCRATES**).

---

## 4. Evaluation Checklist for RIPPLE Prompts

* [ ] Is the Input artifact (code, log, dataset) explicitly provided or located?
* [ ] Is the diagnostic Process defined sequentially?
* [ ] Are specific inspection Points (security, concurrency, performance) itemized?
* [ ] Does the Layout mandate clear severity categorization and line-linked findings?
* [ ] Is there an empirical verification step (test runner, benchmark, assertion check)?

---

## 5. Practical Examples

### Example 1: Code Review & Bug Diagnostics (Rust)

```markdown
**Role:** Senior Systems Programmer and Rust Safety Auditor.
**Input:** Our concurrent threadpool implementation in `src/pool.rs` (attached) causing intermittent panics under heavy load.
**Process:**
1. Trace channel closure and worker shutdown sequence.
2. Audit all `unsafe` blocks for undefined behavior and pointer aliasing.
3. Inspect mutex lock ordering to detect potential deadlock cycles.
4. Verify error propagation when worker threads panic.
**Points:**
- Deadlock vulnerability under concurrent `shutdown()` calls.
- Memory leak on unconsumed tasks during shutdown.
- Thread panic isolation (ensuring one failing task does not crash the supervisor).
**Layout:**
1. Executive Summary.
2. Findings Table (Severity, File/Line, Description).
3. Root Cause Walkthrough.
4. Corrected Rust code with unified diff.
**Evaluate:**
- Provide a unit test with 50 concurrent threads triggering shutdown that reproduces the panic without the fix and passes with the fix.
```

### Example 2: Dataset Quality & Pipeline Audit

```markdown
**Role:** Senior Data Quality Engineer.
**Input:** Production user analytics export `analytics_2026_q1.csv` (1.2M records).
**Process:**
1. Schema & type conformance inspection.
2. Null/missing value quantification per column.
3. Outlier and anomalous distribution detection (timestamp anomalies, negative durations).
4. Referential integrity check against `users` dimension.
**Points:**
- Timestamp formatting consistency (UTC ISO-8601 vs local timestamps).
- Duplicate event UUIDs.
- Cardinality anomalies in categorization fields.
**Layout:**
- Tabular Data Quality Scorecard.
- Top 5 data corruption risks.
- SQL remediation script to quarantine invalid rows.
**Evaluate:**
- Output executable Python assertions using `pandas` to validate cleaned data.
```
