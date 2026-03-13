# Script: Update Registries

## Purpose

Maintains and updates the source registries in swipe-sources/ to ensure
they remain current, accurate, and comprehensive. Registries decay over
time as sources change, move, or become obsolete.

## Trigger

- Scheduled: Monthly review cycle
- Event-driven: When a source is found to be outdated during research
- Ad-hoc: When a significant new source is discovered

## Inputs

- `registry_files`: All files in swipe-sources/
- `usage_logs`: Which sources have been used recently
- `quality_feedback`: Feedback on source quality from research agents
- `new_sources`: Sources discovered during recent research

## Process

### Step 1: Source Accessibility Check
For each source in each registry:
- Is the URL still active?
- Has the access model changed (free → paywalled, etc.)?
- Has the source been updated recently?
- Has the publisher changed or merged?

### Step 2: Quality Reassessment
For sources used in recent research:
- Did the source deliver quality data?
- Were there accuracy issues discovered?
- Has the source's methodology changed?
- Should the reliability tier be adjusted?

### Step 3: New Source Integration
For each new source discovered:
- Classify by type and tier
- Assess reliability and access model
- Add to appropriate registry file
- Note discovery context

### Step 4: Deprecation Review
Identify sources that should be removed or downgraded:
- Sources that are no longer updated
- Sources with demonstrated quality problems
- Sources that have been superseded by better alternatives
- Sources behind prohibitive paywalls with no alternatives

### Step 5: Gap Analysis
Identify gaps in registry coverage:
- Are emerging source types covered (podcasts, substacks)?
- Are all relevant geographies represented?
- Are domain-specific sources adequate for common research topics?

## Output

```
REGISTRY UPDATE REPORT
======================
Date: [Date]
Registries Reviewed: [Count]
Sources Checked: [Count]

Changes Made:
- Added: [Count] new sources
- Updated: [Count] existing entries
- Deprecated: [Count] sources
- Tier changed: [Count] sources

Gaps Identified:
- [Gap description]

Next Review: [Date]
```

## Update Rules

1. Never delete a source without documenting the reason
2. Tier changes require evidence (not just opinion)
3. New sources need at least one successful research use before Tier 1
4. Maintain changelog at bottom of each registry file
5. Review frequency: monthly for Tier 1 sources, quarterly for Tier 2-3
