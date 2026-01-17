# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,node,cur_max):
        if node is None:
            self.ans = max(self.ans,cur_max)
            return -1*(10**18)

        cur_val = node.val
        now_max = cur_max
        if now_max+cur_val <= cur_val:
            now_max = cur_val
        else:
            now_max += cur_val
        
        cl = self.rec(node.left,now_max)
        cr = self.rec(node.right,now_max)
        # print(cur_val,now_max,cl,cr)
        self.ans = max(cl,cr,cl+cur_val+cr,now_max+cl,now_max+cr,now_max,cur_val,self.ans)
        return max(cl+cur_val,cr+cur_val,cur_val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -1*(10**18)
        self.rec(root,-1*(10**18))
        return self.ans