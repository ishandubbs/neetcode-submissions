class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge case:
        if t == "": return ""
        if len(s) < len (t):
            return ""

        countT, window = {}, {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)
            #if char exists, it will get the char, if not, it will return 0

        have, need = 0, len(countT)
        result, resultLen = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)
            #same thing as above
            if char in countT and window[char] == countT[char]:
                have += 1
                #if the char is in the countT and also in the window
            
            while have == need:
                #update our result if we found a new minimum result
                if (right - left + 1) < resultLen: #if window length < result length
                    result = [left, right]
                    resultLen = (right - left + 1)
                
                #pop from the left of our window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = result
        return s[left:right + 1] if resultLen != float("infinity") else ""
