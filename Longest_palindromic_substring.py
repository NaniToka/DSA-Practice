"""
5. Longest Palindromic Substring - Python 3.11+ Implementation
Medium Level

Given a string s, return the longest palindromic substring in s.

Modern Features:
- Type hints with modern syntax
- Dataclass for test cases
- Pattern matching
- F-string formatting
- Expand around center approach: O(n²) time, O(1) space
"""

from dataclasses import dataclass


@dataclass
class TestCase:
    """Represents a test case for palindrome finding."""
    input_str: str
    description: str


class PalindromeHelper:
    """Helper class for finding longest palindromic substring."""
    
    @staticmethod
    def expand_around_center(s: str, left: int, right: int) -> str:
        """
        Expand around center to find palindrome.
        
        Args:
            s: Input string
            left: Left pointer
            right: Right pointer
        
        Returns:
            The palindromic substring found
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left + 1:right]


class Solution:
    """LeetCode Solution for Longest Palindromic Substring."""
    
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring using expand around center.
        
        Algorithm:
        - For each character (and between characters), expand outward
        - Check for both odd-length palindromes (single center)
        - And even-length palindromes (two character center)
        - Track the longest found
        
        Args:
            s: Input string (1 <= length <= 1000)
        
        Returns:
            The longest palindromic substring
        
        Time Complexity: O(n²) - For each of n centers, we expand O(n) times
        Space Complexity: O(1) - Only using pointers, no extra data structures
        
        Example:
            >>> solution = Solution()
            >>> solution.longestPalindrome("babad")
            'bab'
            >>> solution.longestPalindrome("cbbd")
            'bb'
        """
        if not s or len(s) < 2:
            return s
        
        longest = ""
        
        for i in range(len(s)):
            # Check for odd-length palindromes (single character center)
            palindrome1 = self._expand_around_center(s, i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1
            
            # Check for even-length palindromes (two character center)
            palindrome2 = self._expand_around_center(s, i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2
        
        return longest
    
    @staticmethod
    def _expand_around_center(s: str, left: int, right: int) -> str:
        """
        Expand around center to find palindrome.
        
        Args:
            s: Input string
            left: Left pointer
            right: Right pointer
        
        Returns:
            The palindromic substring found by expanding from center
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left + 1:right]


def run_tests() -> None:
    """Run comprehensive test suite."""
    
    test_cases = [
        TestCase("babad", "Example 1: Multiple palindromes possible"),
        TestCase("cbbd", "Example 2: Even-length palindrome"),
        TestCase("a", "Edge case: Single character"),
        TestCase("ab", "Edge case: No palindrome > 1"),
        TestCase("racecar", "Single odd-length palindrome"),
        TestCase("aabbaa", "Even-length palindrome"),
        TestCase("abcdefg", "No palindromes > 1"),
        TestCase("abacabad", "Multiple overlapping palindromes"),
        TestCase("zzz", "All same characters"),
        TestCase("abba", "Perfect even palindrome"),
        TestCase("aba", "Perfect odd palindrome"),
        TestCase("abaxyzzyx", "Mixed palindromes"),
    ]
    
    solution = Solution()
    
    print("=" * 80)
    print("LONGEST PALINDROMIC SUBSTRING - TEST SUITE".center(80))
    print("=" * 80)
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        try:
            result = solution.longestPalindrome(test.input_str)
            
            # Verify result is actually a palindrome
            is_palindrome = result == result[::-1]
            
            # Check if we found a palindrome that exists in original string
            found_in_string = result in test.input_str
            
            status = "✓ PASS" if (is_palindrome and found_in_string) else "✗ FAIL"
            
            if "PASS" in status:
                passed += 1
            else:
                failed += 1
            
            print(f"\nTest {i}: {test.description}")
            print(f"  Input:      '{test.input_str}'")
            print(f"  Output:     '{result}'")
            print(f"  Palindrome: {is_palindrome}")
            print(f"  In String:  {found_in_string}")
            print(f"  Status:     {status}")
            
        except Exception as e:
            failed += 1
            print(f"\nTest {i}: {test.description}")
            print(f"  Input:  '{test.input_str}'")
            print(f"  Status: ✗ ERROR - {e}")
    
    print("\n" + "=" * 80)
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 80)
    
    # Complexity analysis
    print("\n" + "ALGORITHM ANALYSIS".center(80))
    print("=" * 80)
    print("Approach: Expand Around Center")
    print("Time Complexity:  O(n²) - For each of n centers, expand O(n) times")
    print("Space Complexity: O(1)  - Only pointers, no extra data structures")
    print("=" * 80)


if __name__ == "__main__":
    run_tests()