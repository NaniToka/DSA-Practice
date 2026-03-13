class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Roman to Integer
        LeetCode #13 | Easy
        
        Convert Roman numeral string to integer.
        If current value < next value: subtract (subtractive case)
        Otherwise: add
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
            
            # Check next character
            if i + 1 < len(s):
                next_value = char_values[s[i + 1]]
                
                # If current < next, subtract (subtractive case: IV, IX, XL, XC, CD, CM)
                if current_value < next_value:
                    result -= current_value
                else:
                    result += current_value
            else:
                # Last character, always add
                result += current_value
        
        return result