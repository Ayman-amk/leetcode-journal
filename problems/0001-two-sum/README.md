# 0001. Two Sum

**Link:** [LeetCode Problem](https://leetcode.com/problems/two-sum/)  
**Difficulty:** Easy  
**Tags:** Hash Map, Array, One-Pass

---

### Intuition

We need two distinct indices `i` and `j` such that `nums[i] + nums[j] == target`.  
A brute-force approach checks all pairs in O(n²) — too slow.  
Instead, we can use a hash map to record values we’ve already seen and their indices,  
allowing instant complement lookup in O(1).

---

### Approach

- Initialize an empty hash map `seen`.
- Iterate through the array:
  1. Compute `complement = target - num`.
  2. If the complement exists in `seen`, return the indices `[seen[complement], i]`.
  3. Otherwise, store `seen[num] = i`.
- If no pair is found (theoretically impossible per problem statement), return an empty list.

---

### Complexity

| Metric    | Value | Notes                       |
| :-------- | :---- | :-------------------------- |
| **Time**  | O(n)  | One hash lookup per element |
| **Space** | O(n)  | Map stores up to n entries  |

---

### Implementations & Tests

| Language       | File                                         | Tested | Notes                          |
| -------------- | -------------------------------------------- | ------ | ------------------------------ |
| **C++**        | [`cpp/solution.cpp`](./cpp/solution.cpp)     | Yes | Fast, memory-efficient         |
| **Python**     | [`python/solution.py`](./python/solution.py) | Yes | Clear reference implementation |
| **JavaScript** | [`js/solution.js`](./js/solution.js)         | No  | Optional extra reference       |

> **C++ and Python** versions include standalone test files demonstrating correctness.  
> C++ uses `<cassert>` tests for performance and verification; Python uses `pytest`-style asserts.

---

### Example

**Input:**  
`nums = [2, 7, 11, 15], target = 9`  
**Output:**  
`[0, 1]`  
**Explanation:** `nums[0] + nums[1] = 2 + 7 = 9`

---

### Notes

- `unordered_map` (C++) and `dict` (Python) provide O(1) average lookup.
- Always prefer one-pass solution: less memory churn, earlier return.
- Validates problem-solving fluency and algorithmic reasoning — typical FAANG warm-up question.

---

**Last Updated:** 2025-11-08
