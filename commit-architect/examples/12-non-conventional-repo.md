# Example 12: Non-Conventional Repository (Natural Developer Language)

This example demonstrates the standard behavior of Commit Architect on a standard software repository where developers communicate in natural, concise, professional developer language.

---

## 1. The Task
"Add email validation and strip leading/trailing whitespace when users update their profile email address."

## 2. Repository State & Discovery
* Inspection reveals:
  * No `commitlint`, no `cz-cli`, no `.commitlintrc`.
  * `CONTRIBUTING.md` contains standard coding guidelines but no commit message format restrictions.
  * `git log -n 5 --oneline` shows:
    ```text
    9a8b7c6 Allow downloading invoice PDFs from customer billing page
    5d4e3f2 Fix rounding error in quarterly sales tax summary
    1a2b3c4 Upgrade Postgres driver to 3.2.0
    ```
* **Decision:** The repository uses natural programmer-style messages. Commit Architect applies its default natural style without any Conventional Commit prefixes.

## 3. Discovered Work
1. Update `normalizeEmail()` helper to trim whitespace and lowercase domains.
2. Update profile update controller to validate email against RFC 5322 regex.
3. Add unit tests covering invalid formats (missing `@`, trailing spaces, unicode whitespace).

## 4. Proposed Commit Plan
* **Single Cohesive Commit:**
  `Trim whitespace and validate email format during profile updates`

## 5. Implementation Sequence
1. Update `src/utils/email.py` and `src/views/profile.py`.
2. Add unit tests in `tests/test_email_normalization.py`.
3. Run tests. Verify all pass.
4. Review staged diff (`git diff --cached`).
5. Validate message:
   ```bash
   python scripts/verify-commit.py -m "Trim whitespace and validate email format during profile updates"
   ```
6. Commit.

## 6. Final Commit Message
```text
Trim whitespace and validate email format during profile updates

Strip leading and trailing whitespace from submitted email addresses before
running syntax validation. Reject invalid formats with an explicit 400 error
rather than allowing database write failures.
```

## 7. Why This Message Format is Used
* **Professional Harmony:** The message blends seamlessly into the existing Git log, matching the tone and style of human engineers on the project.
* **Clarity:** It clearly explains what changed and why, without forced prefixes or artificial taxonomies.

## 8. What the Agent Should Avoid
* ❌ Forcing `feat(profile): ...` or `fix(user): ...` when human maintainers do not use them.
* ❌ Adding vague messages like `Update email handling` or `Fix profile bugs`.
* ❌ Generating robotic AI templates like `Enhance profile email validation with robust normalization logic`.
