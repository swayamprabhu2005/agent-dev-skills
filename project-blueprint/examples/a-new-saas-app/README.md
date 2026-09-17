# Example A: New SaaS Application (Freelance Invoice Manager)

This example illustrates the complete end-to-end lifecycle of Project Blueprint for a brand-new SaaS application, from initial vague prompt through clarification, document generation with Mermaid diagrams, human review, explicit approval, and implementation plan derivation.

---

## 1. Initial User Request
> *"I want to build a clean web app where freelancers can create invoices, send them to clients, and get paid with Stripe."*

## 2. Interactive Clarification Exchange

### Turn 1:
**Agent:**
> *"I'd love to help plan this freelance invoicing app before we start coding. To ensure the architecture is sound, I have two quick questions:*
> *1. Should freelancers be able to invite team members or accountants to their workspace, or is this strictly single-user per account?*
> *2. For payments, should clients pay via a hosted Stripe Checkout page, or an embedded card form directly on the invoice view?"*

**User:**
> *"1. Let's make it multi-tenant so freelancers can invite a bookkeeper or assistant later, but MVP can just have Owner and Member roles.*
> *2. Hosted Stripe Checkout is fine and simpler."*

### Turn 2:
**Agent:**
> *"Got it. One follow-up:*
> *What currency and tax handling is required for v1? Should we support multi-currency or start with USD and flat percentage tax?"*

**User:**
> *"USD only with flat percentage tax for MVP."*

### Turn 3: Understanding Synthesis
**Agent:**
> *"Here is my synthesized understanding before I generate the Project Blueprint:*
> *- Product: Multi-tenant freelance invoice management web application.*
> *- Organization Model: Organizations contain Users (roles: `OWNER`, `MEMBER`).*
> *- Core Entities: Clients, Invoices, Line Items, Payments.*
> *- Payments: Hosted Stripe Checkout with webhook fulfillment.*
> *- Stack: React (TypeScript/Tailwind), Node.js (FastAPI/Express), PostgreSQL.*
> *- Assumptions: ASSUM-001 (USD only), ASSUM-002 (Flat percentage sales tax).*
>
> *I will now generate the 5 blueprint documents and diagrams for your review."*

---

## 3. Generated Artifacts

The agent generated the following five specification documents in `docs/project-blueprint/`:
* [`PRD.md`](PRD.md): Product requirements with traceable IDs (`REQ-001` through `REQ-006`).
* [`TRD.md`](TRD.md): System architecture, Stripe webhook security, and architecture flowchart.
* [`UI_UX.md`](UI_UX.md): Visual tokens, invoice builder layout, and state matrices.
* [`BACKEND_SCHEMA.md`](BACKEND_SCHEMA.md): Complete PostgreSQL schema and Mermaid ER diagram.
* [`APP_FLOW.md`](APP_FLOW.md): Mermaid flowchart tracing invoice creation to payment receipt.

---

## 4. Review Presentation

```text
┌────────────────────────────────────────────────────────┐
│ Project Blueprint Ready for Review (v1)                │
│                                                        │
│ • PRD               [docs/project-blueprint/PRD.md]    │
│ • TRD               [docs/project-blueprint/TRD.md]    │
│ • UI/UX             [docs/project-blueprint/UI_UX.md]  │
│ • Backend Schema    [docs/project-blueprint/BACKEND...]│
│ • App Flow          [docs/project-blueprint/APP_FLOW] │
│                                                        │
│ Generated Diagrams:                                    │
│ - System Architecture Block Flowchart                  │
│ - Database Entity-Relationship Diagram                 │
│ - Invoice Payment User Journey Flowchart               │
│                                                        │
│ Status: READY FOR REVIEW                               │
│                                                        │
│ ⚠️ Implementation is strictly BLOCKED until explicit   │
│ approval is granted.                                   │
└────────────────────────────────────────────────────────┘
```

---

## 5. Human Approval & Implementation Plan

**User:**
> *"I have reviewed the 5 documents and diagrams. Approved."*

**Agent Action:**
1. Executes `python scripts/blueprint-state.py approve`.
2. Updates `.blueprint/state.yaml` to `status: APPROVED, approved_version: 1`.
3. Generates [`IMPLEMENTATION_PLAN.md`](IMPLEMENTATION_PLAN.md) mapping out implementation phases.
4. Unlocks coding mode (ready for Project Sync & Commit Architect).
