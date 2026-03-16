class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Letter Combinations of a Phone Number
        LeetCode #17 | Medium
        
        Generate all possible letter combinations for phone digits.
        Uses backtracking approach.
        
        Time: O(4^n) where n = length of digits
        Space: O(4^n) for output
        """
        if not digits:
            return []
        
        # Phone keypad mapping
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index: int, current_combination: str):
            """Recursively build combinations"""
            # Base case: processed all digits
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get letters for current digit
            letters = digit_map[digits[index]]
            
            # Try each letter for this digit
            for letter in letters:
                backtrack(index + 1, current_combination + letter)
        
        backtrack(0, "")
        return result