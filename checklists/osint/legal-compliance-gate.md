# OSINT Legal Compliance Gate

## Purpose

Verify that all open-source intelligence collection and analysis activities
comply with applicable legal frameworks, platform terms of service, and
ethical standards. Non-compliance exposes the research to legal liability and
reputational risk.

## When Triggered

- Before initiating any OSINT collection activity.
- When collection methods change or expand beyond the original plan.
- Before publishing or sharing OSINT findings externally.
- When handling personally identifiable information (PII).

## Prerequisites

- OSINT collection plan documented with methods and target sources.
- Applicable legal jurisdictions identified.
- Data handling and retention policies established.

## Checklist

- [ ] Applicable privacy laws (GDPR, CCPA, etc.) for target jurisdictions are identified.
- [ ] Collection methods comply with the laws of both the collector's and target's jurisdictions.
- [ ] Platform terms of service for each source are reviewed and respected.
- [ ] No unauthorized access, scraping beyond permitted limits, or circumvention of access controls.
- [ ] Personally identifiable information is handled according to data protection requirements.
- [ ] Data minimization principle applied: only necessary data is collected.
- [ ] Retention periods are defined and enforced for collected data.
- [ ] No collection from sources restricted by sanctions, embargoes, or court orders.
- [ ] Ethical review completed for sensitive subjects (minors, vulnerable populations, private individuals).
- [ ] Chain of custody for collected evidence is maintained for legal defensibility.
- [ ] All collection activities are logged with timestamps and method descriptions.
- [ ] Output reports redact PII unless its inclusion is justified and lawful.

## Pass / Fail Criteria

**Pass**: All collection activities have been reviewed against applicable laws
and platform terms, PII handling follows data protection requirements, and
activities are fully logged.

**Fail**: Any collection activity lacks legal review, PII is mishandled, or
terms of service are violated.

## Escalation if Failed

- Halt the non-compliant collection activity immediately.
- Consult legal counsel if there is uncertainty about jurisdiction or law.
- Purge unlawfully collected data according to data protection requirements.
- Escalate to the Chief if legal exposure affects the broader research
  engagement.
- Document the compliance failure and remediation steps taken.
