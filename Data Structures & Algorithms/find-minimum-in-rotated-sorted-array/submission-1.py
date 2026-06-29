class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])
            # DISCLAIMER: THIS ONLY WORKS ON A ROTATED SORTING ARRAY
            if nums[mid] >= nums[left]:
                left = mid + 1 # search right
            
            else:
                right = mid - 1

        return result