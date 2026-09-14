# Full Skill Catalog

## Architecture

### `ai-feature-review`

Review AI-powered product features for whether AI is necessary, failure containment, evaluation, latency, privacy and deterministic fallbacks.

**Triggers:** AI feature; LLM integration; model in product.

### `api-boundary-review`

Check service and module boundaries for coherent ownership, stable contracts and avoidable chatty coupling.

**Triggers:** service split; module boundary; chatty internal API.

### `api-consumer`

Review an API strictly from the integrating client's perspective for predictability, low round trips and usable contracts.

**Triggers:** API DX; integration pain; public API review.

### `architecture-review`

Challenge architecture for unnecessary complexity, coupling, failure modes, ownership ambiguity and operational burden.

**Triggers:** architecture proposal; system design review; new services or queues.

### `build-vs-buy`

Decide whether to build, adopt or outsource a capability using lifecycle cost, fit, lock-in and operational burden.

**Triggers:** build vs buy; commodity capability; vendor evaluation.

### `caveman`

Solve the real problem with the fewest moving parts, dependencies and abstractions that satisfy current requirements.

**Triggers:** overbuilt architecture; dependency for later; simplify system.

### `cheap-ass`

Minimize recurring infrastructure and vendor cost without violating required reliability or developer productivity.

**Triggers:** reduce cloud bill; early-stage infra; cost review.

### `dependency-hater`

Challenge dependencies whose value does not justify supply-chain, upgrade, bundle or operational cost.

**Triggers:** too many dependencies; large package for small feature; dependency audit.

### `distributed-systems-review`

Review distributed designs for ownership, consistency, retries, idempotency, clocks, partitions and partial failure.

**Triggers:** distributed workers; message queue; consistency guarantees.

### `future-proof`

Preserve extension points only where future change is credible, expensive to retrofit and cheap to accommodate now.

**Triggers:** known roadmap growth; hard-to-migrate boundary; counterweight to caveman.

### `legacy-survivor`

Change old fragile systems safely using characterization, seams and incremental replacement instead of reckless rewrites.

**Triggers:** legacy code; old framework; fragile subsystem.

### `mobile-native-feasibility`

Determine whether a mobile requirement belongs in web, PWA, cross-platform native or platform-native code based on APIs and performance.

**Triggers:** mobile architecture; React Native Flutter native; device API.

### `modularity-review`

Assess whether module boundaries match domain responsibility and change patterns instead of arbitrary technical layers.

**Triggers:** circular dependencies; changes touch everywhere; module boundaries.

### `nfc-workflow-review`

Review NFC-based user workflows for reader/platform constraints, identity mapping, offline behavior, retries and physical failure modes.

**Triggers:** NFC; badge reader; tap workflow.

### `offline-first-review`

Review offline-capable workflows for local state, sync ownership, conflict resolution, retries and user-visible freshness.

**Triggers:** offline first; sync; field app.

### `state-machine`

Make complex lifecycle behavior explicit as states, legal transitions, guards, side effects and invariants.

**Triggers:** many status fields; workflow lifecycle; invalid state bugs.

### `tech-debt-review`

Identify technical debt that measurably slows delivery or increases defects and rank it by payoff instead of aesthetics.

**Triggers:** tech debt backlog; messy codebase; cleanup planning.

### `technical-feasibility`

Determine whether a proposed capability is buildable within platform, integration, performance, schedule and maintenance constraints.

**Triggers:** can we build this; novel integration; hardware or platform risk.

## Backend

### `api-design-review`

Review API semantics, schemas, errors, pagination, validation, idempotency and compatibility from consumer goals backward.

**Triggers:** API design; new endpoint; contract review.

### `api-versioning`

Design API evolution and deprecation so clients can migrate without surprise breakage or permanent version sprawl.

**Triggers:** API versioning; breaking API change; deprecation.

### `background-jobs-review`

Review queued and scheduled jobs for identity, retries, leases, idempotency, cancellation and operability.

**Triggers:** background job; cron worker; queue consumer.

### `concurrency-review`

Review concurrent access for lost updates, double processing, deadlocks, shared-state races and contention.

**Triggers:** concurrent writes; lost update; locking.

### `data-pipeline-review`

Review ingestion and ETL pipelines for schema drift, idempotency, late data, retries, backfills, lineage and observability.

**Triggers:** ETL; data ingestion; pipeline backfill.

### `data-retention`

Design deletion, archival and retention across primary, cache, search, analytics, object storage and backups.

**Triggers:** data retention; account deletion; archive policy.

### `database-change`

Design schema changes and deployment order to preserve data, compatibility and availability.

**Triggers:** schema migration; add column index; database change.

### `event-schema-review`

Review event and message schemas for ownership, versioning, idempotency, ordering and consumer compatibility.

**Triggers:** event schema; message contract; event bus.

### `feature-flag-review`

Review feature flags for ownership, targeting, rollout, rollback, test matrix, interactions and cleanup.

**Triggers:** feature flag; gradual rollout; flag debt.

### `idempotency-review`

Ensure retried or duplicated commands do not create duplicate side effects or corrupt state.

**Triggers:** idempotency; duplicate request; at-least-once.

### `migration-doctor`

Review or repair risky migrations with attention to locks, backfills, partial progress, retry and recovery.

**Triggers:** migration risk; large backfill; failed migration.

### `openapi-review`

Review OpenAPI descriptions for runtime accuracy, generator friendliness, auth/error completeness and compatibility.

**Triggers:** OpenAPI; Swagger; client generation.

### `pagination-review`

Review pagination for stable ordering, cursor correctness, filters, totals, large datasets and concurrent mutation behavior.

**Triggers:** pagination; large list API; cursor.

### `query-hunter`

Find N+1, duplicate, unbounded and badly shaped database access from actual application paths.

**Triggers:** N+1; too many queries; ORM performance.

### `schema-review`

Review data models for ownership, invariants, constraints, keys, indexes and lifecycle relationships.

**Triggers:** database schema; ORM model; entity design.

### `search-review`

Review search for relevance, indexing lag, tenant/access boundaries, broad-query behavior and safe degradation.

**Triggers:** search feature; full text search; search index.

### `time-zone-review`

Review temporal modeling for instants, local dates, wall times, DST, recurring schedules and API serialization.

**Triggers:** timezone; DST; scheduling.

### `transaction-review`

Review multi-step writes for atomicity, isolation, external side effects and ambiguous commit outcomes.

**Triggers:** transaction boundary; partial write; financial workflow.

### `websocket-review`

Review WebSocket and SSE behavior for auth, ordering, reconnect, replay, slow consumers and backpressure.

**Triggers:** WebSocket; SSE; realtime updates.

## Delivery

### `code-quality-review`

Review maintainability and clarity after correctness risks, focusing on future change cost rather than stylistic preference.

**Triggers:** maintainability review; complex module; cleanup pass.

### `commit-and-pr`

Turn a finished working tree into reviewable commits and a truthful pull request with verification evidence.

**Triggers:** prepare PR; clean commits; PR description.

### `dependency-upgrade`

Upgrade dependencies with controlled scope, release-note awareness, compatibility testing and rollback clarity.

**Triggers:** dependency bump; framework upgrade; security update.

### `documentation-sync`

Update developer and operator documentation to match actual changed behavior, configuration, contracts and commands.

**Triggers:** docs stale; API/config changed; setup changed.

### `fix-bug`

Reproduce a defect, isolate root cause, add regression coverage and make the smallest responsible fix.

**Triggers:** bug report; failing behavior; runtime defect.

### `git-conflict-resolution`

Resolve merge and rebase conflicts semantically by reconstructing both sides' intended behavior.

**Triggers:** merge conflict; rebase conflict; branch integration.

### `hotfix`

Repair an urgent production defect with the smallest blast radius, rollback readiness and explicit follow-up debt.

**Triggers:** production hotfix; urgent incident fix.

### `implement-feature`

Implement a defined feature as the smallest coherent vertical slice while preserving project conventions and proving behavior.

**Triggers:** build feature; acceptance criteria exist; production code change.

### `productionize`

Turn prototype code into production software by filling reliability, security, observability, configuration and operational gaps.

**Triggers:** prototype to production; hardening; client-facing launch.

### `prototype`

Build the cheapest artifact that answers a specific product or technical unknown without becoming accidental production architecture.

**Triggers:** proof of concept; high-risk unknown; demo.

### `refactor`

Improve internal structure while preserving externally observable behavior and limiting migration risk.

**Triggers:** refactor; reduce coupling; cleanup without behavior change.

### `release-manager`

Prepare and execute a release with exact artifact provenance, rollout gates, migrations, rollback and post-deploy checks.

**Triggers:** release; promote to production; versioned deploy.

### `remove-dead-code`

Delete unused code, dependencies, routes, styles and flags only after proving they are not part of active or dynamic behavior.

**Triggers:** dead code; deprecated feature; unused dependency.

### `review-pr`

Review a pull request for correctness, regressions, security, performance, maintainability and missing verification.

**Triggers:** PR review; pre-merge audit; diff review.

### `systematic-debugging`

Debug through evidence, narrowing boundaries and hypothesis testing before attempting fixes.

**Triggers:** confusing failure; intermittent bug; multiple failed fixes.

### `test-driven-development`

Use short red-green-refactor cycles when behavior is known and executable tests can define correctness first.

**Triggers:** TDD; test-first; regression bug fix.

## Frontend

### `background-location-review`

Review background location tracking for platform constraints, permission UX, battery, batching, offline buffering and recovery.

**Triggers:** background GPS; location tracking; Android tracking.

### `browser-compatibility-review`

Review web code for APIs, CSS and behaviors likely to differ across supported browsers before cross-browser execution.

**Triggers:** browser compatibility; new web API; CSS support.

### `cli-ux-review`

Review command-line interfaces for discoverability, composability, stable exit/output contracts and safe defaults.

**Triggers:** CLI design; developer tool UX; command interface.

### `copy-review`

Improve labels, helper text, confirmations and error messages for clarity, consistency and actionability.

**Triggers:** UX copy; microcopy; error messages.

### `design-system-review`

Assess whether components, variants and tokens form a coherent reusable system rather than near-duplicate wrappers.

**Triggers:** design system; component library; shadcn sprawl.

### `empty-state-review`

Design first-use, no-results and zero-data states that explain context and offer the next meaningful action without decorative filler.

**Triggers:** empty state; no results; first-use UI.

### `error-state-review`

Review how UI failure states explain what happened, preserve work and provide safe recovery without false success.

**Triggers:** error state; API failure UI; retry UX.

### `form-ux`

Make forms understandable, fast, recoverable and accessible while reducing unnecessary input and validation friction.

**Triggers:** form UX; checkout form; signup form.

### `frontend-slop-obliterator`

Remove generic AI-generated UI slop and replace it with deliberate product-specific hierarchy, density, components and iconography.

**Triggers:** AI slop UI; too many cards; generic dashboard.

### `grandma`

Evaluate whether a nontechnical first-time user can understand and complete the primary task using only visible cues.

**Triggers:** usability review; first-time user; confusing UI.

### `information-architecture`

Organize navigation and content around user tasks and domain concepts so features are discoverable without memorizing the system.

**Triggers:** navigation redesign; feature sprawl; findability.

### `localization-review`

Review UI and data handling for locale-aware dates, numbers, currency, Unicode, text expansion and international input.

**Triggers:** localization; internationalization; currency locale.

### `low-end-device`

Test and design for constrained CPU, memory, GPU and network so the product stays usable beyond flagship hardware.

**Triggers:** low-end Android; constrained device; mobile performance.

### `no-mouse`

Verify important web functionality is usable keyboard-only with sensible focus order, visible focus and control semantics.

**Triggers:** keyboard only; accessibility; focus order.

### `one-handed`

Review mobile interactions for thumb reach, touch target sizing and common one-handed use.

**Triggers:** mobile ergonomics; thumb reach; touch targets.

### `pixel-cop`

Review visual consistency in typography, spacing, hierarchy, tokens, alignment, icons, radius and responsive states.

**Triggers:** UI polish; design drift; visual consistency.

### `responsive-review`

Verify layouts adapt intentionally across viewport widths, text lengths, zoom and virtual keyboards instead of merely shrinking.

**Triggers:** responsive UI; mobile layout; breakpoint bugs.

### `ux-feasibility`

Determine whether a proposed UX can be implemented well on target platforms within stack, performance, accessibility and schedule constraints.

**Triggers:** UX feasibility; mockup review; complex interaction.

## Meta

### `codebase-orientation`

Teach a new developer or agent how a repository works quickly enough to make safe changes.

**Triggers:** new contributor; unfamiliar codebase; handoff.

### `handoff`

Produce a dense continuation artifact containing state, decisions, evidence, blockers and next actions.

**Triggers:** switch developer or agent; pause work; continuation summary.

### `intern-test`

Check whether a competent new developer can build, run, test and modify the project without tribal knowledge.

**Triggers:** onboarding review; bus factor; README setup.

### `project-profiler`

Fingerprint an unfamiliar repository's stack, boundaries, risks, tests and delivery shape before other skills act.

**Triggers:** new repository; route skills by stack; plan substantial work.

### `skill-author`

Create or revise focused Agent Skills with good activation descriptions, workflows, resources and verification.

**Triggers:** create a skill; improve a skill; package team expertise.

### `skill-router`

Select and sequence the smallest useful set of specialist skills for the current task.

**Triggers:** multi-domain engineering task; unclear specialist; compose several skills.

### `verification-before-completion`

Gate completion claims behind fresh evidence that directly proves the claimed outcome.

**Triggers:** before saying done; before PR or release; after final code change.

## Performance

### `benchmark-scientist`

Produce reproducible benchmarks with controlled variables, repeated measurements and defensible comparison rather than cherry-picked runs.

**Triggers:** benchmark; compare implementations; performance claim.

### `breakpoint-test`

Find the load knee where SLOs fail and identify the first saturated resource without confusing crash point with sustainable capacity.

**Triggers:** breakpoint test; max capacity; scaling ceiling.

### `capacity-plan`

Convert measured sustainable performance into headroom, failure capacity, infrastructure sizing and scaling triggers.

**Triggers:** capacity planning; node sizing; traffic growth.

### `database-performance`

Diagnose database performance using query plans, indexes, locks, transactions, pools and workload evidence.

**Triggers:** slow database; query plan; DB bottleneck.

### `frontend-performance`

Improve user-visible frontend responsiveness by measuring network, bundle, main-thread, rendering and interaction costs on representative devices.

**Triggers:** slow frontend; bundle size; janky UI.

### `generator-sanity`

Prove the load generator and network are not the bottleneck before attributing a throughput ceiling to the system under test.

**Triggers:** load generator bottleneck; RPS plateau; network ceiling.

### `load-modeler`

Translate real product usage or recorded journeys into representative arrival rates, concurrency, scenario weights, data cardinality and think time.

**Triggers:** traffic model; journey to load; performance scenario design.

### `load-test`

Design, execute and interpret realistic authorized load tests using traffic models, explicit SLOs, progressive ramps and system telemetry.

**Triggers:** load test; capacity validation; performance before release.

### `map-performance-review`

Review interactive map rendering, layers, markers, data updates and geospatial payloads for smooth constrained-device performance.

**Triggers:** map performance; MapLibre; many markers.

### `model-serving-review`

Review local or hosted model-serving paths for memory fit, batching, concurrency, latency, queueing and fallback behavior.

**Triggers:** vLLM; Ollama; model serving.

### `profiler`

Find where CPU, latency, allocations, I/O or contention are actually spent before optimizing.

**Triggers:** profile slow code; CPU high; latency investigation.

### `regression-analysis`

Compare performance runs fairly and identify operationally meaningful regressions while accounting for environment and variance.

**Triggers:** performance regression; before after benchmark; CI perf gate.

### `soak-test`

Run sustained workloads long enough to expose leaks, queue growth, cache drift, connection exhaustion and time-dependent degradation.

**Triggers:** soak test; endurance test; resource leak.

### `speed-demon`

Aggressively optimize measured hot paths after correctness is established while keeping overhead and complexity accountable.

**Triggers:** hot path optimization; latency critical; throughput optimization.

### `spike-test`

Validate system behavior, amplification and recovery when traffic increases abruptly beyond normal steady-state assumptions.

**Triggers:** traffic spike; flash crowd; burst testing.

### `take-my-load-operator`

Operate Take My Load safely for distributed capacity-aware tests with authorization, synchronized workers and generator sanity checks.

**Triggers:** take-my-load; distributed load generation; multi-worker load.

## Planning

### `brainstorming`

Compare materially different solution approaches, assumptions and tradeoffs before committing when the design space is open.

**Triggers:** brainstorm; compare approaches; pressure-test direction.

### `decision-record`

Capture context, drivers, options, decision, consequences and revisit triggers in a durable engineering decision record.

**Triggers:** architecture choice; ADR; tradeoff worth preserving.

### `requirements-audit`

Trace implementation against authoritative requirements and classify each item as complete, partial, missing, changed or unverifiable.

**Triggers:** before demo; scope audit; release requirements.

### `requirements-to-tasks`

Convert messy product or client requirements into testable acceptance criteria and implementable vertical tasks.

**Triggers:** client notes to tickets; ambiguous feature; acceptance criteria needed.

## Qa

### `accessibility-tester`

Test keyboard, semantics, focus, forms, names, contrast, zoom and assistive-technology behavior as product functionality.

**Triggers:** accessibility QA; keyboard testing; screen reader concerns.

### `api-contract-tester`

Verify API status, schema, validation, errors, auth differences and backwards-compatibility behavior from a consumer perspective.

**Triggers:** API test; contract test; schema drift.

### `automated-test-designer`

Choose and design automated tests at the lowest reliable layer while minimizing brittleness, duplication and runtime.

**Triggers:** add regression tests; test suite design; new behavior.

### `bug-reproducer`

Turn vague or intermittent defect reports into minimal reliable reproductions with evidence and regression candidates.

**Triggers:** sometimes bug; vague report; timing bug.

### `cross-browser-qa`

Verify critical behavior across supported browser engines and capture compatibility failures with exact browser evidence.

**Triggers:** cross browser; Firefox Safari Chromium; browser-specific bug.

### `data-integrity-tester`

Verify persisted data stays internally consistent across success, failure, retry, cancellation and migration paths.

**Triggers:** data corruption; transaction QA; migration integrity.

### `edge-case-goblin`

Generate nasty but plausible input, state, timing, concurrency and permission combinations that happy-path tests miss.

**Triggers:** edge cases; fuzz-like QA; boundary testing.

### `journey-compiler`

Compile a semantic journey into manual cases, browser E2E, API sequences and load scenarios without brittle coordinate coupling.

**Triggers:** recording to tests; compile journey; Playwright API load.

### `journey-recorder`

Record human or agent interactions as structured semantic journeys with browser, network and assertion evidence.

**Triggers:** record workflow; capture QA session; turn use into tests.

### `llm-eval`

Design repeatable evaluations for LLM features using representative cases, rubrics, failure taxonomies and regression baselines.

**Triggers:** LLM eval; prompt regression; AI quality.

### `manual-test-designer`

Design concise manual test cases where human judgment, hardware or low-frequency workflows make automation a poor fit.

**Triggers:** manual QA; hardware test; acceptance test.

### `mobile-device-qa`

Test mobile experiences across realistic screens, touch input, keyboards, orientation, lifecycle and constrained devices.

**Triggers:** mobile QA; Android iOS; device matrix.

### `mutation-test-planner`

Use targeted mutation testing to find important behavior that existing tests execute but fail to protect.

**Triggers:** mutation testing; high coverage low confidence; test effectiveness.

### `qa-explorer`

Explore an application like a skeptical human tester by varying input, navigation, timing, state and failure conditions.

**Triggers:** exploratory QA; new workflow; find edge cases.

### `qa-orchestrator`

Plan and coordinate the right mix of exploratory, manual, automated, visual, API, data, accessibility, device and performance testing.

**Triggers:** QA plan; release testing; choose test types.

### `regression-suite`

Build a compact regression suite from critical journeys and escaped defects, with a fast smoke subset.

**Triggers:** regression suite; smoke tests; repeated bugs.

### `release-candidate-qa`

Run risk-based final QA against the exact release candidate and produce a go, conditional-go or no-go recommendation.

**Triggers:** staging signoff; release candidate; pre-production QA.

### `test-architect`

Design the overall test portfolio and CI tiers so confidence comes from complementary layers rather than maximum test count.

**Triggers:** test strategy; slow flaky suite; coverage gaps.

### `visual-regression`

Detect unintended visual changes using stable screenshot baselines while separating environmental noise from real regressions.

**Triggers:** visual QA; CSS changes; screenshot diff.

## Reliability

### `2am-debugger`

Judge whether a tired on-call engineer can identify impact, recent changes and likely root cause quickly using documented tooling.

**Triggers:** runbook review; on-call readiness; 2am debug.

### `backup-restore-drill`

Validate backups by restoring them into clean infrastructure and checking application-level integrity and recovery time.

**Triggers:** restore drill; backup verification; disaster recovery.

### `bad-network`

Evaluate behavior under latency, jitter, bandwidth limits, connection resets, offline transitions and reconnects.

**Triggers:** bad network; offline testing; mobile connectivity.

### `cache-skeptic`

Challenge caches for necessity, invalidation correctness, stampedes, stale permissions and operational cost.

**Triggers:** cache review; stale cache; cache proposed.

### `ci-pipeline-review`

Review CI pipelines for trustworthy gating, caching, secret exposure, flaky behavior, artifact provenance and wasted runtime.

**Triggers:** CI review; GitHub Actions; pipeline slow or flaky.

### `config-review`

Review runtime configuration for unsafe defaults, drift, missing validation, secret confusion and production footguns.

**Triggers:** environment variables; config drift; unsafe defaults.

### `container-review`

Review container images and runtime configuration for reproducibility, size, permissions, signals, health and secret handling.

**Triggers:** Dockerfile; container image; container runtime.

### `dependency-failure`

Review and test behavior when downstream services become slow, malformed, partially available or completely unavailable.

**Triggers:** third-party outage; downstream failure; dependency resilience.

### `deployment-review`

Review deployment flow for artifact immutability, environment promotion, migrations, health gates, rollback and drift.

**Triggers:** deployment pipeline; staging to production; deploy review.

### `docker-compose-review`

Review Compose stacks for dependency readiness, durable state, networks, volumes, health, local-prod drift and operability.

**Triggers:** Docker Compose; local stack; compose production.

### `failure-injector`

Inject bounded failures to verify timeouts, retries, degradation, recovery and state integrity rather than trusting design claims.

**Triggers:** chaos test; failover test; dependency failure injection.

### `health-check-review`

Ensure liveness, readiness and startup probes represent actionable process state without causing cascades.

**Triggers:** health check; Kubernetes probe; readiness issues.

### `incident-commander`

Coordinate an active incident around impact reduction, reversible mitigation, evidence preservation, communication and recovery criteria.

**Triggers:** production incident; outage; severity response.

### `kubernetes-review`

Review Kubernetes workloads for resource requests, probes, rollout, disruption, storage, networking and failure semantics.

**Triggers:** Kubernetes; k3s; deployment manifest.

### `logging-review`

Review logging for stable structure, useful context, privacy, noise and ingestion cost.

**Triggers:** logging review; noisy logs; incident context.

### `observability-doctor`

Ensure operators can diagnose important failures from logs, metrics and traces without reproducing them locally.

**Triggers:** observability review; hard incident debugging; telemetry gaps.

### `paranoid`

Assume dependencies, operators, networks and processes fail and expose the hidden assumptions most likely to hurt production.

**Triggers:** reliability review; critical workflow; failure assumptions.

### `production-readiness`

Gate production launch on configuration, migrations, reliability, observability, backup, rollback, security and verified critical journeys.

**Triggers:** production readiness; launch review; go live.

### `queue-pressure`

Review queues under bursty producers, slow consumers, poison messages, retries and backlog growth.

**Triggers:** queue backlog; worker pressure; poison message.

### `race-hunter`

Find concurrency defects by forcing unsafe interleavings, duplicate operations and shared-state races.

**Triggers:** race condition; intermittent concurrency bug; parallel writes.

### `resource-leak-hunter`

Find memory, goroutine/thread, file descriptor, connection, timer and subscription leaks under repeated or sustained workloads.

**Triggers:** memory leak; connection leak; resource growth.

### `reverse-proxy-review`

Review reverse-proxy configuration for routing, headers, timeouts, buffering, TLS, websocket behavior and safe reloads.

**Triggers:** Caddy; Nginx; reverse proxy.

### `rollback-review`

Prove a release can be reverted or forward-fixed safely, including schema compatibility and irreversible side effects.

**Triggers:** rollback plan; risky release; database deploy.

### `shutdown-review`

Verify processes stop gracefully without dropping in-flight work, corrupting state or hanging deployments.

**Triggers:** graceful shutdown; rolling restart; worker drain.

## Security

### `auth-review`

Review authentication, reset, MFA, lockout and federation flows for bypass, enumeration and credential weaknesses.

**Triggers:** login change; password reset; OAuth OIDC.

### `authorization-review`

Verify sensitive operations enforce server-side permissions at resource boundaries and resist horizontal and vertical escalation.

**Triggers:** RBAC; IDOR; permission review.

### `dependency-security`

Review dependency and supply-chain risk, advisories, provenance, update strategy and unnecessary exposure.

**Triggers:** dependency CVE; supply chain; package security.

### `input-validation-review`

Review untrusted input validation, canonicalization, limits and dangerous sinks at real trust boundaries.

**Triggers:** input validation; injection; parser security.

### `multi-tenant-review`

Prove tenant isolation across queries, caches, files, jobs, logs, exports, search and administrative paths.

**Triggers:** multi-tenant SaaS; tenant isolation; cross-tenant risk.

### `payment-integrity`

Review payment workflows so retries, ambiguous gateway outcomes, webhooks, local state and settlement cannot create duplicate charges or false success.

**Triggers:** payment integration; gateway state; settlement reconciliation.

### `privacy-review`

Review personal and sensitive data collection, exposure, logging, sharing, retention and deletion with minimization as the default.

**Triggers:** PII; privacy; data collection.

### `prompt-injection-review`

Review LLM-integrated systems for untrusted instruction/data boundaries, tool authorization, secret exposure and unsafe action chaining.

**Triggers:** prompt injection; LLM security; agent tool safety.

### `rate-limit-review`

Design and test rate limits that constrain abuse without letting one actor deny service to legitimate users.

**Triggers:** rate limit; abuse prevention; 429.

### `secrets-review`

Prevent credentials and sensitive keys from leaking through source, history, logs, client bundles, CI artifacts or container layers.

**Triggers:** secret handling; credential leak; new API key.

### `security-review`

Perform risk-driven application security review of changed attack surface and trust boundaries instead of dumping a generic checklist.

**Triggers:** security review; public endpoint; sensitive feature.

### `session-review`

Review session and token lifecycle for fixation, theft, storage, expiry, rotation, revocation and concurrent-device behavior.

**Triggers:** session cookies; JWT; refresh token.

### `threat-model`

Build a focused threat model around assets, actors, trust boundaries, attack paths and mitigations for a feature or system.

**Triggers:** threat model; new sensitive system; security design.

### `tls-review`

Review TLS termination, certificate lifecycle, protocol policy, proxy trust and mixed-content/redirect behavior.

**Triggers:** TLS; certificate; HTTPS.

### `upload-security`

Review uploads for size, path, content, storage, rendering, archive and malware risks.

**Triggers:** file upload; image upload; archive import.

### `webhook-security`

Review webhooks for signature verification, replay resistance, duplicate delivery, retries, ordering and secret rotation.

**Triggers:** webhook; provider callback; signed event.
