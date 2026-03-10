# ===============================================
# SOLUTION 2: SYSTEM APPROACH (Mathematical)
# ===============================================
def convert_system(s: str, numRows: int) -> str:
    """Mathematical approach - pattern based"""
    if numRows == 1 or len(s) <= numRows:
        return s
    
    result = []
    n = len(s)
    cycle_len = 2 * (numRows - 1)
    
    for row in range(numRows):
        index = row
        
        while index < n:
            result.append(s[index])
            
            if row != 0 and row != numRows - 1:
                next_index = index + (cycle_len - 2 * row)
                if next_index < n:
                    result.append(s[next_index])
            
            index += cycle_len
    
    return ''.join(result)


# ===============================================
# TEST CASES
# ===============================================
if __name__ == "__main__":
    print("=" * 50)
    print("ZIGZAG STRING CONVERSION")
    print("=" * 50 + "\n")
    
    # Test Case 1
    print("Test 1:")
    print("Input: s = \"PAYPALISHIRING\", numRows = 3")
    print("Expected: PAHNAPLSIIGYIR")
    print("LeetCode:", convert_leetcode("PAYPALISHIRING", 3))
    print("System:  ", convert_system("PAYPALISHIRING", 3))
    print()
    
    # Test Case 2
    print("Test 2:")
    print("Input: s = \"PAYPALISHIRING\", numRows = 4")
    print("Expected: PINALSIGYAHRPI")
    print("LeetCode:", convert_leetcode("PAYPALISHIRING", 4))
    print("System:  ", convert_system("PAYPALISHIRING", 4))
    print()
    
    # Test Case 3
    print("Test 3:")
    print("Input: s = \"A\", numRows = 1")
    print("Expected: A")
    print("LeetCode:", convert_leetcode("A", 1))
    print("System:  ", convert_system("A", 1))
    print()
    
    # Test Case 4
    print("Test 4:")
    print("Input: s = \"ABCDEFGHIJK\", numRows = 2")
    print("Expected: ACEGIKBDFHJ")
    print("LeetCode:", convert_leetcode("ABCDEFGHIJK", 2))
    print("System:  ", convert_system("ABCDEFGHIJK", 2))
    print()
    
    # Test Case 5
    print("Test 5:")
    print("Input: s = \"ABCD\", numRows = 2")
    print("Expected: ACBD")
    print("LeetCode:", convert_leetcode("ABCD", 2))
    print("System:  ", convert_system("ABCD", 2))
