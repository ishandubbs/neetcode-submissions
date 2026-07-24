class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        # [1, 2, 3]
        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1) # different subset

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1) # empty subset
        
        dfs(0)
        return result