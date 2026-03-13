# Decision Card Component

## Purpose

Documents a research-informed decision, capturing reasoning, alternatives
considered, trade-offs, and the evidence basis for the chosen option.

## Structure

```yaml
decision_card:
  id: string                      # Unique identifier (e.g., DEC-001)
  title: string                   # Brief title of the decision
  status: string                  # pending | decided | revisiting | deferred
  decision_type: string           # recommendation | selection | trade-off | go-no-go
  question: string                # The decision question being answered
  options:
    - name: string                # Option name
      pros: list[string]          # Advantages
      cons: list[string]          # Disadvantages
      evidence_ids: list[string]  # Supporting evidence
      score: float                # 0.0 to 1.0 overall assessment
  chosen_option: string           # Name of selected option
  rationale: string               # Why this option was chosen
  confidence: float               # 0.0 to 1.0
  risks: list[string]             # Risks of the chosen option
  reversibility: string           # easily-reversible | costly-to-reverse | irreversible
  decision_date: datetime
  review_date: datetime           # When to revisit this decision
  dependencies: list[string]      # Decision card IDs this depends on
```

## Usage Example

```yaml
decision_card:
  id: DEC-005
  title: "Primary database selection for analytics platform"
  status: decided
  decision_type: selection
  question: "Which database best serves our real-time analytics needs?"
  options:
    - name: "ClickHouse"
      pros: ["Fastest analytical queries", "Excellent compression"]
      cons: ["Smaller community", "Complex cluster management"]
      evidence_ids: [EV-033, EV-061]
      score: 0.85
    - name: "TimescaleDB"
      pros: ["Familiar ecosystem", "Strong community"]
      cons: ["Slower at scale for pure analytics"]
      evidence_ids: [EV-041, EV-055]
      score: 0.72
  chosen_option: "ClickHouse"
  rationale: "Query performance at projected data volume is top priority"
  confidence: 0.80
  risks: ["Operational complexity may slow initial team velocity"]
  reversibility: costly-to-reverse
  decision_date: 2026-03-13T16:00:00Z
  review_date: 2026-06-13T00:00:00Z
  dependencies: [DEC-002, DEC-003]
```

## When to Use

- When research has produced enough evidence to inform a choice
- When multiple viable options exist and trade-offs must be explicit
- When decisions need to be revisited later with new information
