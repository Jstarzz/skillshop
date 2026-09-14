# Routing model

SkillShop is designed for progressive disclosure. A host should inspect cheap skill metadata first, select a small candidate set, and load full skill instructions only for candidates that materially improve the task.

## Suggested routing stages

1. **Profile the project** — language, framework, runtime, data stores, deployment shape, clients, critical domains, test tooling, and known constraints.
2. **Classify the task** — build, debug, QA, performance, architecture, security, reliability, delivery, or mixed.
3. **Retrieve candidates** — use names, descriptions, triggers, project compatibility, and task semantics.
4. **Diversify perspectives** — include an intentional counterweight when useful (`caveman` vs `future-proof`, `speed-demon` vs `cheap-ass`).
5. **Cap activation** — prefer 2–6 strong skills over context-dumping the catalog.
6. **Compose dependencies** — specialist skills may recommend another skill when the task crosses boundaries.
7. **Verify before completion** — use fresh evidence before calling the task done.

## Routing anti-patterns

- Activating every skill in a category.
- Routing solely by keyword equality.
- Selecting a tool-specific skill just because its tool exists.
- Using perspective skills as substitutes for domain specialists.
- Keeping a skill active after its part of the workflow is finished.

The bundled search and router scripts are deterministic debugging aids. Semantic routing should be performed by the host model.
