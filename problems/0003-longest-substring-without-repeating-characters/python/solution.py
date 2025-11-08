"""LeetCode Problem 3: Longest Substring Without Repeating Characters solution."""


class Solution:
    """Solution class for Longest Substring Without Repeating Characters."""

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Uses sliding window technique with hash map to track character positions.

        Args:
            s: Input string.

        Returns:
            Length of longest substring without repeating characters.
        """
        if not s:
            return 0

        char_index = {}  # Maps character to its last seen index
        max_length = 0
        start = 0  # Start of current window

        for end, char in enumerate(s):
            # If character seen before and within current window, move start
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1

            # Update character's last seen index
            char_index[char] = end

            # Update max length
            max_length = max(max_length, end - start + 1)

        return max_length
