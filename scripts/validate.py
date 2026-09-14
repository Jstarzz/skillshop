#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

root = Path(__file__).resolve().parents[1]
skills_dir = root/"plugins"/"skillshop"/"skills"
errors = []
names = []

for d in sorted(skills_dir.iterdir()):
    if not d.is_dir():
        continue
    f = d/"SKILL.md"
    if not f.exists():
        errors.append(f"missing SKILL.md: {d.name}")
        continue
    text = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"invalid frontmatter: {d.name}")
        continue
    fm = m.group(1)
    nm = re.search(r"^name:\s*(.+)$", fm, re.M)
    ds = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not nm:
        errors.append(f"missing name: {d.name}")
        continue
    raw_name = nm.group(1).strip().strip('"')
    if raw_name != d.name:
        errors.append(f"name mismatch {d.name}: {raw_name}")
    if len(raw_name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", raw_name):
        errors.append(f"invalid skill name: {raw_name}")
    if not ds:
        errors.append(f"missing description: {d.name}")
    else:
        desc = ds.group(1).strip()
        # descriptions are emitted as JSON/YAML double quoted strings
        try:
            parsed = json.loads(desc)
        except Exception:
            parsed = desc.strip('"')
        if not (1 <= len(parsed) <= 1024):
            errors.append(f"description length {len(parsed)}: {d.name}")
    if len(text.splitlines()) > 500:
        errors.append(f"SKILL.md over 500 lines: {d.name}")
    names.append(d.name)

registry = json.loads((root/"registry.json").read_text())
reg_names = sorted(x["name"] for x in registry["skills"])
if sorted(names) != reg_names:
    errors.append("registry names do not match skill directories")
if registry.get("count") != len(names):
    errors.append("registry count mismatch")

market = json.loads((root/".claude-plugin"/"marketplace.json").read_text())
if market.get("$schema") != "https://anthropic.com/claude-code/marketplace.schema.json":
    errors.append("missing/incorrect marketplace schema")
if not market.get("plugins"):
    errors.append("marketplace has no plugins")

plugin = json.loads((root/"plugins"/"skillshop"/".claude-plugin"/"plugin.json").read_text())
if plugin.get("name") != "skillshop":
    errors.append("plugin manifest name mismatch")

if errors:
    for e in errors:
        print("ERROR:", e)
    raise SystemExit(1)

print(f"OK: {len(names)} skills validated")
print("categories:", ", ".join(sorted({x["category"] for x in registry["skills"]})))
