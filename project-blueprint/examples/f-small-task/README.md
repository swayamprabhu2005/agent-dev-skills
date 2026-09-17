# Example F: Small Task (When NOT to Invoke Project Blueprint)

This example demonstrates the essential negative boundary: recognizing when a user's task is too small or routine to justify invoking Project Blueprint.

---

## 1. The User Request
> *"Change the background color of the 'Export CSV' button on the reports page from blue to emerald green (`#059669`)."*

---

## 2. Decision Logic: Why Project Blueprint Stays Silent

Project Blueprint evaluates the request against its activation criteria:
* Is this a brand-new application? **NO.**
* Is this an architectural migration or database schema change? **NO.**
* Is this a major multi-screen user capability? **NO.**
* Does this introduce new entities or third-party integrations? **NO.**

### Anti-Pattern: Over-Engineering Minor Tasks
* ❌ An agent responds: *"Before I change this button color, let us generate a PRD, TRD, UI/UX specification, and ER diagram, and block implementation until you approve."*
* **Why it fails:** This creates massive user friction, wastes tokens, and turns a 5-second style edit into a bureaucratic delay.

---

## 3. Correct Agent Behavior

The agent recognizes this as routine maintenance within an established codebase:
1. Skips Project Blueprint entirely.
2. Locates the button component in `src/components/ReportExportButton.tsx`.
3. Changes the Tailwind class or hex code:
   ```diff
   - className="bg-blue-600 hover:bg-blue-700"
   + className="bg-emerald-600 hover:bg-emerald-700"
   ```
4. Verifies the change locally.
5. Emits a concise direct response:
   > *"Updated the 'Export CSV' button styling to emerald green (`#059669`) in `ReportExportButton.tsx`."*
