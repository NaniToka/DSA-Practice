# ============================================================
# LeetCode #3 - Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: String, Sliding Window, HashMap
# Time Complexity:  O(n)
# Space Complexity: O(n)
# ============================================================

class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index = {}  # stores last seen index of each character
        max_length = 0
        left       = 0  # left pointer of sliding window

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1  # move left past the duplicate

            char_index[char] = right                    # update last seen index
            max_length = max(max_length, right - left + 1)  # update max length

        return max_length