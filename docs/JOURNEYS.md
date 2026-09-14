# Semantic QA journeys

A semantic journey records **what the user is doing and what must be true**, not brittle screen coordinates.

A recorder may observe DOM/accessibility targets, network traffic, screenshots, console output, timings, and application state. The canonical journey should normalize that evidence into stable business actions and assertions.

## Pipeline

```text
human/agent interaction
        ↓
 journey-recorder
        ↓
 semantic journey
        ↓
 journey-compiler
   ┌────┼─────┬─────┐
manual E2E   API   load
```

## Required properties

- actor and role
- preconditions and test data
- semantic actions
- dynamic values and extraction rules
- expected assertions
- relevant network/API evidence
- redaction rules for secrets and sensitive data

## Never make these canonical

- raw x/y coordinates
- ephemeral DOM indexes such as `button:nth-child(3)`
- production credentials or raw payment secrets
- arbitrary sleeps when a semantic readiness condition exists

See the schemas and references under `journey-recorder` and `journey-compiler` for the detailed model.
