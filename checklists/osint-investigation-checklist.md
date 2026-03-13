# OSINT Investigation Quality Checklist

## Purpose
Ensure that open source intelligence (OSINT) investigations are conducted systematically, ethically, and with appropriate rigor. This checklist validates that OSINT findings are reliable, sources are properly documented, and the investigation process respects legal and ethical boundaries while maximizing intelligence value.

## When to Use
- Before delivering any OSINT investigation findings or reports
- When reviewing OSINT research conducted by squad members
- During quality assurance of competitive intelligence, background research, or digital footprint analysis
- When OSINT findings will support due diligence, risk assessment, or strategic decisions

## Prerequisites
- Investigation scope and objectives are clearly defined
- Legal and ethical guidelines for OSINT collection have been reviewed and acknowledged
- Target entities, keywords, and initial leads have been identified
- OSINT tools and platforms are available and current
- Data handling and storage procedures for collected intelligence are established
- Analyst has current training on OSINT methods and ethical constraints

## Checklist Items

### Section 1: Investigation Planning
1. [ ] Investigation scope is documented with clear boundaries — PASS: scope defined; FAIL: unbounded investigation
2. [ ] Research questions are specific and answerable through open sources — PASS: focused questions; FAIL: questions requiring non-open sources
3. [ ] Collection plan identifies target source categories — PASS: structured collection plan; FAIL: ad hoc browsing
4. [ ] Timeline for investigation is established — PASS: time-boxed effort; FAIL: open-ended investigation
5. [ ] Legal review of collection methods has been completed — PASS: legal clearance obtained; FAIL: legal status uncertain

### Section 2: Source Coverage and Collection
6. [ ] Multiple source categories are covered (web, social media, public records, media, forums) — PASS: 4+ categories; FAIL: fewer than 4
7. [ ] Both surface web and deep web (non-indexed public) sources are searched — PASS: both layers covered; FAIL: surface-only search
8. [ ] Historical and archived content is checked (web archives, cached pages) — PASS: historical sources consulted; FAIL: current content only
9. [ ] Non-English sources are considered where relevant — PASS: multilingual coverage or justified exclusion; FAIL: English-only bias
10. [ ] Automated collection tools are supplemented with manual analysis — PASS: combined approach; FAIL: fully automated without analyst review

### Section 3: Verification and Validation
11. [ ] Each key finding is corroborated by at least 2 independent sources — PASS: corroboration achieved; FAIL: single-source findings presented as verified
12. [ ] Source authenticity is verified (not fabricated, spoofed, or manipulated) — PASS: authenticity checks performed; FAIL: source legitimacy not assessed
13. [ ] Information currency is verified (dates confirmed, not stale) — PASS: temporal accuracy confirmed; FAIL: undated or potentially stale information
14. [ ] Digital artifacts are preserved with metadata (screenshots, URLs, timestamps) — PASS: evidence preserved; FAIL: findings without preservation
15. [ ] Disinformation and misinformation risks are assessed — PASS: mis/disinformation screening done; FAIL: no screening for false information

### Section 4: Ethical and Legal Compliance
16. [ ] No unauthorized access to private systems or accounts occurred — PASS: open sources only; FAIL: boundary crossed
17. [ ] Personal data handling complies with applicable privacy regulations — PASS: privacy compliance; FAIL: privacy violations or uncertainty
18. [ ] Collection methods are documented and auditable — PASS: methods recorded; FAIL: untraceable collection process
19. [ ] Analyst operational security (OPSEC) was maintained — PASS: OPSEC procedures followed; FAIL: investigation footprint created unnecessarily
20. [ ] Proportionality of investigation depth to the objective is appropriate — PASS: proportionate effort; FAIL: disproportionate intrusion

### Section 5: Analysis and Reporting
21. [ ] Raw intelligence is analyzed and synthesized, not just collected — PASS: analysis present; FAIL: data dump without interpretation
22. [ ] Confidence levels are assigned to each key finding — PASS: confidence ratings; FAIL: unrated findings
23. [ ] Information gaps and intelligence requirements not met are documented — PASS: gaps acknowledged; FAIL: false completeness
24. [ ] Findings are organized by relevance and priority — PASS: prioritized presentation; FAIL: unprioritized data
25. [ ] Recommendations for further investigation or monitoring are provided — PASS: next steps outlined; FAIL: no follow-up guidance
26. [ ] Chain of reasoning from evidence to conclusion is transparent — PASS: logical chain documented; FAIL: conclusions without supporting trail

## Scoring
- Count the total number of items marked PASS
- Quality Score = (PASS count / 26) x 100
- Grade thresholds:
  - 92-100%: Excellent — thorough, ethical, and reliable OSINT investigation
  - 80-91%: Good — solid investigation with minor improvements needed
  - 68-79%: Acceptable — usable findings but gaps in coverage or methodology
  - Below 68%: Insufficient — investigation lacks rigor or has ethical concerns

## Escalation
- **Accept**: Score of 80% or above with no FAIL on items 5, 11, 16, or 17
- **Revise**: Score of 68-79%, or any FAIL on items 5, 11, 16, or 17
- **Escalate to lead**: Score below 68%, or ethical or legal boundary concerns, or evidence of disinformation contaminating findings
- **Escalate to stakeholder**: Investigation reveals matters requiring legal counsel, or findings have security implications beyond the original scope, or OSINT alone cannot answer the research question
