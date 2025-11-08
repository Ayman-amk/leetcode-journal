#include <unordered_map>
#include <vector>

using namespace std;

/**
 * @brief 1. Two Sum
 * Given an array of integers nums and an integer target,
 * return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution.
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */
class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen;  // value -> index

    for (size_t i = 0; i < nums.size(); ++i) {
      int complement = target - nums[i];
      if (seen.find(complement) != seen.end()) {
        return {seen[complement], static_cast<int>(i)};
      }
      seen[nums[i]] = static_cast<int>(i);
    }
    return {};
  }
};
