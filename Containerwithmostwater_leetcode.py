class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Container With Most Water
        LeetCode #11 | Medium
        
        Find two lines that form container with max water area.
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update maximum
            max_area = max(max_area, current_area)
            
            # Move pointer with smaller height (greedy approach)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area