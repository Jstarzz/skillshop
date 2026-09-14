# Routing model

SkillShop v0.2 uses a **single model-invocable router** over a cold library of 157 playbooks.

## Stages

1. **Understand the task** — state the concrete engineering objective, not vague nouns.
2. **Read cheap project signals** — stack/runtime/test/deployment hints from top-level project files.
3. **Retrieve candidates** — `recommend.py` ranks catalog metadata by names, triggers, descriptions, categories and a few high-value intent mappings.
4. **Select semantically** — Claude chooses the smallest useful composition; deterministic scores are hints.
5. **Load only selected playbooks** — read `library/playbooks/<name>/SKILL.md`.
6. **Compose** — reconcile overlap and disagreement.
7. **Re-route on scope change** — do not keep irrelevant playbooks mentally active forever.

## Selection caps

- 1-3 playbooks: normal focused task.
- 3-5: cross-cutting review/release.
- >5: exceptional.

## Router anti-patterns

- Loading every high-scoring result.
- Loading an entire category.
- Treating keyword score as expertise.
- Selecting tool-specific guidance merely because the tool exists.
- Loading generic umbrella playbooks when a precise specialist covers the risk.
- Recreating 157 first-class plugin skills.

## Manual routing

```text
/skillshop:find payment race condition
/skillshop:apply payment-integrity
/skillshop:shop production readiness for a multi-tenant SaaS
```

## Debug the router

```bash
python3 plugins/skillshop/scripts/recommend.py \
  --query "multi-tenant payment app production load test" \
  --project . \
  --top 10 \
  --json
```

Inspect `why` and `project_signals`. If ranking is weak, improve metadata or intent aliases before adding complicated retrieval infrastructure.
