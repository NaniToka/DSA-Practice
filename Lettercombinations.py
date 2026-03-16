#!/usr/bin/env python3

"""
Problem #17: Letter Combinations of a Phone Number
Difficulty: Medium
Topics: String, Backtracking, Hash Table
Time: O(4^n) | Space: O(4^n)

Generate all possible letter combinations for a phone number.
Uses backtracking for optimal solution.

Approach: Backtracking with Digit-to-Letter Mapping
"""

class Solution:
    """Letter Combinations of a Phone Number"""
    
    # Phone keypad mapping
    DIGIT_MAP = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    # ===============================================
    # SOLUTION 1: Backtracking (Optimal)
    # ===============================================
    def letterCombinations_backtracking(self, digits: str) -> list[str]:
        """
        Backtracking approach - recursively build combinations.
        
        Algorithm:
        1. If digits is empty, return empty list
        2. For each digit, get corresponding letters
        3. For each letter, recursively add combinations from next digit
        4. Backtrack and explore other branches
        
        Time: O(4^n) where n = length of digits (max 4 letters per digit)
        Space: O(4^n) for output, O(n) for recursion stack
        
        Why optimal:
        - Clean and intuitive
        - Minimal overhead
        - Natural recursive structure
        """
        if not digits:
            return []
        
        result = []
        
        def backtrack(index: int, current_combination: str):
            """
            Recursively build combinations.
            
            Args:
                index: Current position in digits string
                current_combination: Current combination being built
            """
            # Base case: processed all digits
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get letters for current digit
            current_digit = digits[index]
            letters = self.DIGIT_MAP[current_digit]
            
            # Try each letter for this digit
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        
        backtrack(0, "")
        return result
    
    
    # ===============================================
    # SOLUTION 2: Iterative Approach
    # ===============================================
    def letterCombinations_iterative(self, digits: str) -> list[str]:
        """
        Iterative approach - build combinations bottom-up.
        
        Algorithm:
        1. Start with empty combination
        2. For each digit:
           - For each existing combination:
             - Append each letter of current digit
        3. Return final combinations
        
        Time: O(4^n)
        Space: O(4^n) for output
        
        Advantages:
        - No recursion overhead
        - Clearer state progression
        - Easier to understand for some
        """
        if not digits:
            return []
        
        result = [""]
        
        for digit in digits:
            temp = []
            letters = self.DIGIT_MAP[digit]
            
            # For each existing combination, add each letter
            for combination in result:
                for letter in letters:
                    temp.append(combination + letter)
            
            result = temp
        
        return result
    
    
    # ===============================================
    # SOLUTION 3: BFS (Breadth-First Search)
    # ===============================================
    def letterCombinations_bfs(self, digits: str) -> list[str]:
        """
        BFS approach - generate combinations level by level.
        
        Algorithm:
        1. Start with queue containing empty string
        2. For each digit:
           - Dequeue all current combinations
           - For each combination and letter:
             - Create new combination and enqueue
        3. Return final queue
        
        Time: O(4^n)
        Space: O(4^n) for queue and output
        
        Use case:
        - When you need combinations in specific order
        - When processing multiple levels is needed
        """
        if not digits:
            return []
        
        from collections import deque
        queue = deque([""])
        
        for digit in digits:
            letters = self.DIGIT_MAP[digit]
            
            # Process all combinations at current level
            for _ in range(len(queue)):
                current = queue.popleft()
                
                # Add each letter to current combination
                for letter in letters:
                    queue.append(current + letter)
        
        return list(queue)
    
    
    # ===============================================
    # SOLUTION 4: Dynamic Programming Approach
    # ===============================================
    def letterCombinations_dp(self, digits: str) -> list[str]:
        """
        Dynamic programming approach - build on previous results.
        
        Algorithm:
        1. Initialize dp[0] with combinations for first digit
        2. For each subsequent digit:
           - For each previous combination:
             - Append each letter of current digit
        3. Return final dp result
        
        Time: O(4^n)
        Space: O(4^n) for dp table
        
        Similar to iterative but with explicit dp table.
        """
        if not digits:
            return []
        
        # dp[i] stores all combinations up to digit i
        dp = [[] for _ in range(len(digits))]
        
        # Base case: first digit
        dp[0] = list(self.DIGIT_MAP[digits[0]])
        
        # Build combinations for remaining digits
        for i in range(1, len(digits)):
            letters = self.DIGIT_MAP[digits[i]]
            
            # For each previous combination, add each letter
            for prev_combo in dp[i - 1]:
                for letter in letters:
                    dp[i].append(prev_combo + letter)
        
        return dp[-1]


# ===============================================
# TEST CASES
# ===============================================

def run_tests():
    """Run comprehensive test suite"""
    solution = Solution()
    
    test_cases = [
        # (digits, expected_output)
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ["a", "b", "c"]),
        ("", []),
        ("234", [
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ]),
        ("9", ["w", "x", "y", "z"]),
        ("22", ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]),
        ("26", ["am", "an", "ao", "bm", "bn", "bo", "cm", "cn", "co"]),
        ("34", ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]),
    ]
    
    print("=" * 100)
    print("LETTER COMBINATIONS OF A PHONE NUMBER - TEST SUITE")
    print("=" * 100 + "\n")
    
    passed = 0
    failed = 0
    
    for digits, expected in test_cases:
        result_backtrack = sorted(solution.letterCombinations_backtracking(digits))
        result_iterative = sorted(solution.letterCombinations_iterative(digits))
        result_bfs = sorted(solution.letterCombinations_bfs(digits))
        result_dp = sorted(solution.letterCombinations_dp(digits))
        expected_sorted = sorted(expected)
        
        all_correct = (result_backtrack == expected_sorted and 
                      result_iterative == expected_sorted and 
                      result_bfs == expected_sorted and 
                      result_dp == expected_sorted)
        
        status = "✅ PASS" if all_correct else "❌ FAIL"
        if all_correct:
            passed += 1
        else:
            failed += 1
        
        display_digits = f'"{digits}"' if len(digits) <= 4 else f'"{digits}"'
        result_count = len(expected)
        print(f"Input: {display_digits:8s} | Expected count: {result_count:3d}")
        print(f"Backtracking: {len(result_backtrack):3d} combinations {'✓' if result_backtrack == expected_sorted else '✗'}")
        print(f"Iterative:    {len(result_iterative):3d} combinations {'✓' if result_iterative == expected_sorted else '✗'}")
        print(f"BFS:          {len(result_bfs):3d} combinations {'✓' if result_bfs == expected_sorted else '✗'}")
        print(f"DP:           {len(result_dp):3d} combinations {'✓' if result_dp == expected_sorted else '✗'}")
        
        if len(digits) <= 2:
            print(f"Output: {result_backtrack}")
        
        print(f"Status: {status}\n")
    
    print("=" * 100)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(test_cases)}")
    print("=" * 100)


# ===============================================
# EXPLANATION & KEY INSIGHTS
# ===============================================

def explain_algorithm():
    """Explain the algorithm"""
    print("\n" + "=" * 100)
    print("ALGORITHM EXPLANATION: Backtracking Approach")
    print("=" * 100 + "\n")
    
    print("Key Insight:")
    print("-" * 100)
    print("""
The Letter Combinations problem generates all combinations of letters for phone digits.

Phone Keypad Mapping:
  2: abc    5: jkl    8: tuv
  3: def    6: mno    9: wxyz
  4: ghi    7: pqrs

Example: digits = "23"

Step 1: Map digits to letters
  2 → abc
  3 → def

Step 2: Generate combinations
  For each letter in '2' (a, b, c):
    For each letter in '3' (d, e, f):
      Combine them

Result:
  ad, ae, af,
  bd, be, bf,
  cd, ce, cf

Total: 3 × 3 = 9 combinations

Backtracking Approach (Recursive):
──────────────────────────────────

def backtrack(index, current):
    if index == len(digits):
        result.append(current)
        return
    
    for letter in DIGIT_MAP[digits[index]]:
        backtrack(index + 1, current + letter)

Call tree for "23":
        backtrack(0, "")
       /    |    \\
      a     b     c
     /|     |\\    |\\
    d e f  d e f d e f
    ↓ ↓ ↓  ↓ ↓ ↓ ↓ ↓ ↓
   ad ae af bd be bf cd ce cf

Key Points:
- At each level, we choose one letter for current digit
- Then recursively process next digit
- When we've processed all digits, add to result

Iterative Approach:
───────────────────

result = [""]

For digit '2':
  For each combo in [""], add 'a', 'b', 'c'
  result = ["a", "b", "c"]

For digit '3':
  For each combo in ["a", "b", "c"]:
    Add 'd', 'e', 'f'
  result = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Key Points:
- Start with one empty combination
- For each digit, expand all existing combinations
- Each expansion adds letters of current digit

Complexity Analysis:
────────────────────

Time: O(4^n)
  - n = length of digits (max 4)
  - Each digit contributes factor of 3 or 4 letters
  - Max: 4^4 = 256 combinations for 4 digits
  - Each combination takes O(n) to build/append
  - Total: O(n × 4^n) for building all combinations

Space: O(4^n)
  - Output array stores all combinations
  - Each combination has length n
  - Recursion depth: O(n) for call stack

Comparison of Approaches:
─────────────────────────

Backtracking:
  ✓ Most intuitive
  ✓ Natural recursive structure
  ✓ Easy to understand
  ✓ Standard interview solution

Iterative:
  ✓ No recursion overhead
  ✓ Clear bottom-up progression
  ✓ Easy to trace execution
  ✓ Better for stack-limited environments

BFS:
  ✓ Level-by-level generation
  ✓ Queue-based processing
  ✓ Combinations generated in BFS order
  ✗ More overhead than iterative

DP:
  ✓ Explicit subproblem storage
  ✓ Shows subproblem structure
  ✓ Easy to analyze dependencies
  ✗ Extra space for DP table

Edge Cases:
───────────

✓ Empty string → []
✓ Single digit → 3-4 letters
✓ Four digits → 4^4 = 256 combinations
✓ All same digit (e.g., "2222") → 3^4 = 81 combinations
✓ Mix of 3-letter and 4-letter digits → Product varies

Phone Number Digits:
────────────────────

2: abc (3 letters)
3: def (3 letters)
4: ghi (3 letters)
5: jkl (3 letters)
6: mno (3 letters)
7: pqrs (4 letters) ← Has 4!
8: tuv (3 letters)
9: wxyz (4 letters) ← Has 4!

Note: 1 and 0 have no letters!
    """)
    print("-" * 100)


if __name__ == "__main__":
    run_tests()
    explain_algorithm()