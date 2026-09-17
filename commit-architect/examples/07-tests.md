# Example 07: Tests (Companion Tests vs. Dedicated Test Suites)

This example explores the boundary rules for test placement: when tests belong in the same commit as implementation code, and when a dedicated test commit is warranted.

---

## 1. The Principle of Companion Tests
In general software engineering, **unit and component tests should accompany the code they test in the same commit**.

### Why Companion Tests are Standard:
1. **Verifiable Correctness:** A reviewer can inspect the code on the left and the tests on the right in the same diff to verify that edge cases are covered.
2. **Bisectability:** If tests are added in a later commit, a `git bisect` run landing on the implementation commit cannot verify that the implementation is bug-free.
3. **Prevention of Broken Intermediate States:** Committing tests before implementation (unless strictly doing TDD check-ins on personal branches) creates failing commits on shared branches.

---

## 2. Case A: Companion Tests (Default Pattern)
* **Task:** "Add token bucket rate limiter to API middleware."
* **Files:**
  * `src/middleware/rate_limiter.py`
  * `tests/unit/test_rate_limiter.py`
* **Commit Plan:** 1 Commit
* **Commit Message:**
  ```text
  Add token bucket rate limiter middleware

  Implement in-memory token bucket algorithm for throttling burst traffic.
  Includes unit tests verifying refill rates, burst allowances, and HTTP 429
  rejection.
  ```

---

## 3. Case B: When Separate Test Commits ARE Appropriate

There are specific, valid circumstances where a separate test commit is the right architectural choice:

### 1. Retroactive Test Coverage for Existing Legacy Code
* **Task:** "Add test coverage for the legacy order calculation service before we refactor it next sprint."
* **Files:** `tests/unit/test_legacy_order_service.py` (No application code changed).
* **Commit Message:**
  ```text
  Add unit tests for legacy order calculation service

  Characterize existing discounts, coupon codes, and sales tax edge cases
  to establish regression protection prior to service refactoring.
  ```

### 2. End-to-End or Stress / Load Test Suites
* **Context:** An entire multi-commit feature (auth, billing, dashboard) was implemented across multiple commits. A comprehensive Cypress/Playwright suite tests the cross-system user journey.
* **Files:** `tests/e2e/onboarding_journey.spec.ts`
* **Commit Message:**
  ```text
  Add end-to-end onboarding journey test suite

  Cover complete signup, workspace creation, and first project deployment
  flows using Playwright.
  ```

### 3. Test Infrastructure and Harness Upgrades
* **Task:** "Migrate test runner from Jest to Vitest."
* **Files:** `vitest.config.ts`, `package.json`, test helper setups.
* **Commit Message:**
  ```text
  Migrate test runner from Jest to Vitest

  Update configuration, test mocks, and setup files for native ESM execution.
  All 142 existing unit tests pass without assertion changes.
  ```

---

## 4. What the Agent Should Avoid
* ❌ Mechanically creating `Add feature X` followed immediately by `Add tests for feature X` as two tiny commits when both could have been developed and reviewed together.
* ❌ Submitting code changes with no tests when test files already exist in the repository for that component.
