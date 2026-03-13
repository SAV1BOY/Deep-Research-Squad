# Timeline Counterfactual Analysis Framework

## Purpose

Test causal claims and identify critical dependencies by asking "What if this had not happened?" Counterfactual reasoning reveals which events were truly necessary for an outcome and which were incidental, strengthening or weakening causal narratives.

## When to Use

- When evaluating whether a claimed cause was actually necessary for an outcome.
- When assessing the importance of a specific event, decision, or actor.
- When identifying single points of failure or critical dependencies in a historical sequence.
- When a user asks whether something could have turned out differently.

## Inputs

- A causal narrative or chain of events with a claimed outcome.
- The specific event or factor to be counterfactually removed or altered.
- Knowledge of the broader context, including parallel developments and structural forces.
- Understanding of available alternatives that existed at the time.

## Process

### Step 1: Anchor the Actual
Document the actual sequence of events and the actual outcome with precision. You cannot reason about what might have been without clarity about what was.

### Step 2: Select the Counterfactual Target
Choose the specific event, decision, or condition to alter. Be precise: "What if X had not happened?" is better than "What if things were different?"

### Step 3: Define the Alteration
Specify exactly what changes in the counterfactual scenario. Options include:
- **Removal**: The event simply does not occur.
- **Delay**: The event occurs later.
- **Modification**: The event occurs differently (specify how).
- **Substitution**: A different event occurs in its place (specify which).

### Step 4: Trace First-Order Effects
Identify the immediate consequences of the alteration. What is the first thing that changes? Keep this tightly connected to the altered event.

### Step 5: Trace Higher-Order Effects
Follow the chain of consequences outward. Second-order effects are consequences of first-order effects. Third-order effects are consequences of second-order effects. Stop when uncertainty becomes too high to reason productively.

### Step 6: Assess Convergence vs. Divergence
Would the world have eventually reached a similar outcome through a different path (convergence), or would the outcome have been fundamentally different (divergence)? Convergence suggests the removed event was not critical. Divergence suggests it was.

### Step 7: Evaluate Structural Forces
Consider whether structural forces (economic trends, technological trajectories, demographic shifts) would have produced a similar outcome regardless. Individual events matter less when structural forces are strong.

### Step 8: Confidence Calibration
Rate your confidence in the counterfactual conclusion. Near-miss counterfactuals (the event almost did not happen) are more credible than remote ones. Counterfactuals supported by parallel cases are stronger than purely speculative ones.

### Step 9: Synthesize Findings
State whether the counterfactual target was: critical (outcome would not have occurred without it), accelerating (outcome would have occurred but later), shaping (outcome would have occurred but in a different form), or incidental (outcome was largely independent of this event).

## Outputs

- A clearly stated counterfactual scenario with precise alterations.
- A traced chain of likely consequences at first, second, and third order.
- A convergence or divergence assessment.
- A classification of the target event as critical, accelerating, shaping, or incidental.
- Confidence level with justification.

## Common Pitfalls

- **Minimal rewrite rule violation**: Changing too many things at once. Good counterfactuals alter one thing and trace consequences.
- **Deterministic thinking**: Assuming there was only one possible alternative path. Reality offers multiple counterfactual branches.
- **Ignoring structural constraints**: Imagining outcomes that were structurally impossible regardless of the altered event.
- **Present-knowledge contamination**: Using knowledge unavailable at the time to construct implausible counterfactual paths.
- **Butterfly effect overreach**: Claiming massive consequences from tiny changes without a credible mechanism for amplification.
- **Emotional attachment**: Favoring counterfactuals that produce outcomes we prefer rather than those that are most plausible.

## Related Frameworks

- **timeline-causal-chain.md** - Provides the causal chain that counterfactual analysis tests.
- **timeline-turning-points.md** - Identifies the events most worth subjecting to counterfactual analysis.
- **insight-modeler-scenario-tree.md** - Counterfactuals applied forward become scenario trees for future planning.
- **decision-analyst-uncertainty.md** - Counterfactual reasoning supports decision-making under uncertainty.
