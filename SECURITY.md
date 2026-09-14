# Security

SkillShop contains agent instructions, scripts, references, schemas, and templates. Treat contributions as executable supply-chain inputs even when they look like Markdown.

## Reporting

For a vulnerability in SkillShop itself, open a private GitHub security advisory rather than a public issue when possible.

## Contribution security rules

- Do not add secrets, credentials, private endpoints, production tokens, or customer data.
- Skill scripts must not silently exfiltrate files, environment variables, repository contents, or prompts.
- Network access must be explicit in the skill's compatibility/instructions when required.
- Dangerous mutations must be clearly scoped and should require explicit authorization/confirmation in the host environment.
- Load/performance skills must target systems the operator owns or is explicitly authorized to test.
- Security testing skills are for defensive review and authorized environments.
- Do not hide executable payloads in assets or references.
- Pin or justify new third-party execution dependencies.

The repository validator checks structure, not semantic safety. Human review is still required for contributed instructions and scripts.
