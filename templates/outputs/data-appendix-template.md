# Data Appendix

> **Purpose:** Provide a structured appendix containing all data referenced in a research
> report. Ensures transparency, reproducibility, and easy verification of claims.
> Use `{{placeholder}}` markers to fill in project-specific details.

---

## When to Use

- Accompanying a deep-dive report, market thesis, or due diligence report
- When stakeholders need to verify data points or conduct their own analysis
- When regulatory or compliance requirements demand data traceability

---

**Parent Report:** {{title_of_main_report}}
**Appendix Version:** {{version_number}}
**Date:** {{date_yyyy_mm_dd}}
**Prepared By:** {{researcher_name}}

---

## A. Data Sources Summary

| ID | Source Name | Type | Access Date | Coverage Period | Reliability |
|----|-----------|------|-------------|-----------------|-------------|
| D1 | {{source_name}} | {{database_survey_api_report}} | {{date}} | {{start_to_end}} | {{high_medium_low}} |
| D2 | {{source_name}} | {{type}} | {{date}} | {{period}} | {{high_medium_low}} |
| D3 | {{source_name}} | {{type}} | {{date}} | {{period}} | {{high_medium_low}} |

## B. Key Data Tables

### B.1 {{data_table_1_title}}

> Description: {{what_this_table_shows_and_how_it_was_derived}}

| {{column_1_label}} | {{column_2_label}} | {{column_3_label}} | {{column_4_label}} |
|--------------------|--------------------|--------------------|-------------------|
| {{value}} | {{value}} | {{value}} | {{value}} |
| {{value}} | {{value}} | {{value}} | {{value}} |
| {{value}} | {{value}} | {{value}} | {{value}} |

Source: {{source_id_from_section_A}}

### B.2 {{data_table_2_title}}

> Description: {{what_this_table_shows_and_how_it_was_derived}}

| {{column_1_label}} | {{column_2_label}} | {{column_3_label}} |
|--------------------|--------------------|--------------------|
| {{value}} | {{value}} | {{value}} |
| {{value}} | {{value}} | {{value}} |

Source: {{source_id_from_section_A}}

## C. Calculations and Transformations

| Metric | Formula / Method | Inputs | Result | Notes |
|--------|-----------------|--------|--------|-------|
| {{metric_name}} | {{formula_or_description}} | {{input_variables}} | {{computed_value}} | {{assumptions}} |
| {{metric_name}} | {{formula_or_description}} | {{input_variables}} | {{computed_value}} | {{assumptions}} |

> Instruction: Document every derived metric so readers can reproduce your calculations.

## D. Data Quality Notes

- **Completeness:** {{description_of_any_missing_data_and_how_handled}}
- **Accuracy:** {{known_issues_with_data_precision}}
- **Timeliness:** {{how_current_the_data_is_and_refresh_frequency}}
- **Consistency:** {{cross_source_discrepancies_noted}}

## E. Raw Data References

| Dataset | Format | Size | Location | Access Instructions |
|---------|--------|------|----------|-------------------|
| {{dataset_name}} | {{csv_json_xlsx}} | {{row_count_or_file_size}} | {{path_or_url}} | {{access_notes}} |
| {{dataset_name}} | {{format}} | {{size}} | {{location}} | {{access_notes}} |

---

### Example (Filled)

**Parent Report:** Q3 Market Expansion Feasibility Study

**B.1 Regional Market Size Estimates**
| Region | TAM ($M) | CAGR (%) | Our Addressable Share (%) |
|--------|----------|----------|--------------------------|
| Southeast Asia | 8,200 | 34 | 4.2 |
| Latin America | 5,100 | 22 | 6.8 |

Source: D1 (Gartner Market Report, accessed 2025-03-01)

---

*Appendix prepared by {{researcher_name}} on {{date_yyyy_mm_dd}}*
*Data integrity last verified: {{verification_date}}*
