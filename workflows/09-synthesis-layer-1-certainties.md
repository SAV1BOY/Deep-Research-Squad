# Workflow 09: Synthesis Layer 1 - Certainties

## Purpose
Synthesize what we know for certain based on the collected, filtered, and graded evidence. This layer captures only high-confidence findings where the evidence is strong, consistent, and corroborated. It forms the factual foundation upon which all further analysis, probability assessments, and recommendations are built.

## Trigger
- Evidence grading (Workflow 05), contradiction analysis (Workflow 06), timeline (Workflow 07), and benchmarking (Workflow 08) are complete.
- A re-synthesis is triggered after new high-grade evidence is added.

## Agents Involved
- **Research Lead**: Reviews and approves certainty classifications.
- **Synthesis Writer**: Drafts the certainty layer narrative.
- **Evidence Analyst**: Provides evidence backing for each certainty claim.
- **Quality Auditor**: Validates that certainty standards are met.

## Inputs
- Graded evidence registry from Workflow 05.
- Contradiction map (resolved contradictions only) from Workflow 06.
- Master timeline from Workflow 07.
- Benchmark summary from Workflow 08.
- Confidence thresholds from the research plan (Workflow 01).

## Steps

1. **Define certainty threshold**: Establish what qualifies as "certain" for this research:
   - Minimum evidence grade: Grade A or B only.
   - Minimum corroboration: At least 2 independent sources agreeing.
   - No unresolved contradictions affecting the claim.
   - Confidence level >= 90%.
   - Document these thresholds for transparency.

2. **Identify certainty candidates**: Scan the evidence registry for claims that meet the threshold:
   - Claims supported by Grade A/B evidence from multiple independent sources.
   - Claims with no contradictions or only resolved contradictions.
   - Quantitative claims validated by benchmarking.
   - Causal claims verified by timeline analysis.

3. **Validate each candidate**: For every certainty candidate, run a validation check:
   - **Source check**: Confirm sources are truly independent (not circular citations).
   - **Methodology check**: Confirm the underlying methods are sound.
   - **Recency check**: Confirm the evidence is current and not superseded.
   - **Scope check**: Confirm the claim applies within the scope of the research question.
   - Reject candidates that fail any check. Demote them to Layer 2 (probabilities).

4. **Structure certainties by subquestion**: Organize validated certainties under their respective subquestions from the question tree. For each subquestion, list:
   - The certain findings (stated as clear, unambiguous claims).
   - The evidence backing (source references with grades).
   - The corroboration count (number of independent sources).

5. **Write certainty statements**: Draft each certainty as a precise, falsifiable statement:
   - Use clear, unambiguous language.
   - Include quantification where possible ("increased by 25%" not "increased significantly").
   - State the scope and time period the certainty applies to.
   - Avoid hedging language (no "probably," "likely," "seems to").
   - If hedging feels necessary, the claim belongs in Layer 2, not Layer 1.

6. **Build the evidence chain for each certainty**: For every certainty statement, document the full evidence chain:
   - Primary source(s) with publication details.
   - Corroborating source(s) with publication details.
   - How contradictions were resolved (if any existed).
   - Benchmark context (how the data compares).
   - Timeline context (when the finding applies).

7. **Test for over-certainty**: Challenge each certainty with a calibration question:
   - "Would I bet significant resources on this being true?"
   - "If this turned out to be wrong, would it be surprising?"
   - If the answer to either is "not really," demote to Layer 2.

8. **Identify certainty gaps**: For each subquestion, assess:
   - Are there subquestions with NO certainties? (These are high-uncertainty zones.)
   - Are there subquestions where all findings are certain? (Check for confirmation bias.)
   - Document the gap pattern as input for the probability layer.

9. **Compile Layer 1 synthesis document**: Assemble the complete certainty layer:
   - Executive summary of all certain findings (bulleted list).
   - Detailed section per subquestion with evidence chains.
   - Certainty gap analysis.
   - Visual: certainty coverage map across the question tree.

10. **Research Lead and Auditor review**: Both review the Layer 1 document:
    - Research Lead checks for completeness and alignment with research question.
    - Quality Auditor checks that every certainty meets the defined threshold.
    - Reject or demote any certainties that do not pass review.
    - Approve the final Layer 1 document.

## Quality Gates
- Every certainty must be backed by at least 2 independent Grade A/B sources.
- No certainty may have an unresolved contradiction.
- Every certainty must be stated as a precise, falsifiable claim.
- Over-certainty calibration must be performed for all claims.
- Certainty gaps must be documented for all subquestions.
- Both Research Lead and Quality Auditor must approve before Layer 1 is finalized.

## Outputs
- Layer 1 Synthesis Document (certain findings with evidence chains).
- Certainty coverage map (visual showing which subquestions have certainties).
- Certainty gap analysis (subquestions lacking high-confidence findings).
- Demoted claims list (candidates that did not meet certainty threshold, forwarded to Layer 2).

## Next Workflow
- **10-synthesis-layer-2-probabilities.md** (synthesize probable findings from remaining evidence).
- **11-model-building.md** (use certainties as inputs for model construction).
