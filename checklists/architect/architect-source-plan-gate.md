# Architect Source Plan Gate

## Purpose

Ensure the planned source strategy is adequate before search execution begins.
Validates that the source plan covers enough types, geographies, and access
methods to produce reliable findings.

## Gate Question

**Is the source plan adequate to answer the research question with the
required confidence?**

## Prerequisites

- Sub-questions and layers finalized.
- Source Agent has proposed an initial source plan.
- Known source availability and access constraints documented.
- Target confidence level set by Chief Agent.

## Pass Criteria

1. At least 3 distinct source classes are planned (academic, news, government,
   industry, primary data, expert opinion, etc.).
2. Primary sources are prioritized over secondary where available.
3. Source plan includes at least one non-English source when the topic is
   international.
4. Paywalled or restricted sources have access routes identified.
5. Planned source count is proportionate to the depth tier (quick: 5-10,
   standard: 10-25, deep: 25-50+).
6. Redundancy exists: no single source failure would leave a sub-question
   unanswerable.
7. Source freshness targets are defined (e.g., within last 2 years for
   fast-moving domains).

## Fail Actions

- If fewer than 3 source classes: expand the plan before execution.
- If no primary sources planned: mandate at least one primary source attempt.
- If access routes are missing for key sources: resolve access or find
  alternatives.
- If source count is too low for the depth tier: increase targets.
- If no freshness target set: Source Agent must define one.

## Escalation Rules

- Escalate if critical sources require institutional access not available.
- Escalate if the topic is in a language none of the agents can process.
- Escalate if source plan changes would delay delivery past the deadline.
