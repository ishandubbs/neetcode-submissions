class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            # edge case

        s1Count, s2Count = [0] * 26, [0] * 26 # a - z as 0s

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 # maps to one of the 26 indexes in s1 and incrememnts it by 1
            s2Count[ord(s2[i]) - ord('a')] += 1 # maps to one of the 26 indexes in s2 and incrememnts it by 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        # sliding window approach
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]: #incrementing causes it to be equal
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]: #incrememnting causes it to be unequal
                matches -= 1

            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1 #same thing as above, only we decrement instead of increment
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]: #s1Count[index] - 1 instead of + 1 because we are changing left.
                matches -= 1
            left += 1
        return matches == 26
            