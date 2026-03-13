# Naming Conventions

## Purpose

This document defines naming conventions for all artifacts produced by the
Deep Research Squad. Consistent naming enables findability, reduces confusion,
and supports automation.

## File Naming

### General Rules

- Use lowercase letters only.
- Separate words with hyphens (kebab-case).
- No spaces, underscores, or special characters.
- Keep names descriptive but concise (3-5 words maximum).

### Pattern by Directory

| Directory              | Pattern                        | Example                          |
|------------------------|--------------------------------|----------------------------------|
| voice/tone-profiles/   | `[style].md`                   | `executive.md`                   |
| voice/language-guides/  | `[topic]-language.md`         | `evidence-language.md`           |
| voice/calibration/     | `[topic]-scale.md`             | `audience-depth-scale.md`        |
| voice/channels/        | `[channel]-delivery.md`        | `deep-dive-delivery.md`         |
| phrases/               | `[topic]-prompts.md`           | `scoping-questions.md`          |
| docs/                  | `[topic].md`                   | `evidence-policy.md`             |

### Date-Stamped Files

When versions matter, append the date:
```
[type]-[topic]-[YYYY-MM-DD].[ext]
```
Example: `brief-market-entry-latam-2026-03-13.md`

## Document Titles

- Use sentence case (capitalize first word only).
- Be specific: "AI infrastructure market analysis" not "Research report."
- Include scope qualifiers: geography, timeframe, segment.

## Confidence Tags

Standard tags used inline in deliverables:

| Tag            | Meaning                              |
|----------------|--------------------------------------|
| [CONFIRMED]    | Multiple independent sources confirm |
| [PROBABLE]     | Strong evidence, minor uncertainty   |
| [HYPOTHESIS]   | Plausible, alternatives exist        |
| [UNKNOWN]      | Insufficient evidence                |

## Source Type Codes

| Code | Source Type          |
|------|----------------------|
| PR   | Peer-reviewed        |
| GV   | Government data      |
| CF   | Company filing       |
| IR   | Industry report      |
| NM   | News (major outlet)  |
| EI   | Expert interview     |
| BO   | Blog / opinion       |
| SM   | Social media         |
| AN   | Anonymous / leaked   |

## Channel Naming (Slack)

- `#research-[function]`: e.g., `#research-deliverables`, `#research-alerts`
- `#project-[name]`: e.g., `#project-market-entry-latam`

## Version Control

- Use semantic labels: `draft`, `review`, `final`.
- Append to filename or use document metadata.
- Example: `deep-dive-ai-infrastructure-draft.md`

## Quality Check

- Do all files follow the naming pattern?
- Are dates in YYYY-MM-DD format?
- Are confidence tags used consistently?
- Are source codes applied correctly?
