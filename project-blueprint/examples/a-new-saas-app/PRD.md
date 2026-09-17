# Product Requirements Document (PRD): Freelance Invoice Manager

## 1. Overview & Problem Statement
Freelancers lose billable hours using clunky, expensive enterprise accounting software to generate simple invoices. This product provides a lightweight, focused invoicing platform where solo operators and small agencies can draft professional invoices, send them to clients, and collect payments via Stripe.

## 2. Goals & Non-Goals
* **Goals:**
  * Fast invoice drafting in under 60 seconds.
  * Frictionless client payment via hosted Stripe Checkout.
  * Multi-tenant workspaces supporting Owner and Member roles.
* **Non-Goals (v1):**
  * Double-entry bookkeeping or general ledger accounting.
  * Multi-currency support (deferred to v2).
  * Automated recurring subscriptions (deferred to v2).

## 3. Target Personas
* **Alex (Solo Freelancer):** Web developer billing 3 to 5 clients monthly. Wants clean PDF and instant card payment.
* **Sarah (Agency Owner):** Runs a design studio with 2 contractors. Needs team members to draft invoices while retaining owner-only payment settings.

## 4. Functional Requirements
* **REQ-001:** Users authenticate via email/password or Google OAuth2.
* **REQ-002:** Users can create and manage multiple Organizations with `OWNER` and `MEMBER` roles.
* **REQ-003:** Users can create, update, and archive Client contacts (name, email, billing address).
* **REQ-004:** Users can draft Invoices with dynamic Line Items (description, quantity, unit price) and flat sales tax.
* **REQ-005:** Invoices can be published, generating a unique public payment link.
* **REQ-006:** Clients can settle published invoices via Stripe Checkout; webhook marks invoice as `PAID`.

## 5. Assumptions
* **ASSUM-001:** All amounts are denominated in USD for v1.
* **ASSUM-002:** Invoices become immutable once transitioned to `PAID` status.

## 6. Success Metrics
* Average time to create and send first invoice under 2 minutes.
* Zero billing calculation discrepancies across line-item rounding.
