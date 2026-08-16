class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0


        for i in range(len(s)):
            # odd length
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1


            # even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1


        return result
