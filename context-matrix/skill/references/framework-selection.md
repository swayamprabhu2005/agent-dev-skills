# Framework Selection Engine

The Framework Selection Engine is the analytical core of Context Matrix. Rather than mechanically treating prompt engineering as an arbitrary set of templates, the engine evaluates the user's objective, inspects repository context, selects the optimal prompt framework, and composes high-fidelity instructions.

---

## 1. Core Selection Decision Tree

```text
Incoming Task / Request
       │
       ▼
Explicit Framework Requested? ──(Yes)──► Honor explicit selection (validate appropriateness)
       │
      (No / Auto)
       │
       ▼
Is this a creative, artistic, or storytelling task?
       ├──(Yes)──► MAGIC (Motivation, Audience, Goal, Input, Create)
       │
      (No)
       ▼
Is this a quick, straightforward everyday communication or short request?
       ├──(Yes)──► CATCH (Context, Aim, Tone, Criteria, Help)
       │
      (No)
       ▼
Is the primary goal systematic inspection, code review, debugging, or dataset audit?
       ├──(Yes)──► RIPPLE (Role, Input, Process, Points, Layout, Evaluate)
       │
      (No)
       ▼
Is the task educational, a tutorial, courseware, or audience-tailored training?
       ├──(Yes)──► ANTICIPATE (Audience, Need, Task, Info, Constraints, Illustrate, Plan, Act, Test, Enhance)
       │
      (No)
       ▼
Does the task require deep external research, vendor/tool evaluation, or multi-step discovery?
       ├──(Yes)──► PARTNER (Purpose, Audience, Research, Think, Narrow, Execute, Review)
       │
      (No)
       ▼
Is it high-stakes decision support, recommendation, or personalized advisory?
       ├──(Yes)──► TRUST (Task, Reason, Understand, Structure, Tailor)
       │
      (No)
       ▼
Does it involve architectural planning, trade-off analysis, feasibility, or system design?
       ├──(Yes)──► SOCRATES (Situation, Objective, Constraints, Role, Action, Thinking, Evaluation, Summary)
       │
      (No)
       ▼
General software engineering, implementation, technical explanation, or core instruction?
       └─────────► CLARITY (Context, Look & Feel, Ask, Rules, Input, Target, You)
```

---

## 2. Default Framework Routing Matrix

| Task Archetype | Primary Framework | Key Distinguishing Need | Why This Framework? |
| :--- | :---: | :--- | :--- |
| **Core Coding & Engineering** | **CLARITY** | Precise functional specs, input/output contracts, technical boundaries | Balances explicit requirements without forcing irrelevant narrative fields. |
| **Architectural Planning & Trade-offs** | **SOCRATES** | Multi-alternative comparison, resource limits, formal evaluation | Distinguishes planning from execution; systematically weighs constraints. |
| **Tutorials & Educational Guides** | **ANTICIPATE** | Learner empathy, progressive exercises, comprehension checks | Structures pedagogical flow from audience need to active testing. |
| **Technology Evaluation & Research** | **PARTNER** | Evidence gathering, source grounding, competitive narrowing | Prevents hallucination; enforces empirical research before execution. |
| **Tailored Decision Support** | **TRUST** | User-specific context, trade-off reasoning, structured advice | Identifies ambiguity; tailors recommendations to real circumstances. |
| **Code Review, Debugging, Audits** | **RIPPLE** | Structured analytical methodology, explicit inspection points | Separates the diagnostic process from presentation; demands verification. |
| **Everyday Requests & Concise Comms** | **CATCH** | Rapid execution, clear criteria, minimal overhead | Prevents specification bloat on straightforward, low-risk requests. |
| **Creative Content & Narrative Media** | **MAGIC** | Creative motivation, tone, visual/narrative continuity | Defines creative vision and artifact structure without false guarantees. |

---

## 3. Multi-Framework Combinations

A task often crosses functional boundaries. In such cases, the engine allows combining two (or at most three) frameworks, where each framework governs a distinct phase of the workflow:

1. **SOCRATES + RIPPLE (Architectural Evaluation & Code Audit):**
   * *Role:* SOCRATES establishes system constraints and trade-offs; RIPPLE executes the structured audit of candidate implementations against those constraints.
2. **CLARITY + RIPPLE (Rigorous Bug Fixing & Diagnostics):**
   * *Role:* RIPPLE diagnoses the root cause through structured inspection points; CLARITY specifies the precise remediation requirements, test inputs, and target patch.
3. **ANTICIPATE + MAGIC (Engaging Educational Content / Visual Tutorials):**
   * *Role:* ANTICIPATE designs the pedagogy, exercises, and learner checks; MAGIC authors the creative narrative, metaphors, or comic script layout.
4. **PARTNER + SOCRATES (Research-Driven Architectural Strategy):**
   * *Role:* PARTNER gathers empirical ecosystem data and library benchmarks; SOCRATES analyzes technical feasibility, hardware limits, and trade-offs.
5. **CATCH + CLARITY (Short Task with Strict Delivery Constraints):**
   * *Role:* CATCH keeps the turnaround fast and direct; CLARITY enforces exact output schema and rule boundaries.

> [!IMPORTANT]
> Never combine frameworks arbitrarily. Add a secondary framework only when it provides a distinct, measurable benefit that a single framework cannot address alone.

---

## 4. Context Inspection & Grounding Protocol

When operating in an existing software repository, Context Matrix does not generate generic prompts in a vacuum. It executes a targeted context audit:

1. **Audit Project Anatomy:**
   * Inspect directory layout, configuration files (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`), and build tooling.
2. **Verify Architecture & Existing Conventions:**
   * Inspect existing coding patterns, error handling paradigms, and naming conventions in relevant source files.
3. **Respect Existing Specifications & Gates:**
   * If `.blueprint/state.yaml` or formal PRDs/TRDs exist (e.g. from Project Blueprint), treat them as hard constraints. Do not bypass approval gates.
4. **Classify Knowledge Rigorously:**
   * **Verified Facts:** Code, configurations, and test suites directly inspected.
   * **User Requirements:** Explicit parameters provided in the current prompt.
   * **Assumptions:** Inferred implementation details, clearly marked as assumptions.
   * **Unresolved Questions:** Ambiguities that materially alter correctness, raised as concise questions.

---

## 5. Execution Boundary Rules

Context Matrix strictly distinguishes between three execution intents:

| User Intent | Invocation Pattern | Permitted Agent Action | Prohibited Action |
| :--- | :--- | :--- | :--- |
| **Prompt Engineering** | `/context-matrix prompt ...` or `/context-matrix improve ...` | Output formatted, copyable prompt string and quality evaluation. | Modifying repository code or creating implementation files. |
| **Methodology Explanation** | `/context-matrix explain ...` | Explain the framework, components, use cases, and give an illustrative example. | Executing tasks or analyzing unrelated project files. |
| **Task Execution** | `/context-matrix [framework] Implement ...` | Apply the framework methodology to directly plan, execute, and verify the work. | Executing code changes without adhering to project validation gates. |
