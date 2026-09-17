# Example 03: Database Migration (Live Production Schema Migration)

This example illustrates the appropriate ordering and separation of schema migrations, application logic, tests, and data deprecation when modifying live database structures.

---

## 1. The Task
"Split the existing `full_name` column in the `users` table into `first_name` and `last_name` without interrupting live service."

## 2. Repository State
* Project: Ruby on Rails with PostgreSQL.
* Existing schema: `users.full_name` VARCHAR(255).
* 100,000+ active records in production.

## 3. Discovered Work
To migrate a live database safely using the Expand/Contract pattern:
1. **Expand Phase:** Add `first_name` and `last_name` nullable columns to `users` via migration.
2. **Backfill & Dual-Write:** Backfill existing rows via a background data migration task, and update the application `User` model to dual-write to both `full_name` and `first_name`/`last_name`.
3. **Switch Reads & Remove Legacy:** Switch all readers to use `first_name` and `last_name`, then drop the legacy `full_name` column in a subsequent release.

## 4. Dependencies Between Work Units
* The schema addition must be deployable independently before the application begins executing queries containing `first_name`.
* Backfill scripts and dual-write logic depend on columns existing.
* Dropping the old column can only happen after application code has completely ceased referencing `full_name`.

## 5. Proposed Commit Plan
* **Commit 1:** Add first_name and last_name columns to users table
* **Commit 2:** Support dual-writing to first_name, last_name, and full_name
* **Commit 3:** Add backfill task for populating user name columns
* **Commit 4:** Switch user profile readers to first_name and last_name

## 6. Implementation Sequence
1. Generate Rails migration adding `first_name` and `last_name` (nullable). Verify schema rollback and forward migration. Commit.
2. Update `app/models/user.rb` callbacks to synchronize names during writes. Add model unit tests. Commit.
3. Add `lib/tasks/backfill_user_names.rake` with batch processing (find_in_batches) and rake task tests. Commit.
4. Update profile serializers, views, and controller parameters. Update integration tests. Commit.

## 7. Final Commit Messages
```text
Add first_name and last_name columns to users table

Support dual-writing to first_name, last_name, and full_name in User model

Add batch rake task to backfill user first_name and last_name

Switch user views and serializers from full_name to first_name and last_name
```

## 8. Why These Boundaries Make Sense
* **Zero-Downtime Deployment:** In modern continuous delivery (CD) pipelines, Commit 1 can be deployed and migrated before Commit 2 is deployed.
* **Safe Rollbacks:** If a bug is detected during the backfill (Commit 3), it can be rolled back without reverting the database schema.
* **Review Isolation:** A DBA can review the migration in Commit 1 in 30 seconds without reading 200 lines of template view changes.

## 9. What the Agent Should Avoid
* ❌ Putting migration, data backfill, model callbacks, and view rewrites into a single commit.
* ❌ Dropping `full_name` in the same commit that adds `first_name` (instantly breaks running application servers during rolling deployment).
