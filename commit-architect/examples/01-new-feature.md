# Example 01: New Feature (OAuth2 Social Login)

This example illustrates how a large, multi-file feature implementation is architected into clean, reviewable, and stable logical commits.

---

## 1. The Task
"Add GitHub OAuth2 authentication to the application so users can sign in with their GitHub account."

## 2. Repository State
* Project: FastAPI / Python backend with SQLite database.
* Current branch: `main` (clean working tree).
* Existing commit style: Natural developer phrasing.
* Existing components: `User` model, email/password authentication service, auth router.

## 3. Discovered Work
Upon inspecting the codebase, adding GitHub OAuth2 requires:
1. Adding `httpx` to dependencies for async HTTP calls to GitHub's API.
2. Adding `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` configuration variables.
3. Updating the `User` database model to store an optional `github_id` and OAuth profile data.
4. Implementing a `GitHubOAuthService` that exchanges the callback code for an access token and queries user info.
5. Adding `/auth/github/login` and `/auth/github/callback` routes to the API router.
6. Adding integration unit tests with mocked GitHub API responses.
7. Updating the README / environment setup guide.

## 4. Dependencies Between Work Units
* Database schema (`github_id` column) must exist before the service attempts to query or update users by GitHub ID.
* Configuration variables must be loaded before the OAuth service initializes.
* The OAuth service and mockable client must exist before route handlers can call it.
* Router endpoints must exist before full integration route tests run.
* Documentation should reference confirmed configuration variables and endpoints.

## 5. Proposed Commit Plan
* **Commit 1:** Add GitHub OAuth configuration and httpx dependency
* **Commit 2:** Add github_id to User model with migration and schema tests
* **Commit 3:** Implement GitHub OAuth2 authentication service and token client
* **Commit 4:** Expose GitHub OAuth login and callback endpoints with route tests
* **Commit 5:** Update authentication setup documentation with GitHub OAuth instructions

## 6. Implementation and Validation Sequence
1. **Slice 1:** Update `pyproject.toml` and `config.py`. Run `pytest` to ensure config loads defaults. Stage and commit.
2. **Slice 2:** Add Alembic migration script and update `User` SQLAlchemy model. Run migration test. Stage and commit.
3. **Slice 3:** Create `src/services/github_oauth.py` and `tests/test_github_oauth.py`. Run tests. Stage and commit.
4. **Slice 4:** Add routes in `src/routers/auth.py` and `tests/test_auth_routes.py`. Run tests. Stage and commit.
5. **Slice 5:** Update `docs/auth-setup.md` and `README.md`. Stage and commit.

## 7. Final Commit Messages
```text
Add GitHub OAuth configuration and httpx dependency

Add github_id to User model with migration

Implement GitHub OAuth2 authentication service and client

Expose GitHub OAuth login and callback endpoints

Document GitHub OAuth application setup and environment variables
```

## 8. Why These Boundaries Make Sense
* **Bisectability:** Every intermediate commit builds and passes all tests. No commit imports an uncommitted module or refers to an unmigrated column.
* **Reviewability:** Reviewers can inspect the cryptographic and API security logic in Commit 3 independently from the HTTP routing in Commit 4.
* **Reversibility:** If the team decides to swap the OAuth provider or delay frontend rollout, individual layers can be adjusted without tearing apart a 500-line diff.

## 9. What the Agent Should Avoid
* ❌ Creating one monolithic commit: `Add GitHub OAuth authentication` touching 12 files.
* ❌ Over-splitting: Making a separate commit for `Add httpx to pyproject.toml` and another for `Add GITHUB_CLIENT_ID to config.py`.
* ❌ Smuggling unrelated work: Fixing unrelated lint errors in `User` model while adding `github_id`.
* ❌ Using artificial Conventional Commits on a project that doesn't use them: `feat(auth-oauth-github-api-router): add callback`.
