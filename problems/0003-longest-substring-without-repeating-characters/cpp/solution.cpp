#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

/**
 * @brief 3. Longest Substring Without Repeating Characters
 * Given a string s, find the length of the longest substring without
 * repeating characters.
 *
 * Time Complexity:  O(n) where n is the length of the string
 * Space Complexity: O(min(n, m)) where m is the size of the charset
 */
class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    if (s.empty()) {
      return 0;
    }

    unordered_map<char, int> char_index;  // Maps character to last seen index
    int max_length = 0;
    int start = 0;  // Start of current window

    for (size_t end = 0; end < s.length(); ++end) {
      char current_char = s[end];

      // If character seen before and within current window, move start
      if (char_index.find(current_char) != char_index.end() &&
          char_index[current_char] >= start) {
        start = char_index[current_char] + 1;
      }

      // Update character's last seen index
      char_index[current_char] = static_cast<int>(end);

      // Update max length
      max_length = max(max_length, static_cast<int>(end) - start + 1);
    }

    return max_length;
  }
};
