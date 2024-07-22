# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rec(self,node,p,q):
        if node == None:
            return None

        cnt,flag = 0,None
        if node.val in [p.val,q.val]:
            flag = node
            cnt += 1

        v1 = self.rec(node.left,p,q)
        v2 = self.rec(node.right,p,q)

        if v1 is not None and v1.val in [p.val,q.val]:
            flag = v1
            cnt += 1

        if v2 is not None and v2.val in [p.val,q.val]:
            flag = v2
            cnt += 1

        if v1 is not None and v1.val not in [p.val,q.val]:
            flag = v1
            cnt += 1

        if v2 is not None and v2.val not in [p.val,q.val]:
            flag = v2
            cnt += 1

        if cnt == 2:
            return node

        if cnt == 1:
            return flag

        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.rec(root,p,q)