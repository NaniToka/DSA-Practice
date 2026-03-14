class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Longest Common Prefix
        LeetCode #14 | Easy
        
        Find the longest common prefix string amongst an array of strings.
        Uses vertical scanning - compare character by character at each position.
        """
        if not strs:
            return ""
        
        # Find minimum length to avoid index out of bounds
        min_len = min(len(s) for s in strs)
        
        # Compare character by character at each position (vertical scan)
        for i in range(min_len):
            # Get character at position i from first string
            char = strs[0][i]
            
            # Compare with character at position i in all other strings
            for j in range(1, len(strs)):
                # If character doesn't match or position exceeds string length
                if strs[j][i] != char:
                    return strs[0][:i]
        
        # All characters up to min_len matched
        return strs[0][:min_len]