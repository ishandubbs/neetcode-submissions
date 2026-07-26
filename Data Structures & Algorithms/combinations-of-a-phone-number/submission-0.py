class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return

            for char in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + char)
        
        if digits:
            backtrack(0, "")
        
        return result