"""
Median of Two Sorted Arrays - Latest Python 3.11+ Implementation
Problem: Find the median of two sorted arrays with O(log(m+n)) time complexity

Modern Features:
- Type hints with modern Union syntax (|)
- Dataclass for test cases
- Pattern matching (match-case)
- F-string formatting
- Proper error handling
"""

from dataclasses import dataclass
from typing import Never


@dataclass
class TestCase:
    """Represents a test case for median calculation."""
    nums1: list[int]
    nums2: list[int]
    expected: float
    description: str


class MedianFinder:
    """Efficient median finder for two sorted arrays using binary search."""
    
    @staticmethod
    def find_median(nums1: list[int], nums2: list[int]) -> float:
        """
        Find the median of two sorted arrays.
        
        Uses binary search partition algorithm to achieve O(log(min(m,n))) complexity.
        
        Args:
            nums1: First sorted array
            nums2: Second sorted array
        
        Returns:
            The median value as a float
        
        Raises:
            ValueError: If both arrays are empty
        
        Time Complexity: O(log(min(m, n)))
        Space Complexity: O(1)
        
        Example:
            >>> MedianFinder.find_median([1, 3], [2])
            2.0
            >>> MedianFinder.find_median([1, 2], [3, 4])
            2.5
        """
        if not nums1 and not nums2:
            raise ValueError("At least one array must be non-empty")
        
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            return MedianFinder.find_median(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Get boundary values with proper defaults
            left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right1 = float('inf') if partition1 == m else nums1[partition1]
            
            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if valid partition found
            if left1 <= right2 and left2 <= right1:
                total_len = m + n
                match total_len % 2:
                    case 0:  # Even length
                        return (max(left1, left2) + min(right1, right2)) / 2.0
                    case _:  # Odd length
                        return float(max(left1, left2))
            
            # Adjust binary search bounds
            if left1 > right2:
                high = partition1 - 1
            else:
                low = partition1 + 1
        
        return -1.0  # Should never reach here


def run_tests() -> None:
    """Run comprehensive test suite with modern formatting."""
    
    test_cases = [
        TestCase([1, 3], [2], 2.0, "Example 1: Simple merge"),
        TestCase([1, 2], [3, 4], 2.5, "Example 2: Larger arrays"),
        TestCase([], [1], 1.0, "Edge case: Empty first array"),
        TestCase([1], [], 1.0, "Edge case: Empty second array"),
        TestCase([0, 0], [0, 0], 0.0, "Edge case: All zeros"),
        TestCase([-2, -1], [3], -1.0, "Edge case: Negative numbers"),
        TestCase([2], [1, 3, 4], 2.5, "Edge case: First array smaller"),
        TestCase([1, 3, 5, 7], [2, 4, 6, 8], 4.5, "Even total length"),
        TestCase([1, 3, 5], [2, 4, 6], 3.5, "Odd total length"),
    ]
    
    print("=" * 70)
    print("MEDIAN OF TWO SORTED ARRAYS - TEST SUITE".center(70))
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        try:
            result = MedianFinder.find_median(test.nums1, test.nums2)
            status = "✓ PASS" if abs(result - test.expected) < 1e-5 else "✗ FAIL"
            
            if "PASS" in status:
                passed += 1
            else:
                failed += 1
            
            print(f"\nTest {i}: {test.description}")
            print(f"  Input:    nums1={test.nums1}, nums2={test.nums2}")
            print(f"  Expected: {test.expected}")
            print(f"  Got:      {result}")
            print(f"  Status:   {status}")
            
        except Exception as e:
            failed += 1
            print(f"\nTest {i}: {test.description}")
            print(f"  Status:   ✗ ERROR - {e}")
    
    print("\n" + "=" * 70)
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()