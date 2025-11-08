#include <cassert>
#include <iostream>
#include <vector>

#include "solution.cpp"

using namespace std;

int main() {
  Solution solver;

  vector<int> nums1 = {2, 7, 11, 15};
  vector<int> res1 = solver.twoSum(nums1, 9);
  assert((res1 == vector<int>{0, 1}));

  vector<int> nums2 = {3, 2, 4};
  vector<int> res2 = solver.twoSum(nums2, 6);
  assert((res2 == vector<int>{1, 2}));

  vector<int> nums3 = {3, 3};
  vector<int> res3 = solver.twoSum(nums3, 6);
  assert((res3 == vector<int>{0, 1}));

  cout << "All C++ tests passed for Two Sum!\n";
  return 0;
}
