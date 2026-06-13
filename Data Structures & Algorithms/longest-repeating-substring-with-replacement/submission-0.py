class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0
        # max_freq = 0
        
        for right in range(len(s)): 
            #right goes through every single position in s
            count[s[right]] = 1 + count.get(s[right], 0)
            # max_freq = max(max_freq, count[s[right]])
            #checks if window (right - left + 1) is valid:
            while (right - left + 1) - max(count.values()) > k: 
                # can do max_freq instead of max(count.values())
                count[s[left]] -= 1 #decrememnts the count
                left += 1 #updates left

            result = max(result, right - left + 1)
        #This is for O(26 * N) runtime
        # This is for O(N) runtime
        return result