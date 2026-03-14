#!/usr/bin/env python3

"""
Problem #15: 3Sum
Difficulty: Medium
Topics: Array, Two Pointers, Sorting
Time: O(n^2) | Space: O(1) or O(n)

Find all unique triplets in array that sum to zero.
Uses two-pointer approach after sorting for optimal solution.

Approach: Sort + Two Pointers (No Duplicates)
"""

class Solution:
    """3Sum - Find triplets that sum to zero"""
    
    # ===============================================
    # SOLUTION 1: Two Pointers (Optimal)
    # ===============================================
    def threeSum_twoPointers(self, nums: list[int]) -> list[list[int]]:
        """
        Two pointer approach after sorting.
        
        Algorithm:
        1. Sort the array
        2. For each element as first number:
           - Use two pointers (left, right) for remaining elements
           - Find pairs that sum to -first_num
           - Skip duplicates carefully
        3. Return unique triplets
        
        Time: O(n^2) - O(n log n) sorting + O(n^2) for two pointer
        Space: O(1) - excluding output
        
        Why it works:
        - Sorting helps with two-pointer technique
        - Duplicates automatically handled by skipping
        - Early termination when first > 0 (impossible to sum to 0)
        """
        nums.sort()
        result = []
        n = len(nums)
        
        # If array too small or all positive, no solution
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
                    # Sum too small, need larger number
                    left += 1
                else:
                    # Sum too large, need smaller number
                    right -= 1
        
        return result
    
    
    # ===============================================
    # SOLUTION 2: Hash Set Approach
    # ===============================================
    def threeSum_hashSet(self, nums: list[int]) -> list[list[int]]:
        """
        Hash set approach to find pairs for each first element.
        
        Algorithm:
        1. Sort the array
        2. For each element as first number:
           - Use hash set to find pairs in remaining elements
           - Add valid triplets to result
           - Skip duplicates
        3. Return unique triplets
        
        Time: O(n^2) - nested loop with hash set lookups
        Space: O(n) - for hash set storage
        """
        nums.sort()
        result = set()
        n = len(nums)
        
        if n < 3 or nums[-1] < 0:
            return []
        
        for i in range(n - 2):
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if nums[i] > 0:
                break
            
            # Use hash set for two-sum in remaining elements
            seen = set()
            target = -nums[i]
            
            for j in range(i + 1, n):
                complement = target - nums[j]
                
                if complement in seen:
                    # Found valid pair
                    triplet = tuple(sorted([nums[i], complement, nums[j]]))
                    result.add(triplet)
                
                seen.add(nums[j])
        
        return [list(triplet) for triplet in result]
    
    
    # ===============================================
    # SOLUTION 3: Brute Force (Educational)
    # ===============================================
    def threeSum_bruteForce(self, nums: list[int]) -> list[list[int]]:
        """
        Brute force: Try all triplets and check sum.
        
        Algorithm:
        1. Use three nested loops for all combinations
        2. Check if sum equals zero
        3. Use set to avoid duplicates
        
        Time: O(n^3) - three nested loops
        Space: O(n) - for set of results
        
        Only for small arrays - not recommended for large inputs
        """
        result = set()
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)
        
        return [list(triplet) for triplet in result]
    
    
    # ===============================================
    # SOLUTION 4: Two Pass with HashMap
    # ===============================================
    def threeSum_hashMap(self, nums: list[int]) -> list[list[int]]:
        """
        HashMap approach with careful duplicate handling.
        
        Algorithm:
        1. Sort array to help with duplicate skipping
        2. For each element as first number:
           - Create complement map for remaining elements
           - Find pairs using complement lookup
        3. Handle duplicates by using tuples in set
        
        Time: O(n^2)
        Space: O(n) - for hashmap
        """
        nums.sort()
        result = set()
        n = len(nums)
        
        if n < 3 or nums[-1] < 0:
            return []
        
        for i in range(n - 2):
            # Early termination
            if nums[i] > 0:
                break
            
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two-sum using hashmap
            complement_map = {}
            target = -nums[i]
            
            for j in range(i + 1, n):
                if nums[j] in complement_map:
                    # Found a valid pair
                    triplet = tuple(sorted([nums[i], nums[j], complement_map[nums[j]]]))
                    result.add(triplet)
                
                # Add current number to complement map
                complement = target - nums[j]
                complement_map[complement] = nums[j]
        
        return [list(triplet) for triplet in result]


# ===============================================
# TEST CASES
# ===============================================

def run_tests():
    """Run comprehensive test suite"""
    solution = Solution()
    
    test_cases = [
        # (nums, expected_triplets)
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([-5, -4, -4, -1, -1, 0, 1, 2, 3], [[-5, 2, 3], [-4, 1, 3], [-1, -1, 2], [-1, 0, 1]]),
        ([3, -2, 1, 0], []),
        ([-1, -1, -1, 0, 0, 0, 1, 1, 1], [[-1, 0, 1], [0, 0, 0]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([-1, 0, 1], [[-1, 0, 1]]),
        ([1, 2, -2, -1], []),
    ]
    
    print("=" * 90)
    print("3SUM - TEST SUITE")
    print("=" * 90 + "\n")
    
    passed = 0
    failed = 0
    
    for nums, expected in test_cases:
        result_tp = sorted([sorted(triplet) for triplet in solution.threeSum_twoPointers(nums)])
        result_hs = sorted([sorted(triplet) for triplet in solution.threeSum_hashSet(nums)])
        result_bf = sorted([sorted(triplet) for triplet in solution.threeSum_bruteForce(nums)])
        result_hm = sorted([sorted(triplet) for triplet in solution.threeSum_hashMap(nums)])
        
        expected_sorted = sorted([sorted(triplet) for triplet in expected])
        
        all_correct = (result_tp == expected_sorted and 
                      result_hs == expected_sorted and 
                      result_bf == expected_sorted and 
                      result_hm == expected_sorted)
        
        status = "✅ PASS" if all_correct else "❌ FAIL"
        if all_correct:
            passed += 1
        else:
            failed += 1
        
        display_nums = str(nums) if len(str(nums)) < 40 else str(nums)[:37] + "..."
        print(f"Input: {display_nums}")
        print(f"Expected: {expected_sorted}")
        print(f"TwoPointers: {result_tp} {'✓' if result_tp == expected_sorted else '✗'}")
        print(f"HashSet:    {result_hs} {'✓' if result_hs == expected_sorted else '✗'}")
        print(f"BruteForce: {result_bf} {'✓' if result_bf == expected_sorted else '✗'}")
        print(f"HashMap:    {result_hm} {'✓' if result_hm == expected_sorted else '✗'}")
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
    print("ALGORITHM EXPLANATION: Two Pointers with Sorting")
    print("=" * 90 + "\n")
    
    print("Key Insight:")
    print("-" * 90)
    print("""
The 3Sum problem requires finding all unique triplets that sum to zero.

Naive approach: O(n^3) - try all combinations
Optimal approach: O(n^2) - sort + two pointers

Example: [-1, 0, 1, 2, -1, -4]

Step 1: Sort the array
  [-4, -1, -1, 0, 1, 2]

Step 2: For each element as first number, find pairs that sum to -first_num
  
  i=0 (first=-4):
    Need pairs summing to 4
    Left pointer at -1, Right at 2
    -1 + 2 = 1 (not 4)
    ... continue searching ...
    No valid triplets found

  i=1 (first=-1):
    Need pairs summing to 1
    Left pointer at -1, Right at 2
    -1 + 2 = 1 ✓ → Triplet: [-1, -1, 2]
    Continue searching...
    -1 + 0 = -1 (too small)
    0 + 1 = 1 ✓ → Triplet: [-1, 0, 1]

  i=2 (first=-1):
    Skip (duplicate of previous)

  i=3 onwards:
    First number > 0, impossible to sum to 0, stop

Result: [[-1, -1, 2], [-1, 0, 1]]

Two Pointer Technique Detail:
─────────────────────────────

After sorting: [-4, -1, -1, 0, 1, 2]

For first=-1, target=1:

       left         right
        ↓           ↓
    [-4, -1, -1, 0, 1, 2]
         
    Sum: -1 + 2 = 1 ✓ Found!
    Move both: left++, right--

       left      right
        ↓        ↓
    [-4, -1, -1, 0, 1, 2]
         
    Sum: -1 + 1 = 0 (not 1)
    Too small, need larger: left++

          left  right
           ↓    ↓
    [-4, -1, -1, 0, 1, 2]
         
    Sum: 0 + 1 = 1 ✓ Found!
    But left < right is false now, stop

Duplicate Handling:
──────────────────

When we find a match, skip duplicates:

1. Skip duplicate first numbers:
   if i > 0 and nums[i] == nums[i-1]:
       continue

2. Skip duplicate left values when found:
   while left < right and nums[left] == nums[left + 1]:
       left += 1

3. Skip duplicate right values when found:
   while left < right and nums[right] == nums[right - 1]:
       right -= 1

This ensures each triplet is unique.

Complexity Analysis:
────────────────────

Time: O(n^2)
  - Sorting: O(n log n)
  - Outer loop: O(n)
  - Inner two-pointer loop: O(n)
  - Total: O(n log n) + O(n^2) = O(n^2)

Space: O(1) or O(n)
  - If we don't count output: O(1)
  - Sorting may require O(log n) to O(n) extra space
  - Hash set approach: O(n) for set

Why Two Pointers is Optimal:
────────────────────────────

✓ O(n^2) time (vs O(n^3) for brute force)
✓ O(1) extra space (vs O(n) for hash set)
✓ No hash map overhead
✓ Cache-friendly (sequential access)
✓ Naturally handles duplicates with sorting

Edge Cases:
───────────

✓ All zeros → [[0, 0, 0]]
✓ No solution → []
✓ Negative only → []
✓ Positive only → []
✓ Single triplet → [triplet]
✓ Multiple duplicates → Handle with skipping
    """)
    print("-" * 90)


if __name__ == "__main__":
    run_tests()
    explain_algorithm()