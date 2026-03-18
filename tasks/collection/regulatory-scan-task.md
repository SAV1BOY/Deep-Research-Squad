# Regulatory Scan Task

## Purpose
Scan the regulatory landscape relevant to the research topic, identifying current regulations, pending legislation, enforcement trends, and compliance requirements that could affect findings or recommendations.

## When to Use
- When the research topic operates within a regulated industry
- When recommendations may have legal or compliance implications
- When evaluating market entry, product feasibility, or strategic options
- When regulatory change is a key uncertainty in the research domain

## Agents Involved
- **Lead**: Domain Specialist
- **Supporting**: Data Researcher, OSINT Investigator
- **Consulted**: Source Hunter, Evidence Verifier

## Inputs
- Research topic and geographic scope
- Industry or sector classification
- List of relevant regulatory bodies and jurisdictions
- Known regulations or compliance frameworks already identified
- Timeline of interest (current state, near-term pipeline, long-term trajectory)

## Steps
1. Identify all regulatory bodies and jurisdictions relevant to the topic
2. Catalog current regulations, standards, and compliance requirements in force
3. Search for pending legislation, proposed rules, and regulatory consultations
4. Review recent enforcement actions and regulatory guidance documents
5. Identify regulatory trends and directional signals from policy statements
6. Assess the likelihood and timeline of pending regulatory changes
7. Map regulatory requirements to specific aspects of the research question
8. Flag areas where regulations differ across jurisdictions
9. Document compliance gaps or risks relevant to the research conclusions
10. Compile findings into a regulatory landscape summary

## Quality Gates
- All relevant jurisdictions are covered, not just the most obvious
- Distinction is maintained between enacted regulations and proposed changes
- Enforcement trends are included, not just the text of regulations
- Cross-jurisdictional differences are explicitly noted
- Sources are authoritative (government sites, official gazettes, legal databases)
- Regulatory timeline projections include confidence assessments

## Outputs
- Regulatory landscape summary organized by jurisdiction and topic
- Current regulations inventory with status and applicability
- Pending legislation and proposed rules tracker
- Enforcement trend analysis
- Cross-jurisdictional comparison matrix
- Regulatory risk assessment for the research conclusions

## Estimated Effort
- **Single jurisdiction, narrow topic**: 1-2 hours
- **Multiple jurisdictions or broad topic**: 3-5 hours
- **Global scan, complex regulatory environment**: 5-10 hours

## Dependencies
- Requires defined research scope from `define-scope-and-boundaries.md`
- Feeds into `run-scenario-analysis.md` and `build-implications-map.md`
- Outputs inform `build-decision-brief.md` for actionable recommendations
