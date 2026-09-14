# Journey compilation targets

## Manual QA
Preserve actor, preconditions, semantic actions, test data, expected checkpoints, and cleanup.

## Browser E2E
Prefer accessible role/name and explicit stable test IDs. Avoid coordinate and `nth-child` selectors. Assert visible business outcomes and important network/state completion.

## API sequence
Use recorded requests as evidence, but remove incidental UI/background traffic. Preserve authentication/session semantics, dynamic extraction, idempotency values, and domain assertions.

## Load scenario
Keep business requests, session establishment, dynamic values, realistic data cardinality, and think time. Remove static assets and UI-only traffic unless it materially contributes to production load. Never model thousands of users as one reused identity if production behavior would differ.
