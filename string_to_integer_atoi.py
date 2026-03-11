"""
LeetCode Submission: String to Integer (atoi)
Link: https://leetcode.com/problems/string-to-integer-atoi/

Problem:
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

Algorithm:
1. Ignore leading whitespace
2. Check for sign ('-' or '+')
3. Read digits until non-digit character
4. Clamp result to 32-bit signed range [-2^31, 2^31 - 1]
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        
        # Skip leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Handle empty string or only whitespace
        if i == len(s):
            return 0
        
        # Check for sign
        sign = 1
        if s[i] in ['-', '+']:
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Read digits
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        # Apply sign
        result = sign * result
        
        # Clamp to 32-bit signed integer range
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   # 2147483647
        
        return max(INT_MIN, min(INT_MAX, result))