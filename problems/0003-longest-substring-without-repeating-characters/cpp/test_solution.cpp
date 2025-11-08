#include <cassert>
#include <iostream>
#include <string>

#include "solution.cpp"

using namespace std;

void test_example_1() {
  Solution solver;
  assert(solver.lengthOfLongestSubstring("abcabcbb") == 3 &&
         "Test 1 failed: 'abcabcbb' should return 3");
  cout << "Test 1 passed: 'abcabcbb' -> 3\n";
}

void test_example_2() {
  Solution solver;
  assert(solver.lengthOfLongestSubstring("bbbbb") == 1 &&
         "Test 2 failed: 'bbbbb' should return 1");
  cout << "Test 2 passed: 'bbbbb' -> 1\n";
}

void test_example_3() {
  Solution solver;
  assert(solver.lengthOfLongestSubstring("pwwkew") == 3 &&
         "Test 3 failed: 'pwwkew' should return 3");
  cout << "Test 3 passed: 'pwwkew' -> 3\n";
}

void test_empty_string() {
  Solution solver;
  assert(solver.lengthOfLongestSubstring("") == 0 &&
         "Test 4 failed: empty string should return 0");
  cout << "Test 4 passed: empty string -> 0\n";
}

void test_single_character() {
  Solution solver;
  assert(solver.lengthOfLongestSubstring("a") == 1 &&
         "Test 5 failed: single character should return 1");
  cout << "Test 5 passed: single character -> 1\n";
}

void test_all_unique() {
  Solution solver;
  assert(solver.lengthOfLongestSubstring("abcdef") == 6 &&
         "Test 6 failed: all unique should return 6");
  cout << "Test 6 passed: all unique -> 6\n";
}

void test_repeating_at_end() {
  Solution solver;
  assert(solver.lengthOfLongestSubstring("dvdf") == 3 &&
         "Test 7 failed: 'dvdf' should return 3");
  cout << "Test 7 passed: 'dvdf' -> 3\n";
}

int main() {
  test_example_1();
  test_example_2();
  test_example_3();
  test_empty_string();
  test_single_character();
  test_all_unique();
  test_repeating_at_end();

  cout << "All C++ tests passed for Longest Substring Without Repeating Characters!\n";
  return 0;
}
