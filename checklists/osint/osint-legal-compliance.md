# OSINT Legal Compliance Gate

## Purpose

Ensure all OSINT collection activities comply with applicable laws,
regulations, and ethical standards. Non-compliant collection creates
legal liability and invalidates the research.

## Gate Question

**Does all OSINT collection comply with legal and ethical requirements?**

## Prerequisites

- Applicable jurisdiction(s) identified.
- Data protection laws reviewed (GDPR, CCPA, etc.).
- Terms of service for target platforms reviewed.
- Ethical guidelines for the research context established.

## Pass Criteria

1. All data was collected from publicly accessible sources (no hacking,
   no unauthorized access).
2. Personal data collection complies with relevant data protection laws.
3. No terms of service were violated during automated data collection.
4. Scraping, if performed, respected robots.txt and rate limits.
5. No deception was used to gain access to information (no fake accounts,
   no social engineering).
6. Data storage and handling comply with retention and security policies.
7. Legal compliance assessment is documented and signed off.

## Fail Actions

- If unauthorized access occurred: delete the data and do not use it.
- If personal data was collected without legal basis: assess whether
  a lawful basis exists; if not, delete.
- If terms of service were violated: assess risk, document the violation,
  and seek alternative collection methods.
- If deception was used: flag the ethical violation and exclude the data.
- If compliance documentation is missing: complete it before proceeding.

## Escalation Rules

- Escalate immediately if any collection activity may have violated law.
- Escalate if the research requires personal data and the legal basis
  is uncertain.
- Escalate if a platform sends a cease-and-desist or blocks access
  during collection.
- Escalate if the research involves minors, vulnerable populations, or
  sensitive personal data.
