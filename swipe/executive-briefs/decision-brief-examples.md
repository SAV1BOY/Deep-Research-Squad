# Decision Brief — Swipe Examples

## Purpose

Decision briefs exist for one reason: to help a decision-maker choose between
concrete options. Unlike research reports, they are structured around the
decision, not the topic.

## Gold Standard Structure

### 1. Decision Statement
One sentence: "We need to decide whether to [X], [Y], or [Z] by [date]."

### 2. Context (3-5 sentences max)
Only the context needed to understand the decision. Not a literature review.

### 3. Options Matrix

| Criteria        | Option A       | Option B       | Option C       |
|----------------|---------------|---------------|---------------|
| Cost           | $2.1M         | $4.3M         | $1.8M         |
| Timeline       | 6 months      | 3 months      | 9 months       |
| Risk           | Medium        | Low           | High           |
| Reversibility  | Easy          | Hard          | Medium         |

### 4. Evidence Summary Per Option
For each option: 2-3 strongest data points supporting and 1-2 against.

### 5. Recommendation
"We recommend Option [X] because [one sentence rationale]."
"The primary risk is [Y], mitigated by [Z]."

### 6. What Changes This
Triggers that would invalidate the recommendation.

## Example Decision Brief Opening

> **Decision**: Choose cloud infrastructure provider for ML workloads.
> Decide by March 30 to meet Q2 deployment timeline.
>
> **Context**: Current on-premise GPU cluster reaches capacity in Q3.
> Three providers bid: AWS (SageMaker), GCP (Vertex AI), Azure (ML Studio).
> Annual spend projection: $1.2M-$2.8M depending on provider.

## What Separates Good from Great

1. **Falsifiable recommendation**: Can be proven wrong
2. **Explicit criteria weighting**: States what matters most and why
3. **Honest trade-offs**: Every option has downsides stated clearly
4. **Trigger-based**: "If X happens, switch to Option B"
5. **Time-bounded**: Decision has a clear deadline and reason for it

## Common Failures

- Presenting one option as obviously best (why bother with a brief?)
- Hiding assumptions in the analysis
- Using subjective criteria without grounding in data
- Forgetting reversibility as a key dimension
- Not stating what information would change the recommendation

## Adaptation for Deep Research Squad

- All decision briefs must include options matrix
- Confidence scores required for each evidence point
- Source diversity must be noted per option
- Include reversibility assessment as standard criteria
