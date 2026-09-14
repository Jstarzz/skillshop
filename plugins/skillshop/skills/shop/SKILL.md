---
name: shop
description: "Route substantive software-engineering work to the smallest useful set of specialized SkillShop playbooks. Use for architecture, implementation, debugging, QA, performance, security, reliability, frontend, backend, delivery, migrations, production readiness, mobile, payments, or other engineering work where expert workflow guidance can improve the result."
allowed-tools: "Bash(python3 ${CLAUDE_PLUGIN_ROOT}/scripts/recommend.py *) Read Glob Grep"
---

# SkillShop router

Act as the dispatcher, not as another generic engineering checklist.

## Route first

For substantive engineering work, derive a short routing query from the user's actual task and the repository context. Then run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/recommend.py" \
  --query "<task in concrete engineering terms>" \
  --project "${CLAUDE_PROJECT_DIR}" \
  --top 10 \
  --json
```

For a tiny/local task where a specialist playbook would add no value, skip routing and proceed normally.

## Choose a small composition

From the candidates, select only the playbooks that materially change how the task should be done.

Default:
- 1–3 playbooks for a focused task.
- 3–5 for a broad release/review.
- More than 5 only when the task genuinely spans independent risk domains.

Prefer complementary roles over duplicates. Example: `load-test` + `generator-sanity` + `capacity-plan` is useful; five generic review playbooks are not.

Do not blindly take the highest scores. Use project facts, user intent, risk, and scope.

## Load on demand

For each selected playbook, read:

`${CLAUDE_PLUGIN_ROOT}/library/playbooks/<name>/SKILL.md`

Read only selected playbooks. Supporting files under that playbook directory may be read only when the playbook points to them or they are clearly needed.

Treat each loaded playbook as expert procedural guidance. Reconcile conflicts instead of stacking contradictory instructions. User requirements and project-specific constraints win.

## Make the selection visible only when useful

Normally just use the guidance. If the choice itself matters, briefly say which playbooks were selected and why. Do not dump routing internals or raw scores unless asked.

## Safety and execution

A playbook is guidance, not permission. Preserve existing tool permissions, authorization boundaries, production safeguards, and confirmation requirements.

When the task changes materially, route again rather than assuming the old composition still fits.
