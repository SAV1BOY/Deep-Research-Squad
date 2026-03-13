# Cross-Squad Data Validation Gate

## Purpose

This gate ensures that data received from another squad is validated before
being incorporated into the receiving squad's research. Data crossing squad
boundaries is a common failure point where format mismatches, stale data,
undocumented transformations, and broken provenance chains introduce errors.
This gate enforces validation at the point of data transfer to catch issues
before they propagate into downstream analysis and conclusions.

## Gate Question

**Has cross-squad data been validated for accuracy and usability?**

All data received from another squad must be checked for integrity, currency,
format compatibility, provenance, and fitness for the intended use before
it is incorporated into any analysis or research output.

## Pass Criteria

1. Data provenance is documented with original source, collection date, and any transformations.
2. Data format is compatible with the receiving squad's tools and workflows.
3. Data currency is confirmed relative to the receiving squad's research time boundaries.
4. Data completeness is assessed with any gaps or missing values identified.
5. Data definitions and schema are documented so fields are interpreted correctly.
6. Units of measurement, currencies, and time zones are explicit and consistent.
7. Any data transformations, aggregations, or filters applied by the sending squad are documented.
8. A sample validation check has been performed comparing data against known reference points.
9. Outliers and anomalies in the data have been identified and investigated.
10. Data sensitivity classification and handling requirements are communicated.
11. The data license or usage rights permit the receiving squad's intended use.
12. Version control is applied so the specific dataset version used is traceable.
13. A point of contact for data questions is identified in the sending squad.

## Fail Actions

- If provenance is undocumented, request the full data lineage from the sending squad.
- If format is incompatible, either transform the data or request it in the needed format.
- If data is stale relative to research boundaries, request updated data or flag the limitation.
- If data is incomplete, quantify the gaps and assess their impact on intended analysis.
- If definitions or schema are missing, obtain them before interpreting any fields.
- If units or time zones are ambiguous, confirm with the sending squad before proceeding.
- If transformations are undocumented, request documentation or access to raw data.
- If sample validation reveals discrepancies, investigate before using the data.
- If sensitivity classification is missing, apply the most restrictive handling until confirmed.
- Do not incorporate cross-squad data into analysis until validation is complete.
