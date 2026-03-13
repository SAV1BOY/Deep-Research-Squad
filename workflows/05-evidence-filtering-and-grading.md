# Workflow 05: Evidence Filtering and Grading

## Purpose
Filter collected evidence to remove noise, duplicates, and irrelevant material, then grade each remaining piece using a structured evidence ladder. Assign confidence ratings so downstream synthesis works only with assessed, quality-ranked evidence.

## Trigger
- Unified evidence inventory arrives from Workflow 04.
- New evidence is added during a re-collection cycle and needs assessment.

## Agents Involved
- **Research Lead**: Sets grading standards and reviews edge cases.
- **Evidence Analyst**: Performs filtering and grading.
- **Domain Specialist**: Consulted for domain-specific quality assessment.
- **Quality Auditor**: Spot-checks grading consistency.

## Inputs
- Unified evidence inventory from Workflow 04.
- Evidence ladder framework (grading rubric).
- Subquestion evidence requirements from Workflow 02.
- Source reliability assessments from Workflow 03.

## Steps

1. **Initial triage filter**: Run a fast pass to remove obvious noise:
   - Remove exact duplicates (same source, same content).
   - Remove near-duplicates (same finding from same primary source republished).
   - Remove sources that are clearly off-topic (relevance score < 0.3).
   - Remove sources with broken links, paywalled content without summaries, or corrupted data.
   - Log all removals with reason codes.

2. **Relevance scoring**: For each surviving piece of evidence, score relevance to its assigned subquestion(s) on a 1-5 scale:
   - 5: Directly answers the subquestion with specific data.
   - 4: Strongly relevant, provides important context or supporting evidence.
   - 3: Moderately relevant, useful background.
   - 2: Tangentially relevant, may support synthesis.
   - 1: Marginally relevant, keep only if evidence is scarce.
   - Remove any evidence scoring 1 unless the subquestion is under-collected.

3. **Apply evidence ladder grading**: Grade each piece on the evidence hierarchy:
   - **Grade A (Gold)**: Systematic reviews, meta-analyses, replicated experimental results, official verified datasets.
   - **Grade B (Strong)**: Peer-reviewed studies, government reports with methodology, large-scale surveys with documented methods.
   - **Grade C (Moderate)**: Expert analysis, reputable journalism with named sources, well-documented case studies.
   - **Grade D (Weak)**: Opinion pieces, anecdotal reports, unverified claims from known sources.
   - **Grade E (Provisional)**: Social media, anonymous sources, unverifiable claims. Use only when nothing better exists and flag prominently.

4. **Assess source independence**: Check whether multiple pieces of evidence actually trace back to the same original source. Mark dependent evidence clusters. Adjust effective source count: 5 articles citing the same study count as 1 independent source, not 5.

5. **Bias screening**: For each piece of evidence, check for common biases:
   - **Funding bias**: Is the source funded by a party with a stake in the conclusion?
   - **Selection bias**: Does the source cherry-pick data or examples?
   - **Survivorship bias**: Does the source only consider successes?
   - **Recency bias**: Does the source over-weight recent events?
   - Document identified biases as metadata on the evidence card.

6. **Temporal validation**: Check that evidence is current enough for the research question:
   - Flag evidence older than the relevance window (defined per subquestion).
   - Note if older evidence has been superseded by newer findings.
   - Mark evergreen evidence that remains valid regardless of age.

7. **Cross-reference check**: For high-stakes claims (Grade A and B evidence making strong claims), verify that at least one other independent source corroborates. Flag uncorroborated high-stakes claims for contradiction hunting.

8. **Compile graded evidence registry**: Produce the filtered, graded evidence set:
   - Each piece tagged with: relevance score, evidence grade, independence flag, bias notes, temporal status.
   - Sorted by subquestion, then by grade (highest first).
   - Summary statistics: total pieces per grade, per subquestion.

9. **Evidence sufficiency assessment**: For each subquestion, evaluate:
   - Does the graded evidence meet the minimum threshold from the research plan?
   - Is there sufficient Grade A/B evidence for high-confidence claims?
   - Are there subquestions relying entirely on Grade D/E evidence?
   - Flag insufficient subquestions for re-collection or scope adjustment.

10. **Quality Auditor spot-check**: Quality Auditor reviews a random sample (minimum 20%) of grading decisions. Check for consistency and calibration. If error rate > 10%, re-grade the full set.

## Quality Gates
- All evidence must be graded on both relevance and evidence ladder scales.
- No ungraded evidence may pass to synthesis workflows.
- Source independence must be assessed for every subquestion.
- Bias screening must be documented for all Grade A and B evidence.
- Quality Auditor spot-check must show < 10% error rate.
- Evidence sufficiency assessment must be completed for every subquestion.

## Outputs
- Graded evidence registry (filtered, scored, and annotated).
- Evidence sufficiency report per subquestion.
- Bias screening log.
- Removed evidence log with reason codes.
- Recommendations for re-collection (if gaps found).

## Next Workflow
- **06-contradiction-hunt.md** (hunt for contradictions in the graded evidence).
- **04-collection-sprint.md** (if evidence sufficiency assessment triggers re-collection).
