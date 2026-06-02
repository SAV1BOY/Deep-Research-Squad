# Evolution Layer (Section 19) — Deep-Research LEAF (2nd drop-in)

KPI = `citation_accuracy` (AUTO / external ground-truth: citations resolve), so it MAY drive fitness
(not a conformance KPI). This squad reuses the **byte-identical** shared DET scripts (`harness_lock.py`,
`selection.py`, `archive.py`, `stagnation.py`, `lineage_audit.py`) with **zero edits** plus its own leaf
kernel keyed to `citation_accuracy` — proving the Section-19 portability claim.

## Loops (this leaf)
- **L0 (active):** gate verdict → append `data/metrics/evolution_log.tsv` → `scripts/reporting/fitness.py`
  rolls up `citation_accuracy`. (`status.py` in the HRM repo discovers this squad via that log.)
- **L1/L2 (DISARMED):** require `evolution/harness_lock.py guard` PASS = a human git SIGNED tag re-verified
  live; no env var / hand-edited flag can arm. Until armed, only L0 runs.

## Trust boundary
Same as the fleet: tamper-EVIDENT not tamper-proof; arming = human `git tag -s kernel-seal-<hash>`;
ships DISARMED (`guard` exit 4); `seal.status`/`armed` are advisory (guard is the authority).

## Commands
```
python evolution/harness_lock.py verify        # exit 0 intact / 3 tamper
python evolution/harness_lock.py guard         # exit 4 disarmed (expected)
python scripts/reporting/fitness.py --last 5   # citation_accuracy rollup
```
