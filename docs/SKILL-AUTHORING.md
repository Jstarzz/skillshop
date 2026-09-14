# Authoring a SkillShop skill

Create `plugins/skillshop/skills/<name>/SKILL.md` with Agent Skills frontmatter and a focused workflow. Then add the skill to `registry.json` and the router catalog.

Use this shape:

```yaml
---
name: example-skill
description: "What it does. Use when concrete trigger A, trigger B, trigger C."
license: MIT
compatibility: "Agent Skills compatible hosts; optimized for coding agents with repository and test/tool access."
metadata:
  category: "qa"
  version: "0.1.0"
  maintainer: "SkillShop maintainers"
  maturity: "draft"
---
```

The body should normally contain: activation signals, focus, evidence-gathering workflow, decisions, deliverables, failure modes, composition hints, and exit criteria.

Run:

```bash
python3 scripts/validate.py
python3 scripts/search.py "a task this skill should match"
```

Then test at least one negative query that should *not* rank the skill highly.
