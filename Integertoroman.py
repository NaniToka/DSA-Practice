#!/usr/bin/env python3

"""
Problem #12: Integer to Roman
Difficulty: Medium
Topics: String, Greedy, Math
Time: O(1) | Space: O(1)

Convert an integer (1-3999) to Roman numeral representation.
Uses greedy approach with value-to-symbol mapping including subtractive forms.

Approach: Greedy with Mapping
Process from largest value to smallest, greedily appending symbols.
"""

class Solution:
    """Integer to Roman conversion using greedy approach"""
    
    # ===============================================
    # SOLUTION 1: Greedy with Value-Symbol Mapping
    # ===============================================
    def intToRoman_greedy(self, num: int) -> str:
        """
        Greedy approach: Process from largest to smallest value.
        For each value, append symbol as many times as possible.
        
        Key insight: Include subtractive forms (IV, IX, XL, XC, CD, CM)
        in the mapping to handle them naturally.
        
        Time: O(1) - max 13 iterations (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        Space: O(1) - constant space for result string
        """
        # Mapping includes subtractive forms
        # Order matters: largest to smallest
        values = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        result = ""
        
        for value, symbol in values:
            # Greedily append symbol as many times as possible
            count = num // value
            if count:
                result += symbol * count
                num -= value * count
        
        return result
    
    
    # ===============================================
    # SOLUTION 2: Greedy with While Loop
    # ===============================================
    def intToRoman_while(self, num: int) -> str:
        """
        Similar to Solution 1 but uses while loop instead of division.
        More explicit iteration approach.
        
        Time: O(1)
        Space: O(1)
        """
        values = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        result = ""
        idx = 0
        
        while num > 0 and idx < len(values):
            value, symbol = values[idx]
            
            # Keep appending symbol while num >= value
            while num >= value:
                result += symbol
                num -= value
            
            idx += 1
        
        return result
    
    
    # ===============================================
    # SOLUTION 3: Two Separate Arrays (Alternative)
    # ===============================================
    def intToRoman_arrays(self, num: int) -> str:
        """
        Separate arrays for values and symbols.
        More explicit but same logic.
        
        Time: O(1)
        Space: O(1)
        """
        # Ordered from largest to smallest (including subtractive forms)
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        result = ""
        
        for i in range(len(values)):
            # Append symbol multiple times if needed
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
        
        return result


# ===============================================
# TEST CASES
# ===============================================

def run_tests():
    """Run comprehensive test suite"""
    solution = Solution()
    
    test_cases = [
        # (number, expected)
        (3749, "MMMDCCXLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (1, "I"),
        (4, "IV"),
        (9, "IX"),
        (27, "XXVII"),
        (48, "XLVIII"),
        (59, "LIX"),
        (93, "XCIII"),
        (141, "CXLI"),
        (163, "CLXIII"),
        (402, "CDII"),
        (575, "DLXXV"),
        (644, "DCXLIV"),
        (888, "DCCCLXXXVIII"),
        (900, "CM"),
        (1000, "M"),
        (1500, "MD"),
        (1984, "MCMLXXXIV"),
        (2023, "MMXXIII"),
        (3999, "MMMCMXCIX"),
    ]
    
    print("=" * 80)
    print("INTEGER TO ROMAN - TEST SUITE")
    print("=" * 80 + "\n")
    
    passed = 0
    failed = 0
    
    for num, expected in test_cases:
        result_greedy = solution.intToRoman_greedy(num)
        result_while = solution.intToRoman_while(num)
        result_arrays = solution.intToRoman_arrays(num)
        
        all_correct = (result_greedy == expected and 
                      result_while == expected and 
                      result_arrays == expected)
        
        status = "✅ PASS" if all_correct else "❌ FAIL"
        if all_correct:
            passed += 1
        else:
            failed += 1
        
        print(f"Number: {num:4d} | Expected: {expected:12s}")
        print(f"Greedy: {result_greedy:12s} {'✓' if result_greedy == expected else '✗'}")
        print(f"While:  {result_while:12s} {'✓' if result_while == expected else '✗'}")
        print(f"Arrays: {result_arrays:12s} {'✓' if result_arrays == expected else '✗'}")
        print(f"Status: {status}\n")
    
    print("=" * 80)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(test_cases)}")
    print("=" * 80)


# ===============================================
# EXPLANATION & KEY INSIGHTS
# ===============================================

def explain_algorithm():
    """Explain the greedy approach"""
    print("\n" + "=" * 80)
    print("ALGORITHM EXPLANATION: Greedy Approach")
    print("=" * 80 + "\n")
    
    print("Key Insight:")
    print("-" * 80)
    print("""
The greedy approach works because:

1. Roman numerals follow a strict ordering from largest to smallest values
2. We process values in descending order
3. For each value, we greedily take as many as possible

The trick: Include subtractive forms (4, 9, 40, 90, 400, 900) in mapping!

Instead of handling 4 = "IV" separately, we just include:
  (4, "IV"), (9, "IX"), (40, "XL"), (90, "XC"), (400, "CD"), (900, "CM")

This simplifies the algorithm significantly.

Example: Convert 3749
─────────────────────────────────────────

Value Mapping (ordered largest to smallest):
  1000='M', 900='CM', 500='D', 400='CD', 100='C', 90='XC', 50='L', 40='XL', 
  10='X', 9='IX', 5='V', 4='IV', 1='I'

Step 1: 3749 ÷ 1000 = 3 remainder 749
        Append "MMM" (3 × M)
        num = 749

Step 2: 749 ÷ 900 = 0 (skip)

Step 3: 749 ÷ 500 = 1 remainder 249
        Append "D" (500)
        num = 249

Step 4: 249 ÷ 400 = 0 (skip)

Step 5: 249 ÷ 100 = 2 remainder 49
        Append "CC" (2 × 100)
        num = 49

Step 6: 49 ÷ 90 = 0 (skip)

Step 7: 49 ÷ 50 = 0 (skip)

Step 8: 49 ÷ 40 = 1 remainder 9
        Append "XL" (40)
        num = 9

Step 9: 9 ÷ 10 = 0 (skip)

Step 10: 9 ÷ 9 = 1 remainder 0
         Append "IX" (9)
         num = 0

Result: "MMMDCCXLIX"

Why this works:
✓ Subtractive forms are handled naturally by mapping
✓ Always process largest first → greedy approach works
✓ Time complexity O(1) because we always have max 13 iterations
✓ Space complexity O(1) because output is bounded by input range
    """)
    print("-" * 80)


if __name__ == "__main__":
    run_tests()
    explain_algorithm()