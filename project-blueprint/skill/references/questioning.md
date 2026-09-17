# Interactive Clarification and Questioning Protocol

This guide establishes the conversational protocols used by Project Blueprint to resolve requirement ambiguity without overwhelming the user.

---

## 1. The Core Clarification Philosophy

AI planning tools often make one of two catastrophic mistakes:
1. **The Hallucination Trap:** The agent receives a one-sentence prompt (*"Build an invoicing app"*), asks zero questions, invents a hundred arbitrary architecture decisions, and writes code that the user never wanted.
2. **The Interrogation Trap:** The agent dumps a massive 25-question survey all at once, creating cognitive exhaustion for the user.

Project Blueprint employs a **conversational clarification loop**:
* Ask 1 or 2 high-impact questions at a time.
* Prioritize questions that materially change data architecture or user scope.
* Stop questioning when remaining uncertainties can be safely handled as documented assumptions.

---

## 2. Question Prioritization Hierarchy

When analyzing an ambiguous user request, sequence your questions by potential impact:

```text
Tier 1: Core Problem & Target Users (Highest Impact)
        "Who is this for, and what core problem does it solve?"
        ↓
Tier 2: Tenancy & Security Boundaries
        "Are accounts single-user or multi-tenant organizations?"
        ↓
Tier 3: Core Business Entities & Persistence
        "What are the 2 or 3 central entities (e.g. Invoices, Line Items, Clients)?"
        ↓
Tier 4: Critical Integrations & External Dependencies
        "Does this integrate with Stripe, GitHub, or custom APIs?"
        ↓
Tier 5: Platform & UI Paradigms
        "Is this web-first, mobile, or CLI? Any specific design constraints?"
        ↓
Tier 6: Low-Impact Details (Convert to Assumptions!)
        "Default currency format? Date localization? Pagination limit?"
```

*Never ask Tier 5 or 6 questions while Tier 1 or 2 ambiguity remains.*

---

## 3. Internal Question Categorization

Organize clarification internally using these functional categories:

| Category | High-Impact Question Example |
| :--- | :--- |
| **Product Scope** | What are the strict boundaries of MVP vs. future phases? |
| **Users & Permissions** | Are there distinct user roles (e.g. Admin, Editor, Viewer)? |
| **Data Relationships** | Can a Project belong to multiple Workspaces, or strictly one? |
| **Authentication** | Email/password, OAuth2 social login, or magic link? |
| **Integrations** | Which third-party APIs or webhooks must be supported in v1? |
| **Constraints** | Are there specific runtime/language requirements or hosting targets? |

---

## 4. Stopping Criteria & Assumptions

Do not continue questioning indefinitely. Stop asking when:
1. Core product goals, primary user journeys, and major entities are understood.
2. No remaining unknown would require tearing down the database schema or rewriting the TRD.

### Converting Minor Unknowns to Assumptions (`ASSUM-xxx`)
When minor edge cases remain, formulate them as explicit assumptions in the blueprint:
```markdown
## Assumptions
- **ASSUM-001:** The initial MVP will support English only.
- **ASSUM-002:** Default currency is USD; multi-currency support is deferred to v2.
- **ASSUM-003:** Invoices will be generated server-side using standard HTML-to-PDF.
```
The user can easily confirm or adjust these assumptions during document review.

---

## 5. The Pre-Generation Understanding Summary

Before writing the five blueprint documents, provide a concise 4-to-6 bullet summary of your understanding:

```text
Before I generate the Project Blueprint, here is my synthesized understanding:
- Product: A multi-tenant freelance invoicing platform (MVP web-only).
- Organization Model: Freelancers create organizations and can invite client viewers.
- Core Workflow: Freelancers draft invoices, add line items, and email payment links.
- Integrations: Stripe Checkout for invoice settlement; SendGrid for email dispatch.
- Tech Stack: Node.js/TypeScript, PostgreSQL (Prisma), React (Tailwind).

Key Assumptions:
- ASSUM-001: Invoices are immutable once marked 'PAID'.
- ASSUM-002: Single-currency (USD) for v1.

Does this match your vision, or should we adjust anything before document generation?
```
This enables the human developer to catch misconceptions before 500 lines of specification are written.
