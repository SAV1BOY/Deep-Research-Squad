# Data Comparability Gate

## Purpose

Ensure that data from different sources, time periods, or geographies can
be meaningfully compared. Non-comparable data combined without adjustment
produces misleading conclusions.

## Gate Question

**Is the data comparable across the dimensions being analyzed?**

## Prerequisites

- Data from multiple sources or time periods collected.
- Definitions and methodologies of each data source documented.
- Comparison dimensions identified (cross-country, cross-time, cross-source).
- Known comparability issues in the domain reviewed.

## Pass Criteria

1. Definitions of key variables are consistent across sources (e.g., same
   definition of "unemployment" or "revenue").
2. Measurement methodologies are compatible or differences are documented.
3. Time periods align or adjustments are made for temporal mismatch.
4. Currency values are adjusted for inflation and exchange rates when
   comparing across time or countries.
5. Population denominators are comparable (same base for per-capita
   calculations).
6. Structural breaks (methodology changes by the source) are identified
   and handled.
7. Comparability limitations are disclosed in the analysis.

## Fail Actions

- If definitions differ: standardize where possible or note the
  incompatibility.
- If methodology differences exist: quantify the impact or restrict
  comparisons.
- If inflation/exchange adjustments missing: apply them.
- If structural breaks are found: split the analysis at the break point.
- If comparability limitations are undisclosed: add a limitations section.

## Escalation Rules

- Escalate if data from critical sources is fundamentally non-comparable
  and the research question requires comparison.
- Escalate if comparability adjustments require economic or statistical
  expertise beyond agent capability.
- Escalate if comparability issues are so severe that the intended
  analysis cannot be performed.
