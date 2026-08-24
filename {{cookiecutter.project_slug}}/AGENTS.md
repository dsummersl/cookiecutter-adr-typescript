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