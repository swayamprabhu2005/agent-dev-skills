# Example 01: Beginner-Level Programming Explanation (CLARITY)

---

## 1. User Invocation

```text
/context-matrix Explain recursion in Python to a beginner without confusing jargon.
```

---

## 2. Framework Selected

* **Primary Framework:** `CLARITY`
* **Selection Rationale:** The task requests a clear, bounded technical explanation with specific audience constraints.

---

## 3. Relevant Context & Constraints

* **Audience:** Beginner programmer learning Python functions.
* **Constraints:** Avoid theoretical computer science jargon (call stacks, activation frames, algebraic data types); use an intuitive real-world mental model.
* **Target Output:** Explanatory guide in Markdown with 1 clear Python code example, 1 step-by-step visual trace, and a base-case warning.

---

## 4. Resulting Prompt / Generated Workflow

```markdown
**Context:** The reader is a beginner Python programmer who understands basic `def` functions, variables, and `if/else` statements, but finds recursive functions intimidating.
**Look & Feel:** Warm, encouraging, clear, and plain-English developer prose. Use Markdown formatting.
**Ask:** Explain how recursion works in Python using the intuitive analogy of Russian nesting dolls (Matryoshka).
**Rules:**
1. Do not use academic terms like "call stack activation records" or "lexical scoping".
2. Must explain the concept of the "Base Case" (the smallest doll) and why omitting it creates an infinite loop (`RecursionError`).
3. Provide a working Python countdown function (`def countdown(n):`).
4. Include an ASCII step-by-step trace showing what happens when `countdown(3)` is called.
**Input:** Beginner-level Python syntax.
**Target:** A 3-section tutorial:
  - Section 1: The Doll Metaphor.
  - Section 2: The Two Golden Rules (Base Case & Recursive Step).
  - Section 3: The Code & Execution Trace.
**You:** Friendly senior Python mentor.
```

---

## 5. Evaluation Criteria

* [x] **Goal Clarity:** Clearly asks for an explanation of recursion.
* [x] **Negative Constraints:** Explicitly bans confusing theoretical jargon.
* [x] **Concrete Deliverable:** Mandates Python code and an execution trace diagram.
* [x] **Readiness Status:** `READY`
