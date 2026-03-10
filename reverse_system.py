INT_MAX = 2147483647   # 2^31 - 1
INT_MIN = -2147483648  # -2^31

# ===============================================
# SOLUTION 2: SYSTEM APPROACH (Without string)
# ===============================================
def reverse_system(x: int) -> int:
    """
    Mathematical approach without using strings.
    Checks for overflow before it happens.
    """
    reversed_x = 0
    temp = x
    
    while temp != 0:
        # Handle negative numbers differently
        # Use -(-temp % 10) to get proper digit for negative numbers
        if temp > 0:
            digit = temp % 10
            temp //= 10
        else:
            digit = -((-temp) % 10)
            temp = -((-temp) // 10)
        
        # Check for overflow BEFORE adding the digit
        # For positive: reversed_x > INT_MAX // 10
        # For positive remainder: reversed_x == INT_MAX // 10 and digit > 7
        if reversed_x > INT_MAX // 10 or \
           (reversed_x == INT_MAX // 10 and digit > 7):
            return 0
        
        # For negative: reversed_x < INT_MIN // 10
        # For negative remainder: reversed_x == INT_MIN // 10 and digit < -8
        if reversed_x < INT_MIN // 10 or \
           (reversed_x == INT_MIN // 10 and digit < -8):
            return 0
        
        reversed_x = reversed_x * 10 + digit
    
    return reversed_x


# ===============================================
# TEST CASES
# ===============================================
if __name__ == "__main__":
    print("=" * 50)
    print("REVERSE INTEGER PROBLEM")
    print("=" * 50 + "\n")
    
    test_cases = [
        (123, 321, "Basic positive number"),
        (-123, -321, "Negative number"),
        (120, 21, "Trailing zeros"),
        (0, 0, "Zero"),
        (1534236469, 0, "Overflow positive"),
        (-2147483648, 0, "Overflow negative (min int)"),
        (2147483647, 0, "Overflow positive (max int)"),
        (1, 1, "Single digit"),
        (10, 1, "Single non-zero digit after reverse"),
        (100, 1, "Multiple trailing zeros"),
    ]
    
    passed = 0
    
    for i, (input_x, expected, description) in enumerate(test_cases, 1):
        result_leetcode = reverse_system(input_x)
        result_system = reverse_system(input_x)
        
        leetcode_pass = result_leetcode == expected
        system_pass = result_system == expected
        
        print(f"Test {i}: {description}")
        print(f"Input:    {input_x}")
        print(f"Expected: {expected}")
        print(f"LeetCode: {result_leetcode} {'✓' if leetcode_pass else '✗'}")
        print(f"System:   {result_system} {'✓' if system_pass else '✗'}")
        
        if leetcode_pass and system_pass:
            passed += 1
            print("Status:   PASS ✓")
        else:
            print("Status:   FAIL ✗")
        
        print()
    
    print("=" * 50)
    print(f"RESULTS: {passed}/{len(test_cases)} tests passed")
    print("=" * 50)
