# Example 04: Researching and Comparing Existing Tools (PARTNER)

---

## 1. User Invocation

```text
/context-matrix partner Research open-source schema migration tools for PostgreSQL in Go. Compare golang-migrate, goose, and atlas. We need automated CI linting and zero-downtime safety checks.
```

---

## 2. Framework Selected

* **Primary Framework:** `PARTNER`
* **Selection Rationale:** Deep evidence-based research, vendor/library comparison, and empirical down-selection.

---

## 3. Relevant Context & Constraints

* **Stack:** Go 1.22, PostgreSQL 16, GitHub Actions CI/CD.
* **Core Requirements:** Declarative or versioned migrations, lock timeout safety, CI migration linting (detecting table rewrites or exclusive locks), active open-source maintenance.
* **Anti-Hallucination Guard:** Cite verified features from official docs and repo release notes. Disclose license models (e.g. Atlas community vs commercial limits).

---

## 4. Resulting Prompt / Generated Workflow

```markdown
**Purpose:** Select an enterprise-ready PostgreSQL migration framework in Go that prevents dangerous locking migrations during CD deploys.
**Audience:** Lead Backend Architect and DevOps Platform Lead.
**Research:**
- Audit `golang-migrate/migrate`, `pressly/goose`, and `ariga/atlas`.
- Verify current repository health: release cadence in last 12 months, open security advisories, license terms (MIT, Apache 2.0, or Business Source License).
- Inspect native capabilities for:
  * Transactional DDL execution.
  * Out-of-order migration handling.
  * Static linting of dangerous SQL (e.g., adding non-nullable column without default, index creation without `CONCURRENTLY`).
**Think:**
- Compare developer workflow: raw SQL files vs Go code migrations vs declarative HCL schema files.
- Evaluate CI/CD pipeline integration overhead.
**Narrow:**
- Eliminate contenders lacking static lock-risk analysis or requiring closed-source commercial cloud dependencies for basic CI checks.
- Present top 2 choices with explicit pros and trade-offs.
**Execute:**
- Provide a minimal working Go demonstration script for the top candidate running a migration with a 2-second statement lock timeout.
**Review:**
- Summary recommendation matrix with migration plan from existing raw `.sql` scripts.
```

---

## 5. Evaluation Criteria

* [x] **Evidence-Based:** Requires verified repository metrics and license audits.
* [x] **Down-Selection:** Filters candidates against CI linting and zero-downtime requirements.
* [x] **Concrete Proof-of-Concept:** Requires runnable migration script with timeout bounds.
* [x] **Readiness Status:** `READY`
