# Replication Crisis Lessons

## Purpose

The replication crisis revealed systemic problems in how research is
conducted, published, and trusted. These lessons are essential for
any organization that relies on research evidence.

## What Is the Replication Crisis?

Beginning in the early 2010s, researchers discovered that a significant
proportion of published scientific findings could not be replicated:
- Psychology: ~39% of studies replicated (Open Science Collaboration, 2015)
- Cancer biology: ~25% of landmark studies replicated (Errington et al., 2021)
- Economics: ~60% replicated but with smaller effect sizes (Camerer et al., 2016)

## Root Causes

### 1. P-Hacking
- Running multiple statistical tests until one shows significance (p<0.05)
- Selectively reporting only "significant" results
- Flexible stopping rules (collect data until significance appears)
- The threshold p<0.05 means 1 in 20 random results looks significant

### 2. Publication Bias
- Journals strongly prefer positive/significant results
- Null results rarely published ("file drawer problem")
- Creates a published literature biased toward false positives
- Researchers incentivized to find significant results

### 3. Small Sample Sizes
- Underpowered studies detect effects that don't exist
- Small samples produce unstable, unreliable estimates
- "Winner's curse": published effects from small studies are inflated

### 4. HARKing (Hypothesizing After Results are Known)
- Researchers form hypotheses after seeing the data
- Present post-hoc findings as if they were pre-planned
- Makes exploratory research look confirmatory

### 5. Perverse Incentives
- Publish or perish: quantity over quality
- Novel results valued over replication
- Career rewards for dramatic findings
- No career reward for disproving others' work

## Reforms and Solutions

### Pre-registration
- Register hypotheses and methods before collecting data
- Prevents p-hacking and HARKing
- Registered Reports: journals accept before results are known

### Open Data and Code
- Share raw data and analysis code
- Enables verification and re-analysis
- Catches errors (like Reinhart-Rogoff spreadsheet error)

### Larger Samples and Multi-Site Studies
- Pre-register required sample sizes based on power analysis
- Multi-site studies test generalizability
- Adversarial collaborations between supporters and skeptics

### Statistical Reform
- Move from p-values to effect sizes and confidence intervals
- Bayesian approaches that quantify evidence strength
- Abandon the arbitrary p<0.05 threshold

## Lessons for Deep Research Squad

### Direct Applications
1. **Never rely on single studies**: Always seek replication or triangulation
2. **Check sample sizes**: Small studies get lower confidence scores
3. **Look for pre-registration**: Pre-registered studies are more trustworthy
4. **Seek disconfirming evidence**: Don't just find studies that agree
5. **Effect sizes matter**: A "significant" finding may be trivially small

### Built Into Our Process
- Evidence grading penalizes small, unreplicated studies
- Confidence scorer adjusts for replication status
- Source diversity analyzer prevents single-source reliance
- Contradiction map surfaces conflicting findings
- Anti-BS protocol flags overclaiming from weak evidence
