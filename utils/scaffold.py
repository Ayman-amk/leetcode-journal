#!/usr/bin/env python3
"""
Usage:
    python utils/scaffold.py 0001-two-sum

Creates a new problem folder with structure:
0001-two-sum/
    README.md
    meta.yaml
    python/solution.py
    cpp/solution.cpp
    js/solution.js
"""

import os
import sys
from datetime import datetime
import yaml

def create_folder_structure(problem_id_slug: str):
    root = os.path.join(os.getcwd(), problem_id_slug)
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

🗓 **Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
"""
    with open(os.path.join(root, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # meta.yaml
    meta_data = {
        "id": int(problem_id_slug.split('-')[0]),
        "slug": problem_id_slug.split('-', 1)[1],
        "difficulty": None,
        "patterns": [],
        "languages": langs,
        "status": "todo",
        "last_update": datetime.now().strftime('%Y-%m-%d')
    }
    with open(os.path.join(root, "meta.yaml"), "w", encoding="utf-8") as f:
        yaml.dump(meta_data, f, sort_keys=False)

    # Create empty solution files
    for lang in langs:
        ext = {"python": "py", "cpp": "cpp", "js": "js"}[lang]
        with open(os.path.join(root, lang, f"solution.{ext}"), "w", encoding="utf-8") as f:
            f.write(f"# {problem_id_slug} solution in {lang}\n")

    print(f"Scaffold created successfully for '{problem_id_slug}'")

def main():
    if len(sys.argv) != 2:
        print("Usage: python utils/scaffold.py <problem_id-slug>")
        sys.exit(1)
    create_folder_structure(sys.argv[1])

if __name__ == "__main__":
    main()
