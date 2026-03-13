# Script: Package Delivery

## Purpose

Assembles the final research deliverable package for the requester.
Ensures all components are present, properly formatted, and organized
for the recipient's consumption.

## Trigger

Called after the research audit passes and the deliverable is approved
for delivery.

## Inputs

- `deliverable`: The main research output (approved by audit)
- `supporting_materials`: Evidence tables, source maps, timelines
- `research_brief`: Original brief for reference
- `delivery_format`: Requested format and channel
- `audience`: Who receives this

## Process

### Step 1: Assemble Package Components

**Required in every delivery**:
- [ ] Executive summary (compressed, decision-ready)
- [ ] Main deliverable (full report, brief, or analysis)
- [ ] Confidence scorecard (overall + per-finding scores)
- [ ] Source list with diversity score

**Optional based on deliverable type**:
- [ ] Evidence tables (for deep dives and due diligence)
- [ ] Contradiction map (if significant contradictions exist)
- [ ] Timeline (if temporal analysis was performed)
- [ ] Market map (if landscape analysis was performed)
- [ ] Scenario analysis (if future-oriented)

### Step 2: Format for Audience
Adapt the package based on recipient:

**C-suite / Executive**:
- Lead with executive summary (1 page max)
- Main deliverable as appendix
- Highlight decisions needed and deadlines

**Analyst / Researcher**:
- Full deliverable with methodology details
- Evidence tables and source maps included
- Emphasis on data and methodology

**Cross-squad delivery**:
- Structured for integration into larger workstream
- Includes handoff notes and integration points
- Flags dependencies and open questions

### Step 3: Quality Final Check
Last-pass review:
- [ ] All links and references work
- [ ] No internal-only jargon in external deliverables
- [ ] Formatting is consistent throughout
- [ ] Page/section numbers are correct
- [ ] Date and version clearly marked
- [ ] Confidence scores present on all claims

### Step 4: Metadata Block
Attach delivery metadata:

```
DELIVERY METADATA
=================
Research ID: [Unique identifier]
Delivered: [Date and time]
Requester: [Name/role]
Deadline met: [Yes/No]
Overall confidence: [Score]
Source count: [Number]
Source diversity: [Score]
Audit status: [Passed/Conditional]
Shelf life: [How long this research remains current]
Refresh trigger: [What event should trigger an update]
```

### Step 5: Archive
After delivery:
- Archive complete package with all supporting materials
- Log delivery in quality tracker
- Set reminder for shelf-life expiration
- Note any follow-up research identified during the process

## Output

Final packaged deliverable ready for the requester, with all components
assembled, formatted, and metadata attached.

## Quality Checks

- [ ] Executive summary present and under 1 page
- [ ] Confidence scores on all major claims
- [ ] Source diversity score meets minimum threshold
- [ ] Format matches audience needs
- [ ] Metadata block complete
- [ ] Archive copy saved
