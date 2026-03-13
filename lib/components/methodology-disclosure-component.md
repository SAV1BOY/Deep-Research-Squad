# Methodology Disclosure Component

## Purpose

A reusable block that transparently documents how research was conducted. Ensures
every deliverable includes an honest account of methods, limitations, and potential
biases. Builds trust by showing the work, not just the conclusions.

## Interface

```yaml
methodology_disclosure:
  inputs:
    research_type: string          # From research-type-taxonomy
    sources_used: list[source_card] # All sources consulted
    tools_used: list[string]       # Search engines, databases, APIs
    time_spent: string             # Approximate research duration
    iterations: integer            # Number of research-refine cycles
  outputs:
    disclosure: structured_block   # Formatted methodology section
    limitation_count: integer      # Number of limitations identified
    bias_flags: list[string]       # Potential biases flagged
```

## Required Fields

### 1. Research Approach
- One-paragraph description of overall methodology
- Whether exploratory, confirmatory, or comparative
- Scope boundaries: what was included and excluded

### 2. Source Discovery Method
- How sources were identified (search terms, databases, referrals)
- Languages and geographies covered
- Date range of sources consulted
- Source types prioritized and why

### 3. Analysis Method
- How evidence was evaluated (rubric reference)
- How contradictions were resolved
- How confidence scores were calculated
- Whether peer review or cross-validation was performed

### 4. Limitations

| Category | Description |
|----------|-------------|
| Temporal | Analysis reflects data available as of [date] |
| Geographic | Primarily English-language sources; [regions] underrepresented |
| Source access | Paywalled sources not accessed: [list] |
| Expertise | No domain expert consultation for [topic] |
| Sample | Survey data limited to [n] respondents |

### 5. Potential Biases
- **Selection bias**: Sources may overrepresent [perspective]
- **Recency bias**: Recent events may be overweighted
- **Survivorship bias**: Failed companies/projects underrepresented
- **Confirmation bias**: Mitigated by actively seeking contradictory evidence

### 6. Reproducibility Statement
- Could another researcher reproduce these findings?
- What would they need access to?
- Are all sources publicly available?

## Formatting Rules

| Element | Rule |
|---------|------|
| Limitations | Always present, never "none identified" |
| Biases | List at least 2 potential biases per deliverable |
| Source counts | Exact numbers, not approximations |
| Tool references | Specific tool names and versions |
| Date ranges | Explicit start and end dates |

## Quality Gates

- [ ] Methodology section is present in every deliverable
- [ ] At least 2 limitations documented
- [ ] At least 2 potential biases flagged
- [ ] Source discovery method is specific enough to reproduce
- [ ] Analysis method references scoring rubrics used

## Usage Example

```
methodology_disclosure:
  research_type: "competitive-analysis"
  sources_used: [14 source cards]
  tools_used: ["web search", "SEC EDGAR", "Crunchbase API"]
  time_spent: "6 hours"
  iterations: 3
```

## Dependencies
- `source-card` component for source documentation
- `evidence-strength-rubric` utility for evaluation method reference
- `source-taxonomy` for source type classification
