class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = list(set(nums))
        res = 0
        for num in num_set:
            #check if start of a sequence
            if (num - 1) not in num_set:
                length = 0
                while (num + length) in num_set:
                    length += 1
                res = max(length, res)
        return res
