# Contradiction Taxonomy

## Purpose

Classifies contradictions to guide resolution pattern selection and set expectations
for resolution difficulty.

## Categories

### 1. Factual Contradictions
Sources state mutually exclusive facts about the same thing.
- **Numerical Disagreement** - Different numbers for the same metric
- **Capability Conflict** - One says a feature exists, another says it does not
- **Behavioral Conflict** - Different behavior described for the same operation

**Example:** Source A says max cluster size is 100 nodes; Source B says 500.

### 2. Contextual Contradictions
Both claims are valid under different conditions.
- **Version-Dependent** - True for different software versions
- **Configuration-Dependent** - True under different settings
- **Scale-Dependent** - True at different data volumes
- **Environment-Dependent** - True in different deployment environments

**Example:** "Supports ACID" is true single-region but not multi-region.

### 3. Temporal Contradictions
Each claim was accurate at its time but reality has changed.
- **Superseded** - Older claim replaced by newer reality
- **Regression** - Newer version lost a capability
- **Evolving** - Truth is actively changing

**Example:** "No JSON support" was true in v3, false in v5.

### 4. Methodological Contradictions
Different results from different measurement approaches.
- **Measurement Difference** - Different tools yield different numbers
- **Definition Difference** - Same term defined differently
- **Scope Difference** - Different subsets of the same phenomenon measured

**Example:** Uptime including vs. excluding maintenance windows.

### 5. Perspectival Contradictions
Different stakeholders assess differently.
- **Role-Based** - Developers vs. operators view differently
- **Priority-Based** - Different weighting of trade-offs
- **Experience-Based** - Expert vs. novice assessment differs

**Example:** Developers love the API; operators find it hard to monitor.

### 6. Apparent Contradictions
Seem contradictory but are not upon analysis.
- **Ambiguity** - Vague language creates illusion of conflict
- **Partial Overlap** - Sources discuss overlapping but distinct topics

**Example:** "Fast" means sub-millisecond in one context, sub-second in another.

## Usage

Classify each contradiction card by type to select the right resolution pattern,
estimate effort, and prioritize resolution work.
