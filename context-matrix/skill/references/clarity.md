# CLARITY Framework

> **Purpose:** Produce clear, precise, and robust prompts for general-purpose software development, technical explanations, and rigorous engineering work.

The **CLARITY** framework is the primary workhorse of the Context Matrix prompt system. It is designed to express all technical and operational requirements unambiguously without forcing irrelevant or verbose narrative filler into every request.

---

## 1. The 7 Components of CLARITY

```text
┌────────────────────────────────────────────────────────────────────────┐
│ C — Context    : Relevant background, system architecture, & situation │
│ L — Look & Feel: Tone, communication style, formatting, & perspective   │
│ A — Ask        : The specific, unambiguous task, action, or objective   │
│ R — Rules      : Constraints, performance bounds, exclusions, & guards  │
│ I — Input      : Source code, schemas, raw data, or reference examples  │
│ T — Target     : Exact deliverable format, schema, or output artifacts │
│ Y — You        : Specialized role or domain persona the agent assumes   │
└────────────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

1. **C — Context:**
   * What is the current state of the application or environment?
   * What dependencies, frameworks, or operating parameters are active?
   * *Rule:* Provide grounded project facts. Avoid dumping irrelevant codebase history.

2. **L — Look & Feel:**
   * Tone: Professional, academic, concise developer prose, or pedagogical.
   * Format: Markdown headers, tables, inline code blocks, or raw JSON.
   * *Rule:* Match the recipient's consumption needs (e.g. senior code reviewer vs end user).

3. **A — Ask:**
   * Exactly what must the assistant do?
   * Use active, imperative verbs: *implement*, *refactor*, *benchmark*, *diagnose*, *extract*.
   * *Rule:* Never leave the core deliverable open to interpretation.

4. **R — Rules:**
   * Negative constraints: What is strictly forbidden (e.g., "Do not introduce third-party dependencies", "Do not modify the database schema")?
   * Performance or compliance bounds: Memory limits, backward compatibility, idempotency.
   * *Rule:* Make edge-case handling explicit.

5. **I — Input:**
   * Concrete source materials: Code snippets, API payloads, error traces, or configuration files.
   * *Rule:* Provide only the minimal sufficient code or context necessary to execute the Ask.

6. **T — Target:**
   * What does the finished product look like?
   * Examples: A single drop-in TypeScript function, a unified diff patch, a Markdown analysis table.
   * *Rule:* Specify validation criteria so the result can be tested immediately.

7. **Y — You:**
   * Who is the AI acting as?
   * Examples: Senior distributed systems architect, TypeScript compiler engineer, security auditor.
   * *Rule:* Assigning a domain role primes the model's technical depth and vocabulary.

---

## 2. When to Use CLARITY

* **Primary Use Cases:**
  * Software implementation and feature coding.
  * API and database schema design.
  * Precise technical explanations for engineers.
  * Refactoring existing modules with strict constraints.
  * General-purpose tasks where ambiguity leads to rework.
* **When NOT to Use:**
  * When the task is an open-ended creative exploration (use **MAGIC**).
  * When deciding high-level business feasibility across multiple trade-offs (use **SOCRATES**).
  * When the request is a simple one-liner that needs no complex framing (use **CATCH**).

---

## 3. How the Assistant Applies CLARITY

1. **Context Extraction:** Scan repository configurations (e.g. `tsconfig.json`, `Cargo.toml`) to extract grounded Context rather than asking the user for details already in the repo.
2. **Selective Component Activation:** Not every component is mandatory for every prompt. If Look & Feel is standard developer Markdown, keep it implicit or brief. Do not force empty placeholder fields.
3. **Guardrail Enforcing:** Transform vague desires ("Make it fast and safe") into concrete Rules ("Must be O(N) time complexity, zero memory allocations in the hot loop, return a Result<T, Error>").

---

## 4. Evaluation Checklist for CLARITY Prompts

* [ ] Is the Ask focused on a single primary objective?
* [ ] Are negative constraints (what NOT to do) clearly stated?
* [ ] Are all relevant inputs provided or accurately located in the workspace?
* [ ] Is the target deliverable well-defined and testable?
* [ ] Does the prompt omit redundant or generic filler?

---

## 5. Practical Examples

### Example 1: Software Implementation (TypeScript)
```markdown
**Context:** We have a Node.js 20 backend with Redis 7. We are experiencing intermittent duplicate task execution in our background queue.
**You:** Senior Backend Reliability Engineer.
**Ask:** Implement an idempotent distributed lock utility using Redis `SET key value NX PX`.
**Input:** Our existing Redis client instance `const redis = new Redis(process.env.REDIS_URL);`.
**Rules:**
1. Do not introduce new npm packages.
2. Lock duration must default to 5000ms with optional renewal.
3. Must safely release locks using a Lua script to ensure the token matches.
4. Handle Redis connection timeouts gracefully.
**Look & Feel:** Production-grade TypeScript, strict typing, fully documented with JSDoc.
**Target:** A standalone TypeScript module `distributed-lock.ts` exporting `withDistributedLock<T>()` and unit tests using Jest.
```

### Example 2: Technical Explanation
```markdown
**Context:** Our engineering team is transitioning a monolithic Django app to asynchronous FastAPI services. Junior developers are confused by Python's `asyncio` event loop.
**You:** Principal Python Staff Instructor.
**Ask:** Explain how the Python `asyncio` event loop executes cooperative multitasking, contrasting CPU-bound vs I/O-bound blocking.
**Rules:**
1. Avoid high-level marketing buzzwords.
2. Ground explanations in the CPython runtime mechanics.
3. Include two contrasting code examples (one blocking the loop, one non-blocking).
**Target:** A Markdown technical guide with an ASCII sequence diagram showing task switching.
```
