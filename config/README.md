# Configuration Files

This directory contains configuration files for development tools.

## Files

- **pyproject.toml** - Configuration for Python tools (Black, Flake8, Pytest)

## Usage

These configurations are automatically picked up by the respective tools:
- `black` reads from `config/pyproject.toml`
- `flake8` reads from `config/pyproject.toml`
- `pytest` reads from `config/pyproject.toml`

You can also place tool-specific config files here as the project grows.

