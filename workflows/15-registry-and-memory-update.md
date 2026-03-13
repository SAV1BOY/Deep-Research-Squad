# Workflow 15: Registry and Memory Update

## Purpose
Update all persistent registries and knowledge stores after a research cycle completes. Record sources discovered, claims validated, insights generated, decisions made, and lessons learned so that future research benefits from accumulated institutional memory and avoids repeating past work.

## Trigger
- Research output is delivered to the requester (post-Workflow 14).
- Audit results are finalized from Workflow 13.
- A research project is cancelled or paused (partial update).

## Agents Involved
- **Research Lead**: Supervises registry updates and validates entries.
- **Registry Keeper**: Performs the actual updates across all registries.
- **Quality Auditor**: Verifies that registry entries are accurate and complete.

## Inputs
- Complete research output (all workflow artifacts).
- Audit report and quality score from Workflow 13.
- Source chain documentation from Workflow 04.
- Evidence registry from Workflow 05.
- Decision brief from Workflow 12.
- Any feedback received from the requester.

## Steps

1. **Update the source registry**: For every source used in the research:
   - Add new sources not previously in the registry.
   - Update existing entries with new reliability information.
   - Record: source name, URL/DOI, source class, reliability rating, domain tags, last accessed date.
   - Mark sources that proved especially valuable with a "high-value" flag.
   - Mark sources that proved unreliable or misleading with a "caution" flag.

2. **Update the claims registry**: For every validated claim from synthesis:
   - Add new claims with their confidence level (certain or probable).
   - Link each claim to its supporting evidence and sources.
   - Tag claims with domain, topic, and research question keywords.
   - If a claim updates or supersedes a prior claim in the registry, mark the old claim as superseded and link to the new one.

3. **Update the insights registry**: Extract and record generalizable insights:
   - Patterns observed that may apply to future research.
   - Unexpected findings that challenged assumptions.
   - Connections between previously unrelated domains.
   - Each insight should be a concise statement with context and source reference.

4. **Update the decision registry**: Record the decision outcome:
   - What options were presented.
   - What was recommended and why.
   - What the requester decided (if known).
   - Outcome tracking: set a future date to check whether the decision played out as expected.

5. **Update the methodology registry**: Record what worked and what did not:
   - Which search queries were most effective.
   - Which tools produced the best results for this research type.
   - Which decomposition framework fit best.
   - Which models were most useful to the requester.
   - Time estimates vs. actuals for each workflow phase.

6. **Update the contradiction registry**: Record notable contradictions:
   - Contradictions that were resolved and how.
   - Contradictions that remain unresolved in the domain.
   - Sources that frequently contradict each other (pattern tracking).
   - This helps future research anticipate disagreements.

7. **Update the lessons-learned registry**: Capture operational lessons:
   - What went well in the research process.
   - What caused delays or rework.
   - What quality issues were found during audit.
   - Specific process improvements suggested.
   - These feed directly into Workflow 20 (retrospective).

8. **Cross-link entries**: Ensure all registry entries are properly cross-referenced:
   - Sources link to the claims they support.
   - Claims link to the research questions they answer.
   - Insights link to the evidence that generated them.
   - Decisions link to the research that informed them.
   - This creates a navigable knowledge graph.

9. **Archive research artifacts**: Store the complete set of research artifacts:
   - All workflow outputs in a single research package.
   - Tagged with: research ID, topic, date, quality score, requester.
   - Indexed for future retrieval by keyword, topic, or domain.
   - Set retention period based on topic (default: 12 months active, then archive).

10. **Verify registry integrity**: Quality Auditor checks:
    - No duplicate entries created.
    - All required fields populated.
    - Cross-links are valid (no broken references).
    - New entries do not conflict with existing entries without explanation.
    - Registry statistics updated (total sources, claims, insights, etc.).

## Quality Gates
- Every source used in the research must appear in the source registry.
- Every certainty from Layer 1 must be in the claims registry.
- At least 3 lessons learned must be captured per research project.
- Cross-links must be verified for all new entries.
- Registry integrity check must pass with no broken references.
- Archive must include all workflow artifacts with proper indexing.

## Outputs
- Updated source registry.
- Updated claims registry.
- Updated insights registry.
- Updated decision registry.
- Updated methodology registry.
- Updated contradiction registry.
- Updated lessons-learned registry.
- Archived research package.
- Registry update log (what was added, modified, or superseded).

## Next Workflow
- **16-cross-squad-handoff.md** (if handoff is needed in parallel with registry update).
- **20-research-retro-and-learning.md** (for periodic retrospective using accumulated lessons).
