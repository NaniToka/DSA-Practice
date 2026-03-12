class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Regular Expression Matching
        LeetCode #10 | Hard
        
        Match string s with pattern p supporting '.' and '*'
        """
        m, n = len(s), len(p)
        
        # dp[i][j] = whether s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, etc. matching empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can match zero or more of preceding element
                    zero_match = dp[i][j - 2]
                    one_or_more = dp[i - 1][j] and (
                        p[j - 2] == '.' or p[j - 2] == s[i - 1]
                    )
                    dp[i][j] = zero_match or one_or_more
                else:
                    # Regular character or '.'
                    char_match = p[j - 1] == '.' or p[j - 1] == s[i - 1]
                    dp[i][j] = char_match and dp[i - 1][j - 1]
        
        return dp[m][n]