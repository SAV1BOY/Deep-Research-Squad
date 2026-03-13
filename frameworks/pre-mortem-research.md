# Pre-Mortem Research

## Purpose
A structured technique for identifying how and why research conclusions could be wrong before they are finalized. By assuming failure first, the team surfaces blind spots, biases, and vulnerabilities that forward-looking optimism typically obscures.

## When to Use
- Before finalizing any high-stakes research deliverable
- When confidence in conclusions feels suspiciously high
- After synthesis but before decision-making
- When the research will influence irreversible decisions
- As a mandatory checkpoint in the RalphLoop (complements R12: Contrarian Pass)

## Inputs
- Draft research conclusions and recommendations
- The evidence base supporting those conclusions
- The models and reasoning chains used in synthesis
- Knowledge of stakeholder expectations and decision context

## Process (step-by-step)

### Step 1: Assume Total Failure
Adopt the mental frame: "It is six months from now. The research turned out to be completely wrong. The recommendations led to a bad outcome." Accept this as a given fact for the duration of the exercise.

### Step 2: Brainstorm Failure Causes
Generate as many reasons as possible for why the research failed. Categories to explore:
- **Source failures:** Key sources were biased, outdated, fabricated, or incomplete
- **Reasoning failures:** Logical errors, false analogies, survivorship bias, confirmation bias
- **Scope failures:** Critical factors were outside the defined scope and missed entirely
- **Model failures:** The explanatory model was wrong — the mechanism did not work as theorized
- **Temporal failures:** The conclusions were time-sensitive and decayed before action was taken
- **Adversarial failures:** An actor deliberately seeded misinformation that was not detected
- **Unknown unknowns:** Something no one considered turned out to be the decisive factor

### Step 3: Rank by Likelihood and Impact
For each failure cause, assess:
- **Likelihood:** How plausible is this failure mode? (High / Medium / Low)
- **Impact:** If this failure occurred, how severe would the consequences be? (Critical / Serious / Minor)
- **Detectability:** How easy is it to detect this failure before it causes harm? (Easy / Moderate / Hard)

Priority = High Likelihood + Critical Impact + Hard Detectability

### Step 4: Design Mitigations
For each high-priority failure mode, define a specific mitigation:
- Additional verification steps
- Alternative source categories to consult
- Sensitivity analyses or scenario tests
- Explicit caveats and boundary conditions in the deliverable
- Monitoring triggers that would signal the failure is occurring

### Step 5: Test Against Current Research
Apply each mitigation to the existing research:
- Does the additional verification change any conclusions?
- Do alternative sources confirm or contradict?
- Do sensitivity analyses reveal fragile assumptions?
- Are the caveats already documented, or are they missing?

### Step 6: Document Residual Risks
After mitigations are applied, some risks will remain. Document them explicitly:
- What failure modes could not be fully mitigated?
- What is the residual probability of each?
- What monitoring or early-warning signals should stakeholders watch for?
- Under what conditions should the conclusions be revisited?

## Outputs
- Ranked list of failure modes with likelihood, impact, and detectability ratings
- Mitigation plan for high-priority failure modes
- Updated research conclusions with additional caveats where needed
- Residual risk register with monitoring triggers
- Reversal conditions — specific signals that should trigger re-evaluation

## Common Pitfalls
- Performing the pre-mortem too superficially — treating it as a checkbox rather than genuine stress-testing
- Anchoring on the existing conclusions so strongly that failure modes feel implausible
- Generating only failure modes that are easily dismissed — push for uncomfortable ones
- Skipping the mitigation design step — identifying risks without acting on them is theater
- Not documenting residual risks — stakeholders need to know what uncertainties remain
- Running the pre-mortem too early (before synthesis is complete) or too late (after decisions are locked)

## Related Frameworks
- ralphloop-deepresearch.md (R12: Contrarian Pass is the natural entry point)
- steel-manning.md (steelman the case that the research is wrong)
- epistemic-humility-framework.md (classify residual risks by uncertainty level)
- signal-vs-noise-framework.md (failure modes often stem from noise mistaken for signal)

## Templates (recommended)

### Failure Mode Entry
```
Failure Mode: [description of how the research could be wrong]
Category: [Source / Reasoning / Scope / Model / Temporal / Adversarial / Unknown]
Likelihood: [High / Medium / Low]
Impact: [Critical / Serious / Minor]
Detectability: [Easy / Moderate / Hard]
Priority: [Critical / High / Medium / Low]
```

### Mitigation Plan
```
Failure Mode: [reference]
Mitigation: [specific action to reduce risk]
Owner: [who executes]
Status: [Planned / In Progress / Complete / Not Feasible]
Outcome: [did it change any conclusions?]
```

### Residual Risk Register
```
Risk: [description]
Residual Probability: [estimate]
Monitoring Signal: [what to watch for]
Revisit Trigger: [specific condition that should restart analysis]
```
