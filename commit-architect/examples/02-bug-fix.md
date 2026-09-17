# Example 02: Bug Fix (Race Condition in Checkout Inventory)

This example demonstrates how an investigation and targeted bug fix affect commit boundaries, emphasizing the tight coupling between a regression test and its fix.

---

## 1. The Task
"Investigate and fix intermittent stock underflow during simultaneous checkouts for the last item in stock."

## 2. Repository State
* Project: Node.js / TypeScript with Prisma ORM and PostgreSQL.
* Current branch: `fix/checkout-race-condition`.
* Existing commit style: Natural developer prose.
* Problem: When two checkout requests arrive simultaneously for an item with quantity 1, both requests pass the inventory check and decrement, resulting in negative stock (-1).

## 3. Discovered Work
1. Write an automated reproduction test demonstrating that concurrent checkout operations over-decrement stock.
2. Update the checkout transaction in `inventoryService.ts` to use row-level locking (`SELECT ... FOR UPDATE` via Prisma `$queryRaw` or atomic conditional decrement: `UPDATE inventory SET quantity = quantity - 1 WHERE id = $1 AND quantity >= 1`).
3. Handle the lock contention or zero-affected-rows error by returning an `OutOfStockError` HTTP 409 status.

## 4. Dependencies Between Work Units
* The regression test reproduces the bug against the existing code.
* The atomic decrement fix must resolve the test directly.
* Separating the test from the fix would leave a failing test in the commit history if committed first, or an unvalidated fix if committed without the test.

## 5. Proposed Commit Plan
* **Single Cohesive Commit:** `Prevent inventory underflow during concurrent checkouts`
  * Includes the atomic decrement transaction fix in `src/services/inventory.ts`.
  * Includes the concurrent concurrency regression test in `test/integration/checkout.test.ts`.
  * Includes the custom `OutOfStockError` status mapping in `src/errors.ts`.

## 6. Implementation Sequence
1. Write the concurrent stress test in `test/integration/checkout.test.ts` (verify it fails on current branch).
2. Implement the conditional SQL update in `src/services/inventory.ts`.
3. Run the test suite (verify all tests pass).
4. Run `git diff --cached` to verify only the relevant 3 files are staged.
5. Commit with an explanatory body.

## 7. Final Commit Message
```text
Prevent inventory underflow during concurrent checkouts

Use an atomic conditional decrement query with row-level locking
during order reservation. If stock is insufficient when the lock is
acquired, raise an OutOfStockError (HTTP 409) rather than decrementing
past zero.

Includes an integration test verifying that concurrent checkout attempts
against single-unit inventory reject subsequent buyers cleanly.
```

## 8. Why These Boundaries Make Sense
* **Atomic Unit:** A bug fix and its regression test belong together. Storing them in a single commit guarantees that anyone running `git bisect` finds a green build where the bug is both prevented and regression-tested.
* **No Artificial Separation:** Splitting `Add test for race condition` (failing commit) and `Fix race condition` (passing commit) breaks the bisectability guarantee unless explicitly desired by a TDD workflow convention.

## 9. What the Agent Should Avoid
* ❌ Smuggling a general TypeScript refactoring of the checkout controller into the bug fix.
* ❌ Writing a vague message like `Fix checkout bug`.
* ❌ Appending `fix(inventory): resolve concurrency issue #AI-generated`.
