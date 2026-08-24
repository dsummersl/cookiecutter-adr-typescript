# 1. TypeScript project

Date: 2025-09-05

## Status

Accepted

## Context

A new project is being started that will be implemented in TypeScript.

## Decision

Use a standard layout for the project with the following details:
- Use npm as the package manager.
- Use [vitest](https://vitest.dev/) as the test framework (with v8 coverage).
- Use [tsx](https://github.com/privatenumber/tsx) to run TypeScript directly.
- Use [knip](https://github.com/webpro/knip) to detect dead code and unused dependencies.
- Use [treepeat](https://github.com/) to detect duplicate/similar code.
- Use [adr-tools](https://github.com/npryce/adr-tools) to document architectural decisions.

Use the following layout for the TypeScript project:

```plaintext
project-root/
├── src/
├── test/
└── docs/
```

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.