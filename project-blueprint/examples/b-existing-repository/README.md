# Example B: Existing Repository (Adding Billing to Mature Codebase)

This example illustrates how Project Blueprint operates when introduced into an existing, mature repository with established conventions, documentation, and database schemas.

---

## 1. Context & User Prompt
* **Project:** An existing FastAPI / SQLAlchemy SaaS application with 40,000 active users.
* **Current Docs:** Repository already has `docs/architecture/adr-001-fastapi.md` and `docs/api-guide.md`.
* **User Prompt:**
  > *"We need to add team seat billing to our existing organization workspace. Plan this feature before making any changes."*

## 2. Pre-Planning Inspection Protocol
Before generating documents or asking questions, the agent inspects the existing repository:
1. **Existing Tech Stack:** FastAPI, SQLAlchemy 2.0, PostgreSQL, Alembic.
2. **Existing Models:** `users`, `organizations`, `memberships`.
3. **Existing Docs:** Found `docs/architecture/` structure.
4. **Convention Rule:** The agent does **not** create a conflicting top-level `PRD.md` that overrides project docs. It respects the existing `docs/` hierarchy and derives the blueprint for the *delta* capability.

## 3. Targeted Clarification
The agent asks questions specifically grounded in the existing code:
> *"I noticed your existing `organizations` table has a `tier` column (`FREE`, `PRO`). For team seat billing:*
> *1. Should each additional member beyond 5 automatically trigger a per-seat charge, or should owners purchase prepaid seat blocks?*
> *2. Should we extend your existing Stripe customer ID on `organizations` or create a new `subscriptions` table?"*

## 4. Derived Blueprint Integration
* **`PRD.md`:** Focuses on `REQ-SEAT-001` (metered seat calculation) and `REQ-SEAT-002` (owner seat management UI).
* **`TRD.md`:** References existing `src/db/session.py` and `src/models/org.py`. Recommends adding a Celery beat task to report seat counts to Stripe Metered Billing.
* **`BACKEND_SCHEMA.md`:** Integrates with the existing schema, proposing an Alembic migration (`alembic/versions/0042_add_seat_quota.py`) rather than inventing a completely separate database.

## 5. Non-Destructive Storage
The blueprint is cleanly scoped to `docs/project-blueprint/seat-billing/`, ensuring that none of the repository's existing ADRs or API documentation files are overwritten or deleted.
