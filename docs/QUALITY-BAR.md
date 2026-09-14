# Skill quality bar

A SkillShop skill is a reusable decision procedure, not a costume for the model.

## A strong skill

A strong skill answers five questions:

1. **When should I activate?** The description and trigger phrases define a narrow, useful problem class.
2. **What evidence do I gather first?** Repository state, runtime observations, requirements, traces, screenshots, metrics, or reproduction steps come before confident recommendations.
3. **What decisions do I make?** The workflow encodes tradeoffs and specialist judgment rather than generic advice.
4. **What can go wrong?** Failure modes, false positives, unsafe shortcuts, and tool limitations are explicit.
5. **What does done mean?** Exit criteria require observable evidence rather than an agent merely claiming success.

## Reject these patterns

- “You are a world-class senior engineer.”
- Rephrasing another skill with a new persona.
- Checklists with no prioritization or evidence requirements.
- Mandatory tools where the engineering method should be tool-independent.
- Giant all-purpose skills that should be composed from smaller specialists.
- Hidden destructive actions or unbounded network activity.
- Tests that optimize coverage percentage while ignoring behavioral risk.

## Prefer composition

If a proposed skill mostly embeds existing workflows, compose them instead. `production-readiness`, for example, can invoke security, observability, rollback, data, and QA specialists without copying all their instructions.

## Naming

Names may be serious (`payment-integrity`) or memorable (`edge-case-goblin`) as long as the capability is clear from metadata and the workflow remains professional.
