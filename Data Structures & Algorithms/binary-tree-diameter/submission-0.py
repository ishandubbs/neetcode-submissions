# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # returns height
        self.result = 0

        def dfs(curr):
            if not curr:
                return 0

            lHeight = dfs(curr.left)
            rHeight = dfs(curr.right)

            self.result = max(self.result, lHeight + rHeight)
            return (1 + max(lHeight, rHeight))
        
        dfs(root)
        return self.result

        # another way (using local and global):
        # result = 0

        # def dfs(curr):
        #     if not curr:
        #         return 0

        #     lHeight = dfs(curr.left)
        #     rHeight = dfs(curr.right)

        #     nonlocal result
        #     result = max(result, lHeight + rHeight)
        #     return (1 + max(lHeight, rHeight))
        
        # dfs(root)
        # return result