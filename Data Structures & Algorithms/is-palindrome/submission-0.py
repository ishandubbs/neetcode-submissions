class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            if s[left_pointer] == s[right_pointer]:
                left_pointer += 1
                right_pointer -= 1
            else:
                return False
        return True