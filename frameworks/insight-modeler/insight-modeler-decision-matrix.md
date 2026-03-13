# Decision Matrix Framework

## Purpose

Create structured decision matrices that evaluate multiple options against weighted criteria. Rows represent options. Columns represent criteria with assigned weights reflecting their relative importance. Each option is scored against each criterion. The framework includes sensitivity analysis to test whether the conclusion changes when weights or scores shift.

## When to Use

- When choosing among multiple options that have different strengths and weaknesses.
- When stakeholders disagree and a structured comparison can ground the discussion.
- When the decision involves multiple criteria that trade off against each other.
- When you need to document and justify a recommendation transparently.

## Inputs

- A defined set of options to evaluate (at least 2, typically 3-7).
- Criteria that matter for the decision, informed by stakeholder priorities.
- Information about how each option performs on each criterion.
- Stakeholder input on the relative importance of criteria.

## Process

### Step 1: Options Definition
List each option with a brief description. Ensure options are:
- Mutually exclusive (choosing one means not choosing others) or clearly labeled if they can be combined.
- Genuinely distinct (not minor variations of the same option).
- Feasible (do not include options that are clearly impossible).

### Step 2: Criteria Selection
Identify 5-10 criteria for evaluation. Good criteria are:
- Relevant to the decision's objectives.
- Differentiating (at least some options perform differently on this criterion).
- Measurable or at least assessable (can be scored, even if subjectively).
- Independent of each other (avoid double-counting the same factor under two criteria).

### Step 3: Weight Assignment
Assign a weight to each criterion reflecting its relative importance. Methods:
- **Direct weighting**: Distribute 100 points across all criteria.
- **Pairwise comparison**: Compare each pair of criteria and derive weights from preferences.
- **Ranked weighting**: Rank criteria by importance and assign weights by rank.
Document the rationale for weights. If stakeholders disagree on weights, record multiple weight sets.

### Step 4: Scoring
Score each option on each criterion using a consistent scale (e.g., 1-5 or 1-10). Scoring guidelines:
- Use the full range of the scale.
- Score based on evidence where available, judgment where not.
- Document the reasoning behind each score, especially non-obvious ones.
- Have multiple evaluators score independently if possible, then discuss discrepancies.

### Step 5: Weighted Score Calculation
For each option, multiply each criterion score by the criterion weight and sum the results. The option with the highest weighted total scores best under these weights.

### Step 6: Sensitivity Analysis
Test the robustness of the result by varying weights and scores:
- **Weight sensitivity**: Change the weight of each criterion by plus or minus 20%. Does the top option change?
- **Score sensitivity**: Change each score by plus or minus 1 point. Does the top option change?
- **Threshold analysis**: How much would the top criterion weight need to change before a different option wins?
If the result changes easily, the decision is sensitive and requires more careful judgment.

### Step 7: Qualitative Review
After the quantitative analysis, review the result qualitatively:
- Does the top-scoring option feel right given everything you know?
- Are there important factors not captured in the criteria?
- Are there deal-breakers (minimum thresholds on any criterion) that the quantitative score does not reflect?

### Step 8: Result Documentation
Present the full matrix, the sensitivity analysis, and a narrative explanation of the recommendation.

## Outputs

- A completed decision matrix table with options, criteria, weights, scores, and weighted totals.
- Sensitivity analysis results showing how robust the top option is.
- A narrative explanation of the recommendation and key trade-offs.
- Documentation of scoring rationale for transparency and auditability.

## Common Pitfalls

- **Criteria overload**: Including too many criteria dilutes the important ones. Limit to 5-10.
- **Weight manipulation**: Unconsciously adjusting weights to make a preferred option win. Set weights before scoring.
- **False precision**: Treating a score of 7.2 vs 7.1 as meaningful when the scoring is inherently subjective.
- **Ignoring deal-breakers**: A high total score does not matter if one criterion is fatally low. Use minimum thresholds.
- **Groupthink scoring**: A group converging on scores to avoid conflict rather than scoring honestly.
- **Missing options**: Not including the status quo or a creative alternative that was not initially obvious.

## Related Frameworks

- **decision-analyst-options-matrix.md** - Provides a richer qualitative description of each option before scoring.
- **decision-analyst-trade-off-table.md** - Examines pairwise trade-offs between options in more depth.
- **insight-modeler-taxonomy-builder.md** - Helps structure the criteria into coherent categories.
- **decision-analyst-risk-return.md** - Adds risk-return analysis to complement the matrix scoring.
