# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # L M R
        stack = []
        ans = []
        node = root
        while len(stack) or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            ans.append(node.val)
            node = node.right

        return ans

