# Example 03: Feature Addition (CSV Data Export)

This example illustrates synchronizing documentation when a new CLI user-facing feature is added.

---

## 1. Implementation Change
Added CSV export capability to a CLI reporting utility:
* Added `--format=csv` and `--output=<file>` flags to `src/cli.py`.
* Implemented `src/exporters/csv_exporter.py`.

## 2. Determination of Documentation Impact
* `README.md` documents available CLI commands and flags under `## Usage`.
* The `--format` flag now accepts `csv` in addition to `json` and `table`.
* **Decision:** Update the usage flag description and add a one-line curl/CLI example showing CSV export.

## 3. Determination of Ignore-Rule Impact
* No new generated build directories were created (standard python project already ignores `__pycache__`).
* **Decision:** No changes required for `.gitignore`.

## 4. Resulting Modifications

### `README.md` (Diff):
```diff
 ### Command Options
-`--format`: Output format (`json` or `table`, default: `table`)
+`--format`: Output format (`json`, `csv`, or `table`, default: `table`)
+`--output`: Optional path to write output file (e.g. `--output report.csv`)

+#### Export to CSV
+\`\`\`bash
+analytics-cli generate --format=csv --output=monthly-report.csv
+\`\`\`
```

## 5. Completion Summary
```text
Implementation complete.

Implemented:
- Added CSV exporter for analytics reports
- Added --format=csv and --output options to CLI parser

Project synchronization:
- README.md — Updated: Documented --format=csv and added export usage example
- .gitignore — No changes required: Existing rules cover all build artifacts

Validation:
- Tests: 18 passed (pytest)

Iteration complete.
```
