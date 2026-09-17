# Example D: Contradictory Artifacts (Halting on Conflict Detection)

This example illustrates how Project Blueprint catches a cross-document contradiction during consistency auditing, stops immediately, and forces human clarification instead of silently guessing.

---

## 1. Context: The Contradiction
During the draft generation of a team collaboration platform, requirements and UI designs diverged:
* In `PRD.md`, requirement `REQ-004` specified:
  > *"Projects can only be archived or deleted by Organization Owners."*
* In `UI_UX.md`, the Project Card component was specified with:
  > *"Every card features a three-dot menu with 'Archive Project', accessible to all project contributors."*
* In `TRD.md`, the delete endpoint was specified as:
  > *`DELETE /api/v1/projects/:id` checks `membership.role != 'GUEST'` (permits regular members).*

---

## 2. Automated Consistency Audit
Before presenting the blueprint as `READY_FOR_REVIEW`, the agent runs the consistency audit:
```bash
python scripts/check-consistency.py
```
The audit compares permissions across `REQ-004` and identifies the collision between `PRD.md`, `UI_UX.md`, and `TRD.md`.

---

## 3. The Strict Halting Action

The agent does **NOT**:
* ❌ Silently delete the menu from the UI.
* ❌ Silently loosen the PRD requirement.
* ❌ Present the blueprint with the contradiction buried inside.

Instead, the agent halts and surfaces the conflict to the user:

```text
⚠️ CONFLICT DETECTED — REQ-004 (Project Deletion & Archival)

A specification contradiction was identified across your blueprint drafts:
- PRD.md: Only Organization Owners may delete/archive projects.
- UI_UX.md: All project contributors have an 'Archive Project' button on the project card.
- TRD.md: Endpoint allows any member with role != 'GUEST' to delete projects.

Implementation and review are BLOCKED until this business rule is clarified:
Question: Who should have permission to archive and delete projects?
  A. Strict Owner-Only: Restrict button in UI_UX and enforce role == 'OWNER' in TRD.
  B. Contributor-Allowed: Update PRD to allow any non-guest member to archive projects.
```

---

## 4. User Resolution & Synchronization
**User:**
> *"Option A. Keep it strict: only Owners can archive or delete projects."*

**Agent Action:**
1. Updates `UI_UX.md`: Restricts the three-dot Archive action to users with the `OWNER` badge.
2. Updates `TRD.md`: Enforces `membership.role == 'OWNER'` in `DELETE /api/v1/projects/:id`.
3. Re-runs `check-consistency.py` (passes with zero conflicts).
4. Transitions state to `READY_FOR_REVIEW`.
