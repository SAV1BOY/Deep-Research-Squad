# Data Completeness Gate

## Purpose

Verify that the dataset used for analysis is complete enough to support
valid conclusions. Missing data can introduce bias and invalidate findings
if not properly accounted for.

## Gate Question

**Is the dataset complete enough to support the intended analysis?**

## Prerequisites

- Dataset collected and loaded.
- Expected data dimensions and variables defined.
- Data dictionary or schema available.
- Minimum completeness thresholds set.

## Pass Criteria

1. All expected variables are present in the dataset.
2. Missing value rate is below the threshold (typically < 10% for
   critical variables).
3. Missing data patterns are analyzed (random vs. systematic).
4. Time series have no unexplained gaps in coverage.
5. Geographic or demographic coverage matches the scope requirements.
6. The dataset spans the full time period specified in the scope.
7. Completeness metrics are documented with counts and percentages.

## Fail Actions

- If critical variables are missing entirely: source the missing data
  or adjust the analysis plan.
- If missing value rate exceeds threshold: apply imputation or restrict
  analysis to complete cases with documented caveat.
- If missingness is systematic: investigate the cause and note the bias
  risk.
- If time series gaps exist: fill if possible or exclude the gap period
  with explanation.
- If completeness is undocumented: produce the completeness report.

## Escalation Rules

- Escalate if a critical variable has > 30% missing data and cannot be
  sourced elsewhere.
- Escalate if systematic missingness suggests data suppression or
  censorship.
- Escalate if the dataset is fundamentally too incomplete for any valid
  analysis.
