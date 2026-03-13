# Script: Build Timeline

## Purpose

Constructs a structured timeline for a technology, market, or topic.
Timelines reveal patterns, inflection points, and trajectories that
are invisible in point-in-time analysis.

## Trigger

Called when research requires understanding historical development or
projecting future evolution of a topic.

## Inputs

- `topic`: What the timeline covers
- `time_range`: Start and end dates (including future projections)
- `sources`: Evidence gathered from source map
- `focus`: What aspect to emphasize (technology, market, regulatory, etc.)

## Process

### Step 1: Event Collection
Gather all dated events from sources:

| Date | Event | Source | Confidence | Category | Significance |
|------|-------|--------|------------|----------|-------------|
| YYYY-MM | Event description | Source ref | 0-100 | Tech/Market/Reg | 1-5 |

### Step 2: Phase Identification
Group events into natural phases:
- What are the distinct eras or phases?
- What event marks each phase transition?
- What characterizes each phase?

### Step 3: Parallel Track Mapping
Identify concurrent developments:
- Enabling technologies that made the primary development possible
- Regulatory changes that accelerated or decelerated progress
- Market forces (funding, demand, competition) shaping the trajectory
- Adjacent developments that influenced the timeline

### Step 4: Inflection Point Analysis
For each phase transition:
- What triggered the change?
- Was it anticipated or surprising?
- How long was the transition period?
- What signals preceded the inflection?

### Step 5: Pattern Recognition
Look for recurring patterns:
- S-curve adoption patterns
- Hype cycle positioning
- Consolidation timing
- Regulatory response lag

### Step 6: Forward Projection
Based on patterns and current signals:
- Near-term projection (12 months): High confidence
- Medium-term projection (1-3 years): Medium confidence
- Long-term projection (3-5 years): Low confidence
- Key uncertainties that could alter projections

## Output Template

```
TIMELINE: [Topic]
==================
Period: [Start] to [End]
Phases: [Count]
Key Inflection Points: [Count]

[Phase-by-phase narrative with dated events]

Parallel Tracks:
- [Track 1: Key developments]
- [Track 2: Key developments]

Inflection Points:
1. [Date]: [Event] — [Why it mattered]

Forward Projection:
- 12 months: [Projection] (confidence: [score])
- 1-3 years: [Projection] (confidence: [score])
- 3-5 years: [Projection] (confidence: [score])
```

## Quality Checks

- [ ] All events have dates and sources
- [ ] Phases are clearly defined with transition markers
- [ ] Parallel tracks included (not just primary narrative)
- [ ] Inflection points identified and explained
- [ ] Forward projections include confidence levels
- [ ] Failed alternatives and dead ends noted
