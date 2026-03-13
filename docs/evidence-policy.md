# Evidence Policy

## Purpose

This policy governs how the Deep Research Squad handles evidence throughout
the research lifecycle. It defines evidence tiers, handling rules, and
the standards that all agents must follow.

## Evidence Tier Definitions

| Tier   | Name               | Criteria                                          |
|--------|--------------------|---------------------------------------------------|
| Tier 1 | Confirmed          | Multiple independent primary sources agree         |
| Tier 2 | Strong Indication  | One primary + corroborating secondary sources      |
| Tier 3 | Moderate Indication| Secondary sources agree, no primary contradiction  |
| Tier 4 | Weak Signal        | Single source or unverified, but plausible         |
| Tier 5 | Unverified         | Claim exists but lacks corroboration               |

## Source Type Classification

| Type               | Code | Typical Tier Range |
|--------------------|------|--------------------|
| Peer-reviewed      | PR   | 1                  |
| Government data    | GV   | 1-2                |
| Company filings    | CF   | 2                  |
| Industry reports   | IR   | 2-3                |
| Major news outlet  | NM   | 2-3                |
| Expert interview   | EI   | 3                  |
| Blog / opinion     | BO   | 4                  |
| Social media       | SM   | 4-5                |
| Anonymous / leaked | AN   | 5                  |

## Evidence Handling Rules

### Rule 1: Classify Every Source

Every source entering the research process must be classified by type and tier
before its claims are used in analysis.

### Rule 2: Match Language to Tier

The language used to present a finding must match its evidence tier.
See `voice/language-guides/evidence-language.md` for the mapping.

### Rule 3: Cross-Validate When Possible

Tier 3-5 evidence should be cross-validated against independent sources
before supporting conclusions. If cross-validation is not possible, disclose.

### Rule 4: Flag Interested Parties

Sources with a financial, ideological, or institutional interest in the
outcome must be flagged. Their claims receive additional scrutiny.

### Rule 5: Date-Stamp All Evidence

Every piece of evidence must include the date of the source and the date
it was accessed. Evidence degrades with time.

### Rule 6: Disclose Single-Source Findings

If a finding rests on a single source, this must be disclosed regardless
of the source's tier. Single-source findings cannot exceed [PROBABLE].

### Rule 7: Archive Volatile Sources

Web sources that may change or disappear must be archived (screenshot,
PDF, or web archive link) at the time of access.

## Evidence Aggregation

When combining multiple evidence inputs:
- Converging Tier 2-3 sources can support a [CONFIRMED] confidence level.
- Diverging sources require disclosure of the conflict and a judgment call.
- A single Tier 1 source can support [PROBABLE] on its own.
- No combination of Tier 4-5 sources can support [CONFIRMED].

## Evidence Audit

The Evidence Auditor reviews all deliverables for:
- Correct tier assignment.
- Accurate citations.
- Proper language-to-tier matching.
- Disclosed conflicts of interest.
- Complete source lists with access dates.

## Policy Violations

Evidence policy violations are flagged during the Evidence Audit (Gate 5).
Violations must be corrected before delivery. Repeated violations trigger
a process review.
