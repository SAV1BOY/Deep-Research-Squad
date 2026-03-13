# Workflow 07: Timeline and Context Building

## Purpose
Build a comprehensive timeline of events relevant to the research question. Establish temporal context that reveals how the situation evolved, verify causal claims by checking temporal ordering, and provide the chronological backbone that synthesis workflows need to construct accurate narratives.

## Trigger
- Graded evidence registry and contradiction map are available from Workflows 05 and 06.
- A synthesis workflow requests temporal context for a specific subquestion.

## Agents Involved
- **Research Lead**: Reviews the timeline for completeness and accuracy.
- **Timeline Analyst**: Constructs and validates the chronological record.
- **Data Analyst**: Provides quantitative time-series data to anchor the timeline.
- **Domain Specialist**: Validates domain-specific temporal relationships.

## Inputs
- Graded evidence registry from Workflow 05.
- Contradiction map from Workflow 06.
- Question tree from Workflow 02.
- Any time-series datasets collected during Workflow 04.

## Steps

1. **Extract temporal claims**: Scan all graded evidence for temporal information:
   - Specific dates and date ranges mentioned.
   - Relative time references ("after the regulation passed," "before the merger").
   - Duration claims ("lasted 3 months," "took 2 years to implement").
   - Sequence claims ("A happened before B," "C caused D").
   - Log each temporal claim with its source reference and evidence grade.

2. **Establish anchor events**: Identify the major anchor events that structure the timeline:
   - Events with confirmed, specific dates from Grade A/B sources.
   - Regulatory or legal milestones with official dates.
   - Market events or data releases with timestamps.
   - These anchors form the skeleton of the timeline.

3. **Place relative events**: Position events that have only relative timestamps by triangulating against anchor events. Document the reasoning and confidence level for each placement. Flag events that cannot be reliably placed.

4. **Build master timeline**: Construct a chronological timeline document:
   - Use consistent time granularity (daily, monthly, quarterly, or yearly based on research scope).
   - Include event description, date/date range, source reference, and confidence level.
   - Mark gaps where significant time passes without documented events.
   - Annotate with data trends (quantitative overlays) where available.

5. **Verify causal ordering**: For every causal claim in the evidence ("A caused B"), verify:
   - A occurred before B (temporal precedence).
   - The time gap between A and B is plausible for the claimed mechanism.
   - No confounding event C occurred between A and B that could better explain B.
   - Rate causal claim validity: confirmed, plausible, questionable, or refuted.

6. **Identify temporal patterns**: Look for recurring patterns in the timeline:
   - Cyclical patterns (seasonal, annual, election-cycle driven).
   - Acceleration or deceleration trends.
   - Clustering of events (multiple things happening in a short window).
   - Suspicious gaps (periods where evidence goes silent).
   - Document patterns with supporting data.

7. **Contextualize with external events**: Overlay relevant external events that are not directly part of the research but may have influenced outcomes:
   - Economic conditions (recessions, booms, market shifts).
   - Political events (elections, policy changes, geopolitical events).
   - Technological changes (new tools, platforms, disruptions).
   - This context helps explain anomalies and strengthens causal analysis.

8. **Cross-reference with contradiction map**: Check whether any contradictions from Workflow 06 can be explained by temporal factors:
   - Sources may contradict because they describe different time periods.
   - Data may disagree because conditions changed between measurement points.
   - Update contradiction resolutions where temporal context provides the explanation.

9. **Create temporal context summary**: Write a narrative summary of the timeline that highlights:
   - Key inflection points where the situation changed significantly.
   - The overall trajectory (improving, worsening, oscillating, stable).
   - Critical time dependencies that synthesis must respect.
   - Causal chains that have been verified or refuted.

10. **Flag temporal uncertainties**: Document all remaining temporal uncertainties:
    - Events with uncertain dates or ordering.
    - Causal claims that could not be verified or refuted.
    - Gaps in the timeline that may hide important developments.
    - Recommend targeted collection to fill critical gaps.

## Quality Gates
- Every causal claim in the evidence must be checked for temporal precedence.
- Anchor events must be sourced from Grade A/B evidence only.
- Timeline gaps longer than the relevant time granularity must be flagged and explained.
- At least one external context layer must be overlaid.
- Temporal context summary must explicitly state the overall trajectory.
- All temporal uncertainties must be documented with impact assessment.

## Outputs
- Master timeline document (chronological record with annotations).
- Causal claim verification results.
- Temporal pattern analysis.
- Temporal context summary narrative.
- Updated contradiction resolutions (where temporal context resolved contradictions).
- Temporal uncertainty register.

## Next Workflow
- **08-data-benchmarking.md** (benchmark data points using temporal context).
- **09-synthesis-layer-1-certainties.md** (provide timeline to synthesis as contextual input).
