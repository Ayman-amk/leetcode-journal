"""Test cases for Two Sum problem."""

from solution import Solution


def test_two_sum():
    """Test the twoSum method with various inputs."""
    solver = Solution()
    assert solver.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solver.twoSum([3, 2, 4], 6) == [1, 2]
    assert solver.twoSum([3, 3], 6) == [0, 1]
    print("All Python tests passed for Two Sum.")


if __name__ == "__main__":
    test_two_sum()
