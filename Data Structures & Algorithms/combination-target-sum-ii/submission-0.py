class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []


        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return


            # two-branch decision
            # Branch 1: Include candidates[i]
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i]) # i + 1 if each element is used once
            curr.pop()

            # Branch 2: Skip candidates[i] and all subsequent identical values
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1
            dfs(next_i, curr, total)


        dfs(0, [], 0)
        return result
