class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        3Sum Closest
        LeetCode #16 | Medium
        
        Find three integers whose sum is closest to target.
        Uses two-pointer approach after sorting.
        
        Time: O(n^2)
        Space: O(1) excluding output
        """
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        min_diff = abs(closest_sum - target)
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)
                
                # Update closest sum if current is closer
                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum
                
                # Early termination - exact match found
                if current_sum == target:
                    return current_sum
                
                # Move pointers to get closer to target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum