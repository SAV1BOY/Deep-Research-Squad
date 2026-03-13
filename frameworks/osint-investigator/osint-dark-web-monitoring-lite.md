# OSINT Dark Web Monitoring Lite Framework

## Purpose

Provide guidelines for legally monitoring publicly accessible dark web content for intelligence purposes. This framework is strictly limited to passive observation of publicly accessible forums, markets, and paste sites. It emphasizes operational security (OpSec), legal compliance, and clear boundaries on what is and is not acceptable. This is a monitoring framework, not a participation framework.

## When to Use

- When assessing whether an organization's data has been exposed or leaked.
- When monitoring threat actor discussions relevant to a client or research subject.
- When tracking the availability of specific types of data, goods, or services on dark web markets.
- When building situational awareness about cybersecurity threats.
- Only when legally authorized and ethically justified for the specific investigation.

## Inputs

- Specific intelligence requirements (what are you looking for and why).
- Legal authorization and documented justification for monitoring.
- Operational security protocols and tools.
- Knowledge of relevant dark web platforms and access methods.
- Clear ethical guidelines approved by appropriate authority.

## Process

1. **Establish legal authority.** Document the legal basis for monitoring. Consult legal counsel if there is any doubt. Do not proceed without clear authorization.
2. **Define strict scope.** Specify exactly what you are looking for. Dark web monitoring must be targeted, not exploratory browsing.
3. **Set up OpSec environment.** Use dedicated, isolated hardware or virtual machines. Use Tor or appropriate anonymization tools. Do not use personal or organizational accounts. Do not reuse credentials. Use a VPN as an additional layer. Keep the monitoring environment separate from all other work.
4. **Identify target sources.** Based on intelligence requirements, identify specific forums, paste sites, or market listings to monitor. Use known indexing services and directories.
5. **Passive collection only.** Observe and record publicly visible content. Do not create accounts on illegal marketplaces. Do not post, comment, or interact. Do not purchase anything. Do not click on links to illegal content.
6. **Document findings.** Record observations with timestamps, source identifiers, and screenshots. Maintain chain of custody if findings may be used for legal or compliance purposes.
7. **Analyze in the clean environment.** Transfer findings to a separate analysis environment. Do not analyze on the monitoring machine. Look for relevance to intelligence requirements.
8. **Report through proper channels.** If illegal activity or imminent threats are discovered, report through appropriate legal and organizational channels immediately.
9. **Debrief and clean up.** After each monitoring session, review OpSec. Wipe the monitoring environment. Document what was accessed and what was found.

## What NOT To Do

- **Do not create accounts on illegal platforms.**
- **Do not purchase, download, or possess illegal content or goods.**
- **Do not interact with threat actors or other users.**
- **Do not use entrapment or deception techniques.**
- **Do not access content that is illegal to view in your jurisdiction.**
- **Do not store illegal content, even for evidence purposes, without legal authorization.**
- **Do not browse casually or explore beyond the defined scope.**
- **Do not use organizational networks or identifiable infrastructure.**
- **Do not share raw dark web content outside authorized channels.**

## Outputs

- A monitoring report addressing the specific intelligence requirements.
- Evidence of data exposure or threats relevant to the investigation, if found.
- An assessment of threat levels and recommended actions.
- OpSec review and any security concerns from the monitoring session.
- Referrals to law enforcement if illegal activity affecting the client is discovered.

## Legal Boundaries

- Monitoring must comply with all applicable laws in your jurisdiction.
- Passive observation of publicly accessible content is generally legal; active participation is not.
- Possession of certain content (e.g., CSAM, stolen data) is illegal regardless of intent.
- When in doubt, consult legal counsel before proceeding.
- Document everything to demonstrate lawful purpose and methods.

## Common Pitfalls

- **OpSec failures.** Using identifiable infrastructure, reusing credentials, or failing to isolate the monitoring environment.
- **Scope creep.** Starting with a specific target and drifting into general browsing.
- **Legal overreach.** Crossing from passive monitoring into active participation or possession of illegal material.
- **Attribution errors.** Misidentifying who posted content or misinterpreting dark web communications.
- **Overestimating dark web intelligence.** Much dark web content is scams, outdated, or fabricated. Verification is critical.
- **Neglecting reporting obligations.** Failing to report discovered illegal activity through proper channels.
- **Inadequate documentation.** Not maintaining sufficient records to demonstrate lawful purpose.

## Related Frameworks

- `osint-open-source-intelligence.md` - Dark web monitoring is a specialized OSINT collection method.
- `osint-digital-footprint-mapping.md` - Dark web presence can be part of an entity's digital footprint.
- `osint-corporate-intelligence.md` - Dark web monitoring may reveal corporate data exposure.
- `data-researcher-data-quality-check.md` - Dark web data requires rigorous quality assessment.
