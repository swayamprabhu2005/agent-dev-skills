# Incremental Blueprint Evolution & Implementation Drift

This guide specifies how Project Blueprint evolves specifications over time without full rewrites and how it handles architectural discoveries during implementation.

---

## 1. Incremental Evolution Workflow

Once an initial blueprint is approved (e.g., `version: 1`), subsequent feature requests or scope expansions must be handled incrementally:

```text
User Requests New Capability / Modification
                    ↓
[ 1. Impact Assessment ]
Identify which of the 5 documents are affected
                    ↓
[ 2. Targeted Clarification ]
Ask 1-2 focused questions about the delta
                    ↓
[ 3. Incremental Update ]
Update only the affected sections & diagrams
                    ↓
[ 4. State Transition & Version Bump ]
state.yaml: version = 2, status = READY_FOR_REVIEW
                    ↓
[ 5. Human Re-Review & Approval ]
Approval Gate re-locks until v2 is approved
```

### Document Impact Sizing Example:
* **User Request:** *"Add Stripe subscription billing."*
* **Affected Artifacts:**
  * `PRD.md`: Add `REQ-010` (subscription tiers) and acceptance criteria.
  * `TRD.md`: Add Stripe Webhook listener architecture, HMAC verification, and customer sync service.
  * `BACKEND_SCHEMA.md`: Add `subscriptions` table and update ER diagram.
  * `UI_UX.md`: Add Pricing Table and Billing Settings screen.
  * `APP_FLOW.md`: Add Checkout redirect and subscription status recovery flows.
* **Unaffected Artifacts:**
  * Core existing CRUD routes and unrelated database tables remain untouched.

---

## 2. Implementation Drift Protocol

Implementation drift occurs when an agent begins coding an approved blueprint and discovers a real-world technical impediment that invalidates a planned architecture decision.

### Common Drift Scenarios:
1. An external API does not support a required query parameter described in the TRD.
2. A selected database library lacks native support for an intended constraint.
3. A third-party OAuth provider does not return the expected user claims.

### The Strict Non-Negotiable Drift Rule:
> **Never silently bypass an approved blueprint. When implementation conflicts with the specification, STOP coding immediately.**

### Drift Escalation Procedure:
1. **Halt Code Generation:** Do not commit workaround code or hacky patches.
2. **Surface the Conflict:**
   ```text
   ⚠️ IMPLEMENTATION DRIFT DETECTED

   While implementing the authentication service as approved in TRD v1,
   we encountered an insurmountable technical limitation:
   - Approved Design: Use Google OAuth with direct refresh tokens for background sync.
   - Discovery: The current Google Cloud client library requires the 'offline' access type parameter, which requires consent prompt re-confirmation for refresh tokens.

   Recommended Revision:
   Update TRD and App Flow to include explicit offline consent prompts during initial signup.

   Should I update the blueprint to v2 with this revised flow for your approval?
   ```
3. **Re-Review & Re-Approve:** Update the TRD, bump the version to v2, obtain user approval, and only then proceed with coding.
