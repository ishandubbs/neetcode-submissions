# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        # empty queue for level order traversal
        q = []
        result = []

        # enqueue root
        q.append(root)
        curr_level = 0

        while q:
            len_q = len(q)
            result.append([])

            for _ in range(len_q):
                # add front of queue and remove it from queue
                node = q.pop(0)
                result[curr_level].append(node.val)

                # enqueue left child
                if node.left is not None:
                    q.append(node.left)
                
                # enqueue right child
                if node.right is not None:
                    q.append(node.right)
            curr_level += 1
        return result