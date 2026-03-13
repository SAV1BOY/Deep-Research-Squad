# Data Researcher Data Quality Check Framework

## Purpose

Assess the quality of data before using it for analysis or conclusions. Poor data quality is one of the most common and most damaging sources of research error. This framework provides a systematic approach to evaluating data across five dimensions: completeness, accuracy, consistency, timeliness, and validity. Every dataset used in research should pass through this check.

## When to Use

- Before starting any analysis that depends on a dataset.
- When data comes from a new, unfamiliar, or unverified source.
- When findings seem surprising, as the surprise may be a data quality artifact.
- When combining data from multiple sources that may use different standards.
- As a mandatory step in any research workflow before drawing conclusions.

## Inputs

- The dataset to be assessed.
- Documentation about the dataset: source, collection method, definitions, known limitations.
- Context about how the data will be used and what decisions depend on it.
- Comparison data or benchmarks for validation, if available.

## Process

1. **Assess completeness.** What percentage of expected records are present? Are there missing values, and if so, are they random or systematic? Are there entire categories, time periods, or populations that are absent? Missing data is not neutral; it biases results.
2. **Assess accuracy.** Are the values correct? Cross-reference a sample against independent sources. Look for values that are implausible (negative ages, future dates, impossible magnitudes). Check for data entry errors, transcription errors, and unit mismatches.
3. **Assess consistency.** Is the same thing measured the same way throughout the dataset? Check for definitional changes over time. Look for inconsistencies between related fields (e.g., a city in the wrong country). Ensure categorical values are standardized (no mix of "US," "USA," "United States").
4. **Assess timeliness.** How current is the data? Is it recent enough for the intended use? How frequently is it updated? Is there a lag between events and recording? Stale data can be worse than no data if it creates false confidence.
5. **Assess validity.** Does the data actually measure what it claims to measure? A "customer satisfaction" score based on a single question may not validly measure satisfaction. Check whether the measurement instrument is appropriate for the construct.
6. **Check for known biases.** Does the data collection method introduce systematic biases? Self-reported data, voluntary surveys, and opt-in samples all have known biases. Selection bias, response bias, and measurement bias should be identified.
7. **Examine outliers.** Identify extreme values. Determine whether they are genuine, errors, or artifacts. Document how outliers will be handled.
8. **Test transformations.** If the data has been cleaned, aggregated, or transformed, verify that transformations were applied correctly. Check that aggregation did not introduce errors.
9. **Document findings.** Produce a data quality report summarizing findings across all dimensions with an overall quality rating.
10. **Decide on fitness for use.** Based on the assessment, determine whether the data is fit for the intended purpose. If not, document what must be addressed before the data can be used.

## Outputs

- A data quality scorecard across the five dimensions (completeness, accuracy, consistency, timeliness, validity).
- Specific issues identified with examples and severity ratings.
- Missing data analysis showing patterns and potential impact.
- Outlier catalog with classification (genuine, error, artifact).
- An overall fitness-for-use determination.
- Recommended remediation steps for significant issues.

## Common Pitfalls

- **Skipping the check.** Assuming data quality because the source seems reputable.
- **Checking once.** Data quality can degrade over time; periodic reassessment is needed.
- **Fixing without documenting.** Making corrections without recording what was changed and why.
- **Ignoring systematic missingness.** Missing data that correlates with the variable of interest biases all results.
- **Over-cleaning.** Removing outliers or "anomalies" that are actually real and informative.
- **Trusting aggregated data.** Aggregation can mask underlying quality issues present in granular data.
- **Assuming consistency across sources.** Merging data from different sources without checking that definitions and methods align.
- **Not checking units.** Mixing units (millions vs. thousands, USD vs. EUR, metric vs. imperial) is surprisingly common.

## Related Frameworks

- `data-researcher-benchmarking.md` - Benchmarking depends on comparable, quality data across peers.
- `data-researcher-time-series.md` - Time series analysis is especially sensitive to data quality issues.
- `data-researcher-statistical-literacy.md` - Statistical conclusions are only as good as the data they rest on.
- `osint-digital-footprint-mapping.md` - OSINT data requires quality assessment before drawing conclusions.
