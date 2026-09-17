# Commit Architecture Worked Scenarios

This reference provides a summary index of the 12 real-world scenarios detailing how Commit Architect plans, sequences, stages, and authors commits across various software engineering situations.

For the exhaustive step-by-step breakdown of each scenario, consult the full case studies in the [examples/](../../examples/) directory.

---

## Scenario Index

| # | Scenario | Core Architectural Challenge | Recommended Commit Slices |
|---|:---|:---|:---|
| **01** | [New Feature](../../examples/01-new-feature.md) | Large multi-file capability (OAuth login) | Config → Service → Router → UI → Integration tests |
| **02** | [Bug Fix](../../examples/02-bug-fix.md) | Fixing a race condition in payment checkout | Regression test + Minimal fix bundled together |
| **03** | [Database Migration](../../examples/03-database-migration.md) | Altering existing schema with live production data | Backward-compatible schema migration → Model & Service update → Deprecation cleanup |
| **04** | [Backend + Frontend](../../examples/04-backend-frontend.md) | Full-stack user profile update | Backend API & contract first → Frontend consumption second |
| **05** | [Refactoring](../../examples/05-refactoring.md) | Feature requires preliminary code extraction | Pure refactor commit (zero behavior change) → Feature commit |
| **06** | [Unrelated Changes](../../examples/06-unrelated-changes.md) | Pre-existing dirty tree + multiple independent tasks | Preserving user edits; distinct commits for each independent fix |
| **07** | [Tests](../../examples/07-tests.md) | When tests belong together vs separate suites | Unit tests accompany code; broad end-to-end suites separate |
| **08** | [Documentation](../../examples/08-documentation.md) | Updating guides, OpenAPI specs, and READMEs | Inline docstrings with code; large user manual updates separate |
| **09** | [Configuration](../../examples/09-configuration.md) | Environment variables, docker, and rate limits | Base config & defaults first; service consumption alongside |
| **10** | [Dependency Update](../../examples/10-dependency-update.md) | Upgrading major library version with breaking API | Lockfile/manifest update + required API adaptations in one coherent commit |
| **11** | [Conventional Commit Repo](../../examples/11-conventional-commit-repo.md) | Project explicitly mandates Conventional Commits | Adapting to `feat:`, `fix:`, `chore:` and repo scopes |
| **12** | [Non-Conventional Repo](../../examples/12-non-conventional-repo.md) | Standard repository with human developer prose | Natural, concise, imperative developer messages without prefixes |
