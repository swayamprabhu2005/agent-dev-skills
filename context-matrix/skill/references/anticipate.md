# ANTICIPATE Framework

> **Purpose:** Design audience-centric educational materials, tutorials, developer onboarding guides, and interactive technical documentation with built-in comprehension checks.

The **ANTICIPATE** framework prioritizes the learner or reader. Rather than dumping raw information, it anticipates user prerequisites, stumbling blocks, cognitive load, and questions, guiding the creator through a complete pedagogical lifecycle.

---

## 1. The 10 Components of ANTICIPATE

```text
┌────────────────────────────────────────────────────────────────────────┐
│ A — Audience    : Learner persona, background knowledge, prerequisites │
│ N — Need        : Specific skill gap, challenge, or learning objective │
│ T — Task        : Core deliverable (tutorial, workshop, deep-dive doc) │
│ I — Information : Key concepts, APIs, theoretical background, sources  │
│ C — Constraints : Reading time, vocabulary level, environment limits   │
│ I — Illustrate  : Diagrams, concrete code examples, & mental models    │
│ P — Plan        : Phased pedagogical outline (from simple to complex)  │
│ A — Act         : Hands-on exercise, interactive task, or walkthrough  │
│ T — Test        : Self-assessment, quiz questions, or automated checks │
│ E — Enhance     : Common pitfalls, edge cases, & next steps for mastery│
└────────────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

1. **A — Audience:** Who is reading? (e.g. Junior JavaScript developers learning Rust; seasoned backend engineers new to Kubernetes). What concepts can be assumed? What must be defined?
2. **N — Need:** What specific capability will the learner gain? (e.g. "Understand ownership and borrowing so they can resolve borrow-checker errors independently").
3. **T — Task:** The format: 15-minute tutorial, interactive lab, reference documentation, or conceptual guide.
4. **I — Information:** The core conceptual foundations and factual material that must be taught.
5. **C — Constraints:** Time limit (e.g., "Must be completable in 20 minutes"), dependency constraints ("No Docker required; run in standard browser sandbox").
6. **I — Illustrate:** Visual mental models, ASCII state diagrams, memory layout graphs, or real-world analogies.
7. **P — Plan:** Step-by-step curriculum outline ensuring progressive difficulty without sudden cognitive leaps.
8. **A — Act:** Hands-on code example with clear step-by-step instructions that the learner executes themselves.
9. **T — Test (Checks for Understanding):** Comprehension questions, intentional broken code to fix, or automated test cases.
10. **E — Enhance:** "Gotchas", common misconceptions, debugging tips, and pointers to advanced literature.

---

## 2. Pedagogical Progression

Effective technical training follows a 4-stage pedagogical loop:
```text
Empathize (Audience + Need)
       ↓
Structure (Plan + Information + Constraints)
       ↓
Demonstrate & Practice (Illustrate + Act)
       ↓
Verify & Deepen (Test + Enhance)
```

---

## 3. When to Use ANTICIPATE

* **Primary Use Cases:**
  * Developer onboarding guides and API walkthroughs.
  * Technical documentation for open-source repositories.
  * Interactive programming tutorials and workshop modules.
  * Training material for team members transitioning to a new tech stack.
* **When NOT to Use:**
  * Direct bug fixes in a repository (use **CLARITY** or **RIPPLE**).
  * Rapid internal notes or quick emails (use **CATCH**).

---

## 4. Evaluation Checklist for ANTICIPATE Prompts

* [ ] Is the audience's starting skill level and prerequisite knowledge explicitly defined?
* [ ] Does the material avoid unexplained jargon or hidden assumptions?
* [ ] Is there at least one illustrative diagram or concrete mental model?
* [ ] Does the guide include an active hands-on task for the learner?
* [ ] Are there explicit checks for understanding (quizzes, unit tests, or broken code exercises)?

---

## 5. Practical Example

### Example: Developer Onboarding Tutorial (Database Transactions)

```markdown
**Audience:** Junior Fullstack Engineers familiar with Node.js and SQL SELECT queries, but unfamiliar with database transaction isolation levels and concurrency anomalies.
**Need:** Learn how to use transactions in PostgreSQL with Prisma ORM to prevent race conditions during inventory checkout.
**Task:** Write an interactive 15-minute tutorial with code snippets, diagrams, and a debugging exercise.
**Information:** ACID properties, `BEGIN / COMMIT / ROLLBACK`, row locking with `SELECT FOR UPDATE`, and Prisma interactive transactions (`$transaction`).
**Constraints:** Reading time < 10 minutes; all code must run in standard Node.js without external microservices.
**Illustrate:** Provide an ASCII sequence diagram showing two simultaneous checkouts causing an oversell anomaly without transactions.
**Plan:**
1. The Problem: The naive read-then-write oversell bug.
2. The Concept: ACID transactions and atomicity.
3. The Solution: Implementing Prisma `$transaction` with optimistic vs pessimistic locking.
4. Practice: Fixing an oversell bug.
**Act:** Provide a realistic e-commerce inventory deduction function with a subtle race condition and step-by-step instructions to refactor it.
**Test:** Include 3 multiple-choice comprehension questions and an intentional bug challenge where a transaction fails to roll back on error.
**Enhance:** Explain isolation levels (`READ COMMITTED` vs `SERIALIZABLE`) and deadlocks with mitigation rules.
```
