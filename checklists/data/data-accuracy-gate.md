# Data Accuracy Gate

## Purpose

Confirm that data values are accurate and free from errors that could
distort analysis. Inaccurate data is worse than missing data because it
produces confident but wrong conclusions.

## Gate Question

**Is the data accurate and free from material errors?**

## Prerequisites

- Dataset loaded and completeness check passed.
- Data validation rules defined (acceptable ranges, formats, types).
- Reference values or benchmarks available for spot-checking.
- Data provenance documented (source, collection method, transformations).

## Pass Criteria

1. Data types are correct (numbers are numbers, dates are dates, etc.).
2. Values fall within expected ranges (no impossible values like negative
   ages or percentages > 100).
3. Spot-check of a random sample (minimum 5%) against source documents
   shows < 2% error rate.
4. Known reference values (benchmarks, published statistics) match the
   dataset within acceptable tolerance.
5. Duplicates are identified and handled (removed or justified).
6. Units are consistent throughout (no mixed currencies, measurement
   systems, etc.).
7. Data transformations (aggregation, conversion) are documented and
   verified.

## Fail Actions

- If data type errors found: correct them or exclude affected records.
- If out-of-range values found: investigate, correct if possible, or
  exclude with documentation.
- If spot-check error rate > 2%: expand the check and identify the
  error source.
- If duplicates found: deduplicate with a documented rule.
- If units are mixed: standardize and document the conversion.

## Escalation Rules

- Escalate if the error rate exceeds 5% after correction attempts.
- Escalate if accuracy issues suggest the data source itself is unreliable.
- Escalate if data accuracy problems are discovered after analysis has
  been completed, requiring re-analysis.
