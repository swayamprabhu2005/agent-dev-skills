# Example 09: Combining Two Frameworks (SOCRATES + RIPPLE)

---

## 1. User Invocation

```text
/context-matrix combine socrates ripple We need to evaluate our legacy database connection pooling architecture in src/db/pool.py and audit it against a proposed high-concurrency redesign.
```

---

## 2. Frameworks Selected & Role Allocation

* **Primary Framework:** `SOCRATES` (System Architecture & Trade-Off Analysis)
* **Secondary Framework:** `RIPPLE` (Systematic Code Review & Invariant Audit)
* **Combination Rationale:** SOCRATES analyzes system scale, connection exhaustion risks, and architectural alternatives; RIPPLE conducts line-by-line inspection of mutex locking, timeouts, and leak vulnerabilities in the actual implementation.

---

## 3. Relevant Context & Constraints

* **Existing File:** `src/db/pool.py` (custom hand-rolled connection pool in Python).
* **Production Issue:** Connections hang during sudden traffic spikes of 5,000 req/sec; database reaches `max_connections` (500) within 3 minutes.
* **Constraints:** Maintain backward compatibility with existing repository repository methods (`acquire()`, `release()`); do not restart database instances during deploy.

---

## 4. Resulting Prompt / Generated Workflow

```markdown
### Phase 1: RIPPLE Forensic Audit of `src/db/pool.py`
**Role:** Database Internals and Concurrency Systems Auditor.
**Input:** Source code of `src/db/pool.py` and production PostgreSQL connection spike telemetry.
**Process:**
1. Trace connection lifecycle: creation, validation (`ping`), assignment, release, and reap.
2. Inspect lock contention on `acquire()` under 1,000 simultaneous threads.
3. Audit leak vectors: verify whether unhandled exceptions in caller code leave checked-out connections dangling.
**Points:**
- Mutex lock duration: Is I/O performed while holding the pool lock?
- Queue timeout behavior: Does a full pool block callers indefinitely or reject fast?
**Layout:** Detailed Findings Table with exact line references and severity flags.

---

### Phase 2: SOCRATES Architectural Redesign & Trade-Offs
**Situation:** 5,000 peak RPS microservice communicating with AWS RDS Aurora Postgres (max 500 connections).
**Objective:** Redesign connection pooling layer to survive 10x traffic spikes with bounded latency and zero connection starvation.
**Constraints:**
- Maximum database backend connections: 400 (leaving 100 for admin and worker scripts).
- Client timeout: Must fail fast with 503 if connection cannot be acquired within 200ms.
**Role:** Principal Infrastructure Architect.
**Action:** Compare two architectural options:
1. Application-level pool redesign using `asyncpg` connection pool with bounded checkout queue.
2. Deploying a centralized connection proxy layer (PgBouncer in transaction-pooling mode).
**Thinking:**
- Contrast memory overhead of maintaining 400 application-level TCP sockets vs PgBouncer proxy latency (+0.4ms).
- Evaluate support for prepared statements and session-level variables across both approaches.
**Evaluation:**
- Load test specification: Simulate 5,000 concurrent client requests over 60 seconds. Pool must not leak connections or exceed 400 backend connections.
**Summary:**
- Hybrid roadmap: Short-term code patch for `src/db/pool.py` + long-term PgBouncer deployment plan.
```

---

## 5. Evaluation Criteria

* [x] **Clear Division of Labor:** RIPPLE diagnoses the existing code defect; SOCRATES architects the system redesign.
* [x] **No Redundancy:** Each framework addresses distinct operational questions.
* [x] **Readiness Status:** `READY`
