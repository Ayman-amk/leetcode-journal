from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        """Helper for testing - compare two linked lists."""
        if not isinstance(other, ListNode):
            return False
        current_self = self
        current_other = other
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None

    @staticmethod
    def from_list(values):
        """Helper to create ListNode from list [2,4,3] -> ListNode(2)->ListNode(4)->ListNode(3)"""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def to_list(self):
        """Helper to convert ListNode to list."""
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists.

        Args:
            l1: First number as linked list (digits in reverse order)
            l2: Second number as linked list (digits in reverse order)

        Returns:
            Sum as linked list (digits in reverse order)
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values from current nodes (0 if None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
