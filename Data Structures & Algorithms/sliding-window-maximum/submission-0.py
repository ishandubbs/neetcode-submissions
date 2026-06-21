class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = collections.deque() #index
        left = right = 0

        while right < len(nums):
            while queue and nums[queue[-1]] < nums[right]: #while queue is not empty and the last element in queue is less than right
                queue.pop() #removes values
            queue.append(right) #finds the number (nums[right])

            #remove left value from window
            if left > queue[0]:
                queue.popleft()

            if (right + 1) >= k:
                result.append(nums[queue[0]])
                left += 1
            right += 1

        return result