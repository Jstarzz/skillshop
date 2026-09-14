# SkillShop

**SkillShop is a low-context engineering playbook marketplace for coding agents.**

Instead of registering 157 specialist skills into every Claude Code turn, SkillShop exposes one automatic router and keeps the full expert library off the always-on skill list. Claude "shops" for the playbooks that fit the current project and task, then reads only those playbooks.

## Why this exists

Large skill packs have a hidden cost: Claude Code keeps every model-invocable skill name and description in context so the model knows what is available. With a large catalog, that listing consumes context and descriptions can be truncated.

SkillShop v0.2 fixes that structurally:

```text
user task + project
        |
        v
 /skillshop:shop
        |
        +--> lightweight catalog search
        |
        +--> choose 1-5 useful playbooks
        |
        +--> read only those playbooks
        v
 execute composed workflow
```

The plugin contains **157 engineering playbooks across 10 categories**, but only **4 plugin skills** are registered:

- `/skillshop:shop` — automatic/model-invocable router.
- `/skillshop:find` — search the catalog without loading playbooks.
- `/skillshop:apply` — load one exact playbook by name.
- `/skillshop:catalog` — explain/browse the catalog.

Only `shop` is model-invocable. The other three are user-only, so their descriptions do not stay in Claude's context.

## Install

```text
/plugin marketplace add https://github.com/Jstarzz/skillshop
/plugin install skillshop@skillshop
/reload-plugins
```

After updating an existing v0.1 install:

```text
/plugin marketplace update skillshop
/plugin update skillshop@skillshop
/reload-plugins
```

Depending on your Claude Code version, reinstalling the plugin may be the simplest way to refresh a cached custom marketplace version.

## Use

### Let Claude shop automatically

Just work normally. For substantial engineering tasks Claude can invoke the router when specialist guidance would help.

You can force routing explicitly:

```text
/skillshop:shop prepare this multi-tenant payment app for production and load test checkout
```

A sensible composition might be:

```text
production-readiness
payment-integrity
multi-tenant-review
load-test
generator-sanity
```

The router does **not** blindly load all five. It selects the smallest set that materially changes the work.

### Search manually

```text
/skillshop:find intermittent double-payment bug
/skillshop:find Android background GPS battery
/skillshop:find simplify overbuilt architecture
```

### Apply an exact playbook

```text
/skillshop:apply caveman
/skillshop:apply qa-explorer
/skillshop:apply load-test
/skillshop:apply edge-case-goblin
```

The old v0.1 commands such as `/skillshop:caveman` are intentionally replaced by `/skillshop:apply caveman`; keeping 157 top-level commands would recreate the context-cost problem.

## What is in the shop?

The library covers:

- **Architecture** — `caveman`, `future-proof`, `architecture-review`, `build-vs-buy`, `dependency-hater`, `technical-feasibility`, distributed-systems review, AI feature review.
- **QA** — `qa-orchestrator`, `qa-explorer`, `manual-test-designer`, `automated-test-designer`, `bug-reproducer`, `journey-recorder`, `journey-compiler`, visual regression, API contract testing, device QA.
- **Performance** — `load-test`, `load-modeler`, `generator-sanity`, `capacity-plan`, `benchmark-scientist`, `profiler`, `soak-test`, `spike-test`, `breakpoint-test`, `take-my-load-operator`.
- **Frontend / UX** — `ux-feasibility`, `grandma`, `one-handed`, `low-end-device`, `pixel-cop`, `frontend-slop-obliterator`, responsive/accessibility/browser reviews.
- **Backend** — API design, transactions, idempotency, queues, concurrency, schemas, pagination, background jobs.
- **Reliability** — observability, bad-network, backup/restore, incidents, CI, containers, Kubernetes, health checks, shutdowns.
- **Security** — authentication, authorization, secrets, threat models, uploads, webhooks, prompt injection, privacy.
- **Delivery / planning** — implementation, bug fixing, PR review, release management, migration, rollback, requirements, handoff.

See [`docs/CATALOG.md`](docs/CATALOG.md) for the full list.

## QA journey model

SkillShop includes a semantic journey workflow:

```text
human or agent exploration
          |
          v
   journey-recorder
          |
          v
 semantic journey
          |
   +------+------+------+
   |      |      |      |
 manual browser API    load
 QA     E2E    test  scenario
```

Recordings should preserve semantic targets, state transitions, network evidence, assertions, dynamic values and redactions rather than brittle screen coordinates.

## Load testing

`load-test` is methodology. A load generator is a tool.

`take-my-load-operator` is the playbook for operating the Take My Load platform. It understands the controller/worker/data-plane split and insists on distinguishing configured/planned rate from measured throughput.

## Repository layout

```text
.claude-plugin/marketplace.json
plugins/skillshop/
  .claude-plugin/plugin.json
  skills/
    shop/SKILL.md
    find/SKILL.md
    apply/SKILL.md
    catalog/SKILL.md
  catalog.json
  scripts/recommend.py
  library/playbooks/
    caveman/SKILL.md
    qa-explorer/SKILL.md
    load-test/SKILL.md
    ... 154 more
docs/
scripts/validate.py
registry.json
```

The `library/playbooks/` directory deliberately is **not** named `skills/`. Claude Code therefore does not register those playbooks as top-level plugin skills.

## Design rules

1. Route from the actual task and project, not from tool availability.
2. Prefer 1-3 playbooks for focused work and 3-5 for broad reviews.
3. Load complementary perspectives, not duplicate checklists.
4. A playbook is guidance, not permission.
5. Preserve project-specific constraints and user intent.
6. Verify before making completion claims.
7. Keep the router cheap; spend context only on specialists that matter.

## Validate

```bash
python3 scripts/validate.py
python3 plugins/skillshop/scripts/recommend.py \
  --query "multi-tenant payment app production load test" \
  --top 8
```

CI validates the core plugin surface, the full playbook library, manifests, and router smoke tests.

## Contributing

New playbooks belong under:

```text
plugins/skillshop/library/playbooks/<name>/SKILL.md
```

Add their metadata to `registry.json` and `plugins/skillshop/catalog.json`. Do not add every new playbook under the plugin's `skills/` directory; that directory is reserved for the tiny routing surface.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/SKILL-AUTHORING.md`](docs/SKILL-AUTHORING.md).

## License

MIT.
