# Example 14: Repository with Pre-Existing README Edits

This example demonstrates how Project Sync handles a situation where the user already has unstaged manual edits in `README.md` before the synchronization step runs.

---

## 1. Implementation Change
Added an optional Slack webhook notification URL setting (`SLACK_WEBHOOK_URL`) to alert the team when a deploy finishes:
* Added environment variable handling in `src/notifier.py`.
* Added `SLACK_WEBHOOK_URL` to `.env.example`.

## 2. Working Tree Audit
Running `git status --porcelain` reveals:
```text
 M README.md
 M src/notifier.py
 M .env.example
```
Inspecting `git diff README.md` shows that the human developer was in the middle of writing a new "Troubleshooting FAQ" section at the bottom of the document:
```diff
+## Troubleshooting FAQ
+### Why is port 5432 already in use?
+If you see a port collision, check running Docker containers...
```

## 3. Determination of Documentation Impact
* The Slack webhook setting needs to be documented in the "Configuration" table.
* The human developer's "Troubleshooting FAQ" section must be **strictly preserved**.
* **Decision:** Perform an additive insertion into the Configuration table in the middle of the document. Do not disturb the developer's unstaged FAQ section at the bottom.

## 4. Resulting Modifications

### `README.md` (Additive Insertion):
```diff
 | Variable | Default | Description |
 | :--- | :--- | :--- |
 | `PORT` | `8080` | HTTP listener port |
+| `SLACK_WEBHOOK_URL` | None | Optional Slack incoming webhook for deployment alerts |
 | `LOG_LEVEL` | `info` | Application logging level |
```
*(The user's unstaged `## Troubleshooting FAQ` section remains intact below).*

## 5. Completion Summary
```text
Implementation complete.

Implemented:
- Added Slack webhook deployment notification handler
- Updated .env.example with SLACK_WEBHOOK_URL

Project synchronization:
- README.md — Updated: Added SLACK_WEBHOOK_URL to Configuration table (preserved unstaged user edits in Troubleshooting section)
- .gitignore — No changes required: Existing rules remain accurate

Validation:
- Tests: 21 passed (pytest)

Iteration complete.
```
