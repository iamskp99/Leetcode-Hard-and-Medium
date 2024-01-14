# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,node):
        if node is None:
            return None

        le = self.rec(node.left)
        ri = self.rec(node.right)
        node.left = ri
        node.right = le
        return node


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.rec(root)