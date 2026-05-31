class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area_list = []
        left = 0
        right = len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            area_list.append(area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max(area_list)
        