class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 #input is empty

        left = 0
        right = len(height) - 1
        leftMax, rightMax = height[left], height[right]
        output = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                output += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                output += rightMax - height[right]
        return output