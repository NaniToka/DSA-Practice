# ============================================================
# Longest Substring Without Repeating Characters
# Full Runnable Solution
# ============================================================
# Problem:
#   Given a string s, find the length of the longest substring
#   without duplicate characters.
#
# Example:
#   Input:  s = "abcabcbb"
#   Output: 3  ("abc")
# ============================================================


def lengthOfLongestSubstring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.

    Args:
        s (str): Input string

    Returns:
        int: Length of the longest substring without duplicates
    """
    char_index = {}  # stores last seen index of each character
    max_length = 0
    left       = 0  # left pointer of sliding window

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1  # move left past the duplicate

        char_index[char] = right                         # update last seen index
        max_length = max(max_length, right - left + 1)  # update max length

    return max_length


# ── Test cases ───────────────────────────────────────────────

def run_tests():
    test_cases = [
        {
            "description": "Basic case",
            "input":       "abcabcbb",
            "expected":    3,
        },
        {
            "description": "All same characters",
            "input":       "bbbbb",
            "expected":    1,
        },
        {
            "description": "Mixed case",
            "input":       "pwwkew",
            "expected":    3,
        },
        {
            "description": "Empty string",
            "input":       "",
            "expected":    0,
        },
        {
            "description": "All unique characters",
            "input":       "abcdef",
            "expected":    6,
        },
        {
            "description": "Single character",
            "input":       "a",
            "expected":    1,
        },
    ]

    all_passed = True

    for i, test in enumerate(test_cases, 1):
        result = lengthOfLongestSubstring(test["input"])
        passed = result == test["expected"]

        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"Test {i}: {status} | {test['description']}")

        if not passed:
            print(f"         Expected: {test['expected']}")
            print(f"         Got:      {result}")
            all_passed = False

    print()
    print("All tests passed! 🎉" if all_passed else "Some tests failed. 😬")


if __name__ == "__main__":
    run_tests()