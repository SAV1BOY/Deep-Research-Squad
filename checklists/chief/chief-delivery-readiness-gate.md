# Chief Delivery Readiness Gate

## Purpose

Final quality gate before research output is delivered to the requester.
Confirms the deliverable is complete, coherent, and meets the standards
promised at scope approval.

## Gate Question

**Is the research output ready for delivery to the requester?**

## Prerequisites

- Synthesis Agent has produced the final output document.
- Audit Agent has completed its quality review.
- All verification checks have passed or exceptions are documented.
- Confidence scores are attached to every major claim.
- Requester's original question and scope are available for comparison.

## Pass Criteria

1. Every sub-question from the approved scope is addressed in the output.
2. Confidence levels are explicitly stated (high / medium / low) per finding.
3. All sources are cited with retrievable references.
4. Known gaps and limitations are disclosed in a dedicated section.
5. Executive summary is present and can stand alone.
6. Audit quality score meets the minimum threshold (>= 7/10).
7. No unresolved evidence conflicts remain without documented rationale.
8. Output format matches the requester's specified preference.

## Fail Actions

- If sub-questions are unanswered: return to the responsible agent for
  completion or document why the gap exists.
- If confidence scores are missing: Synthesis Agent must add them before
  release.
- If audit score < 7/10: identify failing dimensions and remediate.
- If evidence conflicts are unresolved: route to Contrarian Agent for
  final adjudication or disclose the conflict explicitly.
- If format is wrong: reformat before delivery.

## Escalation Rules

- Escalate if audit score remains below threshold after one remediation pass.
- Escalate if the research conclusion contradicts prior delivered research
  on the same topic without explanation.
- Escalate if delivery deadline has passed and output is still not ready.
- Escalate if requester has changed requirements after synthesis began.
