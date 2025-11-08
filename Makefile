.PHONY: help test format lint clean scaffold install

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Install Python dependencies
	pip install -r requirements.txt

test-python: ## Run all Python tests
	python -m pytest problems/**/python/test_solution.py -v

test-cpp: ## Run all C++ tests (Linux/macOS)
	find problems -name "test_solution.cpp" -exec sh -c 'cd "$$(dirname "{}")" && g++ -std=c++17 -O2 test_solution.cpp -o test && ./test && rm test' \;

test: test-python ## Run all tests

format-python: ## Format Python code with black
	black problems/ utils/ src/

format-cpp: ## Format C++ code with clang-format
	find problems -name "*.cpp" -exec clang-format -i --style=Google {} \;

format: format-python format-cpp ## Format all code

lint-python: ## Lint Python code with flake8
	flake8 problems/ utils/ src/ --max-line-length=88 --extend-ignore=E203,W503

lint: lint-python ## Run all linters

clean: ## Remove temporary files and caches
	find problems -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find problems -name "*.pyc" -delete 2>/dev/null || true
	find problems -name "*.exe" -delete 2>/dev/null || true
	find problems -name "test" -delete 2>/dev/null || true
	find problems -name "*.o" -delete 2>/dev/null || true

scaffold: ## Create new problem scaffold (usage: make scaffold PROBLEM=0004-median-of-two-sorted-arrays)
	@if [ -z "$(PROBLEM)" ]; then \
		echo "Usage: make scaffold PROBLEM=0004-median-of-two-sorted-arrays"; \
		exit 1; \
	fi
	python utils/scaffold.py $(PROBLEM)

ci-check: format lint test ## Run all CI checks locally

