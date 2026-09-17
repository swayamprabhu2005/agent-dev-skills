---
name: project-blueprint
description: >-
  Pre-implementation planning, interactive requirements clarification, and approval skill.
  Transforms rough software ideas into structured, cross-checked blueprint documents
  (PRD, TRD, UI/UX, Backend Schema, App Flow, and Mermaid diagrams). Blocks implementation
  until explicit human review and approval is granted.
license: MIT
metadata:
  author: SWAYAM KIRAN PRABHU
  version: 0.1.0
---

# Project Blueprint

Project Blueprint teaches an AI coding agent how to transform rough software ideas, feature requests,
and project concepts into a rigorous, cross-checked set of specification documents before any code
is written.

> **The Defining Rule:** The agent must not begin implementation until the required blueprint
> documents have been explicitly approved by the user.

---

## 1. When to Use This Skill

### Trigger Conditions (Substantial Work)
Activate this skill whenever:
* Starting a brand-new software project, application, or service from scratch.
* Introducing a major new capability, domain model, or full-stack feature.
* Undertaking an architectural migration, database redesign, or significant API overhaul.
* The user explicitly invokes planning (e.g., `/project-blueprint init`, "Create a blueprint for X", "Plan this project").

### Silent / Inactive Conditions (Small Tasks)
Do **NOT** force a full blueprint on:
* Routine bug fixes (e.g., fixing a null-pointer error or correcting a typo).
* Trivial cosmetic edits (e.g., updating a button color or adjusting CSS padding).
* Minor follow-up tasks on an already-implemented, established feature.
* Codebase queries, documentation lookups, or conversational discussions.

---

## 2. The Core 5-Artifact Blueprint Set

Project Blueprint organizes project knowledge into five distinct, specialized documents stored in
`docs/project-blueprint/` (or repository-configured path):

```text
docs/project-blueprint/
├── PRD.md              # Product Requirements Document (What & Why)
├── TRD.md              # Technical Requirements Document (Architecture & How)
├── UI_UX.md            # UI/UX Specification (Visuals, Layout, States)
├── BACKEND_SCHEMA.md   # Data Models, Relationships, & Database ER Diagrams
├── APP_FLOW.md         # User Journeys, State Transitions, & Flowcharts
└── .blueprint/
    └── state.yaml      # Machine-readable workflow status & approval lock
```

### Purpose of Each Document:
1. **`PRD.md` (Product Requirements Document):**
   * Answers: *What are we building, why are we building it, who is it for, and what must it do?*
   * Contains: Problem statement, goals, user personas, requirements with stable identifiers (`REQ-001`), user stories, acceptance criteria, non-goals, and success metrics.
2. **`TRD.md` (Technical Requirements Document):**
   * Answers: *How will the product technically work?*
   * Contains: Architectural overview, technology stack, service interactions, API contracts, security/auth model, scalability considerations, error handling, and system architecture Mermaid diagrams.
3. **`UI_UX.md` (UI/UX Specification):**
   * Answers: *What should the product look like, feel like, and how do users interact with it?*
   * Contains: Visual hierarchy, color tokens, typography, component layouts, responsive breakpoints, empty/loading/error states, and accessibility requirements.
4. **`BACKEND_SCHEMA.md` (Backend / Database Schema):**
   * Answers: *How is data represented, related, and stored?*
   * Contains: Entities, tables, columns, data types, primary/foreign keys, indexes, uniqueness constraints, soft-delete policies, audit timestamps, and Mermaid ER diagrams.
5. **`APP_FLOW.md` (Application / User Flow):**
   * Answers: *How do users navigate the system across primary and edge-case journeys?*
   * Contains: Step-by-step user journeys, decision branches, authentication redirects, error recovery flows, and Mermaid flowcharts.

---

## 3. The 10-Step Blueprint Lifecycle

```text
User's Rough Idea / Request
            ↓
1. Inspect Existing Repository & Conventions (if applicable)
            ↓
2. Interactive Clarification (Targeted 1-2 questions at a time)
            ↓
3. Synthesize Understanding & Confirm Key Assumptions
            ↓
4. Generate Blueprint Artifacts (PRD, TRD, UI/UX, Schema, Flow)
            ↓
5. Embed First-Class Mermaid Diagrams (Architecture, ER, Flow)
            ↓
6. Cross-Document Consistency Review (Check for contradictions)
            ↓
7. Present Blueprint for Human Review (Status: READY_FOR_REVIEW)
            ↓
      [ Human Review Gate ]
      ├── If Changes Requested: Revise affected artifacts → Re-verify → Back to Step 7
      └── If Explicitly Approved: Lock version → Advance to Step 8
            ↓
8. Status: APPROVED (Lock revision in .blueprint/state.yaml)
            ↓
9. Generate Implementation Plan (Phases, dependencies, test gates)
            ↓
10. Implementation May Begin (Ready for Project Sync & Commit Architect)
```

---

## 4. Interactive Questioning Protocol

Do **NOT** generate five generic templates immediately upon receiving a vague prompt. Nor should you overwhelm the user with a 20-question interrogation.

### Questioning Rules:
1. **Prioritize by Impact:** Ask first about ambiguities that materially alter architecture, data models, or core scope.
2. **Keep Batches Small:** Ask 1 to 2 focused questions at a time.
3. **Internal Classification:** Group questions mentally (Product Scope, Auth/Security, Data Model, UI/UX, Integrations, Constraints).
4. **Stop Asking When Material Unknowns Resolve:** When remaining details are minor, record them as **Assumptions** (`ASSUM-001`) rather than endlessly delaying progress.
5. **Summarize Before Generating:** Provide a concise understanding summary before creating the documents to give the user a chance to redirect early.

---

## 5. First-Class Mermaid Diagrams

Diagrams are structural engineering artifacts, not decorative art. Use Mermaid diagrams where they materially improve clarity:
* **`TRD.md`:** System architecture block diagrams (`flowchart TD` or `flowchart LR`), sequence diagrams for complex auth/payment handshakes (`sequenceDiagram`).
* **`BACKEND_SCHEMA.md`:** Relational entity models (`erDiagram`) with cardinality indicators (`||--o{`).
* **`APP_FLOW.md`:** Navigation and decision logic (`flowchart TD`).

*Keep diagrams focused and divided by concern. Do not create unreadable 100-node graphs.*

---

## 6. The Strict Human Approval Gate

> **Implementation remains completely locked until the blueprint reaches `APPROVED`.**

### What Counts as Explicit Approval:
* ✅ `"Approved."`
* ✅ `"I approve the blueprint."`
* ✅ `"Proceed with implementation."`
* ✅ `"The blueprint looks complete, please start building."`

### What Does NOT Count as Approval:
* ❌ `"looks good"` / `"nice"` / `"cool"` (Casual feedback is not an approval gate unlock).
* ❌ `"continue"` / `"next"` (Ambiguous command).
* ❌ The user asking another question or opening a file.
* ❌ Silence or moving to a different topic.

If user feedback is ambiguous, ask directly: *"Does this mean the blueprint is approved to proceed with implementation?"*

### Version-Specific Approval:
Approval applies strictly to the current blueprint version:
* Version 1 is `APPROVED`.
* If the user later requests a change (*"Also add team workspaces"*), Version 2 drops to `CHANGES_REQUESTED` and returns to `READY_FOR_REVIEW`.
* **Implementation is re-blocked until Version 2 is explicitly approved.**

---

## 7. Cross-Document Consistency & Conflict Detection

Before presenting the blueprint for review, execute a consistency audit across all five artifacts:
* **Traceable Identifiers:** Major product requirements receive stable IDs (e.g. `REQ-001: Google OAuth2 Login`).
* **Cross-Checking:**
  * If PRD states `REQ-001`, does TRD define the OAuth client service?
  * Does `UI_UX.md` define the login button and error modal?
  * Does `BACKEND_SCHEMA.md` store `google_id` on the `users` table?
  * Does `APP_FLOW.md` trace the redirect URI flow?
* **Conflict Rule:** If PRD states *"Only organization owners can delete projects"*, but UI/UX renders a delete button for all members and TRD has no role checks, **HALT**. Surface the conflict immediately as `CONFLICT DETECTED` and resolve it before requesting review.

---

## 8. Incremental Evolution & Implementation Drift

### Incremental Updates (Post-Approval Changes)
When requirements change after approval:
1. Identify **only** the affected documents (e.g., adding an API key feature affects TRD, Schema, and UI/UX, but leaves App Flow untouched).
2. Ask targeted clarifying questions about the delta.
3. Update only the affected sections.
4. Regenerate affected diagrams (e.g. updating ER diagram when schema changes).
5. Increment blueprint version in `.blueprint/state.yaml` and request review.

### Implementation Drift Protocol
If coding reveals an unforeseen technical blocker (e.g., chosen database cannot support required full-text search):
* **STOP coding immediately.**
* Report the discrepancy: *"Implementation discovery conflicts with approved TRD."*
* Propose an architectural adjustment.
* Update TRD/Schema, re-review, and obtain approval before resuming code.

---

## 9. Relationship with Sibling Skills

Project Blueprint, Project Sync, and Commit Architect work as an integrated triad of independent skills:

```text
                  PROJECT BLUEPRINT [project-blueprint]
                   "What and how should we build?"
                   (PRD, TRD, UI/UX, Schema, Flows, Approval)
                                  ↓
                              [Approval]
                                  ↓
                        Agent Implementation
                                  ↓
                     PROJECT SYNC [project-sync]
                   "Keep docs and ignore rules aligned"
                   (Reconcile README.md, .gitignore, Summary)
                                  ↓
                   COMMIT ARCHITECT [commit-architect]
                   "Organize work into clean Git history"
                   (Logical commit slicing, diff reviews, natural messages)
```

Each skill operates independently and does not require or duplicate the others.

---

## 10. Progressive Disclosure References

Consult the reference guides in `references/` for detailed operational instructions:
* [Interactive Questioning Guide](references/questioning.md) - Question prioritization, categorization, and stopping criteria.
* [Artifact Model & Templates](references/artifact-model.md) - Section-by-section breakdown of the 5 core documents.
* [Approval Gate & State Machine](references/approval-gate.md) - State transitions, ambiguity resolution, and version locking.
* [Document Quality & Traceability](references/document-guidelines.md) - Requirement tagging (`REQ-xxx`) and anti-fluff rules.
* [Mermaid Diagram Standards](references/mermaid-guidelines.md) - Architecture, ER, and flowchart syntax patterns.
* [Cross-Document Consistency Checks](references/consistency-checks.md) - Detecting contradictions and missing links.
* [Incremental Evolution & Drift](references/evolution.md) - Handling requirement changes and implementation deviations.
* [Worked Case Studies](references/examples.md) - Summary index of 6 real-world planning scenarios.

---

## 11. Helper Scripts

Deterministic command-line tools in `scripts/`:
* `python scripts/blueprint-state.py`: Inspects and manages `.blueprint/state.yaml` (status, approve, lock, version bump).
* `python scripts/check-consistency.py`: Scans the 5 blueprint documents for requirement ID coverage, open questions, and contradictions.
* `python scripts/validate-blueprint.py`: Verifies document existence, section completeness, and basic Mermaid diagram syntax.
