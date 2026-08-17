class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums) # 0 -> [-1]
        currMin, currMax = 1, 1

        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
                continue

            temp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(temp, num * currMin, num)
            result = max(result, currMax)
        return result