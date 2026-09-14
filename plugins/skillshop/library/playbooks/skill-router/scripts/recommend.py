#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path
from collections import Counter

STOP = {"the","a","an","and","or","to","of","for","our","my","this","that","with","in","on","app","project","system","review"}

def toks(s):
    return [x for x in re.findall(r"[a-z0-9]+", s.lower().replace("-", " ")) if x not in STOP and len(x) > 1]

p = argparse.ArgumentParser(description="Cheap lexical helper for the engineering skill catalog.")
p.add_argument("task", nargs="+")
p.add_argument("--top", type=int, default=10)
a = p.parse_args()
q = " ".join(a.task).lower()
q_tokens = toks(q)
qset = set(q_tokens)
catalog = json.loads((Path(__file__).parent.parent/"references"/"catalog.json").read_text())["skills"]

# IDF-ish weights so generic words matter less across a large catalog.
df = Counter()
doc_tokens = {}
for s in catalog:
    st = set(toks(" ".join([s["name"], s["category"], s["description"], *s["triggers"]])))
    doc_tokens[s["name"]] = st
    for x in st: df[x] += 1

N = max(1, len(catalog))
ranked = []
for s in catalog:
    score = 0.0
    name_tokens = set(toks(s["name"]))
    trigger_text = " | ".join(s["triggers"]).lower()
    desc_tokens = doc_tokens[s["name"]]
    for token in qset & desc_tokens:
        rarity = 1.0 + (N / max(1, df[token])) ** 0.35
        score += rarity
        if token in name_tokens:
            score += 2.5
    normalized_q = " ".join(toks(q))
    for trig in s["triggers"]:
        nt = " ".join(toks(trig))
        if nt and nt in normalized_q:
            score += 7
    if all(t in qset for t in name_tokens) and name_tokens:
        score += 10
    if score > 0:
        ranked.append((score, s))

for score, s in sorted(ranked, key=lambda x: (-x[0], x[1]["name"]))[:a.top]:
    print(f"{score:5.1f}  {s['name']:<30} {s['category']:<12} {s['description']}")
