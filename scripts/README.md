# Scripts

This directory contains automation scripts for common development tasks.

## Available Scripts

### `run_all_tests.sh`
Runs all Python and C++ tests across all problems.

**Usage:**
```bash
./scripts/run_all_tests.sh
```

### `format_all.sh`
Formats all Python and C++ code in the repository.

**Usage:**
```bash
./scripts/format_all.sh
```

## Alternative: Using Makefile

For convenience, you can also use the Makefile at the root:

```bash
make test        # Run all tests
make format      # Format all code
make lint        # Lint all code
make ci-check    # Run all CI checks
```

See the root [Makefile](../Makefile) for all available commands.

