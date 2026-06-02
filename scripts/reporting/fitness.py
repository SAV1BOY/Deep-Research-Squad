#!/usr/bin/env python3
"""fitness.py (Deep-Research LEAF) — KPI rollup. STDLIB-ONLY.
KPI = citation_accuracy (AUTO / external ground-truth: citations resolve) = mean over the last N rows.
This is an auto-measurable outcome KPI (NOT conformance), so it MAY drive fitness (drives_fitness true).
Reports the leaf kernel fitness_hash so a consumer can confirm fitness measures what was sealed.
Usage: python scripts/reporting/fitness.py --last 5
"""
import sys, os, json, argparse, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
SQUAD = os.path.dirname(os.path.dirname(HERE))
LOG = os.path.join(SQUAD, "data", "metrics", "evolution_log.tsv")
SEAL = os.path.join(SQUAD, "evolution", "kernel", "kernel.seal.json")


def read_rows():
    if not os.path.exists(LOG):
        return []
    with open(LOG, encoding="utf-8") as f:
        header = f.readline().rstrip("\n").split("\t")
        rows = []
        for ln in f:
            ln = ln.rstrip("\n")
            if ln:
                rows.append(dict(zip(header, ln.split("\t"))))
        return rows


def fitness_hash():
    if os.path.exists(SEAL):
        return json.load(open(SEAL, encoding="utf-8")).get("components", {}).get("fitness_hash")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--last", type=int, default=0)
    a = ap.parse_args()
    rows = read_rows()
    if a.last > 0:
        rows = rows[-a.last:]
    if not rows:
        print(json.dumps({"kpi": "citation_accuracy", "n": 0, "note": "no rows yet"}))
        return 0
    vals = [float(r["citation_accuracy"]) for r in rows if r.get("citation_accuracy") not in (None, "", "NA")]
    ca = round(statistics.mean(vals), 4) if vals else None
    print(json.dumps({"kpi": "citation_accuracy", "n": len(rows), "citation_accuracy": ca,
                      "drives_fitness": True, "conformance": False, "fitness_hash": fitness_hash(),
                      "interpretation": ("strong>=0.85" if (ca or 0) >= 0.85 else "needs-work<0.85")}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
