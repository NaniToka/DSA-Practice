#!/usr/bin/env python3

"""
Problem #16: 3Sum Closest
Difficulty: Medium
Topics: Array, Two Pointers, Sorting
Time: O(n^2) | Space: O(1)

Find three integers whose sum is closest to a target.
Uses two-pointer approach after sorting for optimal solution.

Approach: Sort + Two Pointers with Minimum Difference Tracking
"""

class Solution:
    """3Sum Closest - Find triplets closest to target"""
    
    # ===============================================
    # SOLUTION 1: Two Pointers (Optimal)
    # ===============================================
    def threeSumClosest_twoPointers(self, nums: list[int], target: int) -> int:
        """
        Two pointer approach after sorting.
        
        Algorithm:
        1. Sort the array
        2. For each element as first number:
           - Use two pointers (left, right) for remaining elements
           - Track the closest sum to target
           - Move pointers based on comparison with target
        3. Return the closest sum
        
        Time: O(n^2) - O(n log n) sorting + O(n^2) for two pointer
        Space: O(1) - excluding output
        
        Key insight:
        - Track minimum difference between current sum and target
        - When sum < target, move left pointer to increase sum
        - When sum > target, move right pointer to decrease sum
        - Early termination when exact match found
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
    
    
    # ===============================================
    # SOLUTION 2: Optimized Two Pointers with Early Exit
    # ===============================================
    def threeSumClosest_optimized(self, nums: list[int], target: int) -> int:
        """
        Two pointers with early termination optimizations.
        
        Algorithm:
        1. Sort array
        2. For each fixed first number:
           - Use two pointers for remaining elements
           - Track closest sum and minimum difference
           - If exact match found, return immediately
           - Skip iterations when difference is 0
        3. Return closest sum
        
        Time: O(n^2)
        Space: O(1)
        
        Optimizations:
        - Early return on exact match
        - Break outer loop if first > target and all remaining are positive
        """
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        min_diff = abs(closest_sum - target)
        
        for i in range(n - 2):
            # Early termination - if smallest possible sum is too large
            if nums[i] + nums[i + 1] + nums[i + 2] > target and min_diff == 0:
                break
            
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)
                
                # Check if this is the closest sum so far
                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum
                
                # Exact match - no need to continue
                if min_diff == 0:
                    return closest_sum
                
                # Move pointers
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
    
    
    # ===============================================
    # SOLUTION 3: Iterative Refinement (Alternative)
    # ===============================================
    def threeSumClosest_iterative(self, nums: list[int], target: int) -> int:
        """
        Iterative refinement approach with value tracking.
        
        Algorithm:
        1. Sort array
        2. For each element as first number:
           - Use two pointers for remaining elements
           - Track best sum at each step
           - Move pointers based on sum vs target
        3. Return closest sum found
        
        Time: O(n^2)
        Space: O(1)
        
        Similar to optimal but with explicit value tracking.
        """
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        min_distance = abs(closest_sum - target)
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                distance = abs(current_sum - target)
                
                # Update if closer
                if distance < min_distance:
                    min_distance = distance
                    closest_sum = current_sum
                
                # Early exit
                if distance == 0:
                    return current_sum
                
                # Adjust pointers
                if current_sum - target < 0:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
    
    
    # ===============================================
    # SOLUTION 4: Brute Force (Educational)
    # ===============================================
    def threeSumClosest_bruteForce(self, nums: list[int], target: int) -> int:
        """
        Brute force: Try all triplets and find closest sum.
        
        Algorithm:
        1. Use three nested loops for all combinations
        2. Track the sum closest to target
        3. Return closest sum
        
        Time: O(n^3) - three nested loops
        Space: O(1)
        
        Only for educational purposes - too slow for large inputs
        """
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]
        min_diff = abs(closest_sum - target)
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    current_sum = nums[i] + nums[j] + nums[k]
                    current_diff = abs(current_sum - target)
                    
                    if current_diff < min_diff:
                        min_diff = current_diff
                        closest_sum = current_sum
        
        return closest_sum


# ===============================================
# TEST CASES
# ===============================================

def run_tests():
    """Run comprehensive test suite"""
    solution = Solution()
    
    test_cases = [
        # (nums, target, expected)
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([1, 1, 1, 0], -100, 2),
        ([-1, 0, 1, 2, -1, -4], 0, 0),
        ([0, 1, 2], 3, 3),
        ([1, 1, 1, 1], 0, 3),
        ([-1000, 1000, 1000, 1000], -1, 1000),
        ([1, 2, 3, 4, 5], 12, 12),
        ([0, 2, 1, -3], 0, 0),
        ([-4, -1, -1, 0, 1, 2], -2, -2),
        ([1, 1, 1, 0, -1, -1, -1], 0, 0),
        ([13, 2, 0, -5], -5, -3),
    ]
    
    print("=" * 90)
    print("3SUM CLOSEST - TEST SUITE")
    print("=" * 90 + "\n")
    
    passed = 0
    failed = 0
    
    for nums, target, expected in test_cases:
        result_tp = solution.threeSumClosest_twoPointers(nums.copy(), target)
        result_opt = solution.threeSumClosest_optimized(nums.copy(), target)
        result_it = solution.threeSumClosest_iterative(nums.copy(), target)
        result_bf = solution.threeSumClosest_bruteForce(nums.copy(), target)
        
        all_correct = (result_tp == expected and 
                      result_opt == expected and 
                      result_it == expected and 
                      result_bf == expected)
        
        status = "✅ PASS" if all_correct else "❌ FAIL"
        if all_correct:
            passed += 1
        else:
            failed += 1
        
        display_nums = str(nums) if len(str(nums)) < 40 else str(nums)[:37] + "..."
        print(f"Input: {display_nums}, Target: {target}")
        print(f"Expected: {expected}")
        print(f"TwoPointers: {result_tp} {'✓' if result_tp == expected else '✗'}")
        print(f"Optimized:   {result_opt} {'✓' if result_opt == expected else '✗'}")
        print(f"Iterative:   {result_it} {'✓' if result_it == expected else '✗'}")
        print(f"BruteForce:  {result_bf} {'✓' if result_bf == expected else '✗'}")
        print(f"Status: {status}\n")
    
    print("=" * 90)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(test_cases)}")
    print("=" * 90)


# ===============================================
# EXPLANATION & KEY INSIGHTS
# ===============================================

def explain_algorithm():
    """Explain the algorithm"""
    print("\n" + "=" * 90)
    print("ALGORITHM EXPLANATION: Two Pointers with Minimum Difference Tracking")
    print("=" * 90 + "\n")
    
    print("Key Insight:")
    print("-" * 90)
    print("""
The 3Sum Closest problem requires finding a triplet whose sum is closest to target.

Key difference from 3Sum:
- 3Sum: Find triplets that SUM TO ZERO
- 3Sum Closest: Find triplets whose sum is CLOSEST TO TARGET

Naive approach: O(n^3) - try all triplets
Optimal approach: O(n^2) - sort + two pointers

Example: nums = [-1, 2, 1, -4], target = 1

Step 1: Sort the array
  [-4, -1, 1, 2]

Step 2: For each element as first number, find pair closest to target
  
  i=0 (first=-4):
    Target for pair: 1 - (-4) = 5
    Two pointers: left at -1, right at 2
    Sum: -4 + (-1) + 2 = -3 (diff from 1 = 4)
    Sum: -4 + (-1) + 1 = -4 (diff from 1 = 5)
    Best for this: -3

  i=1 (first=-1):
    Target for pair: 1 - (-1) = 2
    Two pointers: left at 1, right at 2
    Sum: -1 + 1 + 2 = 2 (diff from 1 = 1) ← Best so far!
    
  i=2 (first=1):
    Only one element left, skip

Result: 2 (sum -1 + 1 + 2)

Two Pointer Technique Detail:
─────────────────────────────

After sorting: [-4, -1, 1, 2]

For first=-1, target=1:

       left      right
        ↓        ↓
    [-4, -1, 1, 2]
         
    Sum: -1 + 1 + 2 = 2
    Diff: |2 - 1| = 1
    Update closest_sum = 2
    
    Sum > target? YES → Move right pointer left
    right--

       left  right
        ↓    ↓
    [-4, -1, 1, 2]
         
    Sum: -1 + 1 + 1 = 1 (but can't use same index)
    Actually: -1 + (-1) + 1... wait, we're at i=1

Let me redo with correct indices:

For i=1 (first=-1):
    left = 2 (nums[2] = 1)
    right = 3 (nums[3] = 2)
    
    current_sum = -1 + 1 + 2 = 2
    diff = |2 - 1| = 1
    
    Is 2 == 1? NO
    Is 2 < 1? NO
    Is 2 > 1? YES → Move right pointer left
    
    right = 2 (nums[2] = 1)
    left < right? 2 < 2? NO
    Exit while loop

Algorithm Comparison:
────────────────────

Two Pointers (Optimal):
  ✓ O(n^2) time
  ✓ O(1) space
  ✓ Early termination on exact match
  ✓ Efficient pointer movement

Optimized:
  ✓ O(n^2) time
  ✓ O(1) space
  ✓ Includes early termination optimizations
  ✓ Best practical performance

Iterative:
  ✓ O(n^2) time
  ✓ O(1) space
  ✓ Alternative pointer approach
  ✓ Similar to two pointers

Brute Force:
  ✗ O(n^3) time
  ✓ O(1) space
  - Only for educational purposes

Complexity Analysis:
────────────────────

Time: O(n^2)
  - Sorting: O(n log n)
  - Outer loop: O(n)
  - Inner two-pointer loop: O(n)
  - Total: O(n log n) + O(n^2) = O(n^2)

Space: O(1)
  - Only using pointers and variables
  - Not counting output
  - Sorting may use O(log n) to O(n) extra space

Edge Cases:
───────────

✓ Exact match → Return immediately
✓ All positive → Smallest sum is closest
✓ All negative → Largest (least negative) sum is closest
✓ Target is average → Some middle sum
✓ Three identical numbers → Return their sum
    """)
    print("-" * 90)


if __name__ == "__main__":
    run_tests()
    explain_algorithm()