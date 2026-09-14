# Architecture

## Progressive disclosure

This collection follows the Agent Skills model. The host can discover small metadata first, load a selected `SKILL.md` only when relevant, and then read bundled references/scripts/assets on demand.

That is what makes a 157-skill catalog practical: **do not dump 157 full prompts into every coding session**.

## Routing

1. `project-profiler` inspects stack, process boundaries, data stores, test frameworks, deployment, and risk surfaces.
2. `skill-router` selects a small set of directly relevant skills.
3. Skills execute against repository/runtime evidence.
4. Specialist skills may hand off to adjacent skills rather than duplicating them.
5. `verification-before-completion` gates success claims when a change or release is being completed.
6. `handoff` preserves durable state for long-running work.

## Deliberate disagreements

Some skills are supposed to fight:

- `caveman` removes moving parts; `future-proof` preserves only credible cheap extension points.
- `cheap-ass` pressures cost; `production-readiness` refuses savings that violate launch requirements.
- `speed-demon` pressures hot-path performance; `caveman` and `code-quality-review` challenge complexity introduced for small wins.
- `grandma`, `one-handed`, `low-end-device`, `pixel-cop`, and `accessibility-tester` inspect the same UI from different constraints.
- `paranoid` assumes failure; `technical-feasibility` distinguishes actual blockers from imagined ones.

The final decision should synthesize the disagreement rather than treating one skill as absolute authority.

## QA recorder / compiler

`journey-recorder` stores a canonical semantic journey. The recording may come from a person or from an agent running exploratory QA.

`journey-compiler` can then create:
- manual QA cases;
- browser automation;
- API/integration sequences;
- performance/load scenarios.

This avoids having separate teams manually rewrite the same business flow four times.

## Load testing

`load-test` defines methodology. A load engine/platform is a tool.

`take-my-load-operator` knows the current platform shape: Go control plane + Go workers + Rust blast engine, default-deny target policy, capacity-aware planning, synchronized execution, and generator telemetry. The skill must never report configured/planned rate as measured throughput.
