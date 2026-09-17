# Document Quality & Traceability Guidelines

This guide establishes the quality standards, naming conventions, and requirement traceability practices for Project Blueprint documents.

---

## 1. Requirement Traceability (`REQ-xxx`)

To ensure that every visual component and database table serves a legitimate business purpose, core requirements in `PRD.md` receive stable, unique identifiers:

```markdown
### Core Functional Requirements
* **REQ-001:** Users must be able to sign in using Google OAuth2.
* **REQ-002:** Organization owners can invite new members via email link.
* **REQ-003:** Invoices can be exported to downloadable PDF files.
```

### Cross-Document Referencing:
Downstream documents must reference these identifiers:
* **`TRD.md`:** *"The `InvitationService` implements **REQ-002** using signed HMAC tokens with a 7-day expiration."*
* **`UI_UX.md`:** *"The Organization Settings modal implements **REQ-002** with an email input field and Role selector dropdown."*
* **`BACKEND_SCHEMA.md`:** *"The `invitations` table supports **REQ-002** with `token_hash`, `email`, `role`, and `expires_at`."*
* **`APP_FLOW.md`:** *"Step 4 of the Member Onboarding flow executes **REQ-002** acceptance."*

---

## 2. Assumptions & Open Questions

### Assumptions (`ASSUM-xxx`)
Assumptions capture decisions made to prevent blocking progress on non-critical details:
* **Format:** `ASSUM-001: Description of reasonable assumption.`
* Must be explicitly listed in `PRD.md` and highlighted during review.

### Open Questions (`OPEN-xxx`)
Open questions identify material uncertainties that require user resolution:
* **Format:** `OPEN-001: Question text? [Impact: Blocks Schema/TRD].`
* **Rule:** A blueprint cannot enter `APPROVED` status if unresolved material open questions remain.

---

## 3. Writing Style & Anti-Fluff Standards

### Rejecting Generic AI Fluff
* ❌ *"The system features a robust, cutting-edge, comprehensive state-of-the-art architecture designed to synergistically empower users."*
* ✅ *"The system uses a modular Node.js monolith with PostgreSQL read-replicas, achieving p95 response times under 150ms for invoice queries."*

### Concrete Technical Specifications Over Vague Advice
* ❌ *"Ensure the UI looks good on mobile."*
* ✅ *"The layout collapses into a single-column stacked view below 768px (`md` breakpoint). The primary navigation transitions from a fixed sidebar into an off-canvas drawer."*
* ❌ *"Handle database errors gracefully."*
* ✅ *"Database connection timeouts return HTTP 503 with `{ error: 'SERVICE_UNAVAILABLE', retry_after: 5 }`. Connection retries use exponential backoff up to 3 attempts."*

---

## 4. Adapting Depth to Project Complexity

| Scale | Description | Artifact Depth |
| :--- | :--- | :--- |
| **Small Project / Utility** | Single CLI or microservice | Concise documents (1-2 pages each); 1 core flow diagram; 1 schema diagram. |
| **Medium Project** | Full-stack web app with auth & DB | Full sections; requirement IDs; architecture, ER, and auth flow diagrams. |
| **Large / Multi-Tenant** | Enterprise SaaS, billing, RBAC | Complete traceability matrix; detailed state matrices; multiple sequence diagrams. |
