# Query Pivot Readiness Gate

## Purpose

Confirm that fallback and pivot strategies are prepared in case initial
searches fail to yield sufficient results. Prevents dead-end research
paths that consume time without producing evidence.

## Gate Question

**Are pivot strategies planned if the primary search approach fails?**

## Prerequisites

- Primary search strategy defined and documented.
- Success thresholds set (minimum number of relevant results per query).
- Alternative keyword sets and platforms identified.
- Time budget for search phase known.

## Pass Criteria

1. Each primary search trail has at least one defined pivot alternative.
2. Pivot triggers are explicit (e.g., fewer than 3 relevant results on
   the first page, zero results from a platform).
3. Pivot strategies differ meaningfully from the primary (different
   keywords, different platform, different angle).
4. Time allocation allows for at least one pivot per sub-question.
5. Broadening and narrowing options are both available as pivot types.
6. Lateral pivots are planned (searching adjacent topics or upstream
   causes).
7. The pivot sequence is ordered by expected yield (best alternative first).

## Fail Actions

- If no pivots defined: create at least one alternative per primary trail.
- If pivot triggers are vague: define quantitative thresholds.
- If pivots are too similar to primary: redesign for genuine diversity.
- If time budget does not allow pivots: negotiate more time or reduce the
  number of sub-questions searched.
- If no lateral pivot exists: add one adjacent-topic search option.

## Escalation Rules

- Escalate if all primary and pivot strategies yield insufficient results.
- Escalate if pivoting requires access to platforms not currently available.
- Escalate if repeated pivots suggest the question may be unanswerable
  with public sources.
