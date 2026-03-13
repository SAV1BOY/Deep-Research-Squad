# Ioannidis - Reproducibility Crisis Papers Index

## "Why Most Published Research Findings Are False" (2005)

### Core Argument
Most claimed research findings are more likely to be false than true, due to a combination of statistical, methodological, and incentive problems.

### Key Factors That Increase False Findings
1. **Small sample sizes**: Underpowered studies miss true effects and inflate found effects
2. **Small effect sizes**: Harder to detect reliably
3. **Many tested relationships**: Multiple comparisons without correction
4. **Flexibility in design**: Choosing methods after seeing data (p-hacking)
5. **Financial and career incentives**: Pressure to publish positive results
6. **Hot scientific fields**: Competition leads to rushed, unreliable work

### The Math
- Positive Predictive Value (PPV) = P(finding is true | finding is positive)
- When prior probability of hypothesis is low AND many comparisons are made, most "positive" findings are false
- A field where 10% of hypotheses are true, with alpha=0.05 and power=0.80: PPV = ~64%
- With additional bias and flexibility: PPV drops well below 50%

## Reproducibility Crisis Across Fields

### Psychology
- Open Science Collaboration (2015): Only 36-39% of 100 studies replicated
- Effect sizes in replications were half the original on average
- Most failures were in social psychology

### Medicine
- Begley & Ellis (2012): Only 6 of 53 "landmark" cancer studies replicated
- Prinz et al. (2011): Only 25% of 67 preclinical studies confirmed
- Drug development based on irreproducible research wastes billions

### Economics
- Camerer et al. (2016): 61% of 18 economics studies replicated
- Better than psychology but still concerning
- Larger effect sizes help but do not solve the problem

## Root Causes

### Publication Bias
- Journals prefer positive/significant results
- Negative results rarely published
- File drawer problem: failed replications never seen
- Distorts the published literature systematically

### P-Hacking
- Trying multiple analyses until p < 0.05
- Selective reporting of outcomes
- Optional stopping (collecting data until significant)
- Outlier removal to achieve significance

### HARKing
- Hypothesizing After Results are Known
- Presenting exploratory findings as if they were predicted
- Makes false discoveries look like confirmed hypotheses

## Solutions and Reforms

### Pre-registration
- Register hypotheses and analysis plan before data collection
- Prevents p-hacking and HARKing
- Registered Reports: peer review before data collection

### Open Science
- Open data: Share raw data for verification
- Open methods: Full protocol transparency
- Open access: Make findings freely available
- Open peer review: Transparent review process

### Statistical Reforms
- Report effect sizes and confidence intervals, not just p-values
- Use Bayesian methods to quantify evidence
- Require replication before accepting findings
- Adjust for multiple comparisons rigorously

## Application to Deep Research
- Treat individual studies with skepticism; look for replicated findings
- Weight meta-analyses and systematic reviews over single studies
- Check for publication bias indicators
- Prefer pre-registered studies when available
- Consider the base rate of true hypotheses in the field
- Be skeptical of surprising findings from small samples
- Look for convergent evidence across independent research groups
