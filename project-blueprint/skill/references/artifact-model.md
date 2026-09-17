# Blueprint Artifact Model & Structure Reference

This guide details the internal structure, mandatory sections, and semantic responsibilities of the five primary Project Blueprint documents.

---

## 1. Directory Structure

By default, blueprint artifacts are maintained in `docs/project-blueprint/`:

```text
docs/project-blueprint/
├── PRD.md              # Product Requirements Document
├── TRD.md              # Technical Requirements Document
├── UI_UX.md            # UI/UX Specification
├── BACKEND_SCHEMA.md   # Data Models & Schema
├── APP_FLOW.md         # Application & User Flows
├── IMPLEMENTATION_PLAN.md # Generated only after blueprint approval
└── .blueprint/
    └── state.yaml      # Machine-readable status
```

---

## 2. Document Specifications

### Artifact 1: `PRD.md` (Product Requirements Document)
* **Mission:** Defines **what** is being built, **why**, and for **whom**.
* **Standard Sections:**
  1. **Executive Overview & Problem Statement:** What pain point does this solve?
  2. **Goals & Non-Goals:** Explicit boundaries of what is included vs. deferred.
  3. **Target Users & Personas:** Who are the primary actors using the system?
  4. **Product Requirements (`REQ-xxx`):** Discrete, testable requirements.
  5. **User Stories & Acceptance Criteria:** Given / When / Then criteria.
  6. **Assumptions (`ASSUM-xxx`) & Constraints:** Business or technical boundaries.
  7. **Success Metrics (KPIs):** Measurable targets (e.g. latency, conversion).

### Artifact 2: `TRD.md` (Technical Requirements Document)
* **Mission:** Defines **how** the system technically functions and scales.
* **Standard Sections:**
  1. **Architecture Overview:** High-level pattern (monolith, modular service, event-driven).
  2. **Tech Stack & Justifications:** Language, framework, database, and libraries.
  3. **System Architecture Diagram:** Fenced Mermaid `flowchart TD` diagram.
  4. **API Contracts & Endpoints:** REST/GraphQL specifications with request/response types.
  5. **Authentication & Authorization Model:** Tokens, sessions, RBAC/ABAC policies.
  6. **Security & Privacy:** Data encryption, sanitization, rate limiting.
  7. **Scalability & Performance:** Caching strategies, query limits, indexing.
  8. **Error Handling & Observability:** Structured logging, metrics, error payloads.

### Artifact 3: `UI_UX.md` (UI/UX Specification)
* **Mission:** Defines **look, feel, visual direction, and interaction states**.
* **Standard Sections:**
  1. **Design System & Visual Direction:** Tone, aesthetic, color palette, typography.
  2. **Layout & Grid System:** Page anatomy, navigation shell, responsive breakpoints.
  3. **Core Component Specifications:** Modals, tables, cards, forms, action bars.
  4. **Component State Matrix:** Standardized definitions for default, hover, focus, active, disabled, loading, empty, and error states.
  5. **Accessibility (a11y):** Keyboard navigation, contrast ratios, ARIA guidelines.

### Artifact 4: `BACKEND_SCHEMA.md` (Backend / Database Schema)
* **Mission:** Defines **data representations, relationships, and persistence rules**.
* **Standard Sections:**
  1. **Data Model Overview:** Relational, document, or key-value structures.
  2. **Entity-Relationship (ER) Diagram:** Fenced Mermaid `erDiagram`.
  3. **Table / Collection Definitions:** Field names, data types, nullability, defaults.
  4. **Indexes & Constraints:** Primary keys, foreign keys, unique indexes.
  5. **Data Lifecycle Policies:** Soft deletion, audit fields (`created_at`, `updated_at`), retention rules.

### Artifact 5: `APP_FLOW.md` (Application / User Flow)
* **Mission:** Defines **how users navigate the system across primary and error paths**.
* **Standard Sections:**
  1. **User Journey Narratives:** Step-by-step walkthroughs of core jobs-to-be-done.
  2. **Navigation Flowchart:** Fenced Mermaid `flowchart TD` illustrating screen transitions.
  3. **Authentication & Onboarding Flow:** Signup, email verification, login redirects.
  4. **Decision Trees & Error Recovery:** Edge cases, retry paths, validation failure fallbacks.
