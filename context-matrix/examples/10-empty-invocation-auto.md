# Example 10: Invoking `/context-matrix` Without Arguments (Mode A)

---

## 1. User Invocation

```text
/context-matrix
```

---

## 2. Skill Response Behavior

When invoked without trailing arguments, Context Matrix gracefully identifies that no specific task or framework was passed. Instead of failing, asking an unguided questionnaire, or making assumptions, it displays a concise developer cheat sheet.

---

## 3. Delivered Output

```text
Context Matrix (v0.1.0)
Orchestrating 8 Prompt-Engineering Frameworks for Disciplined AI Development

Supported Frameworks:
  • CLARITY    : General software engineering, feature coding, technical specs
  • SOCRATES   : System architecture, feasibility analysis, resource trade-offs
  • ANTICIPATE : Tutorials, onboarding documentation, comprehension exercises
  • PARTNER    : Tool evaluations, competitive research, empirical benchmarks
  • TRUST      : Tailored decision support, situational advisory, recommendations
  • RIPPLE     : Forensic code reviews, root-cause debugging, dataset audits
  • CATCH      : Rapid everyday requests, release notes, concise scripts
  • MAGIC      : Creative storytelling, comic scripts, marketing copy

Quick Invocation Examples:
  /context-matrix Implement JWT authentication with refresh tokens in Go
  /context-matrix socrates Evaluate database partitioning options for 10TB scale
  /context-matrix ripple Review src/auth/session.ts and diagnose memory leak
  /context-matrix prompt Build a rate-limiter middleware using Redis
  /context-matrix improve Fix the backend bug
  /context-matrix evaluate Review this PR and tell me if it works
  /context-matrix combine socrates ripple Redesign connection pool architecture
  /context-matrix help
```

---

## 4. Evaluation Criteria

* [x] **No Phantom Execution:** Does not attempt to execute a fictional task.
* [x] **Actionable Guidance:** Provides immediate, copyable command patterns.
* [x] **Readiness Status:** `READY`
