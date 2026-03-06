# ============================================================
#  LeetCode #1929 — Concatenation of Array
#  Difficulty : Easy
#  Approach   : Linear scan — O(n) time, O(n) space
# ============================================================

class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        Return a concatenation of nums with itself.

        Args:
            nums : List of integers

        Returns:
            A new list of length 2n where ans[i] == ans[i+n] == nums[i]

        Example:
            >>> Solution().getConcatenation([1, 2, 3])
            [1, 2, 3, 1, 2, 3]
        """
        if not nums:
            return []

        ans = []

        for i in range(len(nums)):
            ans.append(nums[i])

        for i in range(len(nums)):
            ans.append(nums[i])

        return ans


if __name__ == "__main__":
    sol = Solution()

    nums   = list(map(int, input("Enter numbers : ").split()))
    result = sol.getConcatenation(nums)

    print(f"Input  → {nums}")
    print(f"Output → {result} ✅")

"""

**Expected Output 📟**
```
Enter numbers : 1 2 3
Input  → [1, 2, 3]
Output → [1, 2, 3, 1, 2, 3] ✅

"""