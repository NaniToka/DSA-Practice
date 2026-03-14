#!/usr/bin/env python3

"""
Problem #14: Longest Common Prefix
Difficulty: Easy
Topics: String, Trie
Time: O(n*m) | Space: O(1)

Find the longest common prefix string amongst an array of strings.
Uses horizontal/vertical scanning approaches for optimal solution.

Approach: Character-by-character vertical scanning
Compare characters at same position across all strings.
"""

class Solution:
    """Longest Common Prefix using multiple approaches"""
    
    # ===============================================
    # SOLUTION 1: Vertical Scanning (Optimal)
    # ===============================================
    def longestCommonPrefix_vertical(self, strs: list[str]) -> str:
        """
        Vertical scanning: Compare character by character at each position.
        
        Algorithm:
        1. For each character position (starting from 0)
        2. Compare that character across all strings
        3. If any mismatch or position exceeds string length: stop
        4. Otherwise, add character to result
        
        Time: O(n*m) where n=number of strings, m=length of shortest string
        Space: O(1) - only using result string
        
        Best when: Short prefix or quick mismatch
        """
        if not strs:
            return ""
        
        # Find minimum length to avoid index out of bounds
        min_len = min(len(s) for s in strs)
        
        # Compare character by character at each position
        for i in range(min_len):
            # Get character at position i from first string
            char = strs[0][i]
            
            # Compare with character at position i in all other strings
            for j in range(1, len(strs)):
                # If character doesn't match or position exceeds string length
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        
        # All characters up to min_len matched
        return strs[0][:min_len]
    
    
    # ===============================================
    # SOLUTION 2: Horizontal Scanning
    # ===============================================
    def longestCommonPrefix_horizontal(self, strs: list[str]) -> str:
        """
        Horizontal scanning: Compare strings one by one.
        
        Algorithm:
        1. Start with first string as prefix
        2. For each subsequent string:
           - Trim prefix until it matches the start of current string
        3. Stop when prefix becomes empty or all strings processed
        
        Time: O(n*m) where n=number of strings, m=length of shortest string
        Space: O(1) - using prefix string
        
        Best when: First string is very short
        """
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare with each subsequent string
        for i in range(1, len(strs)):
            # Keep removing characters from end of prefix until it matches
            while not strs[i].startswith(prefix):
                # Remove last character from prefix
                prefix = prefix[:-1]
                
                # If prefix becomes empty, no common prefix
                if not prefix:
                    return ""
        
        return prefix
    
    
    # ===============================================
    # SOLUTION 3: Binary Search on Prefix Length
    # ===============================================
    def longestCommonPrefix_binarySearch(self, strs: list[str]) -> str:
        """
        Binary search on prefix length.
        
        Algorithm:
        1. Find minimum length (max possible prefix length)
        2. Binary search on prefix length
        3. For each length, check if all strings have that prefix in common
        4. Find maximum length where common prefix exists
        
        Time: O(n*m*log(m)) where n=strings, m=min string length
        Space: O(1)
        
        Best when: Need to minimize string comparisons
        """
        if not strs:
            return ""
        
        def is_common_prefix(length: int) -> bool:
            """Check if first 'length' characters are common prefix"""
            prefix = strs[0][:length]
            for s in strs[1:]:
                if not s.startswith(prefix):
                    return False
            return True
        
        # Binary search on prefix length
        min_len = min(len(s) for s in strs)
        left, right = 0, min_len
        
        while left <= right:
            mid = (left + right) // 2
            if is_common_prefix(mid):
                # Prefix of length mid exists, try longer
                left = mid + 1
            else:
                # Prefix of length mid doesn't exist, try shorter
                right = mid - 1
        
        # right is the longest valid prefix length
        return strs[0][:right]
    
    
    # ===============================================
    # SOLUTION 4: Trie-Based Approach
    # ===============================================
    def longestCommonPrefix_trie(self, strs: list[str]) -> str:
        """
        Build a trie and find common path.
        
        Algorithm:
        1. Insert all strings into a trie
        2. Traverse the trie from root
        3. Stop when a node has more than one child (path diverges)
        4. Return the path traversed
        
        Time: O(n*m) where n=strings, m=length of shortest string
        Space: O(n*m) for trie storage
        
        Best for: Multiple queries on same set of strings
        """
        if not strs:
            return ""
        
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.count = 0  # Number of strings passing through this node
        
        root = TrieNode()
        
        # Insert all strings into trie
        for s in strs:
            node = root
            for char in s:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.count += 1
        
        # Traverse trie and build prefix
        result = ""
        node = root
        
        while node.children:
            # If only one child and it has all strings count, continue
            if len(node.children) == 1:
                child_char = list(node.children.keys())[0]
                child_node = node.children[child_char]
                # Check if all strings pass through this child
                if child_node.count == len(strs):
                    result += child_char
                    node = child_node
                else:
                    break
            else:
                # More than one child - path diverges
                break
        
        return result


# ===============================================
# TEST CASES
# ===============================================

def run_tests():
    """Run comprehensive test suite"""
    solution = Solution()
    
    test_cases = [
        # (strs, expected)
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["a"], "a"),
        (["ab", "a"], "a"),
        (["abc", "abc", "abc"], "abc"),
        (["", "b"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["a", "a", "a", "a"], "a"),
        (["abab", "aba", "abc"], "ab"),
        (["", ""], ""),
        (["aca", "cba"], ""),
        (["leets", "leetcode", "leet", "leeds"], "lee"),
        (["prefix", "presume", "predict"], "pre"),
        (["mississippi", "mission"], "missi"),
    ]
    
    print("=" * 80)
    print("LONGEST COMMON PREFIX - TEST SUITE")
    print("=" * 80 + "\n")
    
    passed = 0
    failed = 0
    
    for strs, expected in test_cases:
        result_vertical = solution.longestCommonPrefix_vertical(strs)
        result_horizontal = solution.longestCommonPrefix_horizontal(strs)
        result_binarySearch = solution.longestCommonPrefix_binarySearch(strs)
        result_trie = solution.longestCommonPrefix_trie(strs)
        
        all_correct = (result_vertical == expected and 
                      result_horizontal == expected and 
                      result_binarySearch == expected and 
                      result_trie == expected)
        
        status = "✅ PASS" if all_correct else "❌ FAIL"
        if all_correct:
            passed += 1
        else:
            failed += 1
        
        display_strs = str(strs) if len(str(strs)) < 40 else str(strs)[:37] + "..."
        print(f"Input: {display_strs}")
        print(f"Expected: '{expected}'")
        print(f"Vertical:     '{result_vertical}' {'✓' if result_vertical == expected else '✗'}")
        print(f"Horizontal:   '{result_horizontal}' {'✓' if result_horizontal == expected else '✗'}")
        print(f"BinarySearch: '{result_binarySearch}' {'✓' if result_binarySearch == expected else '✗'}")
        print(f"Trie:         '{result_trie}' {'✓' if result_trie == expected else '✗'}")
        print(f"Status: {status}\n")
    
    print("=" * 80)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(test_cases)}")
    print("=" * 80)


# ===============================================
# EXPLANATION & KEY INSIGHTS
# ===============================================

def explain_algorithm():
    """Explain the algorithm"""
    print("\n" + "=" * 80)
    print("ALGORITHM EXPLANATION: Vertical Scanning")
    print("=" * 80 + "\n")
    
    print("Key Insight:")
    print("-" * 80)
    print("""
The problem is about finding the longest common prefix.

Example: ["flower", "flow", "flight"]

Vertical Scanning Approach:
─────────────────────────────────────────

Position 0: Compare f, f, f → All match → Add 'f'
Position 1: Compare l, l, l → All match → Add 'l'
Position 2: Compare o, o, i → MISMATCH! → Stop

Result: "fl" ✓

Why Vertical Scanning Works:
✓ Simple and efficient
✓ Early termination when mismatch found
✓ No need to store prefix separately
✓ O(n*m) time where m can be very small

Step-by-Step Example: ["flower", "flow", "flight"]
──────────────────────────────────────────────────

Initialize:
  prefix = ""
  min_len = 4 (length of "flow")

i=0 (Position 0 - 'f'):
  strs[0][0] = 'f'
  strs[1][0] = 'f' ✓
  strs[2][0] = 'f' ✓
  All match → prefix = "f"

i=1 (Position 1 - 'l'):
  strs[0][1] = 'l'
  strs[1][1] = 'l' ✓
  strs[2][1] = 'l' ✓
  All match → prefix = "fl"

i=2 (Position 2 - 'o'):
  strs[0][2] = 'o'
  strs[1][2] = 'o' ✓
  strs[2][2] = 'i' ✗
  MISMATCH! → Return "fl"

Final Result: "fl" ✅

Complexity Analysis:
──────────────────
Time: O(n*m)
  where n = number of strings
  where m = length of shortest string
  In best case (early mismatch): O(n)
  In worst case (full match): O(n*m)

Space: O(1)
  Only using the result string
  No extra data structures

Comparison of All 4 Approaches:
───────────────────────────────

Vertical Scanning:
  ✓ Best for most cases
  ✓ Early termination on mismatch
  ✓ O(n*m) time, O(1) space

Horizontal Scanning:
  ✓ Good when first string is short
  ✓ O(n*m) time, O(1) space
  ✗ Slower for large first string

Binary Search:
  ✓ O(n*m*log(m)) time
  ✗ More complex logic
  - Better for very specific use cases

Trie:
  ✓ Good for multiple queries
  ✓ Easy to visualize
  ✗ O(n*m) space for trie

Edge Cases Handled:
──────────────────
✓ Empty array → ""
✓ Single string → Return that string
✓ One empty string → ""
✓ All identical strings → Return string
✓ No common prefix → ""
✓ Single character strings → ""
    """)
    print("-" * 80)


if __name__ == "__main__":
    run_tests()
    explain_algorithm()