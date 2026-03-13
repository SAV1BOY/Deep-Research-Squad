# Data Researcher Time Series Analysis Framework

## Purpose

Provide a structured approach to analyzing data over time. Identify trends, seasonality, anomalies, and structural breaks. Time series analysis transforms a sequence of data points into actionable insights about patterns, turning points, and trajectory. This framework is designed for research analysts, not statisticians, emphasizing interpretation over mathematical technique.

## When to Use

- When analyzing any metric that changes over time (revenue, usage, sentiment, market share).
- When asked to identify trends, patterns, or turning points in historical data.
- When forecasting or projecting future values based on historical patterns.
- When comparing performance across time periods.
- When investigating whether a change or event had a measurable impact.

## Inputs

- A time-ordered dataset with consistent measurement intervals.
- Context about what the data measures and how it was collected.
- Knowledge of external events that may have influenced the data.
- The time period of interest and the granularity needed (daily, monthly, quarterly, annual).

## Process

1. **Inspect the raw data.** Plot the data. Look at it visually before computing anything. Note obvious patterns, gaps, and outliers.
2. **Check data quality.** Identify missing values, inconsistent intervals, measurement changes, and definitional shifts. Address or document these before analysis.
3. **Identify the trend.** Is there a long-term upward, downward, or flat trajectory? Separate the trend from shorter-term fluctuations using moving averages or similar smoothing.
4. **Identify seasonality.** Are there recurring patterns at regular intervals (weekly, monthly, quarterly, annual)? Quantify the seasonal pattern.
5. **Identify cyclical patterns.** Are there longer-term cycles beyond seasonality? These may correspond to business cycles, product lifecycles, or industry dynamics.
6. **Detect anomalies.** Identify data points that deviate significantly from the expected pattern. Investigate each anomaly: is it a data error, an external event, or a genuine signal?
7. **Detect structural breaks.** Has the underlying pattern changed at some point? A structural break means the rules governing the data shifted. Look for changes in level, trend slope, or volatility.
8. **Correlate with external events.** Map known events (product launches, policy changes, market events, competitor actions) onto the timeline. Assess whether they coincide with observed changes.
9. **Decompose the series.** Mentally or computationally separate the data into trend, seasonal, cyclical, and residual components to understand what drives observed values.
10. **Synthesize and project.** State the key findings: What is the trajectory? Are there inflection points? What are plausible future scenarios based on the patterns identified?

## Outputs

- A visual plot of the time series with annotations for key events and anomalies.
- Trend assessment: direction, strength, and any changes in trend.
- Seasonality description: pattern, amplitude, and consistency.
- Anomaly catalog with explanations.
- Structural break identification with potential causes.
- Plausible future scenarios based on observed patterns (with caveats).

## Common Pitfalls

- **Extrapolating trends indefinitely.** Trends change; projecting a straight line into the future ignores structural breaks and mean reversion.
- **Confusing noise with signal.** Short-term fluctuations may be random variation, not meaningful patterns.
- **Ignoring base effects.** Percentage changes from small bases look dramatic but may be insignificant.
- **Survivorship bias in historical data.** If the data source changed composition over time, comparisons may be invalid.
- **Confusing correlation with causation.** Two series moving together does not mean one causes the other.
- **Inconsistent measurement.** Definition changes, methodology shifts, or data source switches can create artificial patterns.
- **Overfitting.** Finding complex patterns in limited data that do not hold going forward.
- **Ignoring the denominator.** Absolute numbers may rise simply because the population or market grew.

## Related Frameworks

- `data-researcher-benchmarking.md` - Time series can be benchmarked against peer time series.
- `data-researcher-statistical-literacy.md` - Statistical concepts for interpreting time series results.
- `data-researcher-data-quality-check.md` - Data quality is especially critical for time series where small errors compound.
- `osint-social-listening.md` - Sentiment time series from social listening benefit from this framework.
