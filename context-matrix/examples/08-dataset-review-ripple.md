# Example 08: Reviewing a Dataset or Technical Report (RIPPLE)

---

## 1. User Invocation

```text
/context-matrix ripple Audit the customer churn training dataset in data/churn_train.parquet. Look for distribution drift, target leakage, and missing value anomalies.
```

---

## 2. Framework Selected

* **Primary Framework:** `RIPPLE`
* **Selection Rationale:** Forensic analytical audit of tabular data with structured inspection points and empirical validation.

---

## 3. Relevant Context & Constraints

* **Dataset:** `data/churn_train.parquet` containing 450,000 subscriber records across 42 feature columns.
* **Objective:** Ensure dataset integrity before training an XGBoost churn classification model.
* **Points to Check:** Target leakage (future information included in predictors), collinear features, null imputation artifacts, and class imbalance.

---

## 4. Resulting Prompt / Generated Workflow

```markdown
**Role:** Staff Machine Learning Auditor and Quantitative Data Quality Engineer.
**Input:** Tabular dataset `data/churn_train.parquet` and the target column `has_churned_30d`.
**Process:**
1. Execute schema and dtype verification across all 42 features.
2. Calculate missingness percentages and identify non-random missingness patterns.
3. Compute feature correlation with `has_churned_30d` to detect target leakage.
4. Audit timestamp distributions for seasonal discontinuities or train-test boundary leakage.
**Points:**
- Target Leakage: Scan for post-event telemetry (e.g., `account_closure_ticket_created_date`, `refund_amount_issued`) present in training features.
- High-Cardinality Categoricals: Check ZIP codes and free-text agent notes for excessive levels.
- Class Imbalance: Quantify positive vs negative class ratio.
**Layout:**
1. Executive Quality Scorecard (Green / Amber / Red status).
2. Findings Table (Feature Name, Anomaly Type, Severity, Recommended Remediation).
3. Detailed Target Leakage Deep Dive.
4. Python remediation script utilizing Polars or DuckDB.
**Evaluate:**
- Produce an executable Python data test script using `great_expectations` or `pandera` validating all remediated assertions.
```

---

## 5. Evaluation Criteria

* [x] **Analytical Process:** Sequenced 4-step data hygiene methodology.
* [x] **Explicit Metrics:** Focuses on target leakage, class distribution, and temporal boundaries.
* [x] **Verification Script:** Outputs executable schema assertion rules.
* [x] **Readiness Status:** `READY`
