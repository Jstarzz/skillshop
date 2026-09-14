# Changelog

## 0.2.0

- Reworked SkillShop from 157 registered plugin skills into a low-context router architecture.
- Preserved all 157 specialist playbooks under `library/playbooks/`.
- Added `/skillshop:shop` as the single model-invocable router.
- Added user-only `/skillshop:find`, `/skillshop:apply`, and `/skillshop:catalog`.
- Added a project-aware deterministic recommender for candidate retrieval.
- Updated validation to enforce the small registered surface and full cold-library integrity.
- Kept semantic journey QA and Take My Load playbooks in the on-demand library.

## 0.1.0

- Initial public release with 157 engineering skills across 10 categories.
- Added Claude Code marketplace/plugin packaging, catalog, routing helpers, documentation and validation.
