class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = list(set(nums))
        if len(nums) != len(new_nums):
            return True
        return False