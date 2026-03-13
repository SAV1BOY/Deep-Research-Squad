# Timeline Entry Component

## Purpose

Records a single event in the research timeline, providing a chronological audit
trail of the research process from initiation through delivery.

## Structure

```yaml
timeline_entry:
  id: string                    # Unique identifier (e.g., TL-001)
  timestamp: datetime           # When the event occurred
  event_type: string            # milestone | discovery | decision | pivot | escalation
  phase: string                 # planning | gathering | analysis | synthesis | delivery
  title: string                 # Brief title of the event
  description: string           # What happened and why it matters
  actor: string                 # Who or what triggered this event
  artifacts_created: list[string]    # IDs of cards or documents produced
  artifacts_referenced: list[string] # IDs of existing artifacts consulted
  impact: string                # How this event affected research direction
  duration_minutes: integer     # How long this activity took
  tags: list[string]            # Categorization tags
```

## Usage Example

```yaml
timeline_entry:
  id: TL-015
  timestamp: 2026-03-13T10:30:00Z
  event_type: discovery
  phase: gathering
  title: "Found contradictory failover benchmarks"
  description: >
    Official Redis docs and independent blog report significantly different
    failover times. Created CONTRA-003 to track resolution.
  actor: "research-agent"
  artifacts_created: [CONTRA-003, CLM-023]
  artifacts_referenced: [SRC-042, SRC-058, CLM-017]
  impact: "Must resolve before finalizing database recommendation"
  duration_minutes: 15
  tags: [contradiction, redis, failover]

timeline_entry:
  id: TL-016
  timestamp: 2026-03-13T11:00:00Z
  event_type: pivot
  phase: analysis
  title: "Expanded scope to include load-dependent testing"
  description: >
    Contradiction analysis revealed failover performance is highly
    load-dependent. Expanding research to cover varying loads.
  actor: "research-lead"
  artifacts_created: []
  artifacts_referenced: [CONTRA-003, INS-008]
  impact: "Added 3 new sub-questions to question tree"
  duration_minutes: 10
  tags: [scope-change, workload-analysis]
```

## When to Use

- At every significant research milestone or phase transition
- When a discovery changes the direction or scope of research
- When escalations or pivots occur during the research process
