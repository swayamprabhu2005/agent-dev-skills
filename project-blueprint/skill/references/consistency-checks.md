# Cross-Document Consistency & Conflict Resolution

This guide establishes the rules and audit procedures used by Project Blueprint to guarantee that all five specification documents remain in complete mutual agreement.

---

## 1. The Multi-Document Consistency Problem

In complex software planning, specifications frequently fall out of sync:
* The **PRD** promises that *"Members can invite other members"*.
* The **UI/UX** specification only includes an *"Invite"* button inside the Organization Owner's settings panel.
* The **TRD** has no role checks on the `/invitations` endpoint.
* The **Backend Schema** omits the `invitations` table entirely.

When an AI agent begins coding against such a disjointed plan, it generates broken, inconsistent code.

---

## 2. The 5-Point Cross-Document Audit

Before setting `status: READY_FOR_REVIEW`, the agent must verify:

| Source Document | Target Document | Verification Query |
| :--- | :--- | :--- |
| **`PRD.md`** | **`TRD.md`** | Does every `REQ-xxx` have an identified technical service, API route, or architectural component to satisfy it? |
| **`PRD.md`** | **`UI_UX.md`** | Does every user-facing requirement have an explicit screen, modal, or component state defined? |
| **`PRD.md`** | **`BACKEND_SCHEMA.md`** | Does the database schema store all entities, relationships, and status fields implied by the product rules? |
| **`TRD.md`** | **`BACKEND_SCHEMA.md`** | Do foreign keys, indexes, and field types match the API serialization models described in the TRD? |
| **`APP_FLOW.md`** | **`UI_UX.md`** | Does every step and decision branch in the user flow have a matching component state in the UI/UX spec? |

---

## 3. Conflict Detection Protocol

If a contradiction is detected between any two documents:

> **STRICT PROTOCOL: HALT. Do NOT silently choose one document over another.**

### Conflict Report Format:
```text
⚠️ CONFLICT DETECTED

Contradiction identified between blueprint documents for REQ-002:
- PRD.md states: "Organization owners and admins can invite new members."
- UI_UX.md states: "The Invite Member modal is accessible to all logged-in members."
- TRD.md states: "POST /api/v1/invitations requires 'owner' role."
- BACKEND_SCHEMA.md: 'invitations' table lacks 'invited_by_role' field.

Implementation is BLOCKED until this decision is reconciled:
Question: Should non-admin members be permitted to send invitations?
Options:
  A. Restrict to Owners and Admins only (align UI with PRD/TRD).
  B. Allow all Members to invite (align PRD/TRD/Schema with UI).
```

Only after the human user clarifies the intent should the affected documents be synchronized.
