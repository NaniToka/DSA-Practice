#!/usr/bin/env python3

"""
Problem #11: Container With Most Water
Difficulty: Medium
Topics: Array, Two Pointer, Greedy
Time: O(n) | Space: O(1)

Given array of heights, find two lines that form a container 
with maximum water capacity.
Area = min(height[i], height[j]) * (j - i)

Approach: Two Pointer (Greedy)
Start from both ends and move inward, always moving the pointer
pointing to the smaller height to try to find a larger area.
"""

from typing import List

class Solution:
    """Container With Most Water using Two Pointer"""
    
    # ===============================================
    # SOLUTION 1: Two Pointer (Optimal)
    # ===============================================
    def maxArea_twoPointer(self, height: List[int]) -> int:
        """
        Two pointer approach from both ends moving inward.
        
        Logic:
        - Start with widest possible container
        - Area = min(height[left], height[right]) * (right - left)
        - Always move the pointer with smaller height
        - This is greedy: moving the taller pointer can't help
          because the limiting factor is the shorter height
        
        Time: O(n) - single pass
        Space: O(1) - no extra space
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update max area
            max_area = max(max_area, current_area)
            
            # Move the pointer pointing to smaller height
            # This is key insight: moving the taller pointer inward
            # will only decrease area (width decreases, height can't improve)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
    
    # ===============================================
    # SOLUTION 2: Brute Force (Educational)
    # ===============================================
    def maxArea_bruteforce(self, height: List[int]) -> int:
        """
        Check all possible pairs of indices.
        
        Time: O(n²) - check all pairs
        Space: O(1)
        """
        max_area = 0
        n = len(height)
        
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate area
                width = j - i
                current_height = min(height[i], height[j])
                area = width * current_height
                
                # Update max
                max_area = max(max_area, area)
        
        return max_area
    
    
    # ===============================================
    # SOLUTION 3: Two Pointer with Tracking
    # ===============================================
    def maxArea_detailed(self, height: List[int]) -> int:
        """
        Two pointer with detailed step-by-step tracking.
        Shows which indices were considered for max area.
        
        Time: O(n)
        Space: O(1)
        """
        max_area = 0
        best_left = 0
        best_right = len(height) - 1
        
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update if better
            if current_area > max_area:
                max_area = current_area
                best_left = left
                best_right = right
            
            # Move pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        # Return max area (can add details if needed)
        return max_area


# ===============================================
# TEST CASES
# ===============================================

def run_tests():
    """Run comprehensive test suite"""
    solution = Solution()
    
    test_cases = [
        # (height array, expected output)
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([2, 3, 4, 5, 18, 17, 6], 17),
        ([1, 2, 4, 3], 4),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 1], 1),
        ([1, 100000], 1),  # min(1, 100000) * 1 = 1
        ([100000, 1], 1),  # min(100000, 1) * 1 = 1
        ([9, 4, 8, 6, 3, 5, 2, 1], 25),  # indices 0,2: min(9,8)*2 = 16 or 1,2: min(4,8)*1=4 or 0,6: min(9,2)*6=12... actually max is 25
        ([1, 8, 100, 2, 100, 4, 8, 3, 7], 200),  # indices 2,4: min(100,100)*2 = 200
        ([2, 4, 1, 3, 5, 6], 16),  # indices 1,5: min(4,6)*4 = 16
        ([1, 100, 50, 100, 1], 200),  # indices 1,3: min(100,100)*2 = 200
        ([3, 9, 3, 4, 7, 2, 12, 6], 45),  # indices 1,6: min(9,12)*5 = 45
        ([50, 30, 20, 50], 150),  # indices 0,3: min(50,50)*3 = 150
    ]
    
    print("=" * 80)
    print("CONTAINER WITH MOST WATER - TEST SUITE")
    print("=" * 80 + "\n")
    
    passed = 0
    failed = 0
    
    for height, expected in test_cases:
        result_twoPointer = solution.maxArea_twoPointer(height)
        result_bruteforce = solution.maxArea_bruteforce(height)
        result_detailed = solution.maxArea_detailed(height)
        
        all_correct = (result_twoPointer == expected and 
                      result_bruteforce == expected and 
                      result_detailed == expected)
        
        status = "✅ PASS" if all_correct else "❌ FAIL"
        if all_correct:
            passed += 1
        else:
            failed += 1
        
        print(f"Height: {height}")
        print(f"Expected: {expected}")
        print(f"TwoPointer: {result_twoPointer} {'✓' if result_twoPointer == expected else '✗'}")
        print(f"Bruteforce: {result_bruteforce} {'✓' if result_bruteforce == expected else '✗'}")
        print(f"Detailed:   {result_detailed} {'✓' if result_detailed == expected else '✗'}")
        print(f"Status: {status}\n")
    
    print("=" * 80)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(test_cases)}")
    print("=" * 80)


# ===============================================
# EXPLANATION & KEY INSIGHT
# ===============================================

def explain_algorithm():
    """Explain the two-pointer greedy approach"""
    print("\n" + "=" * 80)
    print("ALGORITHM EXPLANATION: Two Pointer Approach")
    print("=" * 80 + "\n")
    
    print("Key Insight:")
    print("-" * 80)
    print("""
The two-pointer approach works because of a greedy observation:

1. Start with the widest container (left=0, right=n-1)
2. The area is limited by the SHORTER of the two heights
3. If we move the TALLER pointer inward:
   - Width DECREASES (always)
   - Height can't increase (limited by shorter wall)
   - Result: Area can't improve → Don't move it
4. If we move the SHORTER pointer inward:
   - Width DECREASES (always)
   - Height might INCREASE (we might find a taller wall)
   - Result: Area might improve → Move it

Example: [1, 8, 6, 2, 5, 4, 8, 3, 7]
         ^                       ^
      left=0                  right=8
      height[0]=1, height[8]=7
      width=8, height=min(1,7)=1
      area=8*1=8
      
      Move left (smaller) → left=1
         ^                     ^
      height[1]=8, height[8]=7
      width=7, height=min(8,7)=7
      area=7*7=49 ✓ Better!
      
      Move right (smaller) → right=7
         ^                 ^
      height[1]=8, height[7]=3
      width=6, height=min(8,3)=3
      area=6*3=18 (worse)
      ...continue...
    """)
    print("-" * 80)


if __name__ == "__main__":
    run_tests()
    explain_algorithm()