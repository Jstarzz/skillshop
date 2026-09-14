#!/usr/bin/env python3
from pathlib import Path
import json, re

root = Path(__file__).resolve().parents[1]
plugin_root = root / "plugins" / "skillshop"
registered = plugin_root / "skills"
library = plugin_root / "library" / "playbooks"
errors = []

CORE = {"shop", "find", "apply", "catalog"}

def parse_skill(path: Path, expected_name: str):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"invalid frontmatter: {path}")
        return
    fm = m.group(1)
    nm = re.search(r"^name:\s*(.+)$", fm, re.M)
    ds = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not nm:
        errors.append(f"missing name: {path}")
    else:
        raw = nm.group(1).strip().strip('"')
        if raw != expected_name:
            errors.append(f"name mismatch {path}: {raw} != {expected_name}")
        if len(raw) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", raw):
            errors.append(f"invalid name: {raw}")
    if not ds:
        errors.append(f"missing description: {path}")
    if len(text.splitlines()) > 500:
        errors.append(f"SKILL.md over 500 lines: {path}")

core_names = {d.name for d in registered.iterdir() if d.is_dir()}
if core_names != CORE:
    errors.append(f"registered plugin skills must be {sorted(CORE)}, got {sorted(core_names)}")
for name in sorted(CORE):
    f = registered / name / "SKILL.md"
    if not f.exists():
        errors.append(f"missing core skill: {name}")
    else:
        parse_skill(f, name)

for name in ("find", "apply", "catalog"):
    f = registered / name / "SKILL.md"
    if f.exists() and "disable-model-invocation: true" not in f.read_text(encoding="utf-8"):
        errors.append(f"{name} must remain user-only to avoid context cost")

shop = registered / "shop" / "SKILL.md"
if shop.exists():
    shop_text = shop.read_text(encoding="utf-8")
    if "disable-model-invocation: true" in shop_text:
        errors.append("shop must remain model-invocable")
    if "when_to_use:" not in shop_text:
        errors.append("shop must define when_to_use for reliable routing")

registry = json.loads((root / "registry.json").read_text(encoding="utf-8"))
reg_names = sorted(x["name"] for x in registry["skills"])
lib_names = sorted(d.name for d in library.iterdir() if d.is_dir())

if registry.get("count") != len(reg_names):
    errors.append("registry count mismatch")
if reg_names != lib_names:
    missing = sorted(set(reg_names) - set(lib_names))
    extra = sorted(set(lib_names) - set(reg_names))
    errors.append(f"library/registry mismatch; missing={missing[:5]} extra={extra[:5]}")

for name in lib_names:
    f = library / name / "SKILL.md"
    if not f.exists():
        errors.append(f"missing playbook SKILL.md: {name}")
    else:
        parse_skill(f, name)

catalog = json.loads((plugin_root / "catalog.json").read_text(encoding="utf-8"))
cat_names = sorted(x["name"] for x in catalog.get("skills", []))
if cat_names != reg_names:
    errors.append("plugin catalog does not match root registry")

plugin = json.loads((plugin_root / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
market = json.loads((root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
entry = market.get("plugins", [{}])[0]
if plugin.get("name") != "skillshop":
    errors.append("plugin manifest name mismatch")
if plugin.get("version") != "0.2.1" or entry.get("version") != "0.2.1":
    errors.append("plugin/marketplace version must be 0.2.1")
if not (plugin_root / "scripts" / "recommend.py").exists():
    errors.append("missing recommender")
if not (plugin_root / "scripts" / "route_prompt.py").exists():
    errors.append("missing prompt routing hook script")
hooks_path = plugin_root / "hooks" / "hooks.json"
if not hooks_path.exists():
    errors.append("missing plugin hooks/hooks.json")
else:
    hooks = json.loads(hooks_path.read_text(encoding="utf-8"))
    if "UserPromptSubmit" not in hooks.get("hooks", {}):
        errors.append("SkillShop must register a UserPromptSubmit hook")

if errors:
    for e in errors:
        print("ERROR:", e)
    raise SystemExit(1)

print(f"OK: {len(core_names)} registered skills + {len(lib_names)} cold playbooks validated")
print("model-invocable SkillShop surface: shop only")
print("deterministic routing hook: UserPromptSubmit")
print("categories:", ", ".join(sorted({x["category"] for x in registry["skills"]})))
