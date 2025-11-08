"""LeetCode Problem 1: Two Sum solution."""

from typing import List


class Solution:
    """Solution class for Two Sum problem."""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers that add up to target.

        Args:
            nums: List of integers.
            target: Target sum.

        Returns:
            List of two indices whose values sum to target.
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
