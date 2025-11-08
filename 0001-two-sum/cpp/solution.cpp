#include <vector>
#include <unordered_map>
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
        unordered_map<int, int> seen; // value -> index

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (seen.find(complement) != seen.end()) {
                return { seen[complement], i };
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
