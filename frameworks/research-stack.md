# Research Stack

## Purpose
A 4-layer pipeline that transforms raw research questions into actionable decisions. Each layer builds on the previous, ensuring systematic progression from exploration to conclusion.

## When to Use
- Starting any new research effort from scratch
- Structuring an ad-hoc investigation into a repeatable process
- When research feels scattered and needs a backbone
- As the default pipeline for all deep research tasks

## Inputs
- A research question or problem statement
- Initial context, constraints, and stakeholder needs
- Available time and resource budget

## Process (step-by-step)

### Layer 1: Discovery
**Inputs:** Raw question, initial context
**Activities:**
1. Define the scope boundary — what is in, what is out
2. Decompose the question into sub-questions
3. Identify candidate source categories (academic, industry, OSINT, expert)
4. Perform broad-sweep searches across source categories
5. Catalogue initial findings without judgment

**Outputs:** Source list, sub-question map, raw evidence pool
**Quality Gate:** At least 3 independent source categories represented. Sub-questions cover the full scope.

### Layer 2: Validation
**Inputs:** Raw evidence pool from Discovery
**Activities:**
1. Verify each claim against its primary source
2. Cross-reference claims across independent sources
3. Identify contradictions and flag them explicitly
4. Assess source credibility (expertise, bias, recency)
5. Rate evidence strength: Strong / Moderate / Weak / Unreliable

**Outputs:** Verified evidence set, contradiction map, credibility ratings
**Quality Gate:** Every key claim has at least 2 independent corroborations or is flagged as single-source.

### Layer 3: Synthesis
**Inputs:** Verified evidence set, contradiction map
**Activities:**
1. Integrate verified evidence into coherent themes
2. Build explanatory models that account for the data
3. Resolve contradictions or document them as open questions
4. Identify implications, second-order effects, and emergent patterns
5. Stress-test models against edge cases

**Outputs:** Integrated analysis, explanatory models, implication map
**Quality Gate:** Models account for at least 90% of verified evidence. Contradictions are resolved or explicitly documented.

### Layer 4: Decision
**Inputs:** Integrated analysis, models, implication map
**Activities:**
1. Generate concrete options or answer candidates
2. Evaluate trade-offs for each option
3. Assign confidence levels using the epistemic humility scale
4. Formulate recommendations with supporting rationale
5. Document what would change the recommendation (reversal conditions)

**Outputs:** Options with trade-offs, ranked recommendations, confidence levels, reversal conditions
**Quality Gate:** Every recommendation has a stated confidence level and at least one reversal condition.

## Outputs
- Structured research deliverable moving from evidence to recommendation
- Clear audit trail from source to conclusion
- Explicit confidence levels and reversal conditions

## Common Pitfalls
- Skipping Validation and jumping from Discovery to Synthesis — leads to unreliable conclusions
- Staying in Discovery too long — diminishing returns after initial broad sweep
- Treating the layers as strictly sequential when iteration is needed — loop back when new evidence emerges
- Omitting reversal conditions — makes recommendations brittle and unfalsifiable
- Conflating evidence strength with conclusion confidence — they are related but distinct

## Related Frameworks
- ralphloop-deepresearch.md (detailed 18-step expansion of this pipeline)
- bayesian-updating.md (for updating beliefs within the Validation layer)
- signal-vs-noise-framework.md (for filtering evidence in Validation)
- epistemic-humility-framework.md (for confidence classification in Decision)

## Templates (recommended)

### Discovery Brief
```
Research Question: [main question]
Sub-questions: [list]
Scope In: [what we cover]
Scope Out: [what we exclude]
Source Categories: [list with rationale]
```

### Validation Log
```
Claim: [statement]
Primary Source: [reference]
Corroboration: [independent sources]
Contradictions: [any conflicting evidence]
Strength: [Strong / Moderate / Weak / Unreliable]
```

### Decision Matrix
```
Option: [description]
Supporting Evidence: [references]
Trade-offs: [pros and cons]
Confidence: [Certain / Probable / Plausible / Speculative]
Reversal Condition: [what would change this recommendation]
```
