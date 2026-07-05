"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = { None : None } # hash set

        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy # stores it in hash map
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next] # if curr.next is Null, we modify oldToCopy
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]