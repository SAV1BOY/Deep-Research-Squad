# Script: Generate Contradiction Map

## Purpose

Identifies and maps contradictions across sources for a given research topic.
Contradictions are not problems to hide — they are signals of complexity,
uncertainty, or evolving knowledge that must be surfaced transparently.

## Trigger

Called during evidence synthesis when multiple sources address the same
claims with different conclusions.

## Inputs

- `evidence_table`: Completed evidence table with all sources
- `claims`: List of claims being evaluated
- `sources`: Full source details including methodology

## Process

### Step 1: Contradiction Detection
Scan evidence table for sources that disagree:

| Claim | Source A Says | Source B Says | Type | Severity |
|-------|-------------|-------------|------|----------|
| [Claim] | [Finding A] | [Finding B] | [Type] | High/Med/Low |

**Contradiction types**:
- **Factual**: Different numbers or facts reported
- **Interpretive**: Same facts, different conclusions
- **Methodological**: Different methods yield different results
- **Temporal**: True at different times, evolution over period
- **Scope**: True at different scales or in different contexts

### Step 2: Root Cause Analysis
For each contradiction, diagnose why sources disagree:
1. **Different data**: Are they looking at different datasets?
2. **Different methods**: Are measurement approaches different?
3. **Different timeframes**: Are they measuring at different points?
4. **Different definitions**: Are they defining key terms differently?
5. **Different incentives**: Does one source have a bias?
6. **Genuine uncertainty**: Is the answer truly unknown?

### Step 3: Resolution Assessment
For each contradiction, assess if it can be resolved:
- **Resolvable**: One source is clearly more credible (explain why)
- **Partially resolvable**: Context-dependent truth (explain conditions)
- **Unresolvable**: Genuine uncertainty (acknowledge and report both)

### Step 4: Impact Assessment
How does each contradiction affect the research conclusions?
- **Critical**: Changes the bottom-line finding
- **Significant**: Affects confidence level or key details
- **Minor**: Affects supporting details but not conclusions

### Step 5: Recommendation
For each contradiction:
- If resolvable: State resolution and adjust findings
- If partially resolvable: State conditions under which each is true
- If unresolvable: Present both positions with confidence-weighted analysis

## Output Template

```
CONTRADICTION MAP
=================
Research Question: [Question]
Contradictions Found: [Count]
Critical: [Count] | Significant: [Count] | Minor: [Count]

[Table from Step 1]

Resolution Analysis:
1. [Contradiction]: [Root cause] → [Resolution/recommendation]

Impact on Findings:
- Finding X confidence adjusted from [old] to [new] because [reason]

Unresolved Contradictions:
- [Description]: Both positions presented in deliverable
```

## Quality Checks

- [ ] All contradictions identified (not suppressed)
- [ ] Root causes diagnosed for each
- [ ] Resolution attempts documented
- [ ] Impact on confidence scores calculated
- [ ] Unresolvable contradictions transparently reported
