# 0003. Longest Substring Without Repeating Characters

**Link:** [LeetCode Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
**Difficulty:** Medium  
**Tags:** Hash Table, String, Sliding Window, Two Pointers

---

### Intuition

We need to find the longest substring without repeating characters. This is a classic sliding window problem where we maintain a window of unique characters and expand/shrink it as we encounter duplicates.

The key insight is to use a hash map to track the last seen index of each character. When we encounter a character we've seen before (and it's within our current window), we move the start of the window to just after that character's last occurrence.

---

### Approach

1. **Initialize:**
   - Hash map `char_index` to store character → last seen index
   - `max_length` to track the maximum length found
   - `start` to mark the beginning of the current window

2. **Iterate through the string:**
   - For each character at index `end`:
     - If the character exists in the map and its last index is within the current window (`>= start`), move `start` to `char_index[char] + 1`
     - Update the character's last seen index to `end`
     - Calculate current window length: `end - start + 1`
     - Update `max_length` if current window is longer

3. **Return `max_length`**

**Key points:**
- Sliding window technique: expand window by moving `end`, shrink by moving `start`
- Hash map provides O(1) lookup for character positions
- Only move `start` if the duplicate is within the current window

---

### Complexity

| Metric    | Value | Notes                                    |
| :-------- | :---- | :--------------------------------------- |
| **Time**  | O(n)  | Single pass through the string           |
| **Space** | O(m)  | Hash map stores at most m unique chars   |

Where `n` is the length of the string and `m` is the size of the character set (typically 128 for ASCII or 256 for extended ASCII).

---

### Implementations & Tests

| Language   | File                                         | Tested | Notes                          |
| ---------- | -------------------------------------------- | ------ | ------------------------------ |
| **C++**    | [`cpp/solution.cpp`](./cpp/solution.cpp)     | Yes    | Efficient sliding window       |
| **Python** | [`python/solution.py`](./python/solution.py) | Yes    | Clean, readable implementation |

> Both implementations include comprehensive test cases covering edge cases like empty strings, single characters, all unique characters, and various repeating patterns.

---

### Example

**Input:** `s = "abcabcbb"`

**Step-by-step:**
1. `a` (end=0): window=[a], length=1, max=1
2. `b` (end=1): window=[a,b], length=2, max=2
3. `c` (end=2): window=[a,b,c], length=3, max=3
4. `a` (end=3): seen at index 0, move start to 1, window=[b,c,a], length=3, max=3
5. `b` (end=4): seen at index 1, move start to 2, window=[c,a,b], length=3, max=3
6. `c` (end=5): seen at index 2, move start to 3, window=[a,b,c], length=3, max=3
7. `b` (end=6): seen at index 4, move start to 5, window=[c,b], length=2, max=3
8. `b` (end=7): seen at index 6, move start to 7, window=[b], length=1, max=3

**Output:** `3` (substring "abc" or "bca" or "cab")

---

### Notes

- This is a fundamental sliding window problem that appears in many variations
- The hash map approach is optimal - O(n) time and O(min(n,m)) space
- Alternative approach: use a set and remove characters when shrinking window (less efficient)
- Common follow-up: Return the actual substring, not just the length
- Pattern: Sliding window + hash map for substring problems

---

**Last Updated:** 2025-11-08
