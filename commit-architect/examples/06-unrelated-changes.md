# Example 06: Unrelated Changes (Managing Pre-Existing Modifications)

This example illustrates how to safely handle repositories that already contain uncommitted edits from a human developer while performing assigned work.

---

## 1. The Task
"Fix the typo in the error message when an invalid zip code is submitted on checkout."

## 2. Repository State
Running `git status --porcelain` before beginning reveals:
```text
 M src/components/HeaderNavigation.tsx
 M src/styles/theme.css
?? scratchpad.txt
```
The human developer was in the middle of tweaking the header styling when they invoked the agent to fix the zip code typo.

## 3. Discovered Work
1. The zip code typo is in `src/validators/address.ts` and `locales/en.json`.
2. The modifications in `HeaderNavigation.tsx`, `theme.css`, and `scratchpad.txt` are completely unrelated to the zip code task.

## 4. Safety Guardrails & Principles
* **Golden Rule:** Never destroy, overwrite, or stage uncommitted user modifications.
* Under no circumstances run `git add .` or `git checkout -- .`.
* Stage only the files touched for the zip code fix.

## 5. Proposed Commit Plan
* **Single Targeted Commit:** `Correct invalid zip code error message in checkout validator`
  * Stage only `src/validators/address.ts` and `locales/en.json`.
  * Leave `HeaderNavigation.tsx`, `theme.css`, and `scratchpad.txt` completely untouched in the user's working tree.

## 6. Implementation Sequence
1. Update `src/validators/address.ts` and `locales/en.json`.
2. Run unit tests: `npm test src/validators/address.test.ts`.
3. Selectively stage target files:
   ```bash
   git add src/validators/address.ts locales/en.json
   ```
4. Verify staged changes:
   ```bash
   git diff --cached
   ```
   Confirm that only the 2 target files are staged and the header/theme files remain unstaged.
5. Commit.

## 7. Final Commit Message
```text
Correct invalid zip code error message in checkout validator

Fix typo "Inavlid zip code format" -> "Invalid zip code format" in validation
schema and English locale dictionary.
```

## 8. Why These Boundaries Make Sense
* **Preserves Human Work:** The developer's in-progress header work remains safe and intact in their working tree.
* **No Contamination:** The commit contains zero accidental lines from other active tasks.

## 9. What the Agent Should Avoid
* ❌ Running `git add .` and accidentally bundling the user's half-finished header refactor into the zip code commit.
* ❌ Running `git stash drop` or `git reset --hard` to "clean up" the workspace.
* ❌ Adding `scratchpad.txt` to the repository.
