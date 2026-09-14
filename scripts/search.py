#!/usr/bin/env python3
"""Deterministic human/debug search over SkillShop's registry."""
from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STOP = {
    "a", "an", "and", "app", "for", "in", "my", "of", "on", "or", "our",
    "project", "review", "system", "that", "the", "this", "to", "with",
}


def tokens(value: str) -> list[str]:
    return [
        token
        for token in re.findall(r"[a-z0-9]+", value.lower().replace("-", " "))
        if len(token) > 1 and token not in STOP
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Search the SkillShop registry.")
    parser.add_argument("query", nargs="+", help="Task or capability to search for")
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--category")
    args = parser.parse_args()

    registry = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))
    skills = registry["skills"]
    if args.category:
        skills = [s for s in skills if s["category"] == args.category]

    query = " ".join(args.query)
    q_tokens = set(tokens(query))
    docs: dict[str, set[str]] = {}
    frequency: Counter[str] = Counter()

    for skill in skills:
        blob = " ".join(
            [skill["name"], skill["category"], skill["description"], *skill.get("triggers", [])]
        )
        doc = set(tokens(blob))
        docs[skill["name"]] = doc
        frequency.update(doc)

    total = max(1, len(skills))
    ranked: list[tuple[float, dict]] = []
    normalized_query = " ".join(tokens(query))

    for skill in skills:
        doc = docs[skill["name"]]
        score = 0.0
        name_tokens = set(tokens(skill["name"]))
        for token in q_tokens & doc:
            idf = math.log((total + 1) / (frequency[token] + 1)) + 1.0
            score += idf
            if token in name_tokens:
                score += 2.5
        for trigger in skill.get("triggers", []):
            phrase = " ".join(tokens(trigger))
            if phrase and phrase in normalized_query:
                score += 7.0
        if name_tokens and name_tokens <= q_tokens:
            score += 10.0
        if score:
            ranked.append((score, skill))

    for score, skill in sorted(ranked, key=lambda item: (-item[0], item[1]["name"]))[: args.top]:
        print(f"{score:5.1f}  {skill['name']:<30} {skill['category']:<12} {skill['description']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
