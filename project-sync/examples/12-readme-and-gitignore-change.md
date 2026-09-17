# Example 12: README and .gitignore Both Requiring Changes (SQLite Local Database)

This example illustrates an iteration where both `README.md` and `.gitignore` must be synchronized simultaneously.

---

## 1. Implementation Change
Added local SQLite database support as a zero-configuration fallback when PostgreSQL is unavailable:
* Added `DATABASE_TYPE` setting (`postgres` or `sqlite`).
* When `sqlite` is selected, the application creates and writes to `data/app.db`.
* Added `data/` directory with a `.gitkeep` to maintain directory structure.

## 2. Determination of Documentation Impact
* `README.md` previously mandated running a local PostgreSQL container.
* Developers can now run the app immediately with SQLite without installing or running Docker.
* **Decision:** Update the "Quickstart" and "Configuration" sections in `README.md` explaining SQLite zero-config development.

## 3. Determination of Ignore-Rule Impact
* Running the app with SQLite creates `data/app.db` and SQLite write-ahead log files (`data/app.db-wal`, `data/app.db-shm`).
* These files contain local machine state and must never be committed.
* **Decision:** Add SQLite database file patterns to `.gitignore`.

## 4. Resulting Modifications

### `README.md` (Diff):
```diff
 ## Quickstart
 \`\`\`bash
 # Install dependencies
 npm install

+# Run with zero-config SQLite (default for quick testing)
+DATABASE_TYPE=sqlite npm run dev
+
 # Or run with PostgreSQL
 docker compose up -d postgres
 npm run dev
 \`\`\`
```

### `.gitignore` (Diff):
```diff
 # Database Local Files
+*.db
+*.db-wal
+*.db-shm
+data/*.db
```

## 5. Completion Summary
```text
Implementation complete.

Implemented:
- Added zero-configuration SQLite driver fallback for local development
- Added database connection router in src/db/connection.ts

Project synchronization:
- README.md — Updated: Documented zero-config SQLite quickstart and DATABASE_TYPE option
- .gitignore — Updated: Added SQLite database and WAL file patterns

Validation:
- Tests: 48 passed across both SQLite and PostgreSQL adapters
- Build: Successful

Iteration complete.
```
