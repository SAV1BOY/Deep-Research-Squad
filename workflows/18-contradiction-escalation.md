# Workflow 18: Contradiction Escalation

## Purpose
Handle contradictions that cannot be resolved through standard analysis in Workflow 06. When the evidence genuinely conflicts and domain expertise cannot break the tie, escalate to the Research Chief with a structured options package so a judgment call can be made with full transparency about the uncertainty.

## Trigger
- Workflow 06 (Contradiction Hunt) produces unresolved critical contradictions.
- Domain Specialist escalation (Workflow 17) cannot resolve a contradiction.
- Synthesis workflows (09, 10) discover new irreconcilable contradictions.

## Agents Involved
- **Research Lead**: Prepares the escalation package and presents to the Chief.
- **Contradiction Analyst**: Provides the detailed contradiction analysis.
- **Research Chief**: Makes the judgment call on how to handle the contradiction.
- **Quality Auditor**: Ensures the escalation package is complete and fair.

## Inputs
- Unresolved contradiction details from Workflow 06.
- All evidence on both sides of the contradiction with grades and source references.
- Diagnosis of contradiction cause (from Workflow 06 step 5).
- Domain Specialist input (if escalation through Workflow 17 was attempted).
- Impact assessment (how this contradiction affects the research conclusion).

## Steps

1. **Confirm escalation is warranted**: Before escalating, verify:
   - The contradiction is rated as critical severity (affects core findings).
   - Standard resolution methods have been attempted and documented.
   - Domain Specialist input has been sought (or is not applicable).
   - The contradiction genuinely cannot be resolved with available evidence.
   - If any of these are not met, return to Workflow 06 for further analysis.

2. **Build the contradiction dossier**: Compile a complete, balanced package:
   - **Statement of contradiction**: Clear articulation of what conflicts (Claim A vs. Claim B).
   - **Evidence for Claim A**: All supporting evidence with grades, sources, and strengths.
   - **Evidence for Claim B**: All supporting evidence with grades, sources, and strengths.
   - **Diagnosis**: Why the sources disagree (methodological, temporal, definitional, genuine uncertainty).
   - **Impact**: How each side of the contradiction changes the research conclusion.

3. **Present resolution options**: Offer 3-5 structured options for handling the contradiction:
   - **Option 1 - Favor Claim A**: Accept Claim A, state rationale, document risk of being wrong.
   - **Option 2 - Favor Claim B**: Accept Claim B, state rationale, document risk of being wrong.
   - **Option 3 - Present both**: Report both claims with their evidence and let the requester decide.
   - **Option 4 - Conditional framing**: State "If A is true, then X follows; if B is true, then Y follows."
   - **Option 5 - Acknowledge uncertainty**: Mark the area as genuinely uncertain and reduce confidence.
   - For each option, state: impact on research quality, impact on requester decision, and risk.

4. **Provide a recommendation**: Despite the uncertainty, the Research Lead should provide a recommendation:
   - Which option do they lean toward and why?
   - What additional evidence would change their recommendation?
   - What is the worst-case outcome of their recommended option?
   - The recommendation is advisory; the Chief makes the final call.

5. **Quality Auditor fairness check**: Before presenting to the Chief:
   - Verify that both sides of the contradiction are presented with equal depth and care.
   - Verify that no option is framed more favorably than the evidence warrants.
   - Verify that the impact assessment is accurate for all options.
   - Flag any fairness issues for correction.

6. **Present to Research Chief**: Deliver the contradiction dossier in a structured briefing:
   - Start with the statement of contradiction and its impact.
   - Present both sides of the evidence.
   - Walk through the resolution options.
   - Share the Research Lead recommendation.
   - Allow the Chief to ask questions and probe the evidence.

7. **Chief makes judgment call**: The Research Chief selects a resolution option:
   - Documents their reasoning for the selection.
   - Specifies any modifications to the chosen option.
   - Sets the confidence level for the affected findings.
   - Identifies any risk mitigation measures to apply.

8. **Implement the resolution**: Apply the Chief's decision to the research:
   - Update the contradiction map with the resolution and its authority.
   - Adjust synthesis layers (09, 10) to reflect the resolved position.
   - Update confidence levels for affected findings.
   - Add explicit disclosure about the judgment call to the research output.

9. **Document the escalation trail**: Record the complete escalation for transparency:
   - What was the contradiction.
   - What options were considered.
   - What was decided and by whom.
   - What reasoning supported the decision.
   - What risks were accepted.
   - This ensures the research output is honest about where judgment calls were made.

10. **Set review trigger**: Because the resolution involves a judgment call under uncertainty:
    - Set a future date to revisit the contradiction if new evidence emerges.
    - Define what new evidence would trigger a re-evaluation.
    - Add this to the research monitoring queue.

## Quality Gates
- Escalation must be confirmed as warranted (all standard resolution methods exhausted).
- Both sides of the contradiction must be presented with equal evidence depth.
- At least 3 resolution options must be offered.
- Research Lead must provide a recommendation with reasoning.
- Quality Auditor must confirm fairness of presentation.
- Chief's decision must be documented with reasoning and risk acceptance.
- Resolution must include explicit disclosure in the research output.

## Outputs
- Contradiction dossier (complete evidence for both sides).
- Resolution options analysis.
- Chief's decision with documented reasoning.
- Updated contradiction map and synthesis layers.
- Escalation trail documentation.
- Review trigger with re-evaluation criteria.

## Next Workflow
- Return to **09-synthesis-layer-1-certainties.md** or **10-synthesis-layer-2-probabilities.md** (to integrate the resolution).
- **13-audit-before-delivery.md** (escalation must be visible in the audit).
- **15-registry-and-memory-update.md** (log the escalation and judgment call).
