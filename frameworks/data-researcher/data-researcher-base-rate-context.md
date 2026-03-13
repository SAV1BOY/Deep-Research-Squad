# Data Researcher Base Rate Context Framework

## Purpose

Always contextualize claims and findings with base rates. A 50% increase from a tiny base is still small. A 1% failure rate in a high-volume system means thousands of failures. This framework ensures that every quantitative finding is anchored in the appropriate base rate, preventing misleading interpretations of percentages, growth rates, and risk figures.

## When to Use

- When presenting or evaluating percentage changes, growth rates, or risk statistics.
- When a claim uses relative terms ("doubled," "surged," "plummeted") without absolute context.
- When comparing rates across entities of very different sizes.
- When assessing the practical significance of a statistically significant finding.
- When evaluating claims about rare events, exceptional performance, or unprecedented results.

## Inputs

- The claim or finding with its stated metric.
- The base value from which the metric is calculated.
- Comparison base rates from relevant reference classes.
- Context about the scale and significance of the absolute numbers.

## Process

1. **Identify the base.** What is the starting point or denominator? A 200% increase means something very different from a base of 10 versus a base of 10 million.
2. **Calculate the absolute change.** Convert relative changes to absolute numbers. "Revenue grew 50%" becomes "Revenue grew from $2M to $3M" or "from $2B to $3B." The absolute number often changes the narrative.
3. **Find the reference class base rate.** What is normal for this type of metric in this domain? If the industry average growth rate is 30%, a 35% growth rate is unremarkable. If the industry average is 3%, a 35% growth rate is extraordinary.
4. **Compare denominators.** When comparing rates across entities, ensure the denominators are comparable. A 0.1% defect rate at a company producing 100 items means something different than at a company producing 10 million items.
5. **Check for small-number effects.** Small bases make percentages volatile and misleading. One additional event in a base of 5 is a 20% increase. The same event in a base of 5000 is a 0.02% increase. Flag any percentage change calculated from a base under a meaningful threshold.
6. **Apply the "so what" test.** Translate the finding into practical terms. "A 40% reduction in risk" from 0.005% to 0.003% means 2 fewer occurrences per 100,000. Is that actionable?
7. **Provide multiple framings.** Present the finding in both relative and absolute terms. Include the base rate comparison. Let the audience see all three framings before drawing conclusions.
8. **Flag missing bases.** When a source reports only relative changes without base rates, flag this as a significant omission. Relative numbers without bases are incomplete at best and manipulative at worst.
9. **Historical base rate trend.** Is the base rate itself changing? A growth rate that looks strong against last year's base may look weak against a five-year trend.
10. **State the contextualized finding.** Rewrite the finding with full base rate context. This is the version that should appear in the research output.

## Outputs

- The original finding restated with absolute numbers and base rates.
- Reference class comparison showing where this finding sits relative to norms.
- A practical significance assessment (does this matter in real-world terms?).
- Flagged instances of missing or misleading base rate reporting.
- A contextualized version of the finding suitable for the research deliverable.
- Multiple framings (relative, absolute, comparative) for key findings.

## Common Pitfalls

- **Headline number bias.** Leading with dramatic-sounding percentages that dissolve when the base is revealed.
- **Denominator neglect.** Ignoring the size of the base entirely and treating all percentages as equivalent.
- **Cherry-picking the base period.** Choosing a base period that makes the change look more dramatic (e.g., measuring from a temporary trough).
- **Mixing relative and absolute selectively.** Using relative numbers when they sound impressive and absolute numbers when those sound impressive.
- **Ignoring base rate changes.** The base itself may have shifted due to definitional changes, population growth, or methodology updates.
- **Assuming linear scaling.** A percentage change at one scale does not necessarily apply at a different scale.
- **Neglecting risk base rates.** Presenting risk increases without noting how rare the event is in the first place.
- **Forgetting compounding.** Small percentage changes compound over time; a 2% annual difference becomes large over decades.

## Related Frameworks

- `contrarian-base-rate-override.md` - Strategic use of base rates to evaluate exceptional claims.
- `data-researcher-statistical-literacy.md` - Base rate reasoning is a core statistical literacy concept.
- `data-researcher-benchmarking.md` - Benchmarks provide the reference base rates for comparison.
- `data-researcher-time-series.md` - Base rates change over time; time series analysis tracks this evolution.
