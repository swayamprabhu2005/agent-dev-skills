# Example E: Implementation Drift (Handling Unexpected Technical Roadblocks)

This example demonstrates how Project Blueprint handles real-world technical discoveries during implementation that invalidate an approved architecture decision.

---

## 1. Initial Approved State
* Blueprint v1 was explicitly approved by the user.
* `TRD.md` approved an embedded SQLite full-text search architecture using `FTS5` for a document indexing feature.
* Coding began on Phase 2.

---

## 2. The Real-World Roadblock Discovery
While implementing the migration script in Python on the user's specific target server environment, the agent executes `import sqlite3; sqlite3.connect(':memory:').execute('CREATE VIRTUAL TABLE t USING fts5(x)')` and receives:
```text
sqlite3.OperationalError: no such module: fts5
```
* **Discovery:** The user's Python runtime is linked against a system SQLite build that was compiled without the `ENABLE_FTS5` C-compiler flag. SQLite `FTS5` cannot be enabled without recompiling Python or installing custom shared C-libraries, which violates deployment constraints.

---

## 3. The Strict Non-Negotiable Drift Rule

The agent does **NOT**:
* ❌ Quietly hack together a crude `LIKE %query%` search that performs poorly and violates PRD search ranking requirements.
* ❌ Spend 4 hours attempting to recompile the user's operating system Python binary.
* ❌ Proceed without telling the user.

**The Agent Halts Immediately:**

```text
⚠️ IMPLEMENTATION DRIFT DETECTED

While implementing full-text search as approved in TRD v1, we encountered
an insurmountable environment limitation:
- Approved Architecture: SQLite FTS5 extension.
- Environment Reality: System SQLite library was compiled without FTS5 support.

Proposed Revision:
Switch full-text indexing to Whoosh (pure Python search library) or use PostgreSQL pg_trgm if PostgreSQL is acceptable.

Recommendation:
Update TRD and Backend Schema to use pure-Python Whoosh indexing, which avoids any C-extension or SQLite compilation dependency.

May I update the blueprint to v2 with this change for your review?
```

---

## 4. Resolution & Controlled Resumption
**User:**
> *"Yes, switch to Whoosh. I approve."*

**Agent Action:**
1. Updates `TRD.md` to specify Whoosh indexing service.
2. Updates `BACKEND_SCHEMA.md` to remove virtual table definitions.
3. Bumps version to `version: 2, status: APPROVED, approved_version: 2`.
4. Resumes coding under the updated contract.
