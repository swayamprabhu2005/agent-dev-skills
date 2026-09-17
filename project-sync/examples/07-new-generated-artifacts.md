# Example 07: New Generated Artifacts (Client SDK Code Generation)

This example illustrates synchronizing both `README.md` and `.gitignore` when an automated build step introduces persistent generated code artifacts.

---

## 1. Implementation Change
Configured OpenAPI Generator to compile an internal TypeScript API client into a dedicated `generated/sdk/` directory:
* Added `"generate:sdk": "openapi-generator-cli generate -i spec.yaml -g typescript-axios -o generated/sdk"` to `package.json`.
* Running the generator produced 50+ auto-generated files in `generated/sdk/`.

## 2. Determination of Documentation Impact
* `README.md` documents build and code generation scripts under `## Development`.
* Developers need to know how to regenerate the SDK when API specs change.
* **Decision:** Add `npm run generate:sdk` to the list of available commands in `README.md`.

## 3. Determination of Ignore-Rule Impact
* `generated/sdk/` contains machine-generated code from `spec.yaml`.
* The project policy states that generated SDKs are compiled at build time and should not be tracked in Git.
* Checking `.gitignore`: `generated/` is currently untracked and not ignored.
* **Decision:** Add `generated/` to `.gitignore`.

## 4. Resulting Modifications

### `README.md` (Diff):
```diff
 ### Available Scripts
 - `npm run build`: Compile application code
+- `npm run generate:sdk`: Re-generate TypeScript client SDK from OpenAPI spec
 - `npm test`: Run test suite
```

### `.gitignore` (Diff):
```diff
 node_modules/
 dist/
+.generated/
+generated/sdk/
```

## 5. Completion Summary
```text
Implementation complete.

Implemented:
- Configured OpenAPI Generator for TypeScript Axios client SDK
- Added npm run generate:sdk command to package.json

Project synchronization:
- README.md — Updated: Documented npm run generate:sdk in Available Scripts
- .gitignore — Updated: Added generated/sdk/ to ignore machine-generated artifacts

Validation:
- Generation: Verified (npm run generate:sdk executed cleanly)
- Tests: All passed

Iteration complete.
```
