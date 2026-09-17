# Example 04: API Change (Query Pagination)

This example illustrates updating high-level API usage documentation when query parameters are altered.

---

## 1. Implementation Change
Updated the customer search API endpoint to require cursor-based pagination parameters:
* `GET /api/v1/customers` now accepts `?cursor=<string>&limit=<int>`.
* Removed legacy `?offset=<int>` parameter.
* Added cursor pagination serialization to `CustomerController.java`.

## 2. Determination of Documentation Impact
* `README.md` contains an "API Quickstart" section demonstrating sample API requests with `curl`.
* The legacy curl example used `?offset=10`, which now returns an HTTP 400 validation error.
* **Decision:** Update the curl snippet in `README.md` to reflect `?cursor=...&limit=25`.

## 3. Determination of Ignore-Rule Impact
* Maven build artifacts (`target/`) are already covered in `.gitignore`.
* **Decision:** No changes required for `.gitignore`.

## 4. Resulting Modifications

### `README.md` (Diff):
```diff
 ### Query Customers
 \`\`\`bash
-# Fetch second page of customers (legacy offset)
-curl -X GET "https://api.example.com/v1/customers?offset=10&limit=10"
+# Fetch customers using cursor-based pagination
+curl -X GET "https://api.example.com/v1/customers?limit=25&cursor=eyJpZCI6MTAwfQ"
 \`\`\`
```

## 5. Completion Summary
```text
Implementation complete.

Implemented:
- Migrated customer search from offset pagination to cursor-based pagination
- Updated API query parameter validation

Project synchronization:
- README.md — Updated: Corrected API curl example to show cursor pagination
- .gitignore — No changes required: Maven target directory already ignored

Validation:
- Tests: 29 passed (mvn test)

Iteration complete.
```
