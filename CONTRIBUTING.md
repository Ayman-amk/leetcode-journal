# Contributing to LeetCode Journal

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this repository.

## Code of Conduct

- Be respectful and professional
- Focus on code quality and learning
- Provide clear, helpful feedback

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce (if applicable)
   - Expected vs actual behavior

### Adding New Problems

1. **Scaffold the problem:**
   ```bash
   python utils/scaffold.py <problem-id>-<problem-slug>
   ```

2. **Implement solutions:**
   - Write clean, well-documented code
   - Follow the existing code style
   - Include comprehensive tests

3. **Update documentation:**
   - Fill in README.md with approach and complexity
   - Update docs/PATTERNS.md if introducing new patterns
   - Update meta.yaml with correct difficulty and patterns

4. **Ensure quality:**
   - All tests pass
   - Code is formatted (black, clang-format)
   - No linting errors

5. **Submit:**
   - Create a feature branch
   - Commit with clear messages
   - Push and create a merge request

## Code Standards

### Python
- Follow PEP 8 style guide
- Use type hints
- Write docstrings for all functions/classes
- Maximum line length: 88 characters (Black default)

### C++
- Follow Google C++ Style Guide
- Use meaningful variable names
- Include comments for complex logic
- Compile with `-Wall -Wextra -Werror`

### Testing
- Write tests for all solutions
- Cover edge cases
- Tests should be self-contained and runnable

## Commit Messages

Use clear, descriptive commit messages:

```
Format: <type>: <subject>

Types:
- feat: New problem or feature
- fix: Bug fix
- docs: Documentation changes
- refactor: Code restructuring
- test: Test additions/modifications
- chore: Maintenance tasks
```

## Pull Request Process

1. Ensure all CI checks pass
2. Update documentation if needed
3. Keep commits focused and logical
4. Request review from maintainers

## Questions?

Open an issue or check the [Developer Guide](docs/DEVELOPER_GUIDE.md) for more details.

