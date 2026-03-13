# Modeling Scenario Coverage Check

## Purpose

Ensure the model explores a sufficient range of scenarios and does not
present only the most likely or most favorable outcome. Scenario coverage
prepares the requester for multiple futures.

## Gate Question

**Does the model cover a sufficient range of plausible scenarios?**

## Prerequisites

- Model structure finalized.
- Key variables and their ranges identified.
- Uncertainty sources catalogued.
- Stakeholder priorities and risk appetite understood.

## Pass Criteria

1. At least 3 scenarios are modeled: optimistic, base case, and
   pessimistic (or equivalent).
2. Scenarios vary on the most impactful and uncertain variables.
3. Each scenario has a stated set of assumptions.
4. Extreme but plausible scenarios (tail risks) are included for
   high-stakes analyses.
5. Scenario probabilities or likelihood assessments are provided
   where possible.
6. The scenarios collectively cover the range of plausible outcomes.
7. Scenarios are internally consistent (no contradictory assumptions
   within a single scenario).

## Fail Actions

- If fewer than 3 scenarios: add scenarios to cover the range.
- If scenarios do not vary key variables: identify the most uncertain
  variables and vary them.
- If assumptions are unstated: document them for each scenario.
- If tail risks are excluded from high-stakes analysis: add them.
- If scenarios are internally inconsistent: fix the contradictions.

## Escalation Rules

- Escalate if the key uncertain variables cannot be identified without
  domain expertise.
- Escalate if scenario analysis reveals that the outcome is highly
  sensitive to a variable the research cannot pin down.
- Escalate if the requester only wants to see the optimistic scenario
  and the analysis shows significant downside risk.
