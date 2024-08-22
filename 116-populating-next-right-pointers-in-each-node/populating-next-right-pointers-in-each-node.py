"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def rec(self,node,other):
        if node is None:
            return

        self.rec(node.left,node.right)
        other_next = None
        if other:
            if other.left:
                other_next = other.left

            else:
                if other.right:
                    other_next = other.right

        self.rec(node.right,other_next)
        node.next = other
        return

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.rec(root,None)
        return root