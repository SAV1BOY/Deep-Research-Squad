# Source Catalog

> **Purpose:** Comprehensive catalog of all sources consulted during a research engagement.
> Tracks provenance, reliability, usage, and access details for every source.
> Use `{{placeholder}}` markers to fill in project-specific details.

---

## When to Use

- Building a master reference list for a multi-squad research project
- Ensuring no source is lost or unattributed across handoffs
- Providing an auditable trail of all information inputs

---

**Project:** {{project_name}}
**Catalog Owner:** {{researcher_or_squad_name}}
**Date Started:** {{date_yyyy_mm_dd}}
**Last Updated:** {{date_yyyy_mm_dd}}
**Total Sources:** {{count}}

---

## 1. Source Registry

### Primary Sources

| ID | Title / Description | Author(s) | Type | Date | URL / Location | Reliability | Status |
|----|-------------------|-----------|------|------|---------------|-------------|--------|
| S-001 | {{source_title}} | {{author}} | {{type_eg_report_paper_dataset}} | {{pub_date}} | {{url_or_path}} | {{high_medium_low}} | {{used_reviewed_rejected}} |
| S-002 | {{source_title}} | {{author}} | {{type}} | {{pub_date}} | {{url_or_path}} | {{reliability}} | {{status}} |
| S-003 | {{source_title}} | {{author}} | {{type}} | {{pub_date}} | {{url_or_path}} | {{reliability}} | {{status}} |

### Secondary Sources

| ID | Title / Description | Author(s) | Type | Date | URL / Location | Reliability | Status |
|----|-------------------|-----------|------|------|---------------|-------------|--------|
| S-101 | {{source_title}} | {{author}} | {{type}} | {{pub_date}} | {{url_or_path}} | {{reliability}} | {{status}} |
| S-102 | {{source_title}} | {{author}} | {{type}} | {{pub_date}} | {{url_or_path}} | {{reliability}} | {{status}} |

> Instruction: Primary = directly informs findings. Secondary = provides context or corroboration.

## 2. Source Type Breakdown

| Type | Count | % of Total | Notes |
|------|-------|-----------|-------|
| Academic papers | {{count}} | {{percent}} | {{notes}} |
| Industry reports | {{count}} | {{percent}} | {{notes}} |
| News articles | {{count}} | {{percent}} | {{notes}} |
| Government/regulatory | {{count}} | {{percent}} | {{notes}} |
| Interviews/surveys | {{count}} | {{percent}} | {{notes}} |
| Datasets | {{count}} | {{percent}} | {{notes}} |
| Other | {{count}} | {{percent}} | {{notes}} |

## 3. Reliability Assessment

| Rating | Criteria | Source Count |
|--------|----------|-------------|
| High | {{definition_eg_peer_reviewed_or_official_data}} | {{count}} |
| Medium | {{definition_eg_reputable_but_unverified}} | {{count}} |
| Low | {{definition_eg_single_source_or_opinion}} | {{count}} |

## 4. Source Gaps

| Topic Area | Sources Available | Gap Description | Impact on Research |
|-----------|------------------|-----------------|-------------------|
| {{topic_1}} | {{count}} | {{what_is_missing}} | {{high_medium_low}} |
| {{topic_2}} | {{count}} | {{what_is_missing}} | {{high_medium_low}} |

> Instruction: Identify where source coverage is thin. This feeds into confidence assessments.

## 5. Access and Licensing Notes

| Source ID(s) | Access Restriction | License / Terms | Expiry |
|-------------|-------------------|-----------------|--------|
| {{source_ids}} | {{paywall_nda_login_required_none}} | {{license_type}} | {{date_or_na}} |
| {{source_ids}} | {{restriction}} | {{license}} | {{expiry}} |

## 6. Rejected Sources

| ID | Title | Reason for Rejection |
|----|-------|---------------------|
| R-001 | {{source_title}} | {{reason_eg_outdated_unreliable_off_topic}} |
| R-002 | {{source_title}} | {{reason}} |

> Instruction: Document why sources were excluded for methodological transparency.

---

### Example (Filled)

**S-001:** Gartner, "Magic Quadrant for AI Code Assistants 2025", Feb 2025
- Type: Industry report | Reliability: High | Status: Used
- Used in: Sections 3.2, 4.1 of main report

**Source Gaps:**
| Topic Area | Sources Available | Gap Description | Impact |
|-----------|------------------|-----------------|--------|
| Asia-Pacific adoption | 2 | No primary research; relying on extrapolated US data | High |

---

*Catalog maintained by {{catalog_owner}} | Last updated {{date_yyyy_mm_dd}}*
