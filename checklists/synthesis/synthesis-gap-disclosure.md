# Synthesis Gap Disclosure Check

## Purpose

Ensure that all known gaps, limitations, and uncertainties are transparently
disclosed in the final output. Hiding gaps creates false confidence and
exposes the requester to uninformed decision-making.

## Gate Question

**Are all gaps and limitations transparently disclosed?**

## Prerequisites

- Evidence completeness assessment available.
- Literature gap analysis completed.
- Feasibility constraints documented.
- Confidence scores assigned to findings.

## Pass Criteria

1. A dedicated "Limitations and Gaps" section exists in the output.
2. Every sub-question that could not be fully answered has its gap
   documented.
3. Evidence gaps are distinguished from scope exclusions (things we
   could not find vs. things we chose not to look for).
4. The impact of each gap on the conclusions is assessed (negligible,
   moderate, significant).
5. Suggestions for how gaps could be addressed (future research,
   additional data) are provided.
6. Confidence levels reflect the gaps (lower confidence where gaps are
   significant).
7. Gaps are described specifically (not vague disclaimers like "more
   research needed").

## Fail Actions

- If no limitations section exists: create one.
- If gaps are not documented: compile them from the evidence completeness
  and literature gap assessments.
- If gap impact is unassessed: evaluate each gap's effect on conclusions.
- If confidence levels do not reflect gaps: adjust them.
- If gap descriptions are vague: make them specific and actionable.

## Escalation Rules

- Escalate if the gaps are so significant that the output may mislead
  the requester.
- Escalate if disclosing certain gaps would undermine the entire research
  product and the requester should be warned.
- Escalate if gaps were discovered only during synthesis and earlier
  gates missed them.
