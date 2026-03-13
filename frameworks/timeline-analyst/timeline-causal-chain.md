# Timeline Causal Chain Framework

## Purpose

Build and verify causal chains across temporal sequences. Establish that Event A led to Event B which caused Event C, ensuring that the temporal order genuinely supports the claimed causality rather than mere correlation or coincidence.

## When to Use

- When a research question involves understanding why something happened over time.
- When sources claim one event caused another and you need to verify the link.
- When constructing a narrative that explains a sequence of outcomes.
- When distinguishing genuine causation from post-hoc rationalization.

## Inputs

- A set of events with dates or temporal ordering.
- Source claims about causal relationships between events.
- Contextual information about the environment in which events occurred.
- Any available counterfactual evidence or parallel cases.

## Process

### Step 1: Event Inventory
List every relevant event with its date, actors involved, and immediate outcome. Be exhaustive before filtering.

### Step 2: Temporal Ordering
Arrange events in strict chronological order. Flag any events with uncertain dates. A cause cannot follow its effect.

### Step 3: Proximity Analysis
For each consecutive pair of events, assess temporal proximity. Immediate succession suggests direct causation. Long gaps require intermediate mechanisms.

### Step 4: Mechanism Identification
For each claimed causal link (A caused B), identify the specific mechanism. How did A produce B? What was the transmission channel? If no mechanism can be articulated, the link is suspect.

### Step 5: Alternative Cause Screening
For each effect, ask: could something other than the claimed cause have produced this? List plausible alternatives and evaluate evidence for each.

### Step 6: Chain Assembly
Connect verified links into a full chain. Mark each link with confidence level: confirmed (multiple sources, clear mechanism), probable (single source or indirect mechanism), or speculative (plausible but unverified).

### Step 7: Chain Stress Test
Test the chain by removing any single link. Does the rest still hold? If the entire chain collapses when one link is questioned, the narrative is fragile.

### Step 8: Documentation
Present the final chain with evidence citations for each link, alternative explanations considered and rejected, and confidence assessments.

## Outputs

- A numbered causal chain with each link annotated by confidence level.
- A list of alternative explanations considered and why they were rejected.
- Identification of the weakest link in the chain.
- An overall confidence assessment for the full causal narrative.

## Common Pitfalls

- **Post hoc ergo propter hoc**: Assuming that because B followed A, A caused B. Always demand a mechanism.
- **Omitted variable bias**: Ignoring a third factor C that caused both A and B independently.
- **Survivorship bias**: Building chains only from events that are visible, ignoring what did not happen.
- **Narrative seduction**: Favoring a clean, compelling story over a messy but accurate one.
- **Confirmation bias**: Seeking evidence that supports the chain while ignoring disconfirming data.
- **Compression of time**: Collapsing long periods into a single causal step, hiding intermediate complexity.

## Related Frameworks

- **timeline-turning-points.md** - Identifies the inflection points that often anchor causal chains.
- **timeline-counterfactual-analysis.md** - Tests causal claims by asking what would have happened otherwise.
- **insight-modeler-causal-map.md** - Visualizes causal relationships as networks rather than linear chains.
- **synthesis-conclusion-ladder.md** - Structures the climb from observed data to causal conclusions.
