"""
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Modern Python 3.11+ Implementation:
- Modern type hints with | operator
- Pattern matching for even/odd logic
- Concise and pythonic code
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays using binary search partition.
        
        Time Complexity: O(log(min(m, n)))
        Space Complexity: O(1)
        
        Algorithm: Binary search to find correct partition where:
        - Left partition size = (m + n + 1) // 2
        - All left elements <= all right elements
        """
        # Ensure nums1 is smaller for optimization
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right1 = float('inf') if partition1 == m else nums1[partition1]
            
            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == n else nums2[partition2]
            
            if left1 <= right2 and left2 <= right1:
                # Pattern matching for even/odd (Python 3.10+)
                match (m + n) % 2:
                    case 0:
                        return (max(left1, left2) + min(right1, right2)) / 2.0
                    case _:
                        return float(max(left1, left2))
            
            if left1 > right2:
                high = partition1 - 1
            else:
                low = partition1 + 1
        
        return -1.0