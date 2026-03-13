# Contrarian Base Rate Override Check

## Purpose

Detect cases where the research conclusion implicitly overrides known base
rates without justification. Extraordinary claims that deviate from base
rates require extraordinary evidence.

## Gate Question

**Does the conclusion deviate from known base rates, and if so, is that
deviation justified by strong evidence?**

## Prerequisites

- Key conclusions formulated.
- Relevant base rates identified and documented.
- Evidence strength ratings assigned.
- Domain norms for base rate deviation understood.

## Pass Criteria

1. Base rates relevant to each major conclusion are stated.
2. Any deviation from base rates is explicitly acknowledged.
3. Deviations are supported by evidence proportionate to the degree of
   deviation (stronger evidence for larger deviations).
4. The reasoning explains WHY this case differs from the base rate.
5. Sample size is adequate to support a base-rate override.
6. The possibility that the conclusion reverts to the base rate is
   discussed.
7. No base rate is overridden based solely on anecdotal evidence.

## Fail Actions

- If relevant base rates are not stated: find and include them.
- If deviation is unacknowledged: add the acknowledgment and justification.
- If evidence is disproportionate to the deviation: either strengthen
  the evidence or soften the conclusion.
- If anecdotal evidence is the sole basis: flag as insufficient and seek
  stronger evidence.
- If reversion to base rate is not discussed: add that scenario.

## Escalation Rules

- Escalate if the conclusion requires overriding a well-established base
  rate and the evidence is only moderate.
- Escalate if base rate data is unavailable and the conclusion implicitly
  assumes a non-default rate.
- Escalate if multiple conclusions collectively override base rates in
  the same direction, suggesting systematic optimism or pessimism bias.
