# Example 05: Refactoring (Preparatory Refactoring vs. Feature Addition)

This example demonstrates how to separate necessary refactoring from feature work, adhering to Kent Beck's maxim: *"Make the change easy, then make the easy change."*

---

## 1. The Task
"Add webhook notification support when an invoice payment succeeds."

## 2. Repository State
* Project: Python / Django.
* Current state: `InvoiceService.mark_paid()` is a 180-line monolithic method handling credit card charging, ledger entries, PDF generation, email sending, and database updates all inline.

## 3. Discovered Work
1. Attempting to add webhook dispatching directly into `mark_paid()` would make the method even longer, harder to test, and tightly coupled.
2. Refactor step: Extract domain events (`InvoicePaidEvent`) and an event dispatcher pattern from `mark_paid()`, moving email and PDF actions into separate listeners without changing any existing functionality.
3. Feature step: Add a new webhook listener that responds to `InvoicePaidEvent` by enqueuing a webhook task to Celery.

## 4. Dependencies Between Work Units
* The refactoring must preserve 100% existing behavior and pass all existing regression tests.
* The new webhook feature builds upon the newly extracted event dispatching structure.
* Mixing structural refactoring with new business features in a single commit makes review impossible: reviewers cannot tell whether a changed line is a refactor or a behavior change.

## 5. Proposed Commit Plan
* **Commit 1:** Extract domain event dispatching from InvoiceService.mark_paid
* **Commit 2:** Dispatch webhook notifications on invoice payment

## 6. Implementation Sequence
1. Refactor `InvoiceService.mark_paid()` to publish `InvoicePaidEvent`. Move email and PDF generation into event listeners.
2. Run existing test suite (`pytest tests/test_invoices.py`). Confirm zero test failures.
3. Stage refactored files and commit Commit 1.
4. Implement `WebhookDispatcher` listener, webhook payload serialization, and integration tests.
5. Run tests. Stage and commit Commit 2.

## 7. Final Commit Messages
```text
Extract domain event dispatching from InvoiceService.mark_paid

Decompose the monolithic payment completion method into an InvoicePaidEvent
with dedicated listeners for email delivery and PDF generation.
No change in existing runtime behavior.
```

```text
Dispatch webhook notifications on invoice payment

Listen for InvoicePaidEvent and enqueue asynchronous Celery tasks to deliver
HMAC-signed webhook payloads to configured tenant webhook endpoints.
```

## 8. Why These Boundaries Make Sense
* **Diff Clarity:** Commit 1 is pure refactoring: a reviewer can verify that no logic changed. Commit 2 is pure feature addition: a reviewer can focus solely on webhook security and payload design.
* **Risk Mitigation:** If the webhook feature in Commit 2 encounters bugs in staging, it can be reverted cleanly without reverting the architectural improvements made in Commit 1.

## 9. What the Agent Should Avoid
* ❌ Blending the refactor and the webhook implementation into one 350-line diff.
* ❌ Performing opportunistic cosmetic refactoring in unrelated modules (`models/user.py`, `views/auth.py`) just because the agent saw them.
