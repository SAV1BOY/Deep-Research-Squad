# Wheelan - Naked Statistics: Stripping the Dread from the Data

## Statistics Made Accessible

### Descriptive Statistics
- **Mean**: Average; sensitive to outliers
- **Median**: Middle value; robust to outliers (use for skewed data)
- **Mode**: Most frequent value
- **Standard deviation**: Spread around the mean
- **Percentiles**: Position relative to the whole distribution

### When to Use What
- **Mean**: Symmetric distributions, no extreme outliers
- **Median**: Skewed distributions, income data, house prices
- **Report both**: When they differ significantly, the discrepancy is informative

## The Central Limit Theorem
- Sample means follow a normal distribution regardless of population shape
- Larger samples = narrower distribution of means
- Foundation for confidence intervals and hypothesis tests
- Explains why averages are more predictable than individual observations

## Correlation and Regression

### Correlation Coefficient (r)
- Ranges from -1 to +1
- Measures linear association only
- Does NOT imply causation
- Can be misleading with nonlinear relationships
- Sensitive to outliers

### Regression Analysis
- Predicts outcome from one or more predictors
- R-squared: Proportion of variance explained (0 to 1)
- Coefficients: Effect size of each predictor
- Always check: residual patterns, outlier influence, multicollinearity

### Common Regression Pitfalls
- Omitted variable bias (missing confounder)
- Reverse causation (X predicts Y, but Y causes X)
- Extrapolation beyond data range
- Overfitting with too many predictors

## Probability Concepts

### Conditional Probability
- P(A|B) is not the same as P(B|A)
- "Prosecutor's fallacy": confusing P(evidence|innocent) with P(innocent|evidence)
- Always specify what is conditioned on what

### Bayes' Theorem (Intuitive)
- Prior belief + new evidence = updated belief
- A positive test result does not mean you have the disease (depends on base rate)
- Low base rate + imperfect test = most positives are false positives

## Statistical Significance
- p-value: Probability of seeing this result if the null hypothesis is true
- p < 0.05 does NOT mean 95% probability the effect is real
- Statistical significance is not the same as practical significance
- Large samples can make trivial effects "significant"
- Small samples can miss large effects

## Common Statistical Mistakes
1. Confusing correlation with causation
2. Cherry-picking data or time periods
3. Using inappropriate averages (mean for skewed data)
4. Ignoring base rates
5. Confusing statistical and practical significance
6. Survivorship bias in samples
7. Regression to the mean mistaken for real effects
8. Simpson's paradox (aggregate vs subgroup trends)

## Application to Deep Research
- Always report measures of spread, not just central tendency
- Use medians for skewed business data (revenue, valuations)
- Check for confounders before claiming relationships
- Be cautious about statistical significance with large datasets
- Use base rates as a reality check on any claim
- Present uncertainty explicitly (confidence intervals, ranges)
- Watch for regression to the mean in performance data
