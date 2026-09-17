# Safety & Preservation Rules Reference Guide

This guide establishes the safety protocols for safeguarding manual user edits, handling pre-existing dirty trees, and verifying synchronization diffs.

---

## 1. The Pre-Sync State Audit

Before altering `README.md` or `.gitignore`, the agent must inspect their current status in Git:

```bash
git status --porcelain README.md .gitignore
git diff -- README.md .gitignore
```

### Three Safety Scenarios:

| State | Diagnosis | Protocol |
| :--- | :--- | :--- |
| **Clean** | Neither file has uncommitted modifications. | Proceed with standard surgical synchronization. |
| **User Modified** | The user has uncommitted edits in `README.md` or `.gitignore`. | **PRESERVE ALL USER EDITS.** Append or merge new items without touching their lines. |
| **Untracked** | The file is completely new in the repository. | Verify whether creation is justified by project context. |

---

## 2. Preserving User Voice and Structure

Never overwrite a human developer's intentional choices:

1. **Custom Badges & Logos:**
   If the user placed custom SVG badges, donation links, or company banners at the top of the README, never delete or re-order them.
2. **Hand-Crafted Comments:**
   If `.gitignore` contains comments like `# Custom ignore for internal QA tool`, preserve both the comment and the associated pattern.
3. **Markdown Syntax Style:**
   If the README uses ATX headers (`# Title`), do not convert them to Setext (`Title\n===`). If list items use `*`, do not convert them to `-`.

---

## 3. Conflict Resolution Heuristics

If the user has modified a section of `README.md` that also requires synchronization (e.g., the user edited the "Configuration" table, and the agent's new feature also needs a new row in that table):

1. **Perform an additive merge:** Insert the new row while keeping the user's edits completely intact.
2. **Do not re-sort or normalize:** Leave the user's row ordering and spacing as written.
3. **If ambiguous:** If the user's edit contradicts the implementation (e.g., user wrote `PORT=8000` but implementation hardcodes `9000`), report the discrepancy in the completion summary rather than silently overwriting the user's text.

---

## 4. Final Diff Verification

Before delivering the completion summary, the agent must inspect the exact diff it produced:

```bash
git diff -- README.md .gitignore
```

Checklist:
* [ ] Did I modify only the lines directly related to the new capability?
* [ ] Did I avoid changing whitespace or formatting in unaffected sections?
* [ ] Does the modified text accurately describe the new behavior?

---

## 5. Absolute Prohibition on Silent Deletion & The Quarantine Rule

* **Never Silently Delete Files:** The agent must NEVER delete files from the repository working tree under the assumption that they are "unneeded" or "temporary". Deleting files without explicit human instruction risks irreversible loss of user investigation, test fixtures, or in-progress code.
* **Quarantine Instead of Deletion:** When genuine agent-created temporary artifacts are identified (e.g., ad-hoc test scripts, data dumps), move them to `.agent/scratch/`.
* **Clean Ignore Configuration:** Add `.agent/scratch/` to `.gitignore` so temporary files remain untracked without polluting `.gitignore` with individual file paths.
* **Transparent Reporting:** Report all quarantined files in the completion summary so the developer can review or remove them at their discretion.
* [ ] Are all surrounding user comments and badges preserved?
