class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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
            subset.pop()

            # decision NOT to include nums[i]
            next_i = i + 1
            while next_i < len(nums) and nums[next_i] == nums[i]:
                next_i += 1        
            dfs(next_i)
       
        dfs(0)
        return result
