#!/bin/bash
# Run all tests across all problems

set -e

echo "Running all Python tests..."
python -m pytest problems/**/python/test_solution.py -v || {
    echo "Some Python tests failed, trying individual tests..."
    for test_file in problems/*/python/test_solution.py; do
        if [ -f "$test_file" ]; then
            echo "Testing: $test_file"
            cd "$(dirname "$test_file")"
            python -m pytest test_solution.py -v
            cd - > /dev/null
        fi
    done
}

echo ""
echo "Running all C++ tests..."
find problems -name "test_solution.cpp" -type f | while read test_file; do
    problem_dir=$(dirname "$test_file")
    echo "Testing: $problem_dir"
    cd "$problem_dir"
    g++ -std=c++17 -O2 -Wall -Wextra test_solution.cpp -o test
    ./test
    rm -f test
    cd - > /dev/null
done

echo ""
echo "All tests completed!"

