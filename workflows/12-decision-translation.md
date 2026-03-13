# Workflow 12: Decision Translation

## Purpose
Translate the full body of research findings, models, and synthesis into a decision-ready format. Present options with their trade-offs, make explicit recommendations where the evidence supports them, and structure the output so a decision-maker can act without needing to re-analyze the underlying research.

## Trigger
- Models are complete from Workflow 11.
- Layer 1 and Layer 2 synthesis are finalized.
- Research Lead confirms the research is ready for decision translation.

## Agents Involved
- **Research Lead**: Validates that recommendations are evidence-grounded.
- **Decision Translator**: Structures findings into decision format.
- **Synthesis Writer**: Ensures narrative coherence across the translation.
- **Quality Auditor**: Checks that no unsupported claims enter recommendations.

## Inputs
- Layer 1 Synthesis Document from Workflow 09.
- Layer 2 Synthesis Document from Workflow 10.
- Models from Workflow 11 (especially decision matrices and scenario trees).
- Original research question and requester context from Workflow 00.
- Research plan scope from Workflow 01.

## Steps

1. **Revisit the decision context**: Return to the original request and confirm:
   - What decision does the requester need to make?
   - What are their constraints (time, budget, risk tolerance, organizational politics)?
   - What does success look like for them?
   - If the research was exploratory (no specific decision), frame the output as a landscape briefing instead.

2. **Identify decision options**: From the research, extract all viable options or courses of action:
   - Options explicitly found in the evidence.
   - Options implied by the models (scenario paths, matrix alternatives).
   - The "do nothing" option (always include as a baseline).
   - Hybrid options (combinations of pure options).
   - Aim for 3-5 options. Too few limits choice; too many causes paralysis.

3. **Define evaluation criteria**: Establish the criteria by which options will be compared:
   - Extract from the research question and requester context.
   - Include both quantitative criteria (cost, time, probability of success) and qualitative criteria (complexity, reversibility, alignment with values).
   - Weight criteria based on requester priorities. If priorities are unknown, present multiple weighting scenarios.

4. **Score options against criteria**: For each option, assign scores on each criterion:
   - Use evidence from synthesis layers to justify each score.
   - Note the confidence level of each score (certain, probable, speculative).
   - Flag scores where evidence is thin or conflicting.
   - Do not score beyond what the evidence supports.

5. **Analyze trade-offs**: For each pair of top options, articulate the trade-off explicitly:
   - "Option A is better on criterion X but worse on criterion Y."
   - "Choosing Option B means accepting risk Z in exchange for benefit W."
   - Identify if any option dominates (better on all criteria). If so, the recommendation is straightforward.
   - If no option dominates, the trade-off analysis IS the value of the research.

6. **Map risks and uncertainties per option**: For each option, document:
   - Key risks (what could go wrong).
   - Probability of each risk (from Layer 2 or scenario trees).
   - Impact if the risk materializes (from models).
   - Mitigation strategies available.
   - Identify any option with catastrophic downside risk, regardless of expected value.

7. **Formulate recommendations**: Based on the evidence, state recommendations:
   - **Strong recommendation**: When one option clearly outperforms on weighted criteria with high confidence. State: "We recommend X because..."
   - **Conditional recommendation**: When the best option depends on an uncertainty. State: "If condition A holds, we recommend X; if condition B, we recommend Y."
   - **No recommendation**: When evidence is insufficient or options are genuinely equivalent. State: "The evidence does not clearly favor one option. The decision depends on..."
   - Always justify recommendations with specific evidence references.

8. **Build decision brief**: Assemble the decision-ready output:
   - One-paragraph situation summary.
   - Options table with scores and trade-offs.
   - Risk summary per option.
   - Recommendation with confidence level and evidence basis.
   - Key uncertainties that could change the recommendation.
   - Suggested next steps or follow-up research.

9. **Validate no unsupported claims**: Quality Auditor reviews the decision brief:
   - Every score must trace to evidence.
   - Every recommendation must be supported by the analysis.
   - No opinion is presented as fact.
   - Uncertainty is honestly represented.
   - Language matches the confidence level of the evidence.

10. **Tailor to audience**: Adjust the decision brief for the requester's context:
    - Technical requester: include methodology details and data.
    - Executive requester: lead with recommendation, minimize methodology.
    - Cross-functional audience: provide both summary and detailed appendix.

## Quality Gates
- Every option must be scored against every criterion with evidence references.
- Trade-offs must be explicitly stated for all pairs of top options.
- Risks must be documented for every option.
- Recommendations must be classified (strong, conditional, or none) with justification.
- No unsupported claims may appear in the decision brief.
- The "do nothing" baseline must be included.
- Audience tailoring must match the requester profile from Workflow 00.

## Outputs
- Decision brief (options, trade-offs, risks, recommendations).
- Options scoring table with evidence references.
- Risk summary per option.
- Recommendation statement with confidence level.
- Suggested next steps.

## Next Workflow
- **13-audit-before-delivery.md** (final quality audit before sending to requester).
- **14-executive-compression.md** (compress into executive format if needed).
