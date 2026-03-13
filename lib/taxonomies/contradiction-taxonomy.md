# Contradiction Taxonomy

## Purpose

Classifies types of contradictions encountered during research, guiding the selection
of appropriate resolution patterns and setting expectations for resolution difficulty.

## Categories

### 1. Factual Contradictions
Two sources state mutually exclusive facts about the same thing.

**Subcategories:**
- **Numerical Disagreement** - Different numbers for the same metric
- **Capability Conflict** - One source says a feature exists, another says it does not
- **Behavioral Conflict** - Sources describe different behavior for the same operation

**Examples:** Source A says max cluster size is 100 nodes; Source B says 500 nodes.
One doc says the feature is supported; another says it is experimental only.

### 2. Contextual Contradictions
Claims appear contradictory but are valid under different conditions.

**Subcategories:**
- **Version-Dependent** - True for different software versions
- **Configuration-Dependent** - True under different settings or configurations
- **Scale-Dependent** - True at different data volumes or user counts
- **Environment-Dependent** - True in different deployment environments

**Examples:** "Supports ACID transactions" is true for single-region but not multi-region.
Performance claims differ because benchmarks used different hardware.

### 3. Temporal Contradictions
Claims were each accurate at their time of writing but reflect different states.

**Subcategories:**
- **Superseded** - Older claim replaced by newer reality
- **Regression** - Newer version lost a capability the older version had
- **Evolving** - The truth is actively changing between the two claim dates

**Examples:** "Does not support JSON" was true in v3 but false in v5.

### 4. Methodological Contradictions
Different results stemming from different measurement approaches.

**Subcategories:**
- **Measurement Difference** - Different tools or methods yield different numbers
- **Definition Difference** - Sources define the same term differently
- **Scope Difference** - Sources measure different subsets of the same phenomenon

**Examples:** Uptime measured including vs. excluding maintenance windows. "Latency"
measured at the client vs. at the server yields different numbers.

### 5. Perspectival Contradictions
Different stakeholder perspectives lead to different assessments.

**Subcategories:**
- **Role-Based** - Developers vs. operators vs. business view differently
- **Priority-Based** - Different weighting of the same trade-offs
- **Experience-Based** - Expert vs. novice assessment differs

**Examples:** Developers love the API; operators find it hard to monitor. One team
says migration was easy; another with different schema complexity says it was painful.

### 6. Apparent Contradictions
Seem contradictory but are not upon closer analysis.

**Subcategories:**
- **Ambiguity** - Vague language creates the illusion of conflict
- **Partial Overlap** - Sources discuss overlapping but distinct topics
- **Misinterpretation** - Reader inference creates a contradiction that the sources
  do not actually contain

**Examples:** "Fast" in one context means sub-millisecond; in another means sub-second.
Two sources discuss different features of the same product.

## Usage

Classify each contradiction card by type. Use this to:
- Select the right resolution pattern (temporal contradictions use temporal resolution)
- Estimate resolution effort (factual contradictions are harder; apparent are easier)
- Prioritize resolution (factual and methodological often matter most for decisions)
- Communicate clearly to stakeholders about the nature of conflicting information
