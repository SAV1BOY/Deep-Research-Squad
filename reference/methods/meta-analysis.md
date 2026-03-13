# Meta-Analysis

## Overview
Meta-analysis is a statistical method for combining results from multiple independent studies to produce a pooled effect estimate. Provides more precise and reliable estimates than individual studies. The quantitative component of a systematic review.

## Core Concepts

### Effect Sizes
- **Standardized Mean Difference (Cohen's d)**: Comparing means between groups
  - Small: 0.2, Medium: 0.5, Large: 0.8
- **Odds Ratio (OR)**: Binary outcome comparisons
- **Risk Ratio (RR)**: Relative risk between groups
- **Correlation (r)**: Relationship strength between variables
- Effect sizes allow comparison across studies using different scales

### Fixed vs. Random Effects Models
- **Fixed-effect**: Assumes one true effect size; differences are sampling error only
- **Random-effects**: Assumes true effect varies across studies; includes between-study variance
- Random-effects is almost always more appropriate (and more conservative)

### Heterogeneity
- **Q statistic**: Tests whether studies share a common effect size
- **I-squared (I2)**: Percentage of variability due to true heterogeneity vs. chance
  - 0-25%: Low, 25-75%: Moderate, 75-100%: High
- **Tau-squared**: Estimate of between-study variance
- High heterogeneity suggests moderator analysis is needed

### Moderator Analysis
- Subgroup analysis: Compare effect sizes across categorical moderators
- Meta-regression: Continuous moderators predicting effect size variation
- Helps explain WHY effects differ across studies

## Key Steps
1. Define inclusion criteria precisely (PICO framework)
2. Comprehensive literature search with documented strategy
3. Study selection with inter-rater reliability check
4. Data extraction and quality assessment (e.g., Cochrane Risk of Bias)
5. Effect size calculation and pooling
6. Heterogeneity assessment and moderator analysis
7. Publication bias assessment (funnel plot, Egger's test, trim-and-fill)
8. Sensitivity analysis (leave-one-out, quality-stratified)

## Publication Bias Detection
- **Funnel plot**: Scatter plot of effect size vs. precision; asymmetry suggests bias
- **Egger's test**: Statistical test for funnel plot asymmetry
- **Trim-and-fill**: Imputes "missing" studies to estimate adjusted effect
- **p-curve analysis**: Tests whether significant results reflect true effects

## Strengths
- Increases statistical power through combined sample sizes
- Provides precise pooled effect estimate with confidence interval
- Identifies patterns across studies through moderator analysis
- Transparent and reproducible methodology

## Limitations
- "Garbage in, garbage out" - quality depends on included studies
- Combining heterogeneous studies can be misleading
- Publication bias inflates pooled estimates
- Requires sufficient number of comparable studies

## Application to Deep Research
- Look for existing meta-analyses as highest-quality evidence on a topic
- When multiple studies disagree, mentally estimate the "pooled" direction
- Pay attention to heterogeneity - high I2 means context matters greatly
- Check for publication bias assessment in any meta-analysis you cite
- Use meta-analytic thinking: weight evidence by quality and precision

## Key References
- Borenstein, M. et al. (2021). *Introduction to Meta-Analysis*. 2nd ed. Wiley.
- Higgins, J.P.T. et al. (Eds.). *Cochrane Handbook for Systematic Reviews of Interventions*.
- Cooper, H. et al. (Eds.) (2019). *The Handbook of Research Synthesis and Meta-Analysis*. 3rd ed. Russell Sage.
