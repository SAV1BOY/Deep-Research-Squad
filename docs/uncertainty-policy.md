# Uncertainty Policy

## Purpose

This policy defines how the Deep Research Squad handles and communicates
uncertainty. Uncertainty is inherent in research. Our job is not to eliminate
it but to characterize it precisely and communicate it honestly.

## Principles

1. **Uncertainty is information.** Knowing what we do not know is valuable.
2. **Uncertainty is not weakness.** Precise uncertainty signals competence.
3. **Uncertainty must be characterized.** Vague uncertainty is useless.
4. **Uncertainty must be communicated.** Hidden uncertainty is dangerous.

## Types of Uncertainty

### Epistemic Uncertainty (Knowledge Gaps)

Uncertainty due to incomplete information. Can be reduced with more data.

- "We lack data on [specific dimension]."
- "Additional research could narrow this uncertainty."
- Remediation: identify what data would reduce the gap.

### Aleatory Uncertainty (Inherent Randomness)

Uncertainty due to the nature of the system. Cannot be eliminated with more data.

- "The outcome is inherently probabilistic."
- "Even with perfect information, the outcome would remain uncertain."
- Remediation: present scenarios or probability ranges.

### Model Uncertainty (Framework Limitations)

Uncertainty due to the analytical approach chosen.

- "A different analytical framework could yield different conclusions."
- "Our model assumes [assumption] which simplifies reality."
- Remediation: test sensitivity to framework choice.

## Communicating Uncertainty

### Mandatory Disclosures

Every deliverable must:
- State the overall confidence level.
- Identify the largest source of uncertainty.
- Distinguish epistemic from aleatory uncertainty when relevant.
- Quantify uncertainty where possible (ranges, probabilities, scenarios).

### Language Standards

Use the language defined in:
- `voice/language-guides/uncertainty-language.md`
- `voice/calibration/confidence-scale-guide.md`
- `phrases/uncertainty-language.md`

### Formatting Standards

| Uncertainty Level | Presentation Format                        |
|-------------------|--------------------------------------------|
| Low               | Point estimate with brief confidence note   |
| Medium            | Range estimate with explanation             |
| High              | Scenario presentation with probability weights |
| Very High         | Explicit "unknown" flag with gap analysis   |

## Decision-Making Under Uncertainty

When delivering to decision-makers:
- State what is known firmly enough to act on.
- State what would need to be true for the recommendation to change.
- Identify trigger events that would reduce uncertainty.
- Offer decision frameworks (expected value, regret minimization, optionality).

## Uncertainty in Different Formats

| Format           | Uncertainty Treatment                        |
|------------------|----------------------------------------------|
| Deep dive        | Full section on uncertainty and limitations   |
| Executive brief  | One-sentence confidence + one-sentence caveat |
| Synthesis        | Per-finding uncertainty + aggregate assessment|
| Slack update     | Confidence tag + key caveat                   |
| Presentation     | Confidence on each finding slide              |

## Policy Compliance

- The Quality Gate Keeper checks uncertainty disclosure at Gate 3.
- The Evidence Auditor verifies confidence-to-evidence alignment at Gate 5.
- Deliverables without uncertainty disclosure do not pass quality gates.

## Quality Check

- Is the type of uncertainty identified (epistemic, aleatory, model)?
- Is uncertainty quantified where possible?
- Is the communication format appropriate to the audience?
- Does the deliverable help the reader make decisions despite uncertainty?
