# Example 04: Backend + Frontend (User Notification Preferences)

This example illustrates how architectural dependencies between backend API endpoints and frontend user interfaces dictate clean commit boundaries.

---

## 1. The Task
"Implement a notification preferences center allowing users to toggle email, SMS, and push alerts."

## 2. Repository State
* Monorepo: `backend/` (Go / Gin API) and `frontend/` (React / TypeScript / Vite).
* Existing commit style: Natural developer language.

## 3. Discovered Work
1. **Backend:**
   * Add database table `user_notification_preferences`.
   * Add HTTP GET `/api/v1/users/me/notifications` and PATCH `/api/v1/users/me/notifications`.
   * Unit and HTTP handler tests for backend logic.
2. **Frontend:**
   * Generate or write TypeScript API client interface for preferences payload.
   * Create `NotificationSettingsForm.tsx` component with toggle switches and optimistic UI updates.
   * Add component tests in Vitest.

## 4. Dependencies Between Work Units
* The backend API contracts and endpoint handlers must be defined before the frontend client can connect to them.
* In a monorepo, separating backend and frontend commits allows:
  * Backend team members to review the Go code and SQL queries.
  * Frontend engineers to review React state, accessibility, and CSS styling.
  * Staged deployment if frontend and backend deploy via different CI/CD workflows.

## 5. Proposed Commit Plan
* **Commit 1:** Add user notification preferences API endpoints and database storage
* **Commit 2:** Add notification preferences settings page in frontend

## 6. Implementation Sequence
1. Implement the Go handler, database repository, and router in `backend/`.
2. Run Go tests: `go test ./...`. Verify all tests pass.
3. Stage `backend/` files and commit with Commit 1.
4. Implement the React component, API client, and tests in `frontend/`.
5. Run frontend tests: `npm test`. Verify green.
6. Stage `frontend/` files and commit with Commit 2.

## 7. Final Commit Messages
```text
Add user notification preferences API endpoints and storage

Expose GET and PATCH /api/v1/users/me/notifications with support
for email, SMS, and push notification toggles.
```

```text
Add notification preferences settings page in frontend

Render toggle switches for email, SMS, and push notifications with
optimistic updates and toast notifications on save error.
```

## 8. Why These Boundaries Make Sense
* **Clear Ownership & Reviewability:** Full-stack changes touching different languages (Go vs. TypeScript) and frameworks are cleanly isolated for relevant reviewers.
* **Bisectability:** Checking out Commit 1 provides a fully operational backend API without any half-finished UI code.

## 9. What the Agent Should Avoid
* ❌ Squashing Go backend logic, SQL migrations, and React JSX into a single mega-commit.
* ❌ Over-splitting the frontend into 4 tiny commits (`Add API client`, `Add CSS for toggle`, `Add form component`, `Add test for form`).
