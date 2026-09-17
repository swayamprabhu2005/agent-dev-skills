# Dependency Ordering in Commit Architecture

When breaking a large software task into a series of logical commits, the sequence in which those commits are ordered is critical. Every intermediate commit should, whenever feasible, leave the repository in a compiling, runnable, and test-passing state.

---

## 1. The Principle of Dependency Flow

Changes should flow from foundational, low-level building blocks to high-level consumers:

```text
Foundations & Configurations
           ↓
Database Schemas & Data Contracts
           ↓
Core Domain & Business Services
           ↓
API Routers & Controllers
           ↓
User Interface & Presentation Layer
           ↓
End-to-End Tests & Integration Suites
           ↓
Documentation & Release Notes
```

---

## 2. Typical Layered Sequencing Patterns

### Scenario A: Adding a Complete Feature (Full Stack)
1. **Commit 1 (Configuration & Dependencies):** Add required third-party libraries and environment variable declarations in `.env.example`.
2. **Commit 2 (Data Layer & Models):** Define database models, migrations, and repository access methods (along with schema unit tests).
3. **Commit 3 (Domain Service):** Implement business logic service methods and unit tests.
4. **Commit 4 (API Endpoints):** Expose HTTP or RPC endpoints, request validation schemas, and controller tests.
5. **Commit 5 (Client / UI):** Implement frontend components, state management, and API integration.
6. **Commit 6 (Documentation):** Update OpenAPI specs, API docs, or README guides if extensive.

### Scenario B: Database Migration with Application Code
When schema changes alter existing production tables:
* **Commit 1 (Expand Schema):** Add new column or table with migration script (backward-compatible; code still works with or without it).
* **Commit 2 (Dual Write / Update Logic):** Update application services to populate and read the new structure, along with regression tests.
* **Commit 3 (Contract Schema / Cleanup):** Deprecate old fields or remove legacy columns if required.

### Scenario C: Refactoring Before New Feature Work
* **Commit 1 (Structural Refactoring):** Extract shared helpers, rename abstractions, or modularize files. **No change in runtime behavior.** Existing tests pass.
* **Commit 2 (New Feature Implementation):** Implement the requested feature using the newly refactored foundation. Includes new tests.

---

## 3. The Bisectability Guarantee

Every commit in your sequence should satisfy the **Bisectability Guarantee**:

> *"If `git bisect` lands on this commit in the future, the test suite will run without crashing due to missing dependencies, unimported symbols, or unmatched schema changes."*

### Rules for Bisectability:
* Never commit code that imports a module that has not yet been committed.
* Never commit a migration that depends on a database driver that has not yet been added to `requirements.txt` or `package.json`.
* Never commit a frontend component that imports a mock or API client that does not yet exist.

---

## 4. Resolving Chicken-and-Egg Scenarios

Sometimes two components appear mutually dependent. For example, a service method needs a new interface type, and the interface type is only used by that service.

### Resolution:
* **Bundle together:** If separating them would leave one commit failing compilation (e.g., missing type definition), bundle the interface definition and its primary implementation in the **same commit**.
* **Do not artificially split:** Never split an interface declaration and its sole implementation into two commits if the interface alone does not compile or cannot be tested independently.

---

## 5. Ordering Tests

* **Unit Tests:** Should be committed **alongside the code they test** in the same commit. This proves that the new logic works at the exact moment it is introduced.
* **Integration and E2E Tests:** When a suite tests the interaction between backend APIs and frontend UI, place it in a commit **after both the backend and frontend slices exist**, or bundle it with the final consumer layer.
