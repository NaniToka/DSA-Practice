"""
Palindrome Number - Complete System Solution
Problem: Given an integer x, return true if x is a palindrome

Key Insights:
1. Negative numbers are NEVER palindromes (due to minus sign)
2. Numbers ending with 0 are NOT palindromes (except 0 itself)
3. Can use string reversal or mathematical approach
4. Can optimize space by reversing only half the number

Test Cases:
- Positive palindrome: 121 → True
- Negative palindrome: -121 → False (negative sign breaks it)
- Non-palindrome: 123 → False
- Single digit: 7 → True
- Ending with 0: 10 → False
- Zero: 0 → True
"""

# ==============================================================================
# SOLUTION 1: MATHEMATICAL APPROACH - REVERSE HALF (OPTIMAL)
# ==============================================================================

def isPalindrome_v1(x: int) -> bool:
    """
    Reverse the second half of the number mathematically.
    Most efficient - O(log n) time, O(1) space.
    
    Algorithm:
    1. Check if negative or ends with 0 (return False)
    2. Reverse the second half of the number
    3. Stop when x <= reversed_half (handles both even/odd lengths)
    4. Compare: for even length x == reversed_half
                for odd length x == reversed_half // 10 (ignore middle digit)
    
    Example: x = 121
    Step 1: 121 > 0, not negative, doesn't end with 0
    Step 2-3 Loop:
        - reversed_half = 0, x = 121
        - reversed_half = 1, x = 12
        - reversed_half = 12, x = 1 (now 1 <= 12, stop)
    Step 4: x (1) == reversed_half // 10 (12 // 10 = 1) → True
    
    Time Complexity: O(log n) where n is the number of digits
    Space Complexity: O(1) - constant extra space (optimal)
    """
    
    # Edge case: negative numbers are never palindromes
    if x < 0:
        return False
    
    # Edge case: numbers ending with 0 are not palindromes (except 0 itself)
    if x % 10 == 0 and x != 0:
        return False
    
    # Reverse the second half of the number
    reversed_half = 0
    while x > reversed_half:
        # Extract last digit and add to reversed_half
        reversed_half = reversed_half * 10 + x % 10
        # Remove last digit from x
        x //= 10
    
    # For even length numbers: x == reversed_half
    # For odd length numbers: x == reversed_half // 10 (middle digit doesn't matter)
    return x == reversed_half or x == reversed_half // 10


# ==============================================================================
# SOLUTION 2: STRING REVERSAL APPROACH
# ==============================================================================

def isPalindrome_v2(x: int) -> bool:
    """
    Convert to string and compare with reverse.
    Simple and readable but uses O(log n) space.
    
    Algorithm:
    1. Convert number to string
    2. Compare with reversed string
    3. Also check for negative numbers explicitly
    
    Example: x = 121
    - Convert to string: "121"
    - Reverse: "121"
    - "121" == "121" → True
    
    Time Complexity: O(log n) where n is number of digits
    Space Complexity: O(log n) for string storage
    """
    
    # Negative numbers are never palindromes
    if x < 0:
        return False
    
    # Convert to string
    s = str(x)
    
    # Compare with reversed string
    return s == s[::-1]


# ==============================================================================
# SOLUTION 3: TWO-POINTER APPROACH
# ==============================================================================

def isPalindrome_v3(x: int) -> bool:
    """
    Convert to string and use two pointers from both ends.
    Good for understanding two-pointer technique.
    
    Algorithm:
    1. Convert to string
    2. Use left pointer at start, right pointer at end
    3. Compare characters and move pointers toward center
    4. If any mismatch, not a palindrome
    
    Example: x = 121
    - String: "121"
    - Left: 0 ('1'), Right: 2 ('1') → Match, move
    - Left: 1 ('2'), Right: 1 ('2') → Match, stop
    - All matched → True
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) for string
    """
    
    # Negative numbers are never palindromes
    if x < 0:
        return False
    
    # Convert to string
    s = str(x)
    left, right = 0, len(s) - 1
    
    # Compare from both ends
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


# ==============================================================================
# SOLUTION 4: FULL NUMBER REVERSAL
# ==============================================================================

def isPalindrome_v4(x: int) -> bool:
    """
    Reverse the entire number and compare.
    Simple but uses O(log n) space and has overflow concerns in some languages.
    
    Algorithm:
    1. Negative numbers are not palindromes (return False)
    2. Reverse the entire number
    3. Compare original with reversed
    
    Example: x = 121
    - Original: 121
    - Reversed: 121
    - 121 == 121 → True
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) for storing reversed number
    """
    
    # Negative numbers are never palindromes
    if x < 0:
        return False
    
    # Reverse the entire number
    original = x
    reversed_num = 0
    
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    # Compare original with reversed
    return original == reversed_num


# ==============================================================================
# TEST CASES
# ==============================================================================

def run_tests():
    """Run comprehensive test cases for all solutions."""
    
    test_cases = [
        # (input, expected, description)
        (121, True, "Palindrome: 121"),
        (-121, False, "Negative number"),
        (10, False, "Ending with 0"),
        (0, True, "Zero"),
        (1, True, "Single digit: 1"),
        (9, True, "Single digit: 9"),
        (12, False, "Non-palindrome: 12"),
        (1221, True, "Even length palindrome: 1221"),
        (12321, True, "Odd length palindrome: 12321"),
        (12345, False, "Non-palindrome: 12345"),
        (101, True, "Palindrome: 101"),
        (1001, True, "Palindrome: 1001"),
        (1010, False, "Ending with 0: 1010"),
        (9999, True, "All same digits: 9999"),
        (1234321, True, "Long palindrome: 1234321"),
        (123454321, True, "Odd length long: 123454321"),
        (2147483647, False, "Max int: 2147483647"),
        (-2147483648, False, "Min int: -2147483648"),
        (1, True, "Single: 1"),
        (100, False, "Ends with 0: 100"),
    ]
    
    solutions = [
        ("Solution 1 (Reverse Half - OPTIMAL)", isPalindrome_v1),
        ("Solution 2 (String Reversal)", isPalindrome_v2),
        ("Solution 3 (Two Pointers)", isPalindrome_v3),
        ("Solution 4 (Full Reversal)", isPalindrome_v4),
    ]
    
    print("=" * 90)
    print("PALINDROME NUMBER - TEST RESULTS")
    print("=" * 90)
    
    for solution_name, solution_func in solutions:
        print(f"\n{solution_name}")
        print("-" * 90)
        
        passed = 0
        failed = 0
        
        for input_num, expected, description in test_cases:
            result = solution_func(input_num)
            status = "✓ PASS" if result == expected else "✗ FAIL"
            
            if result == expected:
                passed += 1
            else:
                failed += 1
            
            # Show failed tests
            if result != expected:
                print(f"{status} | Input: {input_num}")
                print(f"       | Expected: {expected}, Got: {result}")
                print(f"       | {description}")
        
        print(f"\nSummary: {passed} passed, {failed} failed out of {len(test_cases)}")
    
    print("\n" + "=" * 90)


# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================

def complexity_analysis():
    """Print complexity analysis for all solutions."""
    
    print("\n" + "=" * 90)
    print("COMPLEXITY ANALYSIS")
    print("=" * 90)
    
    solutions_info = [
        {
            "name": "Solution 1 (Reverse Half - OPTIMAL)",
            "time": "O(log n)",
            "space": "O(1)",
            "pros": [
                "Space optimal - constant space",
                "Time efficient - log n time",
                "Doesn't convert to string",
                "No overflow concerns in Python"
            ],
            "cons": [
                "Slightly complex logic",
                "Need to handle even/odd lengths"
            ]
        },
        {
            "name": "Solution 2 (String Reversal)",
            "time": "O(log n)",
            "space": "O(log n)",
            "pros": [
                "Simple and readable",
                "Pythonic approach",
                "Easy to understand",
                "One-liner slice"
            ],
            "cons": [
                "Uses extra space for string",
                "Less efficient than math approach"
            ]
        },
        {
            "name": "Solution 3 (Two Pointers)",
            "time": "O(log n)",
            "space": "O(log n)",
            "pros": [
                "Educational - two-pointer technique",
                "Early exit possible",
                "Can stop at middle"
            ],
            "cons": [
                "Uses string space",
                "Similar complexity to Solution 2"
            ]
        },
        {
            "name": "Solution 4 (Full Reversal)",
            "time": "O(log n)",
            "space": "O(log n)",
            "pros": [
                "Simple logic",
                "Easy to understand",
                "Good for beginners"
            ],
            "cons": [
                "Uses extra space",
                "Processes all digits",
                "Overflow risk in other languages"
            ]
        },
    ]
    
    for solution in solutions_info:
        print(f"\n{solution['name']}")
        print(f"  Time Complexity: {solution['time']}")
        print(f"  Space Complexity: {solution['space']}")
        print(f"  Pros:")
        for pro in solution['pros']:
            print(f"    • {pro}")
        print(f"  Cons:")
        for con in solution['cons']:
            print(f"    • {con}")
    
    print("\n" + "=" * 90)
    print("RECOMMENDATION: Solution 1 (Reverse Half) - Optimal space and time")
    print("=" * 90)


# ==============================================================================
# EDGE CASES EXPLANATION
# ==============================================================================

def explain_edge_cases():
    """Explain how edge cases are handled."""
    
    print("\n" + "=" * 90)
    print("EDGE CASES EXPLANATION")
    print("=" * 90)
    
    edge_cases = [
        {
            "case": "Negative Numbers",
            "example": "-121",
            "output": False,
            "explanation": "Minus sign makes it not a palindrome. First check: x < 0"
        },
        {
            "case": "Ending with Zero",
            "example": "120",
            "output": False,
            "explanation": "Numbers ending with 0 can't be palindromes (except 0). Check: x % 10 == 0 and x != 0"
        },
        {
            "case": "Single Digit",
            "example": "7",
            "output": True,
            "explanation": "All single digits are palindromes"
        },
        {
            "case": "Zero",
            "example": "0",
            "output": True,
            "explanation": "Zero is a palindrome. Special case: handled by x % 10 == 0 and x != 0"
        },
        {
            "case": "Even Length Palindrome",
            "example": "1221",
            "output": True,
            "explanation": "Even length: x == reversed_half after loop"
        },
        {
            "case": "Odd Length Palindrome",
            "example": "12321",
            "output": True,
            "explanation": "Odd length: x == reversed_half // 10 (ignore middle digit)"
        },
        {
            "case": "All Same Digits",
            "example": "9999",
            "output": True,
            "explanation": "Numbers with all same digits are always palindromes"
        },
        {
            "case": "Two Digit Palindrome",
            "example": "11",
            "output": True,
            "explanation": "Two same digits are palindromes"
        },
    ]
    
    for edge_case in edge_cases:
        print(f"\n{edge_case['case']}")
        print(f"  Example: {edge_case['example']}")
        print(f"  Output: {edge_case['output']}")
        print(f"  Explanation: {edge_case['explanation']}")
    
    print("\n" + "=" * 90)


# ==============================================================================
# STEP-BY-STEP WALKTHROUGH
# ==============================================================================

def step_by_step_walkthrough():
    """Show step-by-step how Solution 1 works."""
    
    print("\n" + "=" * 90)
    print("STEP-BY-STEP WALKTHROUGH - Solution 1 (Optimal)")
    print("=" * 90)
    
    examples = [
        121,
        1221,
        12321,
        123,
        10
    ]
    
    for x in examples:
        print(f"\n{'=' * 90}")
        print(f"Example: x = {x}")
        print(f"{'=' * 90}")
        
        # Check negative and ends with 0
        print(f"\nStep 1: Check if negative or ends with 0")
        print(f"  x < 0: {x < 0}")
        print(f"  x % 10 == 0: {x % 10 == 0}")
        
        if x < 0 or (x % 10 == 0 and x != 0):
            print(f"  → Return False")
            continue
        
        print(f"  → Continue")
        
        # Reverse half
        print(f"\nStep 2: Reverse the second half")
        original_x = x
        reversed_half = 0
        step = 1
        
        while x > reversed_half:
            last_digit = x % 10
            reversed_half = reversed_half * 10 + last_digit
            x //= 10
            
            print(f"  Step {step}: x={original_x if step == 1 else ''} → x={x}, reversed_half={reversed_half}")
            step += 1
            
            if x <= reversed_half:
                break
        
        # Compare
        print(f"\nStep 3: Compare")
        print(f"  x = {x}")
        print(f"  reversed_half = {reversed_half}")
        print(f"  x == reversed_half: {x == reversed_half}")
        print(f"  x == reversed_half // 10: {x == reversed_half // 10}")
        
        result = x == reversed_half or x == reversed_half // 10
        print(f"  → Result: {result}")


# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == "__main__":
    # Run all tests
    run_tests()
    
    # Show complexity analysis
    complexity_analysis()
    
    # Explain edge cases
    explain_edge_cases()
    
    # Step-by-step walkthrough
    step_by_step_walkthrough()
    
    # Quick demo
    print("\n" + "=" * 90)
    print("QUICK DEMO - Solution 1 (Recommended)")
    print("=" * 90)
    
    demo_inputs = [121, -121, 10, 1221, 12321, 123]
    
    for demo_input in demo_inputs:
        result = isPalindrome_v1(demo_input)
        print(f"isPalindrome({demo_input}) = {result}")
    
    print("\n" + "=" * 90)