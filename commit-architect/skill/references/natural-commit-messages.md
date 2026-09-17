# Natural Developer Commit Messages

Commit Architect emphasizes natural, professional, human developer language as the primary standard for commit messages.

---

## 1. Why Natural Language is the Default

Many AI coding agents mechanically force Conventional Commits (`feat(auth): ...`, `chore(deps): ...`, `fix(ui): ...`) on every project regardless of project culture. In many professional software teams, this feels artificial, noisy, and robotic.

Unless a repository explicitly states that Conventional Commits are required, Commit Architect instructs agents to write commit messages in the **natural, clean, concise idiom of seasoned software engineers**.

---

## 2. The Core Anatomy of a Natural Commit Message

```text
Short imperative summary (under 50-72 chars)

Optional explanatory body describing the context, the rationale,
and any non-obvious trade-offs. Focus on *why* the change was made,
not just *what* changed (since the diff already shows the what).

- Optional bullet points for multi-part changes
- Only include when genuinely helpful for human reviewers
```

### Key Mechanical Rules:
1. **Use the Imperative Mood:** Write as if giving a command:
   * `Add Google login support` (not `Added Google login support` or `Adds Google login support`)
   * `Handle expired authentication tokens` (not `Handling expired authentication tokens`)
   * `Fix memory leak in WebSocket listener` (not `Fixed memory leak...`)
2. **Capitalize the Subject Line:** Start with a capital letter.
3. **No Trailing Period in the Subject:** Do not end the first line with a period.
4. **Length Discipline:** Keep the subject under 50-72 characters.
5. **Blank Line Before Body:** Always separate the subject line from the body with a blank line.

---

## 3. High-Quality Examples by Change Category

### Feature Addition
* **Good:** `Add Google OAuth2 login flow`
* **Good:** `Support CSV export for monthly billing reports`
* **Good:** `Allow users to invite teammates via email link`
* **Bad:** `feat(auth): implement comprehensive Google OAuth2 authentication flow with token validation` (Robotic, bloated)
* **Bad:** `Add login` (Too brief, lacks context)

### Bug Fixes
* **Good:** `Prevent crash when parsing malformed JSON payloads`
* **Good:** `Handle expired JWT tokens during background sync`
* **Good:** `Correct timezone offset in calendar event reminders`
* **Bad:** `Fix bug` (Completely uninformative)
* **Bad:** `fix: resolved issue with token expiration where user was logged out unexpectedly` (Grammatically awkward, verbose)

### Performance & Optimization
* **Good:** `Cache customer profile queries in Redis`
* **Good:** `Avoid redundant DOM re-renders in order list table`
* **Good:** `Batch database queries in notification dispatcher`
* **Bad:** `perf: optimize query` (Vague)

### Refactoring
* **Good:** `Extract payment gateway logic into dedicated service`
* **Good:** `Simplify date formatting helper functions`
* **Good:** `Move database connection pool initialization to startup lifecycle`
* **Bad:** `refactor: clean up code` (Vague, lacks target)

### Configuration and Infrastructure
* **Good:** `Add rate limiting configuration for public API routes`
* **Good:** `Update Dockerfile to use multi-stage Node.js 20 build`
* **Good:** `Increase maximum file upload size to 25MB in Nginx config`

### Documentation and Tests
* **Good:** `Document webhook signature verification with HMAC-SHA256`
* **Good:** `Add edge case unit tests for invoice tax calculation`
* **Good:** `Update local setup instructions for PostgreSQL 16`

---

## 4. Writing Effective Commit Bodies

Not every commit needs a multi-paragraph body. Small, self-evident commits (`Add missing index to orders.user_id`) are complete on their own.

Write a body when:
* **The "why" is not obvious from the diff:**
  ```text
  Set default timeout to 15 seconds for external webhook requests

  Third-party payment gateways were occasionally hanging indefinitely during
  upstream outages, exhausting the worker thread pool. A 15-second timeout
  allows workers to fail fast and retry asynchronously.
  ```
* **Alternative approaches were rejected:**
  ```text
  Use in-memory LRU cache for tenant permission lookups

  Considered storing permissions in JWT claims, but that would delay
  immediate revocation when an administrator downgrades a user's role.
  ```
* **There are non-obvious side effects or migration steps:**
  ```text
  Rename order status PENDING to AWAITING_PAYMENT

  Existing database records are migrated via migration 0042. External webhook
  consumers will need to update their filter payloads accordingly.
  ```

---

## 5. Respecting Repository-Specific Standards

When does an agent switch away from natural messages to Conventional Commits or ticket-scoped formats?

1. **Explicit Repository Configuration:**
   * An existing `commitlint.config.js` or `.commitlintrc.json` enforces `@commitlint/config-conventional`.
   * `CONTRIBUTING.md` or `AGENTS.md` specifically mandates `feat:`, `fix:`, or `PROJ-123:` format.
2. **Consistent Git History Precedent:**
   * If `git log -n 10 --oneline` reveals 100% adherence to Conventional Commits:
     ```text
     a1b2c3d feat(billing): add stripe webhook handler
     e4f5g6h fix(auth): refresh expired session cookie
     i7j8k9l chore(deps): bump vite from 5.1.0 to 5.2.0
     ```
     Then adapt and match the existing repository conventions!

In the absence of explicit rules or uniform Conventional Commit history, **always use clean, natural developer phrasing**.
