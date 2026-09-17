# README Synchronization Reference Guide

This guide defines the principles, boundaries, and editing mechanics for synchronizing a project's `README.md` with implementation changes.

---

## 1. The Core Objective

The purpose of README synchronization is to keep the project's primary human entryway accurate, honest, and up-to-date with the codebase.

The goal is **not** to inflate documentation or log every commit in the README. The goal is to ensure that a developer cloning the project at this exact commit can follow the README and successfully understand, configure, install, run, and test the software.

---

## 2. When to Update README.md

Update `README.md` only when an implementation change affects:

| Category | Example Trigger | What to Update |
| :--- | :--- | :--- |
| **Prerequisites** | Upgraded from Node 18 to Node 20; added Redis requirement | "Prerequisites" or "Requirements" section |
| **Installation** | Added new optional peer dependency or changed package manager | "Installation" / "Getting Started" commands |
| **Environment Variables** | Added `STRIPE_SECRET_KEY` or renamed `DATABASE_URL` | Configuration table or `.env` example block |
| **CLI Commands** | Added `--export-csv` flag or new npm script `npm run db:seed` | "Usage" or "Available Scripts" section |
| **Public API / Routes** | Added `/api/v1/webhooks` endpoint or changed response format | High-level API overview (if documented in README) |
| **Feature List** | Added Google OAuth2 or removed legacy XML export | "Features" bullet list |
| **Project Structure** | Reorganized monorepo packages or added a new core service | Directory overview diagram (if present in README) |

---

## 3. When NOT to Update README.md

Leave `README.md` completely untouched when:
* **Internal Bug Fixes:** Correcting a null-pointer exception, fixing an off-by-one loop, or resolving an internal race condition.
* **Refactoring:** Moving code between internal classes, extracting helper utilities, or cleaning up type definitions.
* **Test Suite Updates:** Adding unit tests, upgrading mock fixtures, or increasing test coverage.
* **Internal Performance Tuning:** Optimizing SQL queries with indexes, adding memory caches that don't require external configuration.
* **Cosmetic Changes:** Fixing internal code formatting, lint errors, or variable names.

---

## 4. The Minimal Targeted Edit Principle

When an update is required, make the surgical minimum change:

### Anti-Pattern: The Wholesale Rewrite
* ❌ An agent re-formats the entire README, re-words 5 paragraphs of introduction, swaps bullet styles from `*` to `-`, and re-orders headings simply because it added one environment variable.
* **Why it fails:** Generates a 200-line diff for a 1-line conceptual change, obliterates `git blame`, and annoys human maintainers.

### Best Practice: Targeted Surgical Insertion
* ✅ Locate the exact section (e.g., "Environment Variables" table).
* ✅ Add the single new row matching the table's existing formatting.
* ✅ Leave all surrounding text, headers, and spacing completely undisturbed.

---

## 5. Preserving Human Maintainer Style

Maintain absolute fidelity to the repository's established conventions:
* **Tone:** If the existing README is terse and technical, keep your additions terse and technical. If it is friendly and tutorial-oriented, match that style.
* **Badges & Header Blocks:** Never remove, reposition, or alter CI badges, sponsor links, license shields, or project logos.
* **Formatting Syntax:** If the project uses Markdown tables for configuration, use Markdown tables. If it uses fenced code blocks, use fenced code blocks.

---

## 6. Handling Tool-Generated Sections

Many enterprise and open-source repositories use automated documentation generators (e.g., TypeDoc, Swagger-to-Markdown, terraform-docs) to maintain portions of their README:

```markdown
<!-- AUTO-GENERATED-DOCS:START -->
Do not edit this block directly. Run `npm run docs:generate`.
...
<!-- AUTO-GENERATED-DOCS:END -->
```

**Rule for Generated Sections:**
1. Never manually edit the text inside automated generation markers.
2. If the project provides a generation command (e.g., `npm run generate-docs` or `make docs`), execute that command as part of the iteration.
3. If no automated script is available, update the underlying source docstring and notify the user in the completion summary.
