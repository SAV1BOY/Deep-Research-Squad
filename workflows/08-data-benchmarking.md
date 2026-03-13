# Workflow 08: Data Benchmarking

## Purpose
Collect relevant benchmarks, compare quantitative data across sources, and contextualize findings with base rates and reference points. Ensure that numbers cited in the research are meaningful by placing them in proper comparative context rather than presenting them in isolation.

## Trigger
- Graded evidence with quantitative data is available from Workflow 05.
- Timeline and context are established from Workflow 07.
- A synthesis workflow requests comparative context for specific data points.

## Agents Involved
- **Research Lead**: Approves benchmark selections and contextualization approach.
- **Data Analyst**: Performs benchmarking analysis and statistical comparisons.
- **Literature Analyst**: Provides published benchmark references.
- **Domain Specialist**: Validates domain-appropriate benchmarks and base rates.

## Inputs
- Graded evidence registry (quantitative subset) from Workflow 05.
- Master timeline from Workflow 07.
- Question tree from Workflow 02.
- Benchmark database (reference datasets, industry standards, historical baselines).

## Steps

1. **Extract quantitative claims**: Identify all numerical data points and quantitative claims from the graded evidence:
   - Absolute numbers (revenue, counts, measurements).
   - Rates and percentages (growth rates, adoption rates, error rates).
   - Ratios and comparisons (market share, efficiency metrics).
   - Indexes and composite scores.
   - Log each with its source, evidence grade, and the subquestion it addresses.

2. **Identify benchmark needs**: For each quantitative claim, determine what comparison is needed to make it meaningful:
   - Historical comparison (what was it before?).
   - Peer comparison (what are others achieving?).
   - Standard comparison (what is the industry norm or regulatory threshold?).
   - Theoretical comparison (what is the theoretical maximum or minimum?).
   - Base rate comparison (what would we expect by chance or default?).

3. **Source benchmarks**: For each needed comparison, find the appropriate benchmark:
   - Search the benchmark database for existing reference points.
   - Extract benchmarks from collected evidence (comparative data already in hand).
   - Source new benchmarks from standard references (industry reports, government statistics, academic baselines).
   - Document the provenance of each benchmark used.

4. **Validate benchmark relevance**: Ensure each benchmark is a fair comparison:
   - **Apples to apples**: Are the same things being measured in the same way?
   - **Same timeframe**: Is the benchmark from a comparable time period?
   - **Same scope**: Is the benchmark from a comparable geography, market, or population?
   - **Same methodology**: Were the same measurement methods used?
   - Flag any benchmarks that are approximate rather than exact comparisons.

5. **Perform comparative analysis**: For each data point with its benchmark:
   - Calculate the absolute difference and percentage difference.
   - Determine if the difference is statistically significant (where applicable).
   - Classify the finding: above benchmark, at benchmark, below benchmark.
   - Note the trend direction (improving, worsening, stable relative to benchmark).

6. **Contextualize with base rates**: For claims involving probabilities or rates:
   - Identify the relevant base rate (what happens by default without intervention).
   - Calculate how much the observed rate deviates from the base rate.
   - Assess whether the deviation is meaningful or within normal variation.
   - This prevents the base rate fallacy in synthesis.

7. **Normalize across sources**: When multiple sources report the same metric differently:
   - Identify unit differences and convert to common units.
   - Identify methodology differences and note caveats.
   - Present a normalized range rather than a single point estimate.
   - Calculate the spread and assess whether sources meaningfully agree or disagree.

8. **Build benchmark summary table**: Create a structured comparison document:
   | Data Point | Value | Source | Benchmark | Benchmark Source | Difference | Classification | Confidence |
   - Sort by subquestion.
   - Highlight any data points that are significantly above or below benchmarks.

9. **Identify outliers and anomalies**: Flag data points that are:
   - More than 2 standard deviations from benchmarks.
   - Inconsistent with the temporal trend from Workflow 07.
   - Suspiciously round numbers (potential estimates rather than measurements).
   - Investigate outliers: are they errors, real anomalies, or evidence of something important?

10. **Produce benchmarking narrative**: Write a concise narrative that translates the numbers into meaning:
    - "Metric X is 30% above the industry average, suggesting strong performance."
    - "Rate Y is within normal variation of the base rate, suggesting no significant effect."
    - This narrative feeds directly into synthesis workflows.

## Quality Gates
- Every quantitative claim used in synthesis must have at least one benchmark comparison.
- Benchmark relevance must be validated (apples-to-apples check) for all comparisons.
- Base rates must be identified for all probability and rate claims.
- Outliers must be investigated and explained or flagged.
- Benchmark summary table must be complete with no missing fields.
- Sources of all benchmarks must be documented with evidence grades.

## Outputs
- Benchmark summary table (all data points with comparisons).
- Benchmarking narrative (plain-language interpretation).
- Outlier and anomaly report.
- Normalized data ranges for multi-source metrics.
- Base rate reference sheet.

## Next Workflow
- **09-synthesis-layer-1-certainties.md** (feed benchmarked data into high-confidence synthesis).
- **10-synthesis-layer-2-probabilities.md** (feed uncertain comparisons into probability synthesis).
