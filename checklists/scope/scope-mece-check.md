# Scope MECE Check

## Purpose

Verify that the sub-question decomposition is Mutually Exclusive and
Collectively Exhaustive (MECE). Ensures no overlaps waste effort and no
gaps leave parts of the question unanswered.

## Gate Question

**Is the sub-question decomposition verified as MECE?**

## Prerequisites

- Sub-questions finalized and completeness gate passed.
- Each sub-question has a written one-sentence definition.
- Scope boundaries documented.
- Domain taxonomy or framework available for cross-check.

## Pass Criteria

1. No two sub-questions cover the same ground (mutual exclusivity).
2. The union of all sub-questions covers the full scope (collective
   exhaustiveness).
3. Each sub-question can be assigned to a distinct agent or layer without
   duplication of effort.
4. Boundary cases between adjacent sub-questions are explicitly assigned
   to one or the other.
5. A domain framework (if applicable) confirms no category is missing.
6. Removing any single sub-question would leave a visible gap.
7. The MECE structure has been visualized or tabulated for review.

## Fail Actions

- If overlap detected: merge the overlapping sub-questions or redraw
  boundaries between them.
- If gap detected: add a new sub-question to cover the gap.
- If boundary cases are ambiguous: write explicit assignment rules.
- If MECE cannot be achieved cleanly: document the known overlap or
  gap with justification.
- If no framework was used for validation: apply at least one standard
  decomposition framework.

## Escalation Rules

- Escalate if the topic inherently resists MECE decomposition (e.g.,
  highly interdependent systems) and agents cannot agree on structure.
- Escalate if achieving MECE would require expanding scope beyond
  approved boundaries.
- Escalate if the decomposition framework itself is contested among agents.
