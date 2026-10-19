# TRUST Framework

> **Purpose:** Deliver tailored, high-conviction decision support and advisory responses that adapt precisely to the user's operational constraints while eliminating guesswork.

The **TRUST** framework is optimized for consultative pair-programming and architectural decision support. It bridges the gap between generic AI answers and situational precision by uncovering the underlying motivation, clarifying essential ambiguities, and tailoring the output structure to immediate user needs.

---

## 1. The 5 Components of TRUST

```text
┌────────────────────────────────────────────────────────────────────────┐
│ T — Task       : The immediate request or inquiry                      │
│ R — Reason     : The underlying business or technical motivation ("why")│
│ U — Understand : Clarifying key ambiguities & environmental parameters │
│ S — Structure  : Clear, scannable format (matrix, decision tree, diff) │
│ T — Tailor     : Customizing specifically to user context & constraints│
└────────────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

1. **T — Task:**
   * What question or decision is being posed? (e.g. "Should we adopt GraphQL or stick with REST for our mobile app?")
2. **R — Reason:**
   * Why is this being evaluated now? (e.g., "Mobile app startup latency is high due to over-fetching on 3G cellular networks"). Understanding the root reason prevents solving the wrong problem.
3. **U — Understand (Discipline of Clarification):**
   * Identify missing parameters that *materially alter* the recommendation (e.g. team familiarity, caching requirements, backend gateway tech).
   * *The Targeted Clarification Rule:*
     * If missing information changes the architecture completely: ask **at most 1–2 focused questions** with opinionated default recommendations.
     * If reasonable assumptions allow useful progress: **proceed with stated assumptions** rather than stalling the user with a questionnaire.
4. **S — Structure:**
   * Organize output for rapid executive consumption: Decision Matrix, Pros/Cons by role, or Phased Action Plan. Avoid walls of unformatted prose.
5. **T — Tailor:**
   * Adjust recommendations to the user's specific stack, team size, timeline, and risk tolerance. Discard generic textbook advice that doesn't fit their situation.

---

## 2. Clarification vs. Assumption Protocol

```text
Is critical information missing?
       │
       ├──(Yes, and correctness is severely compromised)──► Ask 1–2 targeted questions with clear defaults
       │
       └──(No, or reasonable engineering defaults exist)──► State explicit assumptions and deliver tailored result
```

* **Bad Practice:** Asking 8 academic questions before offering any insight.
* **Good Practice:** "Assuming your client app runs on React Native and relies on HTTP caching, here is the tailored comparison. If you instead rely on offline SQLite synchronization, note the caveat in Section 3."

---

## 3. When to Use TRUST

* **Primary Use Cases:**
  * Architecture decisions where trade-offs depend on context (e.g., Monorepo vs Polyrepo, Serverless vs Containers).
  * High-stakes technology migration roadmaps.
  * Senior engineering advisory and code refactoring strategy.
  * Vendor and hosting platform selection.
* **When NOT to Use:**
  * Mechanical code generation tasks with fixed specs (use **CLARITY**).
  * Formal pre-implementation specification suites (use Project Blueprint).

---

## 4. Evaluation Checklist for TRUST Prompts

* [ ] Does the prompt capture the root *Reason* behind the task?
* [ ] Does it avoid asking redundant questions whose answers can be inferred?
* [ ] Are assumptions transparently stated alongside recommendations?
* [ ] Is the output structured for direct decision-making (e.g. tabular comparison, decision tree)?
* [ ] Is the guidance tailored to specific team, stack, or performance constraints?

---

## 5. Practical Example

### Example: Architectural Decision (Monolith vs Microservices)

```markdown
**Task:** Advise on whether our fintech startup should split our monolithic Python service into microservices.
**Reason:** Deployment pipeline takes 45 minutes; 3 separate teams frequently suffer deployment collisions and blocked release trains.
**Understand:**
- Current team: 14 engineers across 3 squads (Payments, Risk, User Auth).
- Traffic: 1,200 RPS peak, mostly database read-heavy.
- Infrastructure: AWS ECS Fargate, single Postgres database.
- Primary bottleneck: Developer workflow collisions, not CPU/memory scale.
**Structure:**
1. Root cause diagnosis.
2. Architectural options matrix (Modular Monolith vs Microservices vs Service Extraction).
3. Tailored recommendation with 90-day execution steps.
**Tailor:**
- Tailor specifically to a 14-person engineering team with minimal dedicated DevOps staff. Avoid high-overhead solutions like Kubernetes/Istio service mesh.
```
