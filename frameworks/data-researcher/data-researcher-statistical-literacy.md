# Data Researcher Statistical Literacy Framework

## Purpose

Provide a reference for key statistical concepts that every research analyst should understand and apply. This is not a statistics textbook but a practical guide to the concepts most frequently misunderstood or misapplied in research: correlation versus causation, p-values, confidence intervals, sample size, base rates, and effect sizes. The goal is to prevent common statistical errors in research conclusions.

## When to Use

- When evaluating claims supported by statistical evidence.
- When reviewing research that reports p-values, confidence intervals, or correlations.
- When assessing whether a sample is large enough to support a conclusion.
- When a research finding seems statistically significant but practically meaningless, or vice versa.
- As a checklist before finalizing any research that involves quantitative evidence.

## Inputs

- Research claims with statistical support.
- Data summaries, study results, or statistical test outputs.
- Context about the domain, decisions at stake, and audience.

## Process

1. **Check correlation versus causation.** If a relationship is reported, determine whether it is correlational or causal. Correlation means two variables move together; causation means one actually drives the other. Ask: Is there a plausible mechanism? Have confounders been controlled? Is there experimental evidence?
2. **Interpret p-values correctly.** A p-value is the probability of observing data this extreme if the null hypothesis were true. It is NOT the probability that the hypothesis is true. A p < 0.05 does not mean the finding is important. Check: Was the threshold set before analysis? Were multiple comparisons made? Is this a single study or replicated?
3. **Examine confidence intervals.** A 95% confidence interval means that if the study were repeated many times, 95% of intervals would contain the true value. Look at the width of the interval: a wide interval means high uncertainty. Does the interval include zero or other critical values?
4. **Assess sample size.** Small samples produce unreliable estimates with wide confidence intervals. Large samples can make trivial effects statistically significant. Ask: Is the sample large enough for the claimed precision? Is the sample representative of the population of interest?
5. **Evaluate effect size.** Statistical significance tells you whether an effect exists; effect size tells you whether it matters. A study can show p < 0.001 for a difference so small it has no practical importance. Always ask: How large is the effect in real-world terms?
6. **Apply base rate thinking.** Before accepting a finding, consider the base rate. If 1 in 1000 people has a condition and a test is 99% accurate, a positive result is still more likely to be a false positive than a true positive.
7. **Check for multiple testing.** If many hypotheses were tested, some will appear significant by chance. Look for corrections (Bonferroni, false discovery rate) or be skeptical of isolated significant findings from large test batteries.
8. **Assess external validity.** Do the study conditions match the real-world context where findings will be applied? Laboratory results may not generalize. Single-country studies may not apply globally.
9. **Look for regression to the mean.** Extreme values tend to be followed by less extreme values. Apparent improvements after an intervention may simply be regression to the mean.
10. **Synthesize the assessment.** For each statistical claim in the research, state whether the statistics support the conclusion, with what strength, and with what caveats.

## Outputs

- A checklist assessment of statistical claims in the research.
- Identified statistical errors or misinterpretations.
- Corrected interpretations where needed.
- An overall assessment of the statistical support for the research conclusions.
- Recommendations for additional statistical evidence if current evidence is insufficient.

## Common Pitfalls

- **Equating statistical significance with importance.** A tiny, meaningless effect can be statistically significant with a large enough sample.
- **Ignoring effect size.** Reporting only p-values without practical magnitude.
- **Confusing absence of evidence with evidence of absence.** A non-significant result does not prove no effect exists.
- **Base rate neglect.** Ignoring how common or rare something is when interpreting test results.
- **Post-hoc hypothesis generation.** Finding a pattern in data and then claiming it was the hypothesis all along.
- **Ecological fallacy.** Applying group-level findings to individuals.
- **Simpson's paradox.** A trend that appears in aggregate data can reverse when the data is split into subgroups.
- **Survivorship bias in data.** Only analyzing cases that reached a certain threshold, ignoring those that did not.

## Quality Criteria

- Every statistical claim in the research must be assessed against this checklist before the research is finalized.
- Corrections must be stated clearly: what the original claim said, what the correct interpretation is, and why it matters.
- The overall assessment must distinguish between findings with strong statistical support, weak support, and no valid support.
- Recommendations for additional evidence must be specific about what type of statistical test or data would resolve the issue.

## Related Frameworks

- `contrarian-null-hypothesis.md` - The null hypothesis framework depends on statistical literacy.
- `contrarian-base-rate-override.md` - Base rate reasoning is a core statistical concept.
- `data-researcher-base-rate-context.md` - Detailed base rate application methodology.
- `data-researcher-benchmarking.md` - Benchmarking requires statistical interpretation of distributions.
