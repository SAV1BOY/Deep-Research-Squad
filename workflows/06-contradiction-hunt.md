# Workflow 06: Contradiction Hunt

## Purpose
Systematically hunt for contradictions within the graded evidence set. Build a contradiction map that exposes where sources disagree, design anti-theses to stress-test key claims, and document unresolved tensions so synthesis does not paper over genuine disagreements.

## Trigger
- Graded evidence registry arrives from Workflow 05.
- Synthesis workflows (09 or 10) discover new contradictions during integration.

## Agents Involved
- **Research Lead**: Reviews contradiction map and decides resolution paths.
- **Contradiction Analyst**: Performs systematic contradiction detection.
- **Devil's Advocate**: Designs anti-theses and stress-tests claims.
- **Domain Specialist**: Consulted when contradictions require domain expertise to evaluate.

## Inputs
- Graded evidence registry from Workflow 05.
- Question tree from Workflow 02.
- Source reliability assessments from Workflow 03.
- Known biases documented during evidence grading.

## Steps

1. **Identify claim clusters**: Group evidence by the claims they support. For each subquestion, list all distinct claims made by the evidence. A claim is a specific factual assertion, causal statement, or evaluative judgment.

2. **Pairwise contradiction scan**: For each subquestion, compare all claim pairs:
   - **Direct contradiction**: Claim A says X, Claim B says not-X.
   - **Quantitative disagreement**: Sources report significantly different numbers for the same metric (>20% variance without explanation).
   - **Causal disagreement**: Sources attribute the same outcome to different causes.
   - **Scope disagreement**: Sources agree on a fact but disagree on its significance or generalizability.
   - Log every detected contradiction with both source references.

3. **Classify contradiction severity**: Rate each contradiction:
   - **Critical**: Contradicts a core finding that would change the research conclusion. Must be resolved.
   - **Significant**: Affects a secondary finding or changes confidence level. Should be resolved.
   - **Minor**: Peripheral disagreement that does not affect the main argument. Document and move on.

4. **Build contradiction map**: Create a structured document showing:
   - Each contradiction with its severity rating.
   - The sources on each side with their evidence grades.
   - The subquestion(s) affected.
   - Visual representation of tension points across the question tree.

5. **Diagnose contradiction causes**: For each critical and significant contradiction, investigate the root cause:
   - **Methodological differences**: Sources used different methods producing different results.
   - **Temporal differences**: Sources measured at different times when conditions changed.
   - **Definitional differences**: Sources define key terms differently.
   - **Sample differences**: Sources studied different populations or datasets.
   - **Genuine uncertainty**: The ground truth is actually unknown or contested.

6. **Design anti-theses**: For the top 3-5 strongest claims in the evidence, design deliberate anti-theses:
   - "What if the opposite were true?"
   - Search for evidence that would support the anti-thesis.
   - If anti-thesis evidence exists, add it to the contradiction map.
   - If no anti-thesis evidence exists, note this as a sign of strong consensus (or potential blind spot).

7. **Attempt resolution**: For each critical and significant contradiction:
   - If cause is methodological: evaluate which method is more rigorous.
   - If cause is temporal: determine which timeframe is more relevant.
   - If cause is definitional: standardize definitions and re-evaluate.
   - If cause is genuine uncertainty: document both positions with confidence levels.
   - Mark resolved, partially resolved, or unresolved.

8. **Assess impact on confidence**: For each subquestion, recalculate confidence considering contradictions:
   - Unresolved critical contradictions reduce confidence by one full tier.
   - Unresolved significant contradictions reduce confidence by half a tier.
   - Resolved contradictions do not affect confidence if resolution is well-supported.

9. **Flag escalation candidates**: Contradictions that remain unresolved after analysis and have critical severity are candidates for escalation. Package these with full context for Workflow 18.

10. **Update evidence registry**: Annotate the evidence registry with contradiction findings:
    - Mark evidence involved in contradictions.
    - Add resolution status to each contradiction.
    - Update confidence levels for affected subquestions.

## Quality Gates
- Every subquestion must undergo pairwise contradiction scan.
- All critical contradictions must have a documented diagnosis and resolution attempt.
- Anti-theses must be designed for at least the top 3 claims.
- Contradiction map must be complete with severity ratings and source references.
- Confidence recalculation must be performed for all affected subquestions.
- Unresolvable critical contradictions must be flagged for escalation.

## Outputs
- Contradiction map (structured document with all contradictions, severities, and resolutions).
- Updated evidence registry with contradiction annotations.
- Revised confidence levels per subquestion.
- Anti-thesis analysis results.
- Escalation candidates list for unresolved critical contradictions.

## Next Workflow
- **07-timeline-and-context-building.md** (build temporal context for the evidence).
- **18-contradiction-escalation.md** (if unresolvable critical contradictions exist).
- **09-synthesis-layer-1-certainties.md** (for resolved evidence ready for synthesis).
