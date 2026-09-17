# Project Sync Worked Scenarios Index

This reference indexes the 17 real-world case studies detailing how Project Sync reconciles documentation and ignore rules across various software development situations.

For full, step-by-step breakdowns, consult the individual scenario files in the [examples/](../../examples/) directory.

---

## Scenario Index

| # | Scenario | Core Synchronization Challenge | README Action | .gitignore Action |
|---|:---|:---|:---|:---|
| **01** | [New Repo Init](../../examples/01-new-repo-init.md) | Fresh repository without existing files | Create minimal accurate README | Create stack-tailored .gitignore |
| **02** | [Existing Repo with README](../../examples/02-existing-repo-readme.md) | Standard repo with established layout | Surgical minimal insertion | No changes required |
| **03** | [Feature Addition](../../examples/03-feature-addition.md) | Added CSV data export feature | Add export command & flags | No changes required |
| **04** | [API Change](../../examples/04-api-change.md) | Added pagination parameters to API | Update API query docs | No changes required |
| **05** | [Auth Change](../../examples/05-auth-change.md) | Added Google OAuth2 authentication | Update setup & env variables | No changes required |
| **06** | [Config Change](../../examples/06-config-change.md) | Added Redis connection URL setting | Add Redis env var to table | No changes required |
| **07** | [New Generated Artifacts](../../examples/07-new-generated-artifacts.md) | Build generates `dist/bundles/` | Update build command | Add bundle dir to .gitignore |
| **08** | [New Temporary Artifacts](../../examples/08-new-temporary-artifacts.md) | Agent test scratchpad `temp.log` | No changes (clean up file) | Do NOT add to .gitignore |
| **09** | [Internal Refactor](../../examples/09-internal-refactor-no-impact.md) | Refactored internal cache service | No changes required | No changes required |
| **10** | [Gitignore-Only Change](../../examples/10-gitignore-only-change.md) | Added test coverage reporting | No changes required | Add `coverage/` to .gitignore |
| **11** | [README-Only Change](../../examples/11-readme-only-change.md) | Added `--verbose` flag to CLI | Document flag in README | No changes required |
| **12** | [README + Gitignore Change](../../examples/12-readme-and-gitignore-change.md) | Added SQLite local DB support | Document DB path config | Add `local.db` to .gitignore |
| **13** | [Neither Requiring Changes](../../examples/13-neither-requiring-changes.md) | Fixed null pointer in helper | No changes required | No changes required |
| **14** | [Pre-existing README Edits](../../examples/14-preexisting-readme-edits.md) | User has unstaged README changes | Additive merge (preserve edits) | No changes required |
| **15** | [Pre-existing Gitignore Edits](../../examples/15-preexisting-gitignore-edits.md) | User has unstaged ignore rules | No changes required | Additive merge (preserve edits) |
| **16** | [Generated README Section](../../examples/16-generated-readme-section.md) | API docs managed by TypeDoc | Run generator script | No changes required |
| **17** | [Generated Gitignore Section](../../examples/17-generated-gitignore-section.md) | Framework tool-managed block | No changes required | Append outside tool block |
