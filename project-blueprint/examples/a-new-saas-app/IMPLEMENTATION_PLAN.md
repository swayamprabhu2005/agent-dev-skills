# Derived Implementation Plan: Freelance Invoice Manager

> **Prerequisite:** Generated based on approved Project Blueprint v1 (`.blueprint/state.yaml`: `APPROVED`).

---

## Implementation Phases

### Phase 1: Database & Foundation
* **Goal:** Scaffolding, PostgreSQL schema, Prisma migrations, and baseline auth.
* **Tasks:**
  * Initialize Node.js TypeScript project and Prisma client.
  * Run migration creating `organizations`, `users`, `clients`, `invoices`, `line_items`, and `payments` tables (**BACKEND_SCHEMA.md**).
  * Implement JWT authentication middleware and password hashing (**REQ-001**).
* **Test Gate:** Database seed and auth integration tests pass.

### Phase 2: Client & Invoice Management API
* **Goal:** Core CRUD endpoints for managing clients, line items, and invoice drafts.
* **Tasks:**
  * Implement `ClientService` and routes `GET/POST /api/v1/clients` (**REQ-003**).
  * Implement `InvoiceService` with line-item calculation, validation, and flat tax math (**REQ-004**).
* **Test Gate:** Unit tests asserting 100% rounding accuracy on line-item tax calculations.

### Phase 3: Stripe Integration & Webhooks
* **Goal:** Hosted Checkout Session generation and idempotent webhook fulfillment.
* **Tasks:**
  * Implement Stripe client service generating checkout sessions (**REQ-005**).
  * Implement webhook listener `POST /api/v1/webhooks/stripe` with HMAC signature verification (**REQ-006**).
  * Handle `checkout.session.completed` event within a database transaction.
* **Test Gate:** Mocked Stripe CLI webhook integration tests passing.

### Phase 4: React UI & Workflow
* **Goal:** Complete frontend dashboard, invoice editor, and client selection.
* **Tasks:**
  * Implement design tokens and layout shell (**UI_UX.md**).
  * Build interactive Invoice Builder with dynamic line-item stepper.
  * Build Invoice Preview and Payment Link share modal.
* **Test Gate:** Cypress/Playwright end-to-end user journey test (**APP_FLOW.md**).
