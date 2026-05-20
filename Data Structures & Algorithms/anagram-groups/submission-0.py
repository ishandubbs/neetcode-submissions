class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list) #maps character count to list of anagrams
        for word in strs:
            count = [0] * 26 #a ... z

            for char in word:
                count[ord(char) - ord("a")] += 1 #increments count at the corresponding index

            result[tuple(count)].append(word) #uses count array as key and appends it to the list associated with the key

        return list(result.values())