# Trade-Off Table Framework

## Purpose

Make trade-offs between options explicit and evaluable. For each pair of competing options, clearly state what you gain by choosing one over the other, what you give up, and whether the trade-off is worth making. This prevents hidden trade-offs from undermining decisions and forces honest assessment of what is being sacrificed.

## When to Use

- When options have been identified but the choice between them is not obvious.
- When stakeholders disagree because they are weighting trade-offs differently.
- When a decision involves genuine tension between competing values or objectives.
- When you need to justify why one option was chosen over another.

## Inputs

- A set of options to compare (typically from decision-analyst-options-matrix.md).
- Understanding of what each option offers and what it costs.
- Stakeholder priorities and values that determine which trade-offs are acceptable.
- Context about constraints that make certain trade-offs unavoidable.

## Process

### Step 1: Pairwise Selection
List all unique pairs of options. For N options, there are N(N-1)/2 pairs. If you have more than 5 options, focus on the most competitive pairs rather than exhaustively comparing all.

### Step 2: Gain-Loss Analysis
For each pair (Option A vs. Option B), complete two statements:
- "By choosing A over B, we gain [specific advantages] and we give up [specific advantages of B]."
- "By choosing B over A, we gain [specific advantages] and we give up [specific advantages of A]."
Be specific. "Better performance" is too vague. "15% faster processing at scale" is useful.

### Step 3: Trade-Off Characterization
For each pair, characterize the nature of the trade-off:
- **Cost vs. quality**: Spending more to get better results.
- **Speed vs. thoroughness**: Moving faster at the expense of completeness.
- **Risk vs. reward**: Accepting higher risk for higher potential return.
- **Short-term vs. long-term**: Immediate gains at the expense of future position.
- **Flexibility vs. commitment**: Keeping options open vs. committing for efficiency.
- **Simplicity vs. capability**: Easier to implement but less powerful.

### Step 4: Quantification Where Possible
Assign numbers to both sides of the trade-off:
- What is the magnitude of the gain? (dollars, time, percentage points)
- What is the magnitude of the loss?
- Is the trade-off symmetric (give up roughly as much as you gain) or asymmetric?
- Asymmetric trade-offs in your favor are good deals. Asymmetric against you are bad deals.

### Step 5: Reversibility Assessment
For each trade-off, assess whether it can be undone:
- Can you switch from A to B later if the trade-off proves wrong?
- What is the cost of switching?
- Are there options that preserve flexibility to revisit the trade-off?

### Step 6: Stakeholder Impact
Identify who bears the cost and who captures the benefit of each trade-off:
- Is the same group both paying and benefiting?
- If not, is the transfer fair and acceptable?
- Will the losing side resist or undermine the decision?

### Step 7: Worth-It Assessment
For each trade-off, make an explicit judgment: is this trade-off worth making?
- **Clearly worth it**: The gain significantly exceeds the cost for all relevant stakeholders.
- **Probably worth it**: The gain exceeds the cost but with some uncertainty or unevenness.
- **Borderline**: The gain and cost are roughly equal. The decision depends on values and priorities.
- **Probably not worth it**: The cost exceeds the gain in most reasonable assessments.
- **Clearly not worth it**: The cost significantly exceeds the gain.

### Step 8: Summary Table
Compile all pairwise comparisons into a summary table with columns: Option Pair, What You Gain, What You Lose, Trade-Off Type, Magnitude, Reversibility, Worth-It Verdict.

## Outputs

- A completed trade-off table covering all significant option pairs.
- Clear gain-loss statements for each pair.
- Worth-it verdicts with supporting rationale.
- Identification of asymmetric trade-offs (good deals and bad deals).
- A narrative summary of the most important trade-offs driving the decision.

## Common Pitfalls

- **Hidden trade-offs**: Presenting an option as "all upside" when it inevitably involves giving something up. Every choice has a cost.
- **Comparing to perfection**: Evaluating options against an ideal rather than against each other. The relevant question is A vs. B, not A vs. perfect.
- **Unacknowledged values**: Trade-off assessments always embed values. Make explicit which values drive the "worth it" verdict.
- **Loss aversion bias**: Overweighting what is given up relative to what is gained. Losses feel larger than equivalent gains.
- **Ignoring distributional effects**: A trade-off may be net positive overall but deeply unfair to one group.
- **Status quo bias**: Treating the status quo as costless. The status quo has its own trade-offs compared to alternatives.

## Related Frameworks

- **decision-analyst-options-matrix.md** - Provides the options and their attributes that feed into trade-off analysis.
- **decision-analyst-risk-return.md** - Deepens the risk dimension of trade-off analysis.
- **insight-modeler-decision-matrix.md** - Provides weighted scoring that can inform worth-it assessments.
- **decision-analyst-recommendation.md** - Incorporates trade-off analysis into the final recommendation.
