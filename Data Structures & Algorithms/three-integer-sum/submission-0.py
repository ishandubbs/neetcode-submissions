class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue #don't want to use the same value twice

            left, right = i + 1, len(nums) - 1 
            #compares the rest of the numbers in the list
            while left < right:
                threeSum = a + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1 #makes sum smaller
                
                elif threeSum < 0:
                    left += 1 #makes sum bigger

                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1 #only update the left pointer and the rest is based on the conditions
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result