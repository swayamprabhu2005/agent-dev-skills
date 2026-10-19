# Example 06: Improving a Vague Prompt (Mode F)

---

## 1. User Invocation

```text
/context-matrix improve Make our authentication faster and add google login.
```

---

## 2. Mode & Framework Selected

* **Mode:** Mode F (`improve`)
* **Underlying Framework:** `CLARITY`
* **Selection Rationale:** Transforms an underspecified prompt into a high-fidelity engineering specification while strictly preserving the user's intent.

---

## 3. Ambiguities & Missing Requirements Identified

* **Ambiguity 1 (Authentication):** What does "faster" mean? Hash algorithm iteration tuning? Token verification caching? Database session lookup reduction?
* **Ambiguity 2 (Google Login):** Which OAuth flow? OpenID Connect (OIDC) with PKCE? Client-side popup token or server-side authorization code grant?
* **Missing Constraints:** No error handling requirements, no session persistence definitions, no backward compatibility constraints for existing password users.

---

## 4. Resulting Improved Prompt

```markdown
**Context:** We have a web application running on Node.js 20 with Express, Prisma ORM, and PostgreSQL. User authentication currently relies on server-side database lookups for session IDs on every request, creating a 45ms latency overhead.
**You:** Senior Identity and Security Engineer.
**Ask:**
1. Optimize authentication latency by migrating session verification to stateless JWT tokens signed with RS256, verified locally without database queries.
2. Implement Google OAuth 2.0 / OpenID Connect login alongside existing password authentication.
**Rules:**
1. Do not break existing email/password login credentials.
2. Link incoming Google accounts to existing user records if the verified email matches.
3. Access tokens must expire in 15 minutes; refresh tokens must be stored in HTTP-only, Secure, SameSite=Strict cookies with automatic rotation.
4. Do not use external authentication services like Auth0 or Firebase Auth; implement using official Google API client libraries.
**Input:**
- Existing User schema in `prisma/schema.prisma`.
- Current authentication middleware in `src/middleware/auth.ts`.
**Target:**
- Updated Prisma schema with `googleId` optional field.
- Google OAuth callback controller in `src/controllers/oauth.ts`.
- JWT generation and verification utilities in `src/utils/jwt.ts`.
- Jest integration test suite verifying Google callback token exchange and account linking.
```

---

## 5. Key Improvements Explained to User

* **Quantified "Faster":** Replaced vague speed desire with stateless local JWT signature verification (0ms database overhead).
* **Specified OAuth Mechanism:** Enforced server-side authorization code exchange with OIDC and automated account linking.
* **Hardened Security Rules:** Mandated HTTP-only cookies, token rotation, and 15-minute expirations.
* **Concrete Deliverables:** Specified exact file paths and integration tests.
