class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        """
        Find two numbers in the list that add up to target.
        
        Args:
            nums   : List of integers
            target : The target sum

        Returns:
            List of two indexes [i, j] where nums[i] + nums[j] == target
            None if no solution exists

        Example:
            >>> Solution().twoSum([2, 7, 11, 15], 9)
            [0, 1]
        """
        # edge case — need at least 2 numbers
        if not nums or len(nums) < 2:
            print("Error: Need at least 2 numbers ❌")
            return None

        hashMap = {}

        for i, num in enumerate(nums):
            required = target - num
            if required in hashMap:
                return [hashMap[required], i]
            hashMap[num] = i

        return None  # no solution found


if __name__ == "__main__":
    sol = Solution()

    nums   = list(map(int, input("Enter numbers : ").split()))
    target = int(input("Enter target  : "))

    result = sol.twoSum(nums, target)

    if result:
        print(f"Indexes  → {result}")
        print(f"Solution → {nums[result[0]]} + {nums[result[1]]} = {target} ✅")
    else:
        print("No solution found ❌")