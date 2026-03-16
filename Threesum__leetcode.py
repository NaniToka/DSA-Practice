class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        3Sum
        LeetCode #15 | Medium
        
        Find all unique triplets that sum to zero.
        Uses two-pointer approach after sorting.
        
        Time: O(n^2)
        Space: O(1) excluding output
        """
        nums.sort()
        result = []
        n = len(nums)
        
        # Early termination - if all positive, no solution
        if n < 3 or nums[-1] < 0:
            return []
        
        for i in range(n - 2):
            # If first number is positive, can't sum to 0
            if nums[i] > 0:
                break
            
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers for remaining elements
            left = i + 1
            right = n - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    # Found valid triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers
                    left += 1
                    right -= 1
                
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result