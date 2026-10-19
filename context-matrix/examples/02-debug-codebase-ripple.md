# Example 02: Debugging an Existing Codebase (RIPPLE)

---

## 1. User Invocation

```text
/context-matrix ripple Our Node.js API worker crashes with "FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory" during daily CSV sync. Inspect src/workers/csv-sync.ts and fix it.
```

---

## 2. Framework Selected

* **Primary Framework:** `RIPPLE`
* **Selection Rationale:** Systematic forensic debugging and memory leak isolation in an existing codebase.

---

## 3. Relevant Context & Constraints

* **Runtime:** Node.js 20, TypeScript.
* **Input File:** `src/workers/csv-sync.ts` parsing 500MB customer CSV files.
* **Failure Mode:** Process OOM crash under V8 heap limit (~1.4GB).
* **Constraints:** Must stream data without buffering full file into memory; do not introduce heavy external queue services.

---

## 4. Resulting Prompt / Generated Workflow

```markdown
**Role:** Senior Node.js Performance and Systems Engineer.
**Input:** `src/workers/csv-sync.ts` and the V8 heap exhaustion crash log.
**Process:**
1. Trace file reading mechanism in `csv-sync.ts` (identify synchronous `fs.readFileSync` or array accumulation).
2. Inspect database insertion batching loop for unreleased object references.
3. Replace unbounded memory buffering with a Node.js `stream.Transform` pipeline.
4. Add backpressure handling between CSV parser and Postgres write stream.
**Points:**
- Peak V8 RSS memory during 500MB stream processing (must remain < 200MB).
- Event loop blockage (ensure hot loop does not starve health check endpoints).
- Transaction rollback safety on malformed CSV rows.
**Layout:**
1. Root Cause Breakdown (exact lines where memory accumulates).
2. Architecture of the streaming solution.
3. Unified diff patch for `src/workers/csv-sync.ts`.
4. Reproduction & verification test script.
**Evaluate:**
- Write an executable Node.js benchmark test feeding a 200MB mock CSV stream while asserting `process.memoryUsage().heapUsed < 150 * 1024 * 1024`.
```

---

## 5. Evaluation Criteria

* [x] **Process Rigor:** Defines explicit 4-step diagnostic sequence.
* [x] **Inspection Points:** Focuses on heap RSS, backpressure, and event loop latency.
* [x] **Empirical Verification:** Demands an executable memory assertion test.
* [x] **Readiness Status:** `READY`
