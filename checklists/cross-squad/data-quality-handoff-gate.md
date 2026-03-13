# Data Quality Handoff Gate

## Purpose

Ensure that data transferred between squads meets quality standards that
prevent downstream errors. Data quality problems introduced at handoff
boundaries are expensive to detect and fix later in the research pipeline.

## When Triggered

- When any squad transfers a dataset or structured data to another squad.
- When data is aggregated from multiple squad outputs into a shared resource.
- Before data is used as input to modeling or quantitative analysis.

## Prerequisites

- Source squad has completed its data collection and processing.
- Data schema or expected format is defined by the receiving squad.
- Data provenance records are available.

## Checklist

- [ ] Data schema matches the receiving squad's expected input format.
- [ ] All required fields are populated with no unexplained missing values.
- [ ] Data types are correct and consistent (dates, numbers, categories).
- [ ] Units of measurement are documented and consistent throughout.
- [ ] Duplicate records are identified and resolved or flagged.
- [ ] Outliers are documented with explanations (valid extremes vs. errors).
- [ ] Data provenance is recorded: original source, collection method, processing steps.
- [ ] Temporal coverage of the data matches the research scope requirements.
- [ ] Known data quality issues are disclosed in an accompanying quality report.
- [ ] A sample validation check has been performed (spot-check against original sources).
- [ ] Data is encoded in an agreed format (CSV, JSON, etc.) with documented encoding.
- [ ] Receiving squad has confirmed they can parse and use the data successfully.

## Pass / Fail Criteria

**Pass**: Data conforms to the expected schema, has documented provenance,
disclosed quality issues, and the receiving squad confirms usability.

**Fail**: Schema mismatches exist, provenance is missing, quality issues are
undisclosed, or the receiving squad cannot use the data as provided.

## Escalation if Failed

- Return data to the sending squad with specific quality issues documented.
- If schema mismatches are structural, coordinate between squad leads to
  agree on a shared format.
- Escalate to the Architect if data quality issues indicate a systemic
  problem in the collection methodology.
- Do not proceed with downstream analysis until data quality criteria are met.
