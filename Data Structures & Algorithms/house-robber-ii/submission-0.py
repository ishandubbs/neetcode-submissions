class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        # [rob1, rob2, n, n+1, ...]
        def rob_linear(sub_list):
            rob1, rob2 = 0, 0
            for num in sub_list:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))