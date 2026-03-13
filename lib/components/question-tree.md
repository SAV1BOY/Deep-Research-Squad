# Question Tree Component

## Purpose

Decomposes a complex research question into a hierarchical tree of sub-questions,
enabling systematic exploration and ensuring comprehensive coverage of all facets.

## Structure

```yaml
question_tree:
  root_question: string          # The original research question
  decomposition_strategy: string # top-down | bottom-up | lateral
  branches:
    - id: string                 # Unique branch identifier (e.g., Q1.2.3)
      question: string           # The sub-question text
      parent_id: string | null   # Parent branch ID (null for root)
      priority: high | medium | low
      status: pending | in-progress | answered | blocked
      answer_summary: string     # Brief answer once resolved
      confidence: float          # 0.0 to 1.0
      children: list[id]         # Child branch IDs
      dependencies: list[id]     # Questions that must be answered first
  metadata:
    depth: integer               # Maximum tree depth
    total_questions: integer
    answered_count: integer
    coverage_estimate: float     # 0.0 to 1.0
```

## Usage Example

```yaml
question_tree:
  root_question: "What is the best database for our real-time analytics platform?"
  decomposition_strategy: top-down
  branches:
    - id: Q1
      question: "What are our latency requirements?"
      parent_id: null
      priority: high
      status: answered
      answer_summary: "Sub-100ms p99 for dashboard queries"
      confidence: 0.95
      children: [Q1.1, Q1.2]
      dependencies: []
    - id: Q1.1
      question: "What query patterns dominate?"
      parent_id: Q1
      priority: high
      status: in-progress
      answer_summary: ""
      confidence: 0.0
      children: []
      dependencies: [Q1]
```

## When to Use

- The research question has multiple independent dimensions to explore
- You need to track progress across many parallel investigation threads
- Dependencies exist between sub-questions requiring ordered resolution
- The research scope is large enough that coverage tracking is valuable
- Stakeholders need visibility into which aspects have been investigated
