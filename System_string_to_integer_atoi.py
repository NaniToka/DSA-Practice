"""
String to Integer (atoi) - Complete System Solution
Problem: Convert string to 32-bit signed integer

Algorithm Steps:
1. Skip leading whitespace
2. Determine sign ('+' or '-')
3. Read digits until non-digit or end of string
4. Clamp result to 32-bit signed range [-2^31, 2^31 - 1]

Test Cases Covered:
- Basic positive number: "42" → 42
- Leading whitespace: "   -042" → -42
- Stop at non-digit: "1337c0d3" → 1337
- No leading digits: "words and 987" → 0
- Overflow: "-91283472332" → -2147483648
- Empty/whitespace only: "" → 0
"""

# ==============================================================================
# SOLUTION 1: STANDARD APPROACH (MOST EFFICIENT & CLEAN)
# ==============================================================================

def myAtoi_v1(s: str) -> int:
    """
    Standard approach using character iteration and pointer.
    
    Time Complexity: O(n) - single pass through string
    Space Complexity: O(1) - only constant extra space
    
    Algorithm:
    1. Use pointer i to traverse string
    2. Skip leading spaces
    3. Check for sign character
    4. Read consecutive digits
    5. Clamp to 32-bit range
    """
    
    i = 0
    
    # Step 1: Skip leading whitespace
    while i < len(s) and s[i] == ' ':
        i += 1
    
    # Edge case: end of string
    if i == len(s):
        return 0
    
    # Step 2: Check for sign
    sign = 1
    if s[i] in ['-', '+']:
        if s[i] == '-':
            sign = -1
        i += 1
    
    # Step 3: Read digits and build number
    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    
    # Apply sign
    result = sign * result
    
    # Step 4: Clamp to 32-bit signed integer range
    INT_MIN = -2**31      # -2147483648
    INT_MAX = 2**31 - 1   # 2147483647
    
    return max(INT_MIN, min(INT_MAX, result))


# ==============================================================================
# SOLUTION 2: EARLY CLAMPING OPTIMIZATION
# ==============================================================================

def myAtoi_v2(s: str) -> int:
    """
    Optimized version that checks for overflow during computation
    instead of after. Prevents potential overflow issues.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    i = 0
    
    # Skip whitespace
    while i < len(s) and s[i] == ' ':
        i += 1
    
    if i == len(s):
        return 0
    
    # Check sign
    sign = 1
    if s[i] in ['-', '+']:
        if s[i] == '-':
            sign = -1
        i += 1
    
    # Read digits with early overflow checking
    result = 0
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])
        
        # Check if next multiplication will overflow
        # INT_MAX = 2147483647, INT_MAX // 10 = 214748364
        if result > INT_MAX // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        if result == INT_MAX // 10 and digit > 7:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit
        i += 1
    
    return sign * result


# ==============================================================================
# SOLUTION 3: REGEX APPROACH (CONCISE)
# ==============================================================================

import re

def myAtoi_v3(s: str) -> int:
    """
    Using regular expression pattern matching.
    More concise but may be less efficient.
    
    Pattern breakdown:
    ^     : Start of string
    \s*   : Zero or more whitespace characters
    [+-]? : Optional + or - sign
    \d+   : One or more digits
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    # Match pattern: optional spaces, optional sign, digits
    match = re.match(r'^\s*[+-]?\d+', s)
    
    # Convert match to integer or return 0
    result = int(match.group()) if match else 0
    
    # Clamp to 32-bit range
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    return max(INT_MIN, min(INT_MAX, result))


# ==============================================================================
# SOLUTION 4: STATE MACHINE APPROACH (EDUCATIONAL)
# ==============================================================================

def myAtoi_v4(s: str) -> int:
    """
    State machine approach for explicit state handling.
    Better for understanding different states of parsing.
    
    States:
    - WHITESPACE: Skipping leading spaces
    - SIGN: Reading optional sign
    - NUMBER: Reading digits
    - END: Parsing complete
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    state = 'WHITESPACE'
    result = 0
    sign = 1
    
    for char in s:
        if state == 'WHITESPACE':
            # Skip spaces
            if char == ' ':
                continue
            # Check for sign
            elif char in ['-', '+']:
                sign = -1 if char == '-' else 1
                state = 'NUMBER'
            # Check for digit
            elif char.isdigit():
                state = 'NUMBER'
                result = int(char)
            # Any other character
            else:
                return 0
        
        elif state == 'NUMBER':
            # Continue reading digits
            if char.isdigit():
                result = result * 10 + int(char)
                # Early clamping
                if result > INT_MAX:
                    return INT_MAX if sign == 1 else INT_MIN
            # Stop at non-digit
            else:
                break
    
    return sign * result


# ==============================================================================
# TEST CASES
# ==============================================================================

def run_tests():
    """Run comprehensive test cases for all solutions."""
    
    test_cases = [
        # (input, expected_output, description)
        ("42", 42, "Basic positive number"),
        ("   -042", -42, "Leading whitespace with negative sign"),
        ("1337c0d3", 1337, "Stop at non-digit character"),
        ("0-1", 0, "No digits at start"),
        ("words and 987", 0, "No digits at beginning"),
        ("", 0, "Empty string"),
        (" ", 0, "Only whitespace"),
        ("+1", 1, "Positive sign"),
        ("-1", -1, "Negative sign"),
        ("123456789", 123456789, "Large positive number"),
        ("-123456789", -123456789, "Large negative number"),
        ("+-123", 0, "Multiple signs"),
        ("-+0", 0, "Multiple signs variation"),
        ("-91283472332", -2147483648, "Overflow - clamp to INT_MIN"),
        ("20000000000000000000", 2147483647, "Overflow - clamp to INT_MAX"),
        ("00000-21474836", 0, "Leading zeros with sign after"),
        ("2147483647", 2147483647, "Max int value"),
        ("-2147483648", -2147483648, "Min int value"),
        ("2147483648", 2147483647, "Just above max"),
        ("-2147483649", -2147483648, "Just below min"),
    ]
    
    solutions = [
        ("Solution 1 (Standard)", myAtoi_v1),
        ("Solution 2 (Early Clamp)", myAtoi_v2),
        ("Solution 3 (Regex)", myAtoi_v3),
        ("Solution 4 (State Machine)", myAtoi_v4),
    ]
    
    print("=" * 80)
    print("STRING TO INTEGER (ATOI) - TEST RESULTS")
    print("=" * 80)
    
    for solution_name, solution_func in solutions:
        print(f"\n{solution_name}")
        print("-" * 80)
        
        passed = 0
        failed = 0
        
        for input_str, expected, description in test_cases:
            result = solution_func(input_str)
            status = "✓ PASS" if result == expected else "✗ FAIL"
            
            if result == expected:
                passed += 1
            else:
                failed += 1
            
            # Show failed tests in detail
            if result != expected:
                print(f"{status} | Input: '{input_str}'")
                print(f"       | Expected: {expected}, Got: {result}")
                print(f"       | {description}")
        
        print(f"\nSummary: {passed} passed, {failed} failed out of {len(test_cases)}")
    
    print("\n" + "=" * 80)


# ==============================================================================
# COMPLEXITY ANALYSIS
# ==============================================================================

def complexity_analysis():
    """Print complexity analysis for all solutions."""
    
    print("\n" + "=" * 80)
    print("COMPLEXITY ANALYSIS")
    print("=" * 80)
    
    solutions_info = [
        {
            "name": "Solution 1 (Standard)",
            "time": "O(n)",
            "space": "O(1)",
            "pros": ["Clean and readable", "Easy to understand", "Single pass"],
            "cons": ["Post-clamping (no early check)"]
        },
        {
            "name": "Solution 2 (Early Clamp)",
            "time": "O(n)",
            "space": "O(1)",
            "pros": ["Prevents overflow", "Optimized", "Safe for large inputs"],
            "cons": ["Slightly more complex logic"]
        },
        {
            "name": "Solution 3 (Regex)",
            "time": "O(n)",
            "space": "O(1)",
            "pros": ["Concise", "Pythonic", "Fewer lines"],
            "cons": ["Regex overhead", "Less readable for some", "Less control"]
        },
        {
            "name": "Solution 4 (State Machine)",
            "time": "O(n)",
            "space": "O(1)",
            "pros": ["Explicit states", "Clear logic flow", "Educational"],
            "cons": ["More verbose", "Harder to understand", "More code"]
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
    
    print("\n" + "=" * 80)
    print("RECOMMENDATION: Solution 1 (Standard) - Best balance of clarity and efficiency")
    print("=" * 80)


# ==============================================================================
# EDGE CASES EXPLANATION
# ==============================================================================

def explain_edge_cases():
    """Explain how edge cases are handled."""
    
    print("\n" + "=" * 80)
    print("EDGE CASES HANDLING")
    print("=" * 80)
    
    edge_cases = [
        {
            "case": "Empty String",
            "input": '""',
            "output": 0,
            "explanation": "After skipping whitespace, if i == len(s), return 0"
        },
        {
            "case": "Only Whitespace",
            "input": '"   "',
            "output": 0,
            "explanation": "All characters are spaces, loop exits, returns 0"
        },
        {
            "case": "No Digits",
            "input": '"words"',
            "output": 0,
            "explanation": "First char is not space or sign, condition fails, return 0"
        },
        {
            "case": "Non-digit in middle",
            "input": '"123abc456"',
            "output": 123,
            "explanation": "Digit loop exits when 'a' encountered, returns 123"
        },
        {
            "case": "Positive Overflow",
            "input": '"20000000000000000000"',
            "output": 2147483647,
            "explanation": "Result > INT_MAX, clamped to 2^31 - 1"
        },
        {
            "case": "Negative Overflow",
            "input": '"-20000000000000000000"',
            "output": -2147483648,
            "explanation": "Result < INT_MIN, clamped to -2^31"
        },
        {
            "case": "Multiple Signs",
            "input": '"+-123"',
            "output": 0,
            "explanation": "After first sign, second '+' is not digit, loop exits"
        },
    ]
    
    for edge_case in edge_cases:
        print(f"\n{edge_case['case']}")
        print(f"  Input: {edge_case['input']}")
        print(f"  Output: {edge_case['output']}")
        print(f"  Explanation: {edge_case['explanation']}")
    
    print("\n" + "=" * 80)


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
    
    # Quick demo
    print("\n" + "=" * 80)
    print("QUICK DEMO - Solution 1 (Recommended)")
    print("=" * 80)
    
    demo_inputs = ["42", "   -042", "1337c0d3", "0-1", "words and 987"]
    
    for demo_input in demo_inputs:
        result = myAtoi_v1(demo_input)
        print(f"myAtoi_v1('{demo_input}') = {result}")
    
    print("\n" + "=" * 80)