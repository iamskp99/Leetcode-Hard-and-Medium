# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self,inorder,postorder):
        if len(postorder) == 0:
            return None
        node_val = postorder[-1]
        node = TreeNode(val=node_val,left=None,right=None)
        mid_ind = inorder.index(node_val)
        in1,in2 = inorder[0:mid_ind],inorder[mid_ind+1:len(inorder)]
        in1_set = set(in1)
        po1,po2 = [],[]
        for i in postorder:
            if i in in1_set:
                po1.append(i)
            else:
                if i == node_val:
                    continue
                else:
                    po2.append(i)
        node.left = self.rec(in1,po1)
        node.right = self.rec(in2,po2)
        return node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.rec(inorder,postorder)