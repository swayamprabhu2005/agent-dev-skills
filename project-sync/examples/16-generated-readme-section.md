# Example 16: Generated README Section (Tool-Managed Documentation)

This example illustrates how Project Sync handles repositories where a section of `README.md` is managed by an automated documentation generator tool.

---

## 1. Implementation Change
Added a new endpoint `POST /api/v1/auth/reset-password` in an API service that uses JSDoc and `swagger-markdown` to generate its documentation table.

## 2. Working Tree & README Inspection
Inspecting `README.md` reveals:
```markdown
## API Documentation

<!-- AUTO-GENERATED-DOCS:START -->
<!-- Do not edit this section manually. Run `npm run generate-docs` -->
| Method | Route | Description |
| :--- | :--- | :--- |
| POST | `/api/v1/auth/login` | Authenticate user session |
<!-- AUTO-GENERATED-DOCS:END -->
```
`package.json` contains:
```json
"scripts": {
  "generate-docs": "swagger-markdown -i spec.yaml -o README.md"
}
```

## 3. Determination of Documentation Impact
* The new password reset endpoint must appear in the API documentation table.
* **Anti-Pattern:** Manually typing a new markdown row inside the `AUTO-GENERATED-DOCS` markers. This would be wiped out the next time CI runs.
* **Correct Action:**
  1. Ensure docstrings and `spec.yaml` are updated with the new endpoint.
  2. Execute the official generation command: `npm run generate-docs`.
  3. Verify that the generator script successfully populated the table in `README.md`.

## 4. Determination of Ignore-Rule Impact
* No new untracked build artifacts created.
* **Decision:** No changes required for `.gitignore`.

## 5. Resulting Modifications
Executed `npm run generate-docs`, which automatically updated the demarcated block inside `README.md`.

## 6. Completion Summary
```text
Implementation complete.

Implemented:
- Added password reset endpoint in src/controllers/auth.ts
- Updated OpenAPI spec definition for reset-password route

Project synchronization:
- README.md — Updated: Re-generated API documentation section via npm run generate-docs
- .gitignore — No changes required: Generated assets remain properly tracked

Validation:
- Documentation generation: Successful (npm run generate-docs)
- Tests: 16 passed (npm test)

Iteration complete.
```
