class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Integer to Roman
        LeetCode #12 | Medium
        
        Convert integer (1-3999) to Roman numeral using greedy approach.
        """
        # Value-symbol mapping including subtractive forms
        # Ordered from largest to smallest
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
        
        # Greedy: process from largest value to smallest
        for value, symbol in values:
            # Append symbol as many times as num >= value
            while num >= value:
                result += symbol
                num -= value
        
        return result