# Workflow 19: Research Quality Review Cycle

## Purpose
Conduct periodic quality reviews across all completed research to identify systemic trends, recurring issues, and opportunities for improvement. Analyze quality scores, audit findings, and feedback patterns to continuously raise the squad's research standards and catch degradation before it affects output quality.

## Trigger
- Scheduled periodic review (default: every 10 completed research projects or monthly, whichever comes first).
- Quality score drops below 75 on two consecutive projects.
- Requester feedback indicates recurring quality concerns.
- Research Lead requests an ad-hoc quality review.

## Agents Involved
- **Quality Auditor**: Leads the review cycle and produces the quality report.
- **Research Lead**: Reviews findings and prioritizes improvements.
- **Methodology Reviewer**: Analyzes process-related quality patterns.
- **Registry Keeper**: Provides historical data from registries.

## Inputs
- Audit reports from all projects in the review period (Workflow 13).
- Quality scores and dimension breakdowns.
- Requester feedback collected post-delivery.
- Lessons-learned registry entries from Workflow 15.
- Escalation logs from Workflows 17 and 18.
- Time tracking data (planned vs. actual per workflow phase).

## Steps

1. **Define review scope**: Establish the boundaries of this review cycle:
   - Which projects are included (by date range or project count).
   - Which quality dimensions will be analyzed.
   - Whether this is a routine review or triggered by a specific concern.
   - Set the review timeline (typically 2-3 days for a routine cycle).

2. **Aggregate quality scores**: Compile quality scores across the review period:
   - Calculate mean, median, and trend for overall quality scores.
   - Break down by dimension: scope completeness, methodology soundness, evidence integrity, bias management, reproducibility.
   - Identify any downward trends or dimension-specific weaknesses.
   - Compare against the previous review cycle.

3. **Analyze audit findings by category**: Group all audit findings across projects:
   - Count frequency of each issue type.
   - Rank issues by frequency and severity.
   - Identify the top 5 most common issues.
   - Determine if issues are concentrated in specific workflows or distributed broadly.

4. **Review requester feedback**: Analyze feedback received from research requesters:
   - Satisfaction ratings (if collected).
   - Specific complaints or praise.
   - Recurring themes in feedback.
   - Gap between what was delivered and what was expected.
   - Identify any systematic misalignment between research output and requester needs.

5. **Examine escalation patterns**: Review escalation data from Workflows 17 and 18:
   - How frequently were domain specialists escalated?
   - How frequently were contradictions escalated to the Chief?
   - Were escalations timely or delayed?
   - Were escalation outcomes satisfactory?
   - Identify if escalation thresholds need adjustment.

6. **Analyze time efficiency**: Compare planned vs. actual timelines:
   - Which workflow phases consistently run over time?
   - Which phases are well-estimated?
   - Is there a pattern in what causes delays (collection, contradiction resolution, rework)?
   - Calculate the rework rate (percentage of projects requiring post-audit fixes).

7. **Identify root causes**: For the top 5 quality issues and any negative trends:
   - Conduct a root cause analysis (ask "why" five times).
   - Distinguish between: skill gaps, process gaps, tool gaps, and resource gaps.
   - Determine if the root cause is systemic or project-specific.
   - Prioritize root causes by impact and fixability.

8. **Benchmark against standards**: Compare squad quality metrics against:
   - Internal quality targets set in the research plan template.
   - Historical squad performance (are we improving?).
   - Any external benchmarks or best practices available.
   - Identify areas where the squad exceeds standards and areas where it falls short.

9. **Draft improvement recommendations**: For each identified root cause, propose a specific improvement:
   - **Process change**: Modify a workflow step or add a new checkpoint.
   - **Training need**: Identify skills that agents need to develop.
   - **Tool improvement**: Recommend new tools or better use of existing ones.
   - **Template update**: Revise templates or checklists that are causing issues.
   - Prioritize recommendations by expected impact and effort to implement.

10. **Produce the quality review report**: Compile the full review:
    - Executive summary: overall quality trend, top issues, and top recommendations.
    - Detailed analysis by dimension with supporting data.
    - Root cause analysis results.
    - Improvement recommendations with priority and ownership.
    - Comparison to previous review cycle.
    - Next review cycle date.

11. **Review and approve actions**: Research Lead reviews the quality report:
    - Approves or modifies improvement recommendations.
    - Assigns ownership for each approved improvement.
    - Sets deadlines for implementation.
    - Communicates changes to the squad.

## Quality Gates
- Review must cover all projects in the defined scope with no omissions.
- At least 5 quality dimensions must be analyzed with trend data.
- Root cause analysis must be performed for every issue ranked in the top 5.
- Improvement recommendations must be specific, actionable, and prioritized.
- Report must include comparison to the previous review cycle.
- Research Lead must approve the action plan before implementation begins.

## Outputs
- Quality review report (trends, issues, root causes, recommendations).
- Approved improvement action plan with owners and deadlines.
- Updated quality benchmarks (if standards need adjustment).
- Communication to the squad on changes.
- Next review cycle scheduled.

## Next Workflow
- **20-research-retro-and-learning.md** (feed quality trends into retrospective).
- **15-registry-and-memory-update.md** (update methodology registry with improvements).
