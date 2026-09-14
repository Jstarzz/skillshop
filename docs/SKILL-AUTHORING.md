# Authoring a SkillShop playbook

SkillShop deliberately separates the **registered plugin surface** from the **playbook library**.

New specialist playbooks belong at:

```text
plugins/skillshop/library/playbooks/<name>/SKILL.md
```

Do **not** add normal specialist playbooks under `plugins/skillshop/skills/`. That directory is reserved for the tiny routing surface (`shop`, `find`, `apply`, `catalog`) so Claude does not carry hundreds of skill descriptions in every turn.

Add the playbook metadata to both `registry.json` and `plugins/skillshop/catalog.json`.

Use this shape:

```yaml
---
name: example-playbook
description: "What it does. Use when concrete trigger A, trigger B, trigger C."
license: MIT
compatibility: "Agent Skills compatible hosts; optimized for coding agents with repository and test/tool access."
metadata:
  category: "qa"
  version: "0.2.0"
  maintainer: "SkillShop maintainers"
  maturity: "draft"
---
```

The body should normally contain activation signals, focus, evidence-gathering workflow, decisions, deliverables, failure modes, composition hints, and exit criteria.

Good playbooks encode repeatable judgment. They should not be generic role prompts like “act as a senior engineer.”

## Routing quality

After adding the metadata, test retrieval:

```bash
python3 scripts/validate.py
python3 plugins/skillshop/scripts/recommend.py \
  --query "a task this playbook should match" \
  --project . \
  --top 10
```

Then test at least one negative query that should *not* rank the playbook highly.

Improve the playbook's description/triggers before adding special-case router boosts. Add an intent boost only when a domain concept has stable specialist meaning that ordinary lexical matching misses.

## Promoting a playbook to a registered skill

Do this rarely. A registered model-invocable skill adds its name/description to Claude's always-on skill listing. Promotion is justified only when the capability needs direct automatic invocation often enough to repay that persistent context cost.

For normal additions, keep the playbook cold and let `shop` load it on demand.
