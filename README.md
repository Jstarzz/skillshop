# SkillShop

> **Claude shops for expert workflows instead of pretending one generic prompt is good at everything.**

[![Validate skills](https://github.com/Jstarzz/skillshop/actions/workflows/validate.yml/badge.svg)](https://github.com/Jstarzz/skillshop/actions/workflows/validate.yml)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-111827)](https://agentskills.io/)
[![Skills](https://img.shields.io/badge/skills-157-2563eb)](docs/CATALOG.md)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**SkillShop** is a composable marketplace of engineering playbooks for coding agents. It packages repeatable expert judgment into small, triggerable [Agent Skills](https://agentskills.io/) so an agent can inspect a project, select the specialists that fit the job, and load only those workflows.

It is deliberately **not** a pile of `You are a senior engineer` prompts.

## What is in the shop?

157 skills across architecture, backend, delivery, frontend/UX, planning, QA, performance, reliability, security, and meta-routing.

A few examples:

- `caveman` — aggressively remove unjustified moving parts and abstractions.
- `future-proof` — preserve only credible, cheap extension points.
- `qa-explorer` — perform evidence-driven exploratory QA like an annoyingly competent tester.
- `journey-recorder` — turn human or agent interaction traces into semantic user journeys.
- `journey-compiler` — compile one semantic journey into manual QA, browser E2E, API tests, or load scenarios.
- `bug-reproducer` — convert vague bug reports into minimal, repeatable reproductions and regression cases.
- `load-test` — design, execute, and interpret realistic performance tests instead of just firing traffic.
- `generator-sanity` — prove the load generator is not the bottleneck before trusting a benchmark.
- `payment-integrity` — review money movement, idempotency, settlement, reconciliation, and duplicate-charge hazards.
- `multi-tenant-review` — hunt for tenant-isolation leaks across data, caches, jobs, files, logs, and APIs.
- `edge-case-goblin` — systematically attack ugly states and weird inputs.
- `2am-debugger` — judge whether an on-call engineer could diagnose the system while half-dead at 2 AM.
- `frontend-slop-obliterator` — hunt generic, incoherent, inaccessible, AI-slop UI patterns.
- `verification-before-completion` — require fresh evidence before an agent claims the work is done.

See the **[full catalog](docs/CATALOG.md)**.

## Install in Claude Code

```text
/plugin marketplace add https://github.com/Jstarzz/skillshop
/plugin install skillshop@skillshop
```

The marketplace exposes the `skillshop` plugin. Compatible hosts discover each skill from its small metadata header and load the full `SKILL.md` only when needed.

## The idea

```text
                     project + task
                          │
                          ▼
                 ┌──────────────────┐
                 │ project-profiler │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   skill-router   │
                 └────────┬─────────┘
                          │
            search / rank / compose skills
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
     caveman          qa-explorer       load-test
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                   evidence-backed work
```

The router should select a **small set of directly relevant skills**, not activate the whole catalog. Some skills are intentionally adversarial to each other so the agent has to synthesize tradeoffs instead of accepting one worldview.

For example, an architecture decision may compose:

```text
caveman + future-proof + paranoid + cheap-ass
                    ↓
            architecture-review
                    ↓
              decision-record
```

## QA: record once, reuse the journey

The QA subsystem treats a semantic user journey as a reusable engineering artifact:

```text
human tester OR agent exploration
              │
              ▼
       journey-recorder
              │
              ▼
        semantic journey
              │
              ▼
       journey-compiler
       ┌──────┼──────┬─────────┐
       ▼      ▼      ▼         ▼
     manual browser   API      load
      case    E2E   sequence  scenario
```

The canonical recording stores actors, preconditions, semantic actions, dynamic values, assertions, network evidence, and redaction rules. Raw screen coordinates are evidence at most; they are never the source of truth.

## Load testing

`load-test` is the methodology skill. The traffic generator is a tool.

A sane performance workflow composes skills such as:

```text
load-modeler
    ↓
generator-sanity
    ↓
load-test
    ├── spike-test
    ├── soak-test
    └── breakpoint-test
    ↓
regression-analysis
    ↓
capacity-plan
```

`take-my-load-operator` is an optional specialist for [Take My Load](https://github.com/Jstarzz/take-my-load), keeping target authorization, worker capacity, synchronized execution, generator telemetry, and measured-vs-configured throughput explicit.

## Repository layout

```text
.claude-plugin/marketplace.json     Claude Code marketplace
plugins/skillshop/
  .claude-plugin/plugin.json        Plugin manifest
  skills/<skill>/SKILL.md           157 Agent Skills
  skills/<skill>/references/        On-demand deep references
  skills/<skill>/scripts/           Skill-local tooling
  skills/<skill>/assets/            Templates/schemas
registry.json                       Machine-readable catalog
scripts/validate.py                 Repository validator
scripts/search.py                   Human/debug catalog search
docs/                               Architecture, routing, catalog, compositions
examples/                           Semantic journey + project profile examples
```

## Search the catalog locally

```bash
python3 scripts/search.py "production multi tenant payments load test"
```

For debugging the skill router itself:

```bash
python3 plugins/skillshop/skills/skill-router/scripts/recommend.py \
  "prepare our multi-tenant payment app for production and load test checkout"
```

The lexical helpers are intentionally simple and deterministic. The host model should route semantically from the skill metadata.

## Validate

No runtime dependencies are required for the repository validator:

```bash
python3 scripts/validate.py
```

CI runs the same checks on every push and pull request.

## Design rules

A SkillShop skill should encode **repeatable expert judgment**. It should tell an agent what evidence to gather, what decisions to make, what traps to avoid, and what counts as done.

Good:

> Reproduce an intermittent bug, minimize the trigger, preserve evidence, identify root cause, add a regression test, and verify the fix under the original trigger.

Bad:

> Act as an expert debugger and fix bugs carefully.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/QUALITY-BAR.md](docs/QUALITY-BAR.md).

## Standards and provenance

Skills follow the open Agent Skills `SKILL.md` format and progressive-disclosure model. Public skill collections and workflow patterns were researched for coverage and structure, but the skill text in this repository is original wording unless a future contribution explicitly records third-party provenance and licensing.

See [docs/SOURCES.md](docs/SOURCES.md).

## License

MIT.
