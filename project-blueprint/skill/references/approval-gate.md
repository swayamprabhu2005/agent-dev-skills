# Human Approval Gate & Workflow State Machine

This guide specifies the formal state transitions, approval criteria, and version locking protocols enforced by Project Blueprint.

---

## 1. The Defining Principle

> **Implementation remains strictly locked until the blueprint reaches the `APPROVED` state.**

The agent must never write production application code, run database migrations, or scaffold UI components until the user has explicitly reviewed and approved the blueprint artifacts.

---

## 2. State Model

Project Blueprint tracks progress through seven explicit lifecycle states:

```text
    [ DRAFT ] ──────────► [ READY_FOR_REVIEW ]
                                 │
           ┌─────────────────────┴─────────────────────┐
           ▼                                           ▼
  [ CHANGES_REQUESTED ]                           [ APPROVED ]
           │                                           │
           ▼                                           ▼
  (Revise artifacts)                        [ IMPLEMENTATION_READY ]
           │                                (Implementation Plan Generated)
           ▼                                           │
  [ READY_FOR_REVIEW ]                                 ▼
                                                [ IMPLEMENTING ]
                                                       │
                                                       ▼
                                                [ IMPLEMENTED ]
```

### State Descriptions:
1. **`DRAFT`:** Artifacts are being initially scaffolded or questions are being answered.
2. **`READY_FOR_REVIEW`:** All 5 artifacts and Mermaid diagrams are complete, cross-document consistency checks have passed, and the blueprint is presented to the user.
3. **`CHANGES_REQUESTED`:** User provided feedback or requested revisions.
4. **`APPROVED`:** User provided unambiguous, explicit approval for the current version.
5. **`IMPLEMENTATION_READY`:** Derived implementation plan has been generated based on the approved blueprint.
6. **`IMPLEMENTING`:** Active coding/implementation is underway.
7. **`IMPLEMENTED`:** Implementation tasks are complete and ready for Project Sync.

---

## 3. Ambiguity Resolution: What Counts as Approval?

AI agents frequently misinterpret polite comments as authorization to write code. Project Blueprint strictly forbids this.

### Permitted Approval Phrases:
* `"Approved."`
* `"I approve this blueprint."`
* `"Blueprint looks good, please proceed with implementation."`
* `"Approved to build."`

### Non-Approval Phrases (Must NOT Unlock Implementation):
* `"looks good"` (Could mean "good start, let me read it closer").
* `"nice"` / `"great job"` (Compliment, not an authorization).
* `"continue"` / `"next"` (Ambiguous command).
* The user asking a clarifying question about an endpoint.
* The user opening or editing a file.

**Protocol for Ambiguity:** If the user says *"Looks great"*, the agent must respond:
> *"Thank you! Should I consider the blueprint officially approved so I can generate the implementation plan and begin coding?"*

---

## 4. Version-Specific Approval & Invalidation

Approval is locked to a specific integer version (e.g. `version: 1`).

If a user approves Version 1, and later says:
> *"Actually, we also need to allow users to export PDF invoices."*

**The state transition is:**
1. State changes from `APPROVED` to `CHANGES_REQUESTED`.
2. `version` increments from `1` to `2`.
3. Affected documents (`PRD.md`, `TRD.md`, `UI_UX.md`) are updated.
4. State transitions to `READY_FOR_REVIEW`.
5. **Implementation is re-blocked until Version 2 is explicitly approved.**

An approval of Version 1 does NOT grant permission to implement Version 2.

---

## 5. State File Specification (`.blueprint/state.yaml`)

Workflow state is persisted in a lightweight YAML file at `docs/project-blueprint/.blueprint/state.yaml`:

```yaml
version: 1
status: READY_FOR_REVIEW
approved_version: null
updated_at: "2026-09-17T23:30:00Z"
documents:
  prd: READY
  trd: READY
  ui_ux: READY
  backend_schema: READY
  app_flow: READY
open_questions_count: 0
unresolved_conflicts: 0
```
This guarantees that approval status is transparent and verifiable in version control, never lost across chat sessions.
