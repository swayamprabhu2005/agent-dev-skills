# Example C: Requirement Change (Incremental Evolution from v1 to v2)

This example illustrates how Project Blueprint handles a mid-flight requirement change after Version 1 has already been approved, demonstrating version invalidation and incremental delta updates.

---

## 1. Initial State: Approved Blueprint v1
* `.blueprint/state.yaml` records:
  ```yaml
  version: 1
  status: APPROVED
  approved_version: 1
  ```
* The user previously approved the v1 blueprint for a single-role workspace application.

---

## 2. The Scope Change
**User:**
> *"Actually, we need custom granular permissions. Instead of just Owner and Member, we need to allow organization owners to define custom roles with granular toggles like 'can_view_billing' and 'can_delete_projects'."*

---

## 3. Impact Analysis & Targeted Clarification

### Step 1: Impact Sizing
The agent evaluates which documents are affected:
* `PRD.md`: **Affected** (Add `REQ-007: Custom Roles & Granular Permissions`).
* `TRD.md`: **Affected** (Add RBAC authorization middleware and bitmask/permission evaluation).
* `BACKEND_SCHEMA.md`: **Affected** (Add `roles` table, `role_permissions` join table; update ER diagram).
* `UI_UX.md`: **Affected** (Add Role Management matrix in Organization Settings).
* `APP_FLOW.md`: **Unaffected** (Core project creation and dashboard navigation remain unchanged).

### Step 2: Targeted Question
**Agent:**
> *"Adding custom roles affects the schema and TRD. Before updating:*
> *Should custom roles be organization-scoped (each org defines its own roles), or system-wide global templates?"*

**User:**
> *"Organization-scoped, with a default 'Member' and 'Admin' template created automatically on org signup."*

---

## 4. State Invalidation & Revision

1. The agent updates `.blueprint/state.yaml`:
   ```yaml
   version: 2
   status: READY_FOR_REVIEW
   approved_version: null  # Version 1 approval no longer valid for v2!
   ```
2. The agent updates only the 4 affected documents and updates the Mermaid ER diagram in `BACKEND_SCHEMA.md`.
3. **Approval Gate Re-locks:** Implementation is strictly blocked.

---

## 5. Review Presentation & Re-Approval

```text
Project Blueprint v2 Ready for Review

Modifications applied:
- PRD.md: Added REQ-007 (Organization-scoped custom roles)
- TRD.md: Added RBAC policy evaluation service
- BACKEND_SCHEMA.md: Added 'roles' & 'role_permissions' tables; updated ER diagram
- UI_UX.md: Added Role Permission Checklist table

Status: READY_FOR_REVIEW (v2)
⚠️ Implementation remains blocked until Version 2 is explicitly approved.
```

**User:**
> *"Approved for v2."*

**Agent Action:**
* Advances state to `status: APPROVED, approved_version: 2`.
* Re-generates the implementation plan to incorporate Phase 2B (Role Management).
* Unlocks coding.
