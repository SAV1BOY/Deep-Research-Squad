# Data Researcher Benchmarking Framework

## Purpose

Provide a structured methodology for benchmarking: comparing an entity's performance against relevant peers or standards. Effective benchmarking requires careful peer selection, appropriate metric choice, proper normalization, and contextualized interpretation. The goal is to produce fair, actionable comparisons rather than misleading rankings.

## When to Use

- When evaluating a company, product, or technology against competitors.
- When assessing whether performance is above or below industry norms.
- When identifying best practices by studying top performers.
- When setting targets or goals based on peer performance.
- When a stakeholder asks "How do we compare?" or "Is this good?"

## Inputs

- The entity to be benchmarked (company, product, metric, process).
- Candidate peer set for comparison.
- Metrics to compare, with definitions and data sources.
- Context about the entity's specific circumstances that may affect comparisons.

## Process

1. **Define the benchmarking objective.** What decision will this benchmark inform? What question does it answer?
2. **Select the peer set.** Choose peers that are genuinely comparable. Consider size, geography, industry segment, maturity, and business model. Document selection criteria and justify inclusions and exclusions.
3. **Choose metrics.** Select metrics that are relevant to the objective, measurable, and comparable across peers. Define each metric precisely to ensure apples-to-apples comparison.
4. **Collect data.** Gather metric data for the entity and all peers. Use consistent data sources and time periods. Document data sources and any data gaps.
5. **Normalize data.** Adjust for differences that would make raw comparisons misleading: company size (per-employee, per-revenue), currency, inflation, seasonality, accounting standards.
6. **Compute benchmarks.** Calculate peer group statistics: median, mean, quartiles, range. Position the entity within the distribution.
7. **Contextualize differences.** For each significant deviation from the peer benchmark, investigate why. Is it strategy, capability, circumstance, or measurement artifact?
8. **Identify actionable insights.** What can the entity learn from peers who outperform it? Are there best practices to adopt? Are there structural reasons performance differs?
9. **Validate findings.** Check results for reasonableness. Do outliers reflect real performance or data errors? Would different peer selection change the conclusions?
10. **Present with appropriate caveats.** Deliver benchmarking results with clear documentation of methodology, peer selection rationale, and limitations.

## Outputs

- A peer selection rationale with inclusion and exclusion criteria.
- A benchmarking data table with all metrics for all peers.
- A positioning analysis showing where the entity ranks on each metric.
- Contextual analysis explaining significant deviations.
- Actionable insights and recommendations.
- Methodology documentation and limitations.

## Common Pitfalls

- **Poor peer selection.** Comparing a startup to Fortune 500 companies, or a niche player to mass-market leaders.
- **Metric manipulation.** Choosing metrics that favor the desired conclusion.
- **Normalization failures.** Comparing absolute numbers when relative numbers are appropriate, or vice versa.
- **Survivorship bias.** Benchmarking only against surviving companies, ignoring those that failed.
- **Point-in-time fallacy.** A single benchmark snapshot misses trends and trajectories.
- **Ignoring context.** Treating all deviations from the benchmark as performance gaps when some reflect deliberate strategic choices.
- **Data quality issues.** Using inconsistent definitions or unreliable data sources across peers.
- **Overgeneralizing best practices.** What works for a top performer may not transfer to a different context.

## Related Frameworks

- `data-researcher-base-rate-context.md` - Base rates provide context for interpreting benchmark results.
- `data-researcher-data-quality-check.md` - Ensures benchmarking data meets quality standards.
- `data-researcher-statistical-literacy.md` - Statistical concepts for interpreting benchmark distributions.
- `contrarian-survivorship-audit.md` - Guards against survivorship bias in peer selection.
