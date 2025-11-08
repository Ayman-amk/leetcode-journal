"""Test cases for Longest Substring Without Repeating Characters problem."""

from solution import Solution


def test_example_1():
    """Test case from LeetCode: 'abcabcbb' -> 3."""
    solver = Solution()
    assert solver.lengthOfLongestSubstring("abcabcbb") == 3


def test_example_2():
    """Test case from LeetCode: 'bbbbb' -> 1."""
    solver = Solution()
    assert solver.lengthOfLongestSubstring("bbbbb") == 1


def test_example_3():
    """Test case from LeetCode: 'pwwkew' -> 3."""
    solver = Solution()
    assert solver.lengthOfLongestSubstring("pwwkew") == 3


def test_empty_string():
    """Test with empty string."""
    solver = Solution()
    assert solver.lengthOfLongestSubstring("") == 0


def test_single_character():
    """Test with single character."""
    solver = Solution()
    assert solver.lengthOfLongestSubstring("a") == 1


def test_all_unique():
    """Test with all unique characters."""
    solver = Solution()
    assert solver.lengthOfLongestSubstring("abcdef") == 6


def test_repeating_at_end():
    """Test where longest substring is at the beginning."""
    solver = Solution()
    assert solver.lengthOfLongestSubstring("dvdf") == 3


def test_all():
    """Run all test cases."""
    test_example_1()
    test_example_2()
    test_example_3()
    test_empty_string()
    test_single_character()
    test_all_unique()
    test_repeating_at_end()
    print("All Python tests passed for Longest Substring Without Repeating Characters.")


if __name__ == "__main__":
    test_all()
