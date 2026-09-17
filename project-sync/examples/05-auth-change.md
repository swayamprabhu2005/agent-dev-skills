# Example 05: Authentication Change (Google OAuth2 Integration)

This example illustrates synchronizing environment variables and setup instructions when a new authentication provider is integrated.

---

## 1. Implementation Change
Added Google OAuth2 login support to a Next.js application:
* Updated `auth.ts` to register `GoogleProvider`.
* Added `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` to `.env.example`.
* Created `/api/auth/callback/google`.

## 2. Determination of Documentation Impact
* `README.md` has an "Authentication Setup" section detailing how to configure authentication providers.
* Developers setting up the project locally must know that Google OAuth credentials are now needed.
* **Decision:** Add Google OAuth setup steps to `README.md` and list the required environment variables.

## 3. Determination of Ignore-Rule Impact
* Inspecting git status reveals `.env.local` was modified locally during manual testing.
* Checking `.gitignore` confirms `.env*.local` is already ignored.
* **Decision:** No changes required for `.gitignore`.

## 4. Resulting Modifications

### `README.md` (Diff):
```diff
 ### Environment Variables
 | Variable | Description | Required |
 | :--- | :--- | :--- |
 | `NEXTAUTH_SECRET` | Used to encrypt the NextAuth.js JWT | Yes |
 | `NEXTAUTH_URL` | Canonical URL of your site | Yes |
+| `GOOGLE_CLIENT_ID` | OAuth Client ID from Google Cloud Console | Optional (if using Google Login) |
+| `GOOGLE_CLIENT_SECRET` | OAuth Client Secret from Google Cloud Console | Optional (if using Google Login) |
```

## 5. Completion Summary
```text
Implementation complete.

Implemented:
- Added Google OAuth2 authentication provider
- Added OAuth callback route and session token mapping

Project synchronization:
- README.md — Updated: Documented GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET environment variables
- .gitignore — No changes required: .env.local already ignored

Validation:
- Tests: 12 passed (npm test)
- Build: Successful (npm run build)

Iteration complete.
```
