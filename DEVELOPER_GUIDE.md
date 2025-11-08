# Developer Guide

This guide explains the architecture, workflows, and best practices for contributing to the LeetCode Journal repository.

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Adding New Problems](#adding-new-problems)
- [Testing Strategy](#testing-strategy)
- [CI/CD Pipeline](#cicd-pipeline)
- [Code Quality Standards](#code-quality-standards)
- [VS Code Integration](#vs-code-integration)
- [Troubleshooting](#troubleshooting)

## Architecture Overview

### Directory Structure

```
leetcode-journal/
├── problems/              # All problem solutions
│   └── <id>-<slug>/      # Individual problem folder
│       ├── README.md      # Problem analysis
│       ├── meta.yaml      # Structured metadata
│       └── <language>/    # Language-specific implementations
├── utils/                 # Utility scripts
│   └── scaffold.py        # Problem scaffolding tool
├── src/                   # Internal scripts (future use)
├── .gitlab-ci.yml         # GitLab CI/CD pipeline
├── .github/workflows/     # GitHub Actions (optional)
└── .vscode/               # Editor configuration
```

### Problem Folder Structure

Each problem follows a consistent structure:

```
problems/0001-two-sum/
├── README.md              # Problem description, approach, complexity
├── meta.yaml              # Problem metadata (id, difficulty, patterns, status)
├── python/
│   ├── solution.py        # Python implementation
│   └── test_solution.py   # Python tests
├── cpp/
│   ├── solution.cpp       # C++ implementation
│   └── test_solution.cpp  # C++ tests
└── js/
    └── solution.js        # JavaScript implementation (optional)
```

## Adding New Problems

### Step 1: Scaffold the Problem

Use the scaffolding tool to create a new problem structure:

```bash
python utils/scaffold.py 0002-add-two-numbers
```

This creates:
- Problem folder with proper naming
- Language subfolders (python, cpp, js)
- Template README.md
- meta.yaml with initial metadata
- Empty solution files
- Test file templates

### Step 2: Implement Solutions

#### Python Solution Template

```python
from typing import List

class Solution:
    def method_name(self, params: List[int]) -> int:
        # Your implementation
        pass
```

#### C++ Solution Template

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> methodName(vector<int>& nums) {
        // Your implementation
        return {};
    }
};
```

### Step 3: Write Tests

#### Python Tests

```python
from solution import Solution

def test_solution():
    solver = Solution()
    assert solver.method_name([1, 2, 3]) == expected_result
    # Add more test cases
    print("All Python tests passed.")

if __name__ == "__main__":
    test_solution()
```

#### C++ Tests

```cpp
#include <cassert>
#include <vector>
#include <iostream>
#include "solution.cpp"

using namespace std;

int main() {
    Solution solver;
    vector<int> input = {1, 2, 3};
    vector<int> result = solver.methodName(input);
    assert(result == expected_result);
    cout << "All C++ tests passed!\n";
    return 0;
}
```

### Step 4: Update Metadata

Edit `meta.yaml`:

```yaml
id: 2
slug: add-two-numbers
difficulty: Medium
patterns:
  - Linked List
  - Math
languages:
  - python
  - cpp
status: completed
last_update: 2025-11-08
```

### Step 5: Document Your Approach

Update `README.md` with:
- Problem link
- Intuition
- Approach (step-by-step)
- Complexity analysis
- Example walkthrough

## Testing Strategy

### Local Testing

#### Python

```bash
# Single problem
python problems/0001-two-sum/python/test_solution.py

# All problems (requires pytest)
pytest problems/**/python/test_solution.py -v
```

#### C++

```bash
# Single problem
cd problems/0001-two-sum/cpp
g++ -std=c++17 -O2 test_solution.cpp -o test && ./test

# All problems (Linux/macOS)
find problems -name "test_solution.cpp" -exec sh -c \
  'cd "$(dirname "{}")" && g++ -std=c++17 -O2 test_solution.cpp -o test && ./test && rm test' \;
```

### VS Code Tasks

Use VS Code tasks for one-click testing:

1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Type "Tasks: Run Task"
3. Select:
   - "Run Python Test (Current Problem)"
   - "Build & Run C++ Test (Current Problem)"
   - "Run All Python Tests"

## CI/CD Pipeline

### Workflow Overview

The CI pipeline (`.gitlab-ci.yml`) runs on every push and merge request:

1. **Python Tests & Linting**
   - Runs on Docker images with Python 3.9, 3.10, 3.11
   - Format check with `black`
   - Lint check with `flake8`
   - Run all Python tests
   - Generate coverage reports

2. **C++ Tests & Formatting**
   - Runs on Ubuntu and Windows Docker images
   - Format check with `clang-format`
   - Build and run all C++ tests
   - Compiler flags: `-std=c++17 -O2 -Wall -Wextra -Werror`

3. **Summary**
   - Aggregates test results
   - Reports problem count
   - Uploads coverage artifacts

### Caching

The pipeline caches:
- Python pip dependencies (via GitLab cache)
- Coverage reports (as artifacts)

### Failure Conditions

The pipeline fails if:
- Any test fails
- Formatting doesn't match standards
- Linting finds errors
- Code doesn't compile

## Code Quality Standards

### Python

#### Formatting (Black)

- Line length: 88 characters
- Double quotes for strings
- Trailing commas in multi-line structures

```bash
# Check formatting
black --check problems/ utils/ src/

# Auto-format
black problems/ utils/ src/
```

#### Linting (Flake8)

- Max line length: 88
- Ignored rules: E203 (whitespace before ':'), W503 (line break before binary operator)

```bash
# Run linter
flake8 problems/ utils/ src/ --max-line-length=88 --extend-ignore=E203,W503
```

### C++

#### Formatting (clang-format)

- Style: Google
- Indentation: 2 spaces
- Column limit: 80

```bash
# Check formatting
clang-format --style=Google --dry-run --Werror problems/**/*.cpp

# Auto-format
find problems -name "*.cpp" -exec clang-format -i --style=Google {} \;
```

#### Compiler Flags

- Standard: C++17
- Optimization: -O2
- Warnings: -Wall -Wextra -Werror

## VS Code Integration

### Settings

The `.vscode/settings.json` configures:

- **Auto-format on save** for all languages
- **Python:** Black formatter, Flake8 linter
- **C++:** clang-format (Google style)
- **Test discovery:** Pytest enabled

### Tasks

Pre-configured tasks in `.vscode/tasks.json`:

- `Run Python Test (Current Problem)` - Run test in current file's directory
- `Build & Run C++ Test (Current Problem)` - Compile and run C++ test
- `Run All Python Tests` - Run all Python tests with pytest
- `Format Python (Black)` - Format all Python files
- `Lint Python (Flake8)` - Lint all Python files

### Recommended Extensions

- Python (Microsoft)
- C/C++ (Microsoft)
- Black Formatter
- Pytest

## Troubleshooting

### Python Tests Fail Locally

1. **Import errors:** Ensure you're running from the problem directory or using proper module paths
2. **Missing dependencies:** Run `pip install -r requirements.txt`
3. **Python version:** Ensure Python 3.9+

### C++ Tests Fail to Compile

1. **Compiler not found:** Install g++ (Linux), Xcode Command Line Tools (macOS), or MinGW (Windows)
2. **C++17 not supported:** Update your compiler
3. **Include paths:** Check that `solution.cpp` is in the same directory as `test_solution.cpp`

### CI Pipeline Fails

1. **Formatting errors:** Run `black` and `clang-format` locally
2. **Linting errors:** Fix flake8 warnings
3. **Test failures:** Run tests locally first
4. **Platform-specific issues:** Test on multiple platforms if possible
5. **GitLab CI issues:** Check pipeline logs in GitLab UI under CI/CD > Pipelines

### VS Code Tasks Not Working

1. **Task not found:** Ensure `.vscode/tasks.json` exists
2. **Compiler not in PATH:** Add compiler to system PATH
3. **Python not found:** Configure Python interpreter in VS Code

## Best Practices

1. **Always write tests** before or alongside implementation
2. **Run tests locally** before pushing
3. **Follow naming conventions:** Use kebab-case for problem folders, snake_case for Python, camelCase for C++
4. **Document your approach** in README.md
5. **Update metadata** when completing a problem
6. **Keep solutions clean** - no debug code, no commented-out solutions
7. **Use meaningful variable names**
8. **Add complexity analysis** to README.md

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your problem following the structure
4. Ensure all tests pass
5. Run formatting and linting
6. Submit a pull request

The CI pipeline will automatically validate your changes.

---

**Questions?** Open an issue or check the main [README.md](./README.md).

