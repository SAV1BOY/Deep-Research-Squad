# Contrarian Survivorship Audit Framework

## Purpose

Check for survivorship bias in every analysis. Survivorship bias occurs when we draw conclusions only from the winners, successes, or survivors while ignoring the failures, dropouts, and casualties that are no longer visible. This framework forces you to ask: "What am I not seeing? Where are the failures?"

## When to Use

- When analyzing success stories, best practices, or case studies of winners.
- When a strategy is recommended based on examples of those who used it successfully.
- When historical data shows an upward trend that might be explained by removal of poor performers.
- When evaluating investment returns, company performance, or technology adoption rates.
- When "lessons from the best" are presented as generalizable advice.

## Inputs

- The conclusion or recommendation based on observed successes.
- The dataset or sample of cases used to reach the conclusion.
- Information about the original population from which the sample was drawn.
- Context about how cases exit the dataset (failure, acquisition, closure, death).

## Process

1. **Identify the survivor pool.** Who or what is in the current dataset? List all the entities being analyzed.
2. **Define the original population.** How many entities started in this category? What was the full cohort before attrition?
3. **Quantify the attrition.** How many entities dropped out, failed, closed, or otherwise left the dataset? Calculate the survival rate.
4. **Characterize the non-survivors.** What do we know about those who did not survive? Did they share traits with the survivors? Did they follow the same strategies?
5. **Test the conclusion against non-survivors.** Would the conclusion still hold if we included the failures? Did failed entities also exhibit the traits we are attributing to success?
6. **Look for reverse causality.** Is the observed trait a cause of survival or a consequence of it? Survivors may adopt certain practices because they can afford to, not because those practices caused their success.
7. **Check the data source for survivorship filtering.** Does the database, index, or sample automatically exclude failures? (e.g., stock indices remove delisted companies, databases drop defunct startups.)
8. **Adjust the conclusion.** Restate the conclusion accounting for survivorship bias. Qualify claims about what drives success.
9. **Estimate the true effect size.** If possible, estimate what the finding would look like with the full population included.

## Outputs

- The survival rate of the original population.
- A characterization of non-survivors and their traits.
- An assessment of whether the conclusion survives after accounting for non-survivors.
- A revised conclusion with survivorship bias factored in.
- Recommendations for obtaining data on non-survivors if it is currently unavailable.
- The estimated true effect size versus the biased effect size.

## Common Pitfalls

- **Assuming survivors are representative.** They are a filtered subset, not a random sample.
- **Ignoring silent evidence.** Failures rarely document their failure in detail; absence of information is not absence of failures.
- **Confusing survival with merit.** Luck, timing, and external factors play significant roles in survival.
- **Accepting curated case studies uncritically.** Case studies are almost always selected from survivors.
- **Focusing only on dramatic failures.** Quiet, unremarkable failures are the majority and the most informative for base rates.
- **Assuming the bias is small.** In many domains, survival rates are below 10%, making the bias enormous.
- **Not looking for the graveyard.** Actively seek out sources that document failures, closures, and dropouts.

## Quality Criteria

- The original population must be quantified, not just the survivor pool.
- The attrition rate must be calculated explicitly; do not proceed without knowing what fraction survived.
- Non-survivors must be characterized with as much detail as available, not treated as an undifferentiated mass.
- The revised conclusion must state how it differs from the pre-audit conclusion and by how much.

## Related Frameworks

- `contrarian-base-rate-override.md` - Survivorship bias inflates perceived base rates of success.
- `contrarian-disconfirming-hunt.md` - Non-survivor data is a key source of disconfirming evidence.
- `contrarian-null-hypothesis.md` - The null often reflects the base rate that survivorship bias distorts.
- `data-researcher-benchmarking.md` - Benchmarking is vulnerable to survivorship bias in peer selection.
