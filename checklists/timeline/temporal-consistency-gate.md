# Temporal Consistency Gate

## Purpose

Verify that dates, durations, and sequences reported across multiple sources
are consistent with one another. Inconsistent timelines undermine causal
reasoning and erode confidence in the overall research narrative.

## When Triggered

- After merging events from two or more independent sources into a single
  timeline.
- When a newly discovered event contradicts an established sequence.
- Before timeline data is passed to synthesis or reporting stages.

## Prerequisites

- At least two independent sources contributing timeline events.
- Events placed in chronological order with source attributions.
- Temporal boundaries defined by the research scope.

## Checklist

- [ ] All dates for the same event agree across sources, or discrepancies are documented.
- [ ] Sequence of events is consistent: no source claims A preceded B while another claims the reverse.
- [ ] Durations reported for the same period are compatible across sources.
- [ ] No event is dated outside the scope's temporal boundaries without justification.
- [ ] Where sources use different calendar systems or time zones, conversions are verified.
- [ ] Approximate dates (e.g., "early 2023") are bounded and do not conflict with precise dates from other sources.
- [ ] Overlapping events are checked for logical compatibility (can they co-occur?).
- [ ] Repeated events have consistent periodicity across sources.
- [ ] Timestamps of source publication do not precede the events they describe (unless forecasts).
- [ ] Any retracted or corrected dates from source errata are reflected in the timeline.

## Pass / Fail Criteria

**Pass**: All date discrepancies are either resolved or explicitly documented
with a confidence assessment. Event sequences are consistent across sources.

**Fail**: Unresolved contradictions exist in event ordering or dating that
could alter causal interpretation.

## Escalation if Failed

- Flag contradictions to the Verification squad for independent date
  confirmation.
- If sources cannot be reconciled, present competing timelines with
  confidence ratings rather than forcing a single narrative.
- Escalate to the Chief if contradictions affect the core research thesis.
