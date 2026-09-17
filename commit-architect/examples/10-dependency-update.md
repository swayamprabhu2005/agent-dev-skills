# Example 10: Dependency Update (Major Library Upgrade with Breaking API)

This example illustrates how dependency upgrades—especially major version updates that introduce breaking changes—should be structured and committed.

---

## 1. The Task
"Upgrade axios from version 0.27 to 1.7 in the web application."

## 2. Repository State
* React / TypeScript web application.
* Existing package: `axios` 0.27.2.
* Breaking change: Axios 1.x changed AxiosError type exports, response interception error handling, and default serialization of FormData.

## 3. Discovered Work
1. Update `package.json` to `"axios": "^1.7.0"`.
2. Run `npm install` to update `package-lock.json`.
3. Update `src/api/client.ts`: adapt to modern `isAxiosError` type guard and new header types.
4. Update `src/api/upload.ts`: adjust FormData payload headers to match Axios 1.x automatic boundary headers.
5. Run test suite: `npm test` and `npm run build`.

## 4. Dependencies Between Work Units
* The manifest (`package.json`), lockfile (`package-lock.json`), and code adaptations in `client.ts` / `upload.ts` **MUST remain in the exact same commit**.
* If you commit `package.json` alone, the project fails to compile (type errors with the old code).
* If you commit code adaptations without upgrading the dependency, the old Axios version throws runtime errors.

## 5. Proposed Commit Plan
* **Single Cohesive Commit:**
  `Upgrade axios to 1.7.0 and adapt error handling and upload headers`

## 6. Implementation Sequence
1. Run `npm install axios@^1.7.0`.
2. Inspect compiler errors (`npm run typecheck`).
3. Update `src/api/client.ts` and `src/api/upload.ts` to satisfy new types and behavior.
4. Run full test suite and build. Confirm zero regressions.
5. Stage `package.json`, `package-lock.json`, `src/api/client.ts`, and `src/api/upload.ts`.
6. Commit.

## 7. Final Commit Message
```text
Upgrade axios to 1.7.0 and adapt error handling and upload headers

Bump axios from 0.27.2 to 1.7.4 in package.json and lockfile.
Adapt custom HTTP client to modern isAxiosError type guard and remove
redundant manual multipart/form-data boundary headers in upload service.
```

## 8. Why These Boundaries Make Sense
* **Bisectability Guaranteed:** At no point does the repository contain a broken build where the package version and the consuming code disagree.
* **Reviewability:** The reviewer sees the version bump and the exact API adjustments required by that bump in one unified diff.

## 9. What the Agent Should Avoid
* ❌ Committing `package.json` without updating the lockfile (`package-lock.json`).
* ❌ Making a separate commit for `Bump axios in package.json` and a second commit for `Fix type errors from axios upgrade`.
* ❌ Running opportunistic `npm update` and upgrading 40 other unrelated packages at the same time.
