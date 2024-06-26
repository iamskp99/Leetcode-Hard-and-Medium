# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,ans = [],[]
        while True:
            while root or len(stack) > 0:
                ans.append(root.val)
                if root.right:
                    stack.append(root.right)

                if root.left:
                    root = root.left
                    continue

                if len(stack) > 0:
                    root = stack.pop()
                    continue

                break

            return ans

            