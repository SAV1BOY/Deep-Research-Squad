# Contrarian Survivorship Bias Check

## Purpose

Detect and correct for survivorship bias in the research. Survivorship bias
occurs when the analysis focuses on entities that passed a selection filter
and overlooks those that did not, leading to systematically distorted
conclusions.

## Gate Question

**Has survivorship bias been identified and accounted for?**

## Prerequisites

- Research conclusions drafted.
- The selection process by which subjects entered the analysis understood.
- Data on failures, dropouts, or non-survivors sought.
- Domain-specific survivorship bias patterns known.

## Pass Criteria

1. The selection filter through which subjects entered the analysis is
   identified and documented.
2. An active search for non-survivors (failures, exits, closures) was
   conducted.
3. Conclusions about success factors account for entities that had the
   same factors but failed.
4. Historical data includes entities that no longer exist (e.g., defunct
   companies, retracted papers).
5. "Best practice" conclusions are tested against cases where the same
   practices did not work.
6. The potential magnitude of survivorship bias is estimated.
7. If bias cannot be corrected, it is disclosed as a limitation.

## Fail Actions

- If the selection filter is not identified: analyze how subjects entered
  the dataset.
- If non-survivors were not sought: search for failure cases, closures,
  or dropouts.
- If conclusions ignore non-survivor data: revise to account for it.
- If historical data excludes defunct entities: reconstruct the full
  population where possible.
- If survivorship bias is undisclosed: add it to the limitations section.

## Escalation Rules

- Escalate if survivorship bias is so severe that the conclusions may be
  fundamentally misleading.
- Escalate if data on non-survivors is unavailable and cannot be
  reconstructed.
- Escalate if correcting for survivorship bias reverses a major
  conclusion.
