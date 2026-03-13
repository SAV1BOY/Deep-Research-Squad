# Causal Map Framework

## Purpose

Create structured causal maps that visualize how factors influence each other within a system. Nodes represent factors or variables. Edges represent causal relationships with direction and estimated strength. The resulting map reveals feedback loops, root causes, leverage points, and unintended consequence pathways.

## When to Use

- When multiple factors interact and simple linear causation is insufficient.
- When stakeholders need to see the system as a whole rather than isolated cause-effect pairs.
- When identifying root causes versus symptoms in a complex problem.
- When predicting how an intervention in one part of the system will ripple through others.

## Inputs

- A list of factors or variables relevant to the system being analyzed.
- Evidence about causal relationships between factors (from research, data, or expert judgment).
- Understanding of the system boundaries (what is included and what is outside scope).
- Estimates of relationship strength and direction where available.

## Process

### Step 1: Factor Identification
List all relevant factors as candidate nodes. Be comprehensive initially; you will prune later. Include:
- Observable variables (measurable quantities).
- Latent factors (not directly measured but causally important).
- External forces (factors outside the system that influence it).

### Step 2: Relationship Mapping
For each pair of factors, assess whether a causal relationship exists:
- **Direction**: Does A cause B, does B cause A, or is it bidirectional?
- **Polarity**: Is the relationship positive (more A leads to more B) or negative (more A leads to less B)?
- **Strength**: Is the relationship strong, moderate, or weak?
- **Lag**: Is the effect immediate or delayed?
Document the evidence or reasoning behind each claimed relationship.

### Step 3: Map Construction
Arrange nodes and draw directed edges with polarity and strength annotations. Layout guidelines:
- Place root causes (nodes with no incoming edges) on the left or top.
- Place outcomes of interest (nodes the analysis focuses on) on the right or bottom.
- Group closely related nodes spatially.
- Use consistent notation: solid lines for strong relationships, dashed for weak, plus/minus for polarity.

### Step 4: Feedback Loop Detection
Trace paths through the map that return to their starting node. Classify each loop:
- **Reinforcing loop**: All positive polarities (or even number of negatives). These amplify change.
- **Balancing loop**: Odd number of negative polarities. These resist change and seek equilibrium.
- **Dominant loops**: Loops that currently drive the system's behavior most strongly.

### Step 5: Root Cause Analysis
Identify nodes with many outgoing edges but few incoming ones. These are upstream drivers. Trace the most important outcome backwards through the map to find the deepest causes.

### Step 6: Intervention Analysis
For proposed interventions, trace the effects forward through the map:
- What is the intended effect path?
- What unintended effect paths exist?
- Does the intervention trigger any reinforcing loops (good or bad)?
- Does it encounter any balancing loops that will resist the change?

### Step 7: Map Validation
Test the map against known cases:
- Does the map correctly predict outcomes that have already been observed?
- Are there known outcomes that the map cannot explain (indicating missing factors)?
- Do domain experts agree with the relationships depicted?

### Step 8: Simplification
Remove factors and relationships that do not materially affect the analysis. A useful causal map has 10-25 nodes. More than that sacrifices clarity without proportional gain in insight.

## Outputs

- A causal map diagram with labeled nodes, directed edges, polarity, and strength indicators.
- A list of identified feedback loops with classification (reinforcing vs. balancing).
- Root cause identification for key outcomes.
- Intervention analysis showing intended and unintended effect pathways.
- A narrative summary explaining the most important causal dynamics.

## Common Pitfalls

- **Correlation as causation**: Drawing an edge because two factors are correlated without evidence of causal mechanism.
- **Missing feedback**: Modeling only forward causation and ignoring how effects feed back to causes.
- **Over-complexity**: Including every conceivable factor, making the map unreadable and unhelpful.
- **Static thinking**: Treating the map as a fixed snapshot when relationships change over time.
- **Ignoring delays**: Modeling all relationships as immediate when some have significant time lags that affect system behavior.
- **Boundary errors**: Including factors outside the system that cannot be influenced, or excluding internal factors that are important.

## Related Frameworks

- **timeline-causal-chain.md** - Provides temporal causal chains that can be inputs to the causal map.
- **insight-modeler-leverage-point.md** - Uses the causal map to identify the most effective intervention points.
- **insight-modeler-scenario-tree.md** - Uses causal map dynamics to generate plausible future scenarios.
- **synthesis-implications-mapping.md** - Maps consequences for stakeholders based on causal map outputs.
