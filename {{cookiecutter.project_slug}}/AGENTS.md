# Agent Guidelines

This file provides guidance when working with code in this repository.

## Project Overview

See this projects README.md for an overview of the project, and ADR documents in docs/adr/ for architectural decisions.

## Development Commands

**IMPORTANT**: Always use the `npm run` commands below for development tasks.

### Setup
```bash
npm install  # Install dependencies
```

### Testing
```bash
npm test           # Run all tests with vitest
npm run coverage   # Run all tests with v8 coverage report and thresholds
```

### Run
```bash
npm start   # Run the entrypoint with tsx
```

### Code Quality
```bash
npm run type      # Type check with tsc --noEmit (strict)
npm run knip      # Detect dead code / unused dependencies
npm run treepeat  # Detect duplicate/similar code
npm run ci        # Run all CI checks (coverage + type + knip + treepeat)
```

**Before completing any feature**, run `npm run ci` to ensure all checks pass.

## Project Structure

```
src/         # Main package source code
test/        # Test files (mirror src/ structure)
docs/adr/    # Architecture Decision Records
```

## Pull request workflow

### Opening a PR
- Add or update an automated test that exercises the feature or fix.
- Fill in the PR template's "Post-merge verification" section with concrete
  steps someone could run on a fresh checkout of main: commands, URLs,
  locations to check, and what a pass looks like.
- After opening the PR, subscribe to its activity and fix CI failures.
- Never merge unless I explicitly say to.

### When I say "approved, merge and verify"
1. Merge the PR (enable auto-merge if checks are still running).
2. Wait for the CI run on main for the merge commit. If it fails, say so
   and open a fix PR.
3. Check out main fresh, follow the README setup exactly as written, and
   note any step that doesn't work as documented.
4. Run each step in the PR's "Post-merge verification" section.
   Take screenshots where a visual check is needed.
5. Comment the results on the merged PR: what you ran, pass or fail for
   each step, and anything that needs my judgment.
6. If something fails, open a fix PR or issue. Do not edit main directly.
