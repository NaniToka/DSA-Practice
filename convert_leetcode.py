# ===============================================
# SOLUTION 1: LEETCODE APPROACH
# ===============================================
def convert_leetcode(s: str, numRows: int) -> str:
    """Simulation approach - easy to understand"""
    if numRows == 1 or len(s) <= numRows:
        return s
    
    rows = ['' for _ in range(numRows)]
    current_row = 0
    direction = 1
    
    for char in s:
        rows[current_row] += char
        
        if current_row == 0:
            direction = 1
        elif current_row == numRows - 1:
            direction = -1
        
        current_row += direction
    
    return ''.join(rows)
