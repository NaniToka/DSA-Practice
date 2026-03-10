#!/usr/bin/env python3

# Constants for 32-bit signed integer range
INT_MAX = 2147483647   # 2^31 - 1
INT_MIN = -2147483648  # -2^31


# ===============================================
# SOLUTION 1: LEETCODE APPROACH
# ===============================================
def reverse_leetcode(x: int) -> int:
    """
    Simple approach using built-in functions.
    Convert to string, reverse, convert back.
    """
    # Handle negative sign
    is_negative = x < 0
    x = abs(x)
    
    # Reverse the digits
    reversed_x = int(str(x)[::-1])
    
    # Apply negative sign back
    if is_negative:
        reversed_x = -reversed_x
    
    # Check for overflow
    if reversed_x > INT_MAX or reversed_x < INT_MIN:
        return 0
    
    return reversed_x
