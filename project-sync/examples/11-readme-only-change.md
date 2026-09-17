# Example 11: README-Only Change (Adding Verbose Flag)

This example illustrates an iteration where only `README.md` requires an update while `.gitignore` remains unchanged.

---

## 1. Implementation Change
Added a `-v` / `--verbose` command-line flag to the repository's CLI migration tool:
* Updated `src/cmd/migrate.go` to parse `-v` for debug query logging.
* Added unit tests verifying logger output level.

## 2. Determination of Documentation Impact
* `README.md` documents the `migrate` CLI tool and lists supported flags under `## Database Migrations`.
* The `-v` flag is a useful user-facing tool option.
* **Decision:** Add `-v, --verbose` to the flag description list in `README.md`.

## 3. Determination of Ignore-Rule Impact
* No new files or directories were created.
* Existing `.gitignore` already covers Go build binaries.
* **Decision:** No changes required for `.gitignore`.

## 4. Resulting Modifications

### `README.md` (Diff):
```diff
 ### Migration Commands
 \`\`\`bash
 # Run pending migrations
 db-migrate up
 \`\`\`

 #### Flags
+- `-v, --verbose`: Enable verbose debug logging of executed SQL statements
 - `--dry-run`: Preview SQL statements without executing
```

## 5. Completion Summary
```text
Implementation complete.

Implemented:
- Added -v/--verbose flag to db-migrate command for SQL query logging

Project synchronization:
- README.md — Updated: Documented -v/--verbose flag in Migration Commands
- .gitignore — No changes required: Build output already ignored

Validation:
- Tests: 15 passed (go test ./...)

Iteration complete.
```
