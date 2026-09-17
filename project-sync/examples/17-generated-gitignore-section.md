# Example 17: Generated .gitignore Section (Framework Managed Blocks)

This example illustrates how Project Sync respects framework-managed blocks inside `.gitignore` and safely places custom project rules outside of those zones.

---

## 1. Implementation Change
Configured a new end-to-end test framework (Cypress) in a Next.js web application.
* Running `npx cypress run` creates local screenshots and video recordings in `cypress/videos/` and `cypress/screenshots/`.

## 2. Working Tree & `.gitignore` Inspection
Inspecting `.gitignore` reveals a framework-managed template:
```gitignore
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem
```

## 3. Determination of Documentation Impact
* Added `npm run test:e2e` to `package.json`.
* **Decision:** Add `npm run test:e2e` to the Available Scripts section in `README.md`.

## 4. Determination of Ignore-Rule Impact
* `cypress/screenshots/` and `cypress/videos/` are high-volume binary test artifacts created locally that must not be checked into Git.
* **Safety Principle:** Do not tamper with or edit lines inside the `# next.js` or `# dependencies` framework blocks.
* **Decision:** Add a clearly commented `# Cypress / E2E Testing` block at the bottom of the file.

## 5. Resulting Modifications

### `.gitignore` (Diff):
```diff
 # misc
 .DS_Store
 *.pem
+
+# Cypress / E2E Testing
+cypress/videos/
+cypress/screenshots/
```

## 6. Completion Summary
```text
Implementation complete.

Implemented:
- Configured Cypress end-to-end testing suite
- Added npm run test:e2e script

Project synchronization:
- README.md — Updated: Documented npm run test:e2e in Available Scripts
- .gitignore — Updated: Added cypress video and screenshot directories (preserved Next.js framework blocks)

Validation:
- Tests: E2E smoke test passed (npm run test:e2e)

Iteration complete.
```
