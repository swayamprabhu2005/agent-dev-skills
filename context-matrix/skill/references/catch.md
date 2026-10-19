# CATCH Framework

> **Purpose:** Rapidly structure everyday requests, short technical tasks, communications, release notes, and focused content generation without unnecessary overhead.

The **CATCH** framework is the lean, agile counterweight in the Context Matrix system. While frameworks like SOCRATES and RIPPLE are designed for deep architectural and forensic analysis, CATCH ensures that simple, routine tasks remain fast, direct, and unencumbered by excessive boilerplate.

---

## 1. The 5 Components of CATCH

```text
┌────────────────────────────────────────────────────────────────────────┐
│ C — Context  : Minimal relevant background (1–2 sentences)             │
│ A — Aim      : The direct goal or deliverable                          │
│ T — Tone     : Desired voice (concise, executive, conversational, dry) │
│ C — Criteria : Essential constraints, length limit, or key bullet points│
│ H — Help     : Specific role or formatting assistance requested        │
└────────────────────────────────────────────────────────────────────────┘
```

### Component Breakdown

1. **C — Context:**
   * What triggered this request? (e.g., "We just shipped v1.4.0 of our CLI tool with 2 bug fixes and a 3x speedup"). Keep it tight and focused.
2. **A — Aim:**
   * What is the immediate deliverable? (e.g., "Draft a release announcement email for beta users").
3. **T — Tone:**
   * Voice and personality: Professional and enthusiastic, direct and technical, or polite and diplomatic.
4. **C — Criteria:**
   * Hard constraints: Word count (e.g. "< 150 words"), specific bullets to highlight, or formatting rules.
5. **H — Help:**
   * The specific prompt request to the AI: "Format as Markdown with a clear call-to-action button text".

---

## 2. The Anti-Complexity Rule

> [!TIP]
> **Do not over-engineer simple tasks.**
> If a user needs a 3-bullet Slack update or a quick shell alias, forcing them through SOCRATES or ANTICIPATE creates friction. CATCH is designed to get the job done in seconds.

---

## 3. When to Use CATCH

* **Primary Use Cases:**
  * Release notes and changelog announcements.
  * Internal team communications (Slack updates, executive summaries).
  * Short technical emails (incident notifications, status reports).
  * Quick scripts, shell one-liners, or regex extraction tasks.
  * Presentation slide bullets or pitch deck snippets.
* **When NOT to Use:**
  * Complex architectural refactors (use **SOCRATES**).
  * Deep forensic code reviews or debugging (use **RIPPLE**).
  * Multi-step engineering features with intricate constraints (use **CLARITY**).

---

## 4. Evaluation Checklist for CATCH Prompts

* [ ] Is the prompt concise and free of unnecessary specification bloat?
* [ ] Is the primary Aim immediately obvious in the first sentence?
* [ ] Are length or formatting constraints clearly defined?
* [ ] Can the output be generated immediately without multi-turn questioning?

---

## 5. Practical Examples

### Example 1: Release Announcement Email
```markdown
**Context:** We deployed v2.1.0 of our developer analytics dashboard. The update adds dark mode support, fixes an OAuth token expiration glitch, and reduces query latency by 40%.
**Aim:** Draft a product release email to our developer user base.
**Tone:** Friendly, developer-focused, concise, and enthusiastic.
**Criteria:** Under 150 words, include 3 bullet points, and highlight the GitHub release link.
**Help:** Provide a compelling subject line and clear Markdown formatting.
```

### Example 2: Short Technical Request (Shell Scripting)
```markdown
**Context:** Our CI pipeline needs to purge orphaned Docker build cache volumes older than 7 days on Linux runner instances.
**Aim:** Write a safe Bash script that cleans prune volumes without interrupting active builds.
**Tone:** Pragmatic developer script.
**Criteria:** Strict error handling (`set -euo pipefail`), dry-run flag support (`--dry-run`), and human-readable logging.
**Help:** Return the self-contained script with usage comments.
```
