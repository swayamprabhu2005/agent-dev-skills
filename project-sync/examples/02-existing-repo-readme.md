# Example 02: Existing Repository with Established README

This example shows how Project Sync makes surgical, targeted insertions into an established, mature repository without disturbing surrounding human prose.

---

## 1. Implementation Change
Added an optional Prometheus metrics endpoint (`GET /metrics`) to an existing production service.
* Modified: `src/server.ts`, `src/metrics.ts`.
* Tests added: `tests/metrics.test.ts`.

## 2. Determination of Documentation Impact
* The existing `README.md` is a 250-line document with custom graphics, architecture diagrams, and an "Endpoints" table.
* The new `/metrics` endpoint is a public operational capability that developers and SREs need to know about.
* **Decision:** Perform a surgical insertion of one row into the existing "Endpoints" table. Do not alter any surrounding headings, badges, or paragraphs.

## 3. Determination of Ignore-Rule Impact
* No new build outputs, caches, or secrets were introduced.
* **Decision:** No changes required for `.gitignore`.

## 4. Resulting Modifications

### `README.md` (Diff):
```diff
 | Endpoint | Method | Description |
 | :--- | :--- | :--- |
 | `/health` | GET | Basic liveness probe |
 | `/ready` | GET | Readiness probe checking database connectivity |
+| `/metrics` | GET | Prometheus exposition format runtime metrics |
 | `/v1/orders`| POST| Submit new order |
```

## 5. Completion Summary
```text
Implementation complete.

Implemented:
- Added Prometheus runtime metrics collector
- Exposed GET /metrics endpoint

Project synchronization:
- README.md — Updated: Added /metrics to Endpoints reference table
- .gitignore — No changes required: No new untracked or generated files

Validation:
- Tests: 42 passed (npm test)

Iteration complete.
```
