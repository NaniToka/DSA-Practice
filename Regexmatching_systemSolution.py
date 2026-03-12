#!/usr/bin/env python3

"""
Problem #10: Regular Expression Matching
Difficulty: Hard
Topics: Dynamic Programming, String Matching, Recursion
Time: O(m*n) | Space: O(m*n)

Given a string s and pattern p with support for '.' and '*', 
implement regular expression matching.
- '.' matches any single character
- '*' matches zero or more of preceding element

Approach: Dynamic Programming (Bottom-up)
"""

from typing import List

class Solution:
    """Regular Expression Matching using DP"""
    
    # ===============================================
    # SOLUTION 1: Dynamic Programming (Optimal)
    # ===============================================
    def isMatch_dp(self, s: str, p: str) -> bool:
        """
        DP approach: Build table from bottom-up
        dp[i][j] = whether s[0:i] matches p[0:j]
        
        Time: O(m*n) where m=len(s), n=len(p)
        Space: O(m*n) for DP table
        """
        m, n = len(s), len(p)
        
        # Create DP table
        # dp[i][j] = s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, etc.
        # Empty string can match pattern with *
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' matches zero or more of preceding element
                    # Zero match: dp[i][j-2]
                    # One or more match: dp[i-1][j] and (p[j-2] matches s[i-1])
                    zero_match = dp[i][j - 2]
                    one_or_more = dp[i - 1][j] and (p[j - 2] == '.' or p[j - 2] == s[i - 1])
                    dp[i][j] = zero_match or one_or_more
                else:
                    # Current characters must match
                    char_match = p[j - 1] == '.' or p[j - 1] == s[i - 1]
                    dp[i][j] = char_match and dp[i - 1][j - 1]
        
        return dp[m][n]
    
    
    # ===============================================
    # SOLUTION 2: Memoized Recursion
    # ===============================================
    def isMatch_memo(self, s: str, p: str) -> bool:
        """
        Recursion with memoization (Top-down DP)
        
        Time: O(m*n)
        Space: O(m*n) for memo
        """
        memo = {}
        
        def match(i: int, j: int) -> bool:
            """
            Recursively check if s[i:] matches p[j:]
            i: index in string s
            j: index in pattern p
            """
            # Base cases
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Both exhausted - match
            if j == len(p):
                return i == len(s)
            
            # Check if current characters match
            first_match = i < len(s) and (p[j] == '.' or p[j] == s[i])
            
            # Handle '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two options:
                # 1. Skip pattern (zero match): match(i, j+2)
                # 2. Match current and stay (one or more): match(i+1, j)
                result = (
                    match(i, j + 2) or  # Zero match
                    (first_match and match(i + 1, j))  # One or more match
                )
            else:
                # No '*', must match and move both pointers
                result = first_match and match(i + 1, j + 1)
            
            memo[(i, j)] = result
            return result
        
        return match(0, 0)
    
    
    # ===============================================
    # SOLUTION 3: Brute Force Recursion (Educational)
    # ===============================================
    def isMatch_bruteforce(self, s: str, p: str) -> bool:
        """
        Pure recursion without memoization
        Shows the logic clearly but inefficient for large inputs
        
        Time: O(exponential) - many repeated subproblems
        Space: O(m+n) - recursion depth
        """
        # Base cases
        if not p:  # Pattern exhausted
            return not s  # String must also be exhausted
        
        # Check if first characters match
        first_match = bool(s) and (p[0] == '.' or p[0] == s[0])
        
        # Handle '*'
        if len(p) >= 2 and p[1] == '*':
            # Two options:
            # 1. Skip pattern: match rest of string with pattern[2:]
            # 2. Use '*' to match one char: match s[1:] with pattern
            return (
                self.isMatch_bruteforce(s, p[2:]) or  # Zero match
                (first_match and self.isMatch_bruteforce(s[1:], p))  # One or more
            )
        else:
            # No '*': must match current and continue
            return first_match and self.isMatch_bruteforce(s[1:], p[1:])


# ===============================================
# TEST CASES
# ===============================================

def run_tests():
    """Run comprehensive test suite"""
    solution = Solution()
    
    test_cases = [
        # (string, pattern, expected)
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", "", True),
        ("a", "a", True),
        ("a", ".", True),
        ("a", ".*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", ".*", True),
        ("aab", "a*b", True),
        ("a", "ab", False),
        ("a", "a*", True),
        ("", "a", False),
        ("", "a*", True),
        ("abc", ".*", True),
        ("aa", "a*a", True),
        ("ba", ".*..a*", True),
        ("aaa", "a.a", True),
        ("aaaa", "***a", False),
    ]
    
    print("=" * 70)
    print("REGULAR EXPRESSION MATCHING - TEST SUITE")
    print("=" * 70 + "\n")
    
    passed = 0
    failed = 0
    
    for s, p, expected in test_cases:
        result_dp = solution.isMatch_dp(s, p)
        result_memo = solution.isMatch_memo(s, p)
        result_brute = solution.isMatch_bruteforce(s, p)
        
        all_correct = (result_dp == expected and 
                      result_memo == expected and 
                      result_brute == expected)
        
        status = "✅ PASS" if all_correct else "❌ FAIL"
        if all_correct:
            passed += 1
        else:
            failed += 1
        
        print(f"String: '{s}' | Pattern: '{p}'")
        print(f"Expected: {expected}")
        print(f"DP:       {result_dp} {'✓' if result_dp == expected else '✗'}")
        print(f"Memo:     {result_memo} {'✓' if result_memo == expected else '✗'}")
        print(f"Brute:    {result_brute} {'✓' if result_brute == expected else '✗'}")
        print(f"Status:   {status}\n")
    
    print("=" * 70)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(test_cases)}")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()