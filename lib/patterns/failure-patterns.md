# Common Failure Patterns to Avoid

## Pattern Name: Confirmation Bias Trap

**Problem:** Researchers unconsciously seek evidence confirming their initial hypothesis.

**Solution:** Actively seek disconfirming evidence. For every "supported" claim, spend
deliberate effort finding sources that disagree. Track the ratio of supporting vs.
contradicting evidence sought.

**When to Use:** Always. This is the most common research failure mode.

**Example:** After finding 3 sources praising ClickHouse, deliberately search for
"ClickHouse problems," "ClickHouse limitations," and "migration regrets."

---

## Pattern Name: Source Echo Chamber

**Problem:** Multiple sources that appear independent actually trace back to a single
original, creating an illusion of corroboration.

**Solution:** Trace claims to their primary source. Check if articles cite the same
benchmark or paraphrase one study. True corroboration requires independent evidence.

**When to Use:** When multiple sources agree suspiciously well.

**Example:** Five blog posts all claim "10x improvement" but all cite the same vendor
benchmark. This is one source, not five.

---

## Pattern Name: Recency Bias

**Problem:** Overweighting recent information while dismissing valid older findings,
or relying on outdated information when the landscape has changed.

**Solution:** Date-stamp all evidence. Verify whether underlying conditions still hold.
Technology changes fast but architectural trade-offs are often stable.

**When to Use:** When sources span a wide time range or the domain evolves rapidly.

**Example:** A 2023 benchmark may be invalidated by a 2025 performance release.

---

## Pattern Name: Premature Convergence

**Problem:** Settling on a conclusion before adequate exploration.

**Solution:** Define minimum evidence thresholds before starting. Do not finalize
conclusions until thresholds are met. Use question tree coverage to verify completeness.

**When to Use:** When early findings strongly point one direction, tempting early closure.

**Example:** One strong benchmark favoring Option A does not justify skipping Options B/C.

---

## Pattern Name: Scope Creep Without Acknowledgment

**Problem:** Research scope gradually expands without explicit recognition.

**Solution:** Track scope changes in the timeline. When new threads emerge, explicitly
decide to include or mark as out-of-scope. Communicate changes to stakeholders.

**When to Use:** When interesting adjacent threads emerge during research.

**Example:** Database research expanding into "which cloud provider" without acknowledging
this is a separate research question.
