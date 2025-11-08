#include <cstddef>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode* next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode* next) : val(x), next(next) {}
};

/**
 * @brief 2. Add Two Numbers
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order, and each of their nodes
 * contains a single digit. Add the two numbers and return the sum as a linked
 * list.
 *
 * Time Complexity:  O(max(m, n)) where m and n are lengths of l1 and l2
 * Space Complexity: O(max(m, n)) for the result list
 */
class Solution {
 public:
  ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode* dummy = new ListNode(0);
    ListNode* current = dummy;
    int carry = 0;

    while (l1 || l2 || carry) {
      // Get values from current nodes (0 if nullptr)
      int val1 = l1 ? l1->val : 0;
      int val2 = l2 ? l2->val : 0;

      // Calculate sum and carry
      int total = val1 + val2 + carry;
      carry = total / 10;
      int digit = total % 10;

      // Create new node with the digit
      current->next = new ListNode(digit);
      current = current->next;

      // Move to next nodes
      if (l1) l1 = l1->next;
      if (l2) l2 = l2->next;
    }

    ListNode* result = dummy->next;
    delete dummy;
    return result;
  }
};
