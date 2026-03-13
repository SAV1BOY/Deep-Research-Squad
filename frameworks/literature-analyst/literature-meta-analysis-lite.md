# Literature Meta-Analysis Lite Framework

## Purpose

Conduct a pragmatic meta-analysis without heavy statistical machinery. Aggregate findings from multiple sources, note the direction and strength of each finding, identify patterns across studies, and produce a synthesis that is more rigorous than a narrative review but more accessible than a formal statistical meta-analysis. This is designed for research contexts where formal meta-analysis is impractical but structured synthesis is essential.

## When to Use

- When multiple sources address the same question but a formal meta-analysis is infeasible.
- When source types are heterogeneous (mixing quantitative studies, qualitative reports, industry analyses).
- When time constraints prevent full statistical meta-analysis.
- When the audience needs a clear synthesis rather than statistical tables.
- When the goal is to identify the overall direction and consistency of findings.

## Inputs

- A set of sources addressing the same research question (ideally from a systematic review).
- Extracted findings from each source, including direction (positive, negative, null), magnitude, and confidence.
- Quality assessments for each source.
- Context about how each source measured its outcomes.

## Process

1. **Define the question precisely.** What specific claim or relationship is being aggregated across sources?
2. **Standardize findings.** Express each source's finding in a common format: direction (supports, contradicts, neutral), strength (strong, moderate, weak), and quality (high, medium, low).
3. **Create the evidence table.** Build a table with columns: Source, Finding Direction, Finding Strength, Source Quality, Sample/Scope, Key Caveats.
4. **Count the vote.** Tally how many sources support, contradict, or are neutral on the claim. Weight by quality.
5. **Assess consistency.** Are findings consistent across sources, or do they diverge? If divergent, identify what explains the divergence (different methods, populations, time periods, definitions).
6. **Identify dose-response or gradient patterns.** Do stronger versions of the independent variable produce stronger effects? This strengthens causal inference.
7. **Check for publication bias signals.** Are there signs that negative or null findings are underrepresented? Are the positive findings suspiciously uniform?
8. **Synthesize the overall finding.** State the aggregate conclusion: What does the preponderance of evidence suggest? At what confidence level?
9. **Note heterogeneity.** If findings diverge, document the heterogeneity and what might explain it. Do not force a single conclusion on genuinely mixed evidence.
10. **State limitations of the lite approach.** Acknowledge that this is not a formal meta-analysis and note what a formal analysis might reveal.

## Outputs

- A structured evidence table with all sources and their findings.
- An aggregate finding with direction, strength, and confidence level.
- An assessment of consistency and heterogeneity across sources.
- Identified moderators or explanations for divergent findings.
- Publication bias indicators.
- Stated limitations and recommendations for formal analysis if warranted.

## Common Pitfalls

- **Treating vote counting as definitive.** Simple tallies do not account for sample size, effect size, or study quality.
- **Ignoring heterogeneity.** Averaging across genuinely different findings produces a misleading result.
- **Equal weighting.** Not all sources deserve equal weight; quality and relevance matter.
- **Overstating precision.** A lite meta-analysis produces directional findings, not precise effect sizes.
- **Cherry-picking for the synthesis.** Including or excluding sources to steer the aggregate finding.
- **Mixing apples and oranges.** Aggregating findings that measure different things under the same label.
- **Neglecting context.** Findings from different contexts may not be comparable even if they use the same terms.

## Quality Criteria

- The evidence table must include every source meeting inclusion criteria, with no selective omission.
- Quality weighting must be explicit: state how source quality affected the aggregate finding.
- Heterogeneity must be addressed directly; do not present a single conclusion when findings genuinely diverge.
- Limitations of the lite approach must be stated in the final output, not buried or omitted.

## Related Frameworks

- `literature-systematic-review.md` - Provides the source set for meta-analysis.
- `literature-gap-mapping.md` - Meta-analysis reveals where evidence is strong versus where gaps exist.
- `literature-taxonomy-builder.md` - The taxonomy organizes findings into meaningful categories for aggregation.
- `data-researcher-statistical-literacy.md` - Statistical concepts relevant to interpreting aggregated findings.
