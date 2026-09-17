# 1. TypeScript project

Date: 2026-09-17

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
- Use [ast-grep](https://ast-grep.github.io/) rules (in `.ast-grep/rules/`) to disallow comments.

Use the following layout for the TypeScript project:

```plaintext
project-root/
├── src/
├── test/
└── docs/
```

### Working with coding agents (and humans)

Much of the code in this project is configured to make working with LLM coding agents easier (and humans too!).
Agents often produce a common problems (stray comments, dead code, near-duplicate code, imports buried inside functions, sprawling functions), so tooling is chosen to catch at CI time:

- **No comments** ([ast-grep](https://ast-grep.github.io/) rules in `.ast-grep/rules/`).
  Code is expected to be self-documenting. `npm run lint` flags them and `npm run fix` strips them. Motivated by
  [Inside Out: Uncovering How Comment Internalization Steers LLMs for Better or Worse](https://arxiv.org/pdf/2512.16790),
  which shows LLMs lean heavily on comments and that this steers their output in
  unpredictable, model- and task-dependent ways. A small allowlist for exceptional cases:
  `@ts-expect-error`, `@ts-ignore`, `eslint-disable`, and `// WHY:` prefixed comments.
- **Dead code is rejected immediately** ([knip](https://github.com/webpro/knip)). Unused code is not allowed by default.
  Agents tend to leave behind unused functions, exports, and dependencies; knip fails CI
  on them so they are removed in the same change that created them.
- **Duplicate code is surfaced** ([treepeat](https://github.com/dsummersl/treepeat)). `npm run treepeat` lets us find and refactor duplicate/similar code. It is advisory (not part of `npm run ci`); run it when looking for refactors. We expect to lower the `--similarity` threshold (default 100, exact matches only) as the project grows, to catch near-duplicates more aggressively.
- **Strict typing** (tsc `strict` and `noUncheckedIndexedAccess`). Use typing to enforce code boundaries.

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.