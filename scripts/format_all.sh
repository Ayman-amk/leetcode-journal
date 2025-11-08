#!/bin/bash
# Format all code in the repository

set -e

echo "Formatting Python code..."
black problems/ utils/ src/ scripts/

echo "Formatting C++ code..."
find problems -name "*.cpp" -o -name "*.h" | while read file; do
    if command -v clang-format &> /dev/null; then
        clang-format -i --style=Google "$file"
        echo "Formatted: $file"
    else
        echo "clang-format not found, skipping C++ formatting"
        break
    fi
done

echo "All code formatted!"

