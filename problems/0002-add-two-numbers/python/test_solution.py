from solution import Solution, ListNode


def test_example_1():
    """Test case from LeetCode: [2,4,3] + [5,6,4] = [7,0,8]"""
    solver = Solution()
    l1 = ListNode.from_list([2, 4, 3])
    l2 = ListNode.from_list([5, 6, 4])
    result = solver.addTwoNumbers(l1, l2)
    expected = ListNode.from_list([7, 0, 8])
    assert (
        result == expected
    ), f"Expected [7,0,8], got {result.to_list() if result else None}"


def test_example_2():
    """Test case from LeetCode: [0] + [0] = [0]"""
    solver = Solution()
    l1 = ListNode.from_list([0])
    l2 = ListNode.from_list([0])
    result = solver.addTwoNumbers(l1, l2)
    expected = ListNode.from_list([0])
    assert (
        result == expected
    ), f"Expected [0], got {result.to_list() if result else None}"


def test_example_3():
    """Test case from LeetCode: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]"""
    solver = Solution()
    l1 = ListNode.from_list([9, 9, 9, 9, 9, 9, 9])
    l2 = ListNode.from_list([9, 9, 9, 9])
    result = solver.addTwoNumbers(l1, l2)
    expected = ListNode.from_list([8, 9, 9, 9, 0, 0, 0, 1])
    assert (
        result == expected
    ), f"Expected [8,9,9,9,0,0,0,1], got {result.to_list() if result else None}"


def test_different_lengths():
    """Test with lists of different lengths"""
    solver = Solution()
    l1 = ListNode.from_list([1, 8])
    l2 = ListNode.from_list([0])
    result = solver.addTwoNumbers(l1, l2)
    expected = ListNode.from_list([1, 8])
    assert (
        result == expected
    ), f"Expected [1,8], got {result.to_list() if result else None}"


def test_carry_over():
    """Test carry-over scenarios"""
    solver = Solution()
    l1 = ListNode.from_list([5])
    l2 = ListNode.from_list([5])
    result = solver.addTwoNumbers(l1, l2)
    expected = ListNode.from_list([0, 1])
    assert (
        result == expected
    ), f"Expected [0,1], got {result.to_list() if result else None}"


def test_all():
    test_example_1()
    test_example_2()
    test_example_3()
    test_different_lengths()
    test_carry_over()
    print("All Python tests passed for Add Two Numbers.")


if __name__ == "__main__":
    test_all()
