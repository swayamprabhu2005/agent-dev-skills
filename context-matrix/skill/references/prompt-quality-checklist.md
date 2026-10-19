# Prompt Quality Evaluation Checklist

> **Purpose:** Provide a rigorous, qualitative evaluation procedure to assess whether an AI prompt is fit for purpose, technically grounded, unambiguous, and testable.

Effective prompt engineering is not measured by word count. A 5-line prompt with razor-sharp constraints can be vastly superior to a 200-line prompt bloated with repetitive fluff. This checklist evaluates structural and operational readiness.

---

## 1. The 10-Point Quality Rubric

```text
┌────┬─────────────────────────────┬───────────────────────────────────────────────────────┐
│ #  │ Dimension                   │ Evaluation Standard                                   │
├────┼─────────────────────────────┼───────────────────────────────────────────────────────┤
│ 1  │ Goal Clarity                │ Is the primary deliverable unmistakable from line 1?  │
│ 2  │ Context Completeness        │ Does it supply grounded facts without repo-dumping?   │
│ 3  │ Task Specificity            │ Are verbs precise (implement, diagnose, benchmark)?   │
│ 4  │ Negative Constraints        │ Are out-of-scope boundaries and prohibitions explicit?│
│ 5  │ Input Sufficiency           │ Is the source code, schema, or error log accessible?  │
│ 6  │ Deliverable Definition      │ Is the target output structure unambiguously specified│
│ 7  │ Feasibility & Realism       │ Can the task be solved within memory & token limits?  │
│ 8  │ Verification Protocol       │ Are there concrete validation steps or tests defined? │
│ 9  │ Signal-to-Noise Ratio       │ Is the prompt free of redundant, hyperbolic filler?   │
│ 10 │ Fact vs. Assumption Boundary│ Are unverified inferences distinguished from facts?   │
└────┴─────────────────────────────┴───────────────────────────────────────────────────────┘
```

---

## 2. Qualitative Readiness Ratings

Rather than arbitrary numerical scores, Context Matrix classifies prompts into three actionable operational states:

### 🟢 State 1: Ready to Use
* **Criteria:** The objective is crisp, negative constraints are explicit, inputs are clearly referenced, the deliverable format is well-defined, and verification criteria exist.
* **Agent Action:** Proceed directly to prompt generation or execution without delay.

### 🟡 State 2: Ready with Assumptions
* **Criteria:** The core ask is clear, but secondary details (e.g., specific library version, minor styling preference, non-critical database schema convention) are unstated.
* **Agent Action:** State explicit, professional engineering assumptions in 1–2 bullet points and proceed immediately. Do not stall the user with questions.

### 🔴 State 3: Needs Clarification
* **Criteria:** The core request is missing fundamental information that makes correct execution impossible without guessing (e.g. "Fix the backend bug" without error logs, stack traces, or repository pointers; or "Choose a database" without knowing scale, consistency model, or data types).
* **Agent Action:** Ask at most 1–2 prioritized, multiple-choice or opinionated questions with clear defaults.

---

## 3. Step-by-Step Prompt Audit Walkthrough

When evaluating a prompt (via `/context-matrix evaluate [prompt]`), apply this analytical sequence:

1. **Scan for Hidden Contradictions:**
   * Does the prompt ask for "Maximum security with zero latency overhead" or "Complete rewrite while maintaining 100% backward compatibility"? Expose these trade-offs.
2. **Audit Negative Constraints:**
   * Does the model know what NOT to touch? (e.g. "Do not modify public API signatures").
3. **Assess Verification Readiness:**
   * How will the user know the model succeeded? If there are no unit tests, compiler checks, or acceptance criteria, recommend them.
4. **Prune Redundancy:**
   * Strip repetitive instructions like "Make sure it is high quality, robust, enterprise-grade, clean, and elegant." Replace them with concrete structural rules.
