#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.json"
PLAYBOOK_ROOT = ROOT / "library" / "playbooks"

STOP = {
    "a","an","and","are","as","at","be","but","by","can","do","for","from","how","i",
    "if","in","into","is","it","me","my","of","on","or","our","should","that","the",
    "their","this","to","use","we","what","when","with","you","your",
}

ALIASES = {
    "perf": {"performance","benchmark","latency","throughput","load"},
    "performance": {"performance","benchmark","latency","throughput","load","capacity","profile"},
    "load": {"load","stress","spike","soak","capacity","throughput","rps"},
    "qa": {"qa","test","testing","regression","exploratory","quality"},
    "test": {"test","testing","qa","regression","verification"},
    "testing": {"test","testing","qa","regression","verification"},
    "ui": {"ui","ux","frontend","visual","responsive","accessibility","design"},
    "ux": {"ux","ui","frontend","usability","mobile","accessibility","design"},
    "frontend": {"frontend","ui","ux","browser","responsive","accessibility","design"},
    "design": {"design","ui","ux","frontend","visual","layout","typography"},
    "threeui": {"threeui","three","webgl","shader","3d","immersive"},
    "webgl": {"webgl","three","threeui","shader","3d","immersive"},
    "backend": {"backend","api","database","queue","worker","service"},
    "db": {"database","sql","postgres","mysql","query","migration","transaction"},
    "database": {"database","sql","postgres","mysql","query","migration","transaction"},
    "security": {"security","auth","authorization","threat","secrets","privacy"},
    "auth": {"auth","authentication","authorization","session","oauth","oidc"},
    "prod": {"production","release","deployment","observability","rollback","incident"},
    "production": {"production","release","deployment","observability","rollback","incident"},
    "mobile": {"mobile","android","ios","touch","offline","location","nfc"},
    "payment": {"payment","payments","transaction","idempotency","webhook","integrity"},
    "payments": {"payment","payments","transaction","idempotency","webhook","integrity"},
    "simple": {"simple","simplify","minimal","caveman","dependency"},
    "simplify": {"simple","simplify","minimal","caveman","dependency"},
    "bug": {"bug","debug","reproduce","regression","failure"},
    "debug": {"debug","bug","reproduce","incident","failure"},
    "api": {"api","contract","endpoint","openapi","consumer","versioning"},
    "multi": {"tenant","multi","isolation"},
    "tenant": {"tenant","multi","isolation","authorization"},
}

PROJECT_FILES = {
    "package.json": {"javascript","typescript","frontend","node"},
    "pnpm-lock.yaml": {"javascript","typescript","frontend","node"},
    "yarn.lock": {"javascript","typescript","frontend","node"},
    "go.mod": {"go","backend","api"},
    "Cargo.toml": {"rust","backend","performance"},
    "pyproject.toml": {"python","backend"},
    "requirements.txt": {"python","backend"},
    "composer.json": {"php","backend"},
    "pom.xml": {"java","backend"},
    "build.gradle": {"java","kotlin","android","backend"},
    "build.gradle.kts": {"kotlin","android","backend"},
    "Dockerfile": {"docker","container","deployment"},
    "compose.yaml": {"docker","container","deployment"},
    "docker-compose.yml": {"docker","container","deployment"},
    "Chart.yaml": {"kubernetes","deployment"},
    "kustomization.yaml": {"kubernetes","deployment"},
}

BOOSTS = {
    "payment": {"payment-integrity": 10, "transaction-review": 6, "idempotency-review": 6, "webhook-security": 4},
    "payments": {"payment-integrity": 10, "transaction-review": 6, "idempotency-review": 6, "webhook-security": 4},
    "load": {"load-test": 10, "load-modeler": 7, "generator-sanity": 6, "capacity-plan": 5},
    "benchmark": {"benchmark-scientist": 10, "profiler": 5, "regression-analysis": 4},
    "production": {"production-readiness": 10, "observability-doctor": 6, "rollback-review": 5, "security-review": 4},
    "prod": {"production-readiness": 10, "observability-doctor": 6, "rollback-review": 5},
    "multi-tenant": {"multi-tenant-review": 12, "authorization-review": 5, "data-integrity-tester": 3},
    "tenant": {"multi-tenant-review": 10, "authorization-review": 5},
    "simplify": {"caveman": 12, "dependency-hater": 5, "modularity-review": 3},
    "simple": {"caveman": 10, "dependency-hater": 4},
    "ux": {"ux-feasibility": 8, "frontend-slop-obliterator": 5, "grandma": 4, "responsive-review": 3},
    "frontend design": {"frontend-slop-obliterator": 14, "ux-feasibility": 5, "responsive-review": 2},
    "ui design": {"frontend-slop-obliterator": 12, "ux-feasibility": 4},
    "landing page": {"frontend-slop-obliterator": 12, "responsive-review": 3},
    "design system": {"frontend-slop-obliterator": 9, "ux-feasibility": 5},
    "threeui": {"frontend-slop-obliterator": 15, "low-end-device": 4, "responsive-review": 3},
    "webgl": {"frontend-slop-obliterator": 12, "low-end-device": 5, "responsive-review": 3},
    "three.js": {"frontend-slop-obliterator": 12, "low-end-device": 5},
    "3d ui": {"frontend-slop-obliterator": 12, "low-end-device": 5},
    "qa": {"qa-orchestrator": 9, "qa-explorer": 7, "test-architect": 5},
    "bug": {"bug-reproducer": 8, "systematic-debugging": 7, "fix-bug": 6},
    "debug": {"systematic-debugging": 9, "bug-reproducer": 6, "2am-debugger": 4},
}


def tokenize(text: str, expand_aliases: bool = False) -> list[str]:
    toks = re.findall(r"[a-z0-9][a-z0-9+.#/-]*", text.lower())
    out: list[str] = []
    for tok in toks:
        for part in re.split(r"[-_/]", tok):
            if part and part not in STOP and len(part) > 1:
                out.append(part)
                if expand_aliases:
                    out.extend(sorted(ALIASES.get(part, ())))
    return out


def project_signals(project: Path | None) -> tuple[set[str], list[str]]:
    if not project or not project.exists():
        return set(), []
    signals: set[str] = set()
    evidence: list[str] = []
    try:
        top = {p.name: p for p in project.iterdir() if not p.name.startswith(".")}
    except OSError:
        return signals, evidence
    for name, tags in PROJECT_FILES.items():
        if name in top:
            signals.update(tags)
            evidence.append(name)
    pkg = top.get("package.json")
    if pkg and pkg.is_file():
        try:
            data = json.loads(pkg.read_text(encoding="utf-8"))
            deps = set(data.get("dependencies", {})) | set(data.get("devDependencies", {}))
            joined = " ".join(deps).lower()
            if any(x in joined for x in ("react", "next", "vue", "svelte", "astro")):
                signals.update({"frontend","ui","browser"})
            if any(x in joined for x in ("playwright", "cypress", "vitest", "jest")):
                signals.update({"qa","test"})
        except Exception:
            pass
    names = " ".join(top).lower()
    if any(x in names for x in ("android", "gradle")):
        signals.update({"mobile","android"})
    if any(x in names for x in ("k8s", "kubernetes", "helm")):
        signals.update({"kubernetes","deployment"})
    return signals, evidence[:8]


def score(entry: dict, query_tokens: Counter[str], raw_query: str, psignals: set[str]) -> tuple[float, list[str]]:
    name = entry.get("name", "")
    category = entry.get("category", "")
    desc = entry.get("description", "")
    triggers = entry.get("triggers", [])
    name_tokens = set(tokenize(name))
    category_tokens = set(tokenize(category))
    desc_tokens = set(tokenize(desc))
    trigger_tokens = set(tokenize(" ".join(triggers)))
    qset = set(query_tokens)
    value = 0.0
    reasons: list[str] = []
    exact_trigger = next((t for t in triggers if t.lower() in raw_query.lower()), None)
    if exact_trigger:
        value += 12
        reasons.append(f"trigger: {exact_trigger}")
    overlap_name = qset & name_tokens
    overlap_trigger = qset & trigger_tokens
    overlap_desc = qset & desc_tokens
    overlap_cat = qset & category_tokens
    value += 5.5 * sum(query_tokens[t] for t in overlap_name)
    value += 3.8 * sum(query_tokens[t] for t in overlap_trigger)
    value += 1.5 * sum(query_tokens[t] for t in overlap_desc)
    value += 2.2 * sum(query_tokens[t] for t in overlap_cat)
    if overlap_name:
        reasons.append("name: " + ", ".join(sorted(overlap_name)[:4]))
    elif overlap_trigger:
        reasons.append("trigger terms: " + ", ".join(sorted(overlap_trigger)[:4]))
    elif overlap_desc:
        reasons.append("description: " + ", ".join(sorted(overlap_desc)[:4]))
    ps_overlap = psignals & (name_tokens | trigger_tokens | desc_tokens | category_tokens)
    if ps_overlap:
        value += min(4.0, 0.8 * len(ps_overlap))
        reasons.append("project: " + ", ".join(sorted(ps_overlap)[:4]))
    qlow = raw_query.lower()
    for phrase, mapping in BOOSTS.items():
        if phrase in qlow and name in mapping:
            value += mapping[name]
            reasons.append(f"intent: {phrase}")
    if value > 0 and name in {"qa-orchestrator", "architecture-review", "security-review", "production-readiness"}:
        value += 0.2
    return value, reasons


def compact_result(item: dict) -> dict:
    return {
        "name": item["name"],
        "category": item.get("category"),
        "score": item["score"],
        "why": item.get("why", [])[:2],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Rank SkillShop playbooks for an engineering task.")
    ap.add_argument("query", nargs="*", help="Task or problem to route")
    ap.add_argument("--query", dest="query_opt", help="Task or problem to route")
    ap.add_argument("--project", help="Project directory used only for lightweight stack signals")
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--category")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--compact", action="store_true", help="With --json, omit descriptions/triggers/paths and return only routing evidence.")
    ap.add_argument("--names-only", action="store_true")
    args = ap.parse_args()
    raw_query = args.query_opt or " ".join(args.query)
    if not raw_query.strip():
        ap.error("provide a query")
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    project = Path(args.project).resolve() if args.project else None
    psignals, evidence = project_signals(project)
    query_tokens = Counter(tokenize(raw_query, expand_aliases=True))
    ranked = []
    for entry in data.get("skills", []):
        if args.category and entry.get("category") != args.category:
            continue
        value, reasons = score(entry, query_tokens, raw_query, psignals)
        if value <= 0:
            continue
        ranked.append({
            "name": entry["name"],
            "category": entry.get("category"),
            "score": round(value, 2),
            "description": entry.get("description"),
            "triggers": entry.get("triggers", []),
            "why": reasons or ["weak semantic match"],
            "playbook": str(PLAYBOOK_ROOT / entry["name"] / "SKILL.md"),
        })
    ranked.sort(key=lambda x: (-x["score"], x["name"]))
    ranked = ranked[: max(1, min(args.top, 25))]
    if args.names_only:
        print("\n".join(x["name"] for x in ranked))
        return 0
    if args.json:
        results = [compact_result(item) for item in ranked] if args.compact else ranked
        payload = {
            "query": raw_query,
            "project_signals": sorted(psignals),
            "results": results,
        }
        if not args.compact:
            payload["project_evidence"] = evidence
        print(json.dumps(payload, indent=None if args.compact else 2, separators=(",", ":") if args.compact else None))
        return 0
    if evidence:
        print("project:", ", ".join(evidence))
    for i, x in enumerate(ranked, 1):
        why = "; ".join(x["why"])
        print(f"{i:>2}. {x['name']:<30} {x['score']:>6.2f}  [{x['category']}]  {why}")
        print(f"    {x['description']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
