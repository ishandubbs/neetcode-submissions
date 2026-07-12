# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(curr):
            if curr is None:
                return 0
            
            return 1 + max(height(curr.left), height(curr.right))

        if root is None:
            return True

        lHeight = height(root.left)
        rHeight = height(root.right)

        if abs(lHeight - rHeight) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)