# Spiegelhalter - The Art of Statistics: Learning from Data

## Statistical Thinking Framework

### The PPDAC Cycle
1. **Problem**: Define the question clearly
2. **Plan**: Design data collection strategy
3. **Data**: Collect and clean data
4. **Analysis**: Apply appropriate statistical methods
5. **Conclusion**: Interpret results and communicate

### Types of Questions Statistics Can Answer
- How big/small is something? (Estimation)
- Is there a real difference? (Comparison)
- Are two things related? (Association)
- Can we predict? (Forecasting)
- What caused what? (Causation - hardest)

## Communicating Uncertainty

### Expected Frequencies (Natural Frequencies)
- Instead of: "The test has 95% sensitivity and 5% false positive rate"
- Say: "Out of 1000 people, 10 have the condition, 9 test positive. Of 990 without it, 50 test positive. So of 59 positives, only 9 actually have it."
- Natural frequencies are vastly easier to understand than probabilities

### Framing Effects
- "90% survival rate" vs "10% mortality rate" (same data, different reaction)
- Always present both positive and negative framing
- Use absolute numbers, not just percentages
- "2x the risk" means nothing without the base rate

### Confidence Intervals
- A range of plausible values, not a definitive answer
- 95% CI: If we repeated this study 100 times, ~95 intervals would contain the true value
- Wider intervals = more uncertainty = more honest
- Report intervals, not just point estimates

## Key Statistical Concepts

### Effect Size vs Significance
- Statistical significance: Is the effect probably real?
- Effect size: How big is the effect?
- A real but tiny effect may be practically irrelevant
- A large effect from a small study may not be statistically significant
- Both matter; neither alone is sufficient

### The Funnel of Causation
1. Association (correlation)
2. Temporal precedence (cause before effect)
3. Dose-response relationship
4. Plausible mechanism
5. Replication across settings
6. Experimental evidence (strongest)
- Each level adds confidence in causal claims

### Regression to the Mean
- Extreme values on first measurement tend toward average on re-measurement
- Not a causal phenomenon; purely statistical
- Explain before-after improvements that required no intervention
- Always consider before attributing improvement to an intervention

## Data Quality Issues
- Selection bias: Who is in the sample? Who is missing?
- Measurement error: How accurately is data captured?
- Missing data: Random or systematic?
- Survivorship bias: Are failures visible?
- Ecological fallacy: Group-level patterns may not apply to individuals

## Communicating Statistics Responsibly
1. Use natural frequencies over probabilities when possible
2. Present absolute risks, not just relative risks
3. Show both framings (positive and negative)
4. Acknowledge uncertainty explicitly
5. Provide appropriate context and comparisons
6. Separate association from causation clearly

## Application to Deep Research
- Use the PPDAC cycle to structure statistical inquiry
- Always communicate uncertainty with ranges, not point estimates
- Present data using natural frequencies for clarity
- Check for common data quality issues before drawing conclusions
- Distinguish association from causation using the funnel
- Report effect sizes alongside statistical significance
- Frame findings both positively and negatively for balanced perspective
