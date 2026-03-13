# Evidence Consistency Gate

## Purpose

Check that evidence from different sources tells a consistent story. When
sources disagree, the inconsistency must be identified, investigated, and
either resolved or transparently reported.

## Gate Question

**Is the evidence consistent across all sources?**

## Prerequisites

- Evidence collected from multiple sources per claim.
- Cross-source comparison matrix built.
- Source quality and authority assessments available.
- Conflict log initialized.

## Pass Criteria

1. Key facts (dates, numbers, names) agree across independent sources.
2. Where numerical data differs, the variance is within an acceptable
   tolerance (defined per domain).
3. Qualitative assessments from different sources point in the same
   direction (even if wording differs).
4. Any inconsistency is logged with both sides documented.
5. Resolved inconsistencies have a stated rationale favoring one source
   over another.
6. Unresolved inconsistencies are presented as open questions in the
   output.
7. The proportion of consistent vs. inconsistent evidence is reported.

## Fail Actions

- If key facts disagree: investigate further to determine which source
  is more reliable (newer, more authoritative, primary vs. secondary).
- If numerical variances exceed tolerance: report the range and identify
  the most credible figure.
- If qualitative assessments conflict: present both perspectives and
  assess which has stronger evidentiary support.
- If inconsistencies are not logged: create the conflict log before
  proceeding.
- If a pattern of inconsistency points to a systematic error in one
  source: flag that source for reduced trust.

## Escalation Rules

- Escalate if more than 30% of evidence items show inconsistencies.
- Escalate if the inconsistency involves a central claim that determines
  the overall conclusion.
- Escalate if inconsistencies suggest deliberate misinformation by a
  source.
