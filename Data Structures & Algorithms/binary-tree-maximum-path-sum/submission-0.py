# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0
        
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # if negative:
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            # compute max path sum WITH split
            result[0] = max(result[0], root.val + leftMax + rightMax)
            
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return result[0]