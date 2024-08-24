# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack1 = [root]
        while stack1[-1].left:
            ele = stack1[-1]
            if ele.left:
                stack1.append(ele.left)

        stack2 = [root]
        while stack2[-1].right:
            ele = stack2[-1]
            if ele.right:
                stack2.append(ele.right)

        ans = False
        # print(stack1)
        # print(stack2)
        while len(stack1) > 0 and len(stack2) > 0 and stack1[-1] != stack2[-1]:
            node1 = stack1[-1].val
            node2 = stack2[-1].val

            if node1+node2 == k:
                ans = True
                break

            if node1+node2 < k:
                ele = stack1[-1]
                stack1.pop()
                if ele.right:
                    stack1.append(ele.right)
                    while stack1[-1].left:
                        ele = stack1[-1]
                        if ele.left:
                            stack1.append(ele.left)

                continue

            ele = stack2[-1]
            stack2.pop()
            if ele.left:
                stack2.append(ele.left)
                while stack2[-1].right:
                    ele = stack2[-1]
                    if ele.right:
                        stack2.append(ele.right)
            

        return ans