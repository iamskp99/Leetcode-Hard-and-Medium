# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node):
        if node == None:
            return 0
        
        r1,r2 = self.helper(node.left),self.helper(node.right)
        if abs(r1-r2) > 1:
            self.ans = False
            
        return max(r1,r2)+1
    
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.helper(root)
        return self.ans