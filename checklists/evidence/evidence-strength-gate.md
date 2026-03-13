# Evidence Strength Gate

## Purpose

Assess the strength of each piece of evidence supporting a claim. Prevents
weak evidence from being treated as strong, and ensures the confidence level
assigned to conclusions is warranted by the underlying proof.

## Gate Question

**Is the evidence strong enough to support the claim it is attached to?**

## Prerequisites

- Claims extracted and listed with associated evidence.
- Evidence classification rubric available (strong, moderate, weak,
  anecdotal).
- Source authority assessments completed.
- Methodology of evidence generation known (where applicable).

## Pass Criteria

1. Each claim has an explicit evidence-strength rating (strong, moderate,
   weak, anecdotal).
2. Strong-rated evidence comes from controlled studies, official records,
   or verified primary data.
3. Moderate-rated evidence comes from reputable secondary sources with
   clear methodology.
4. Weak and anecdotal evidence is flagged and not used as sole support
   for any critical claim.
5. The aggregate evidence for each critical claim reaches at least
   "moderate" strength.
6. Evidence strength ratings are consistent across similar evidence types.
7. Strength downgrades are applied when conflicts or methodological
   concerns exist.

## Fail Actions

- If a critical claim has only weak evidence: search for stronger evidence
  or downgrade the claim's confidence level.
- If strength ratings are missing: apply the rubric to all evidence items.
- If strength ratings are inconsistent: calibrate across the full evidence
  set.
- If aggregate strength is below moderate: flag the claim as insufficiently
  supported and disclose the weakness.

## Escalation Rules

- Escalate if the strongest available evidence is still rated "weak" for
  a high-stakes claim.
- Escalate if evidence strength assessment requires statistical or
  methodological expertise the agents lack.
- Escalate if evidence strength is disputed between agents and cannot
  be resolved.
