# Architecture

## v0.2: router + cold playbook library

SkillShop separates **discoverability** from **registration**.

Claude Code registers only four plugin skills:

```text
shop      model + user invocable
find      user only
apply     user only
catalog   user only
```

The 157 specialist playbooks live under `plugins/skillshop/library/playbooks/`, outside Claude Code's plugin `skills/` discovery path.

This matters because Claude Code keeps model-invocable skill descriptions in context every turn. A 157-skill plugin therefore pays a persistent metadata cost even though full bodies are lazy-loaded. SkillShop v0.2 reduces that always-on surface to one model-invocable router description.

## Routing flow

```text
task + repository
      |
      v
 shop/SKILL.md
      |
      +-- recommend.py reads catalog.json
      |      |
      |      +-- lexical/trigger scoring
      |      +-- lightweight stack signals
      |      +-- intent boosts
      |
      v
 candidate shortlist
      |
      v
 model selects smallest useful composition
      |
      v
 Read library/playbooks/<name>/SKILL.md
      |
      v
 execute
```

The deterministic recommender is retrieval assistance, not the final decision-maker. Claude may reject high-scoring candidates, include a lower-scoring counterweight, or use no playbook for trivial work.

## Cold playbooks

Playbooks remain regular `SKILL.md` documents so they preserve the Agent Skills-style structure and can later be promoted to first-class skills if needed. Inside SkillShop they are treated as library documents and read on demand.

Supporting files stay beside their playbook:

```text
library/playbooks/journey-recorder/
  SKILL.md
  references/
    RECORDING.md
    semantic-journey.schema.json
```

## Manual entry points

`/skillshop:find <query>` searches without loading full playbooks.

`/skillshop:apply <name>` loads one exact playbook.

`/skillshop:catalog` explains the library and can inspect the catalog when the user explicitly wants breadth.

These skills set `disable-model-invocation: true`, so Claude does not keep their descriptions in its automatic skill listing.

## Composition

Default activation caps:

- focused implementation/debug task: 1-3 playbooks;
- broad release/production review: 3-5;
- >5 only when independent risk domains genuinely require it.

Useful intentional disagreements remain:

- `caveman` vs `future-proof`;
- `cheap-ass` vs `production-readiness`;
- `speed-demon` vs maintainability;
- `grandma` / `one-handed` / `low-end-device` / `accessibility-tester`;
- `paranoid` vs feasibility evidence.

The router should synthesize disagreement, not treat a perspective playbook as absolute authority.

## QA journey pipeline

`journey-recorder` and `journey-compiler` remain playbooks in the cold library. Once selected, they support:

```text
recorded behavior
      -> semantic journey
      -> manual QA
      -> browser E2E
      -> API sequence
      -> load scenario
```

## Performance / Take My Load

`load-test` defines testing methodology.

`take-my-load-operator` contains platform-specific operational guidance. It must not confuse planned/configured RPS with achieved throughput.

## Safety

Loading a playbook never grants new permissions. Tool permissions, production safeguards, authorization requirements and explicit user constraints remain in force.
