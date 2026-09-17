# Technical Requirements Document (TRD): Freelance Invoice Manager

## 1. System Architecture Overview
The application follows a clean modular service architecture:
* **Frontend:** React 18 SPA (TypeScript, Tailwind CSS, TanStack Query).
* **Backend:** Node.js / Express REST API (TypeScript).
* **Database:** PostgreSQL 16 managed via Prisma ORM.
* **Payments:** Stripe API (Checkout Sessions & Webhook Events).

## 2. System Architecture Diagram

```mermaid
flowchart TD
    Client["Browser (React SPA)"] -->|HTTPS / JWT| API["Express API Gateway"]
    API --> Auth["Auth & RBAC Middleware"]
    Auth --> InvService["Invoice Service (REQ-004)"]
    Auth --> PayService["Payment Service (REQ-006)"]
    InvService --> DB[("PostgreSQL 16")]
    PayService --> DB
    PayService -->|Create Checkout Session| Stripe["Stripe Hosted Checkout"]
    Stripe -->|Async Webhook (invoice.paid)| Webhook["Webhook Controller"]
    Webhook -->|Verify Signature & Mark Paid| PayService
```

## 3. API Contracts (Excerpts)
* `POST /api/v1/auth/login`: Authenticate and return HTTP-only JWT cookie (**REQ-001**).
* `POST /api/v1/organizations`: Create new workspace (**REQ-002**).
* `POST /api/v1/invoices`: Create invoice draft with line items (**REQ-004**).
* `POST /api/v1/invoices/:id/publish`: Transition to `UNPAID` and create Stripe Checkout Session (**REQ-005**, **REQ-006**).
* `POST /api/v1/webhooks/stripe`: Receive `checkout.session.completed` event with HMAC signature verification.

## 4. Security & Idempotency
* Stripe webhooks verify signatures against `STRIPE_WEBHOOK_SECRET`.
* Database transaction uses idempotency keys on `stripe_event_id` to prevent double-crediting.
