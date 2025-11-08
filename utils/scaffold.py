#!/usr/bin/env python3
"""
Problem scaffolding tool.

Usage:
    python utils/scaffold.py 0001-two-sum

Creates a new problem folder with structure:
problems/0001-two-sum/
    README.md
    meta.yaml
    python/solution.py
    python/test_solution.py
    cpp/solution.cpp
    cpp/test_solution.cpp
    js/solution.js
"""

import os
import sys
from datetime import datetime
import yaml


def create_folder_structure(problem_id_slug: str):
    """
    Create folder structure for a new LeetCode problem.

    Args:
        problem_id_slug: Problem identifier in format "0001-two-sum".
    """
    problems_dir = os.path.join(os.getcwd(), "problems")
    root = os.path.join(problems_dir, problem_id_slug)
    if os.path.exists(root):
        print(f"Folder '{problem_id_slug}' already exists.")
        return

    # Create base folders
    langs = ["python", "cpp", "js"]
    os.makedirs(root, exist_ok=True)
    for lang in langs:
        os.makedirs(os.path.join(root, lang), exist_ok=True)

    # README.md
    readme_content = f"""# {problem_id_slug.replace('-', ' ').title()}

**Link:** https://leetcode.com/problems/{problem_id_slug.split('-', 1)[1]}/
**Difficulty:**
**Tags:**

---

### Intuition
Write your thought process here.

### Approach
Explain step-by-step how you solved it.

### Complexity
- **Time:**
- **Space:**

### Example
Input:
Output:

---

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
"""
    with open(os.path.join(root, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # meta.yaml
    meta_data = {
        "id": int(problem_id_slug.split("-")[0]),
        "slug": problem_id_slug.split("-", 1)[1],
        "difficulty": None,
        "patterns": [],
        "languages": langs,
        "status": "todo",
        "last_update": datetime.now().strftime("%Y-%m-%d"),
    }
    with open(os.path.join(root, "meta.yaml"), "w", encoding="utf-8") as f:
        yaml.dump(meta_data, f, sort_keys=False)

    # Create empty solution files
    for lang in langs:
        ext = {"python": "py", "cpp": "cpp", "js": "js"}[lang]
        solution_path = os.path.join(root, lang, f"solution.{ext}")
        with open(solution_path, "w", encoding="utf-8") as f:
            f.write(f"# {problem_id_slug} solution in {lang}\n")

    # Create test files for Python and C++
    python_test_content = """from solution import Solution

def test_solution():
    solver = Solution()
    # Add your test cases here
    # assert solver.method() == expected
    print("All Python tests passed.")

if __name__ == "__main__":
    test_solution()
"""
    with open(
        os.path.join(root, "python", "test_solution.py"), "w", encoding="utf-8"
    ) as f:
        f.write(python_test_content)

    cpp_test_content = """#include <cassert>
#include <vector>
#include <iostream>
#include "solution.cpp"

using namespace std;

int main() {
    Solution solver;
    // Add your test cases here
    // assert(condition);
    cout << "All C++ tests passed!\\n";
    return 0;
}
"""
    with open(
        os.path.join(root, "cpp", "test_solution.cpp"), "w", encoding="utf-8"
    ) as f:
        f.write(cpp_test_content)

    print(f"Scaffold created successfully for '{problem_id_slug}'")


def main():
    """Process command line arguments and create problem scaffold."""
    if len(sys.argv) != 2:
        print("Usage: python utils/scaffold.py <problem_id-slug>")
        sys.exit(1)
    create_folder_structure(sys.argv[1])


if __name__ == "__main__":
    main()
