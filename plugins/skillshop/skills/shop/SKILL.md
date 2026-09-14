---
name: shop
description: "Route substantive software-engineering work to the smallest useful set of specialized SkillShop playbooks before analysis or execution. Use for architecture, implementation, debugging, QA, performance, security, reliability, frontend, backend, delivery, migrations, production readiness, mobile, payments, or other engineering work where expert workflow guidance can improve the result."
when_to_use: "Invoke before substantive engineering work, including project reviews and production-readiness checks. Do not skip routing merely because the task looks solvable without a specialist playbook."
allowed-tools: "Bash(python3 ${CLAUDE_PLUGIN_ROOT}/scripts/recommend.py *) Read Glob Grep"
---

# SkillShop router

Act as the dispatcher, not as another generic engineering checklist.

## Route first

When this skill is invoked for substantive engineering work, route before doing the substantive analysis or implementation.

Derive a short routing query from the user's actual task and the repository context. Then run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/recommend.py" \
  --query "<task in concrete engineering terms>" \
  --project "${CLAUDE_PROJECT_DIR}" \
  --top 10 \
  --json
```

If the task is genuinely trivial or non-engineering, report that no specialist playbook is needed and return to the request.

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

## Routing receipt

After routing and loading the selected playbooks, always emit exactly one compact routing receipt before the substantive response:

`SkillShop → <playbook>, <playbook>`

List only playbooks whose `SKILL.md` was actually read in this turn, in the order they were loaded. If none were loaded, emit:

`SkillShop → no specialist needed`

Keep the receipt to one line. Do not include scores, candidate lists, reasoning, file paths, or router debug output unless the user explicitly asks for routing details.

Never claim a playbook was selected or used unless its `SKILL.md` was actually read.

If the user later asks whether SkillShop was used, answer from the actual routing/load history in the conversation rather than inferring from the final answer.

## Safety and execution

A playbook is guidance, not permission. Preserve existing tool permissions, authorization boundaries, production safeguards, and confirmation requirements.

When the task changes materially, route again rather than assuming the old composition still fits.
