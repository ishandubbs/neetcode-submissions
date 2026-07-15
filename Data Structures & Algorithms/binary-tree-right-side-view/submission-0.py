# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []

        if root is None:
            return result

        # queue for level order traversal
        q = deque([root])

        while q:
            # number of nodes at current level
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                # if last node of current level
                if i == level_size - 1:
                    result.append(node.val)

                # enqueue left child
                if node.left is not None:
                    q.append(node.left)
               
                # enqueue right child
                if node.right is not None:
                    q.append(node.right)
        return result