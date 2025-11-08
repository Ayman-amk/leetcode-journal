# 0002. Add Two Numbers

**Link:** [LeetCode Problem](https://leetcode.com/problems/add-two-numbers/)  
**Difficulty:** Medium  
**Tags:** Linked List, Math, Recursion

---

### Intuition

We need to add two numbers represented as linked lists where digits are stored in reverse order. This is similar to manual addition we do on paper, but working from right to left (which matches the reverse order of the lists).

The key insight is to:
1. Process both lists simultaneously, digit by digit
2. Handle carry-over when the sum of two digits exceeds 9
3. Continue until both lists are exhausted and no carry remains

---

### Approach

1. **Initialize a dummy node** to simplify edge cases and build the result list
2. **Iterate through both lists** while either list has nodes or there's a carry
3. **For each position:**
   - Extract values from current nodes (0 if node is null)
   - Calculate `total = val1 + val2 + carry`
   - Extract the digit: `digit = total % 10`
   - Update carry: `carry = total / 10`
   - Create a new node with the digit and append to result
4. **Move to next nodes** in both lists
5. **Return the result** (skip the dummy node)

**Key points:**
- Use a dummy node pattern to avoid special cases for the head
- Handle lists of different lengths by treating null nodes as 0
- Continue processing even after both lists end if there's a remaining carry

---

### Complexity

| Metric    | Value | Notes                                    |
| :-------- | :---- | :--------------------------------------- |
| **Time**  | O(n)  | Traverse both lists once, n = max(m, n)  |
| **Space** | O(n)  | Result list has at most max(m, n) + 1 nodes |

Where `m` and `n` are the lengths of the two input linked lists.

---

### Implementations & Tests

| Language   | File                                         | Tested | Notes                          |
| ---------- | -------------------------------------------- | ------ | ------------------------------ |
| **C++**    | [`cpp/solution.cpp`](./cpp/solution.cpp)     | Yes    | Efficient pointer manipulation |
| **Python** | [`python/solution.py`](./python/solution.py) | Yes    | Clean, readable implementation |

> Both implementations include comprehensive test cases covering edge cases like different list lengths, carry-over scenarios, and zero inputs.

---

### Example

**Input:**  
`l1 = [2,4,3]` (represents 342)  
`l2 = [5,6,4]` (represents 465)

**Step-by-step:**
1. Add 2 + 5 = 7, no carry → result: [7]
2. Add 4 + 6 = 10, carry 1, digit 0 → result: [7,0]
3. Add 3 + 4 + 1 = 8, no carry → result: [7,0,8]

**Output:** [7,0,8] (represents 807)

**Explanation:** 342 + 465 = 807

---

### Notes

- The dummy node pattern is essential for clean code - it eliminates the need to check if the result list is empty
- Always handle the final carry - if both lists end but carry is 1, we need one more node
- This problem tests understanding of linked list manipulation and basic arithmetic
- Common follow-up: What if digits are stored in forward order? (Requires reversing lists first or using recursion)

---

**Last Updated:** 2025-11-08
