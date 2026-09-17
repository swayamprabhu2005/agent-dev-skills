# Project Blueprint Worked Scenarios Index

This reference indexes the six representative case studies illustrating how Project Blueprint plans, clarifies, validates, and evolves specifications across diverse engineering situations.

For detailed walkthroughs and sample documents, consult the scenario folders in the [examples/](../../examples/) directory.

---

## Scenario Index

| Scenario | Directory | Context & Challenge | Core Blueprint Lesson |
| :--- | :--- | :--- | :--- |
| **A. New SaaS Application** | [`examples/a-new-saas-app/`](../../examples/a-new-saas-app/) | Building a multi-tenant project manager from a rough idea | Interactive clarification, 5 artifacts with Mermaid, explicit approval gate, and derived implementation plan. |
| **B. Existing Repository** | [`examples/b-existing-repository/`](../../examples/b-existing-repository/) | Adding payments to a mature FastAPI codebase | Inspecting existing conventions, adapting without overwriting existing documentation, and importing architecture. |
| **C. Requirement Change** | [`examples/c-requirement-change/`](../../examples/c-requirement-change/) | User adds team roles to an approved v1 blueprint | Incremental delta updates, version bump to v2, and re-locking the approval gate. |
| **D. Contradictory Artifacts** | [`examples/d-contradictory-artifacts/`](../../examples/d-contradictory-artifacts/) | PRD and UI/UX disagree on permission rules | Halting immediately as `CONFLICT DETECTED` rather than silently picking one interpretation. |
| **E. Implementation Drift** | [`examples/e-implementation-drift/`](../../examples/e-implementation-drift/) | Coding reveals unexpected OAuth limitation | Pausing code generation, explaining discrepancy, updating TRD, and securing v2 re-approval. |
| **F. Small Task** | [`examples/f-small-task/`](../../examples/f-small-task/) | User requests a single CSS button color fix | Recognizing minor maintenance and avoiding unnecessary blueprint overhead. |
