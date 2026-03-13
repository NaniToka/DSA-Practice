#!/usr/bin/env python3

"""
Problem #13: Roman to Integer
Difficulty: Easy
Topics: String, Hash Table
Time: O(n) | Space: O(1)

Convert Roman numeral string to integer.
Process left to right: if current < next, subtract; else add.

Approach: Character Mapping with Subtraction Rule
"""

class Solution:
    """Roman to Integer conversion"""
    
    # ===============================================
    # SOLUTION 1: Single Pass with Comparison
    # ===============================================
    def romanToInt_comparison(self, s: str) -> int:
        """
        Single pass left to right.
        If current value < next value: subtract (subtractive case)
        Otherwise: add
        
        Logic:
        - IV, IX: I before V or X → subtract I
        - XL, XC: X before L or C → subtract X  
        - CD, CM: C before D or M → subtract C
        
        Time: O(n) where n = length of string
        Space: O(1) - only using hashmap of fixed size
        """
        char_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        
        for i in range(len(s)):
            current_value = char_values[s[i]]
            
            # Check if there's a next character
            if i + 1 < len(s):
                next_value = char_values[s[i + 1]]
                
                # If current < next, this is subtractive case
                if current_value < next_value:
                    result -= current_value
                else:
                    result += current_value
            else:
                # Last character, always add
                result += current_value
        
        return result
    
    
    # ===============================================
    # SOLUTION 2: Two Pass Approach (Intuitive)
    # ===============================================
    def romanToInt_twoPass(self, s: str) -> int:
        """
        Two pass approach for clarity:
        Pass 1: Add all character values
        Pass 2: Subtract subtractive cases (when smaller before larger)
        
        Time: O(n)
        Space: O(1)
        """
        char_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Pass 1: Add all values
        result = 0
        for char in s:
            result += char_values[char]
        
        # Pass 2: Subtract subtractive cases
        # When smaller value appears before larger value
        subtractive_pairs = [
            ('I', 'V'),  # IV = 4, subtract 2 (added 1 twice, need only 1 addition)
            ('I', 'X'),  # IX = 9
            ('X', 'L'),  # XL = 40
            ('X', 'C'),  # XC = 90
            ('C', 'D'),  # CD = 400
            ('C', 'M')   # CM = 900
        ]
        
        for small, large in subtractive_pairs:
            # Count occurrences of small before large
            pair = small + large
            count = s.count(pair)
            # Subtract 2x value of small (once added, once subtract)
            result -= count * 2 * char_values[small]
        
        return result
    
    
    # ===============================================
    # SOLUTION 3: Right to Left Scan (Reverse)
    # ===============================================
    def romanToInt_rightToLeft(self, s: str) -> int:
        """
        Right to left approach: scan from end to beginning.
        Keep track of previous value.
        If current < previous: subtract (subtractive case)
        Otherwise: add
        
        Time: O(n)
        Space: O(1)
        """
        char_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        # Scan from right to left
        for i in range(len(s) - 1, -1, -1):
            current_value = char_values[s[i]]
            
            # If current < previous, subtract (subtractive case)
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            
            prev_value = current_value
        
        return result


# ===============================================
# TEST CASES
# ===============================================

def run_tests():
    """Run comprehensive test suite"""
    solution = Solution()
    
    test_cases = [
        # (roman string, expected integer)
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("I", 1),
        ("IV", 4),
        ("V", 5),
        ("IX", 9),
        ("XXVII", 27),
        ("XLVIII", 48),
        ("LIX", 59),
        ("XCIII", 93),
        ("CXLI", 141),
        ("CLXIII", 163),
        ("CDII", 402),
        ("DLXXV", 575),
        ("DCXLIV", 644),
        ("DCCCLXXXVIII", 888),
        ("CM", 900),
        ("M", 1000),
        ("MD", 1500),
        ("MCMLXXXIV", 1984),
        ("MMXXIII", 2023),
        ("MMMCMXCIX", 3999),
    ]
    
    print("=" * 80)
    print("ROMAN TO INTEGER - TEST SUITE")
    print("=" * 80 + "\n")
    
    passed = 0
    failed = 0
    
    for roman, expected in test_cases:
        result_comparison = solution.romanToInt_comparison(roman)
        result_twoPass = solution.romanToInt_twoPass(roman)
        result_rightToLeft = solution.romanToInt_rightToLeft(roman)
        
        all_correct = (result_comparison == expected and 
                      result_twoPass == expected and 
                      result_rightToLeft == expected)
        
        status = "✅ PASS" if all_correct else "❌ FAIL"
        if all_correct:
            passed += 1
        else:
            failed += 1
        
        print(f"Roman: {roman:15s} | Expected: {expected:4d}")
        print(f"Comparison:  {result_comparison:4d} {'✓' if result_comparison == expected else '✗'}")
        print(f"TwoPass:     {result_twoPass:4d} {'✓' if result_twoPass == expected else '✗'}")
        print(f"RightToLeft: {result_rightToLeft:4d} {'✓' if result_rightToLeft == expected else '✗'}")
        print(f"Status: {status}\n")
    
    print("=" * 80)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(test_cases)}")
    print("=" * 80)


# ===============================================
# EXPLANATION & KEY INSIGHTS
# ===============================================

def explain_algorithm():
    """Explain the key insight"""
    print("\n" + "=" * 80)
    print("ALGORITHM EXPLANATION: Key Insight")
    print("=" * 80 + "\n")
    
    print("Key Rule:")
    print("-" * 80)
    print("""
Roman numerals have a special rule for subtraction:

When a SMALLER value appears BEFORE a LARGER value:
  → Subtract the smaller value instead of adding it

Subtractive Cases:
  IV (I before V):   1 < 5   → 5 - 1 = 4
  IX (I before X):   1 < 10  → 10 - 1 = 9
  XL (X before L):   10 < 50 → 50 - 10 = 40
  XC (X before C):   10 < 100 → 100 - 10 = 90
  CD (C before D):   100 < 500 → 500 - 100 = 400
  CM (C before M):   100 < 1000 → 1000 - 100 = 900

Algorithm (Left to Right):
─────────────────────────
1. Iterate through each character
2. Get its Roman value
3. Check next character's value
4. If current < next: SUBTRACT current value
5. Otherwise: ADD current value

Example: Convert "MCMXCIV" = 1994
──────────────────────────────

String: M  C  M  X  C  I  V
Values: 1000 100 1000 10 100 1  5

i=0: M(1000)
  Next: C(100)
  1000 > 100? YES → Add 1000
  result = 1000

i=1: C(100)
  Next: M(1000)
  100 < 1000? YES → Subtract 100 (subtractive CM)
  result = 1000 - 100 = 900

i=2: M(1000)
  Next: X(10)
  1000 > 10? YES → Add 1000
  result = 900 + 1000 = 1900

i=3: X(10)
  Next: C(100)
  10 < 100? YES → Subtract 10 (subtractive XC)
  result = 1900 - 10 = 1890

i=4: C(100)
  Next: I(1)
  100 > 1? YES → Add 100
  result = 1890 + 100 = 1990

i=5: I(1)
  Next: V(5)
  1 < 5? YES → Subtract 1 (subtractive IV)
  result = 1990 - 1 = 1989

i=6: V(5) [Last character]
  No next → Add 5
  result = 1989 + 5 = 1994 ✓

Result: 1994 ✅

Why This Works:
✓ Subtractive rule is naturally handled
✓ Single pass O(n) time
✓ No special data structures needed
✓ Works for all valid Roman numerals
    """)
    print("-" * 80)


if __name__ == "__main__":
    run_tests()
    explain_algorithm()