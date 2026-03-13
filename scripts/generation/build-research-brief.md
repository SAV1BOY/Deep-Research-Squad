# Script: Build Research Brief

## Purpose

Generates a structured research brief from a raw research request. Transforms
vague questions into actionable research plans with clear scope, methodology,
and deliverable specifications.

## Trigger

Called when a new research request is received from any source.

## Inputs

- `research_request`: The raw question or request text
- `requester`: Who is asking (role, context)
- `deadline`: When the output is needed
- `format_preference`: Desired output format (brief, deep dive, decision brief)

## Process

### Step 1: Decompose the Request
Parse the request into:
- **Core question**: What is actually being asked?
- **Sub-questions**: What must be answered to address the core question?
- **Implicit questions**: What is the requester assuming or not asking but needs?
- **Out of scope**: What this research will NOT cover (state explicitly)

### Step 2: Classify Research Type
Determine the research type:
- **Fact-finding**: Verify or discover specific facts
- **Analysis**: Understand dynamics, causes, or implications
- **Comparison**: Evaluate alternatives against criteria
- **Prediction**: Assess likely future outcomes
- **Synthesis**: Combine multiple sources into a unified view

### Step 3: Define Evidence Requirements
For each sub-question:
- Minimum source count (default: 3 independent sources)
- Source diversity requirement (at least 2 source types)
- Confidence threshold (minimum acceptable confidence level)
- Recency requirement (how current must data be?)

### Step 4: Select Methodology
Based on research type, select approach:
- Source hunting strategy
- Verification protocol
- Analysis framework
- Synthesis approach

### Step 5: Define Deliverable
Specify the output:
- Format (from swipe file templates)
- Length constraints
- Key sections required
- Quality checkpoints

## Output Template

```
RESEARCH BRIEF
==============
Core Question: [One sentence]
Research Type: [Classification]
Deadline: [Date]
Confidence Target: [0-100]

Sub-Questions:
1. [Question] — Sources needed: [N], Recency: [requirement]
2. [Question] — Sources needed: [N], Recency: [requirement]

Methodology: [Selected approach]
Deliverable Format: [Template reference]
Quality Gates: [Checkpoints before delivery]

Assigned Agents: [Which squad members]
Estimated Effort: [Hours/complexity]
```

## Quality Checks

- [ ] Core question is specific and answerable
- [ ] Sub-questions are MECE (mutually exclusive, collectively exhaustive)
- [ ] Evidence requirements are explicit
- [ ] Deliverable format matches requester needs
- [ ] Deadline is achievable given scope
