from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self,start):
        ans_dict = {}
        queue = deque([(start,0,0)])
        while len(queue) > 0:
            ele,level,depth = queue.popleft()
            if level in ans_dict:
                now = [(ele.val,depth)]
                while len(ans_dict[level]) > 0:
                    if ans_dict[level][-1][1] == depth:
                        popped_ele = ans_dict[level].pop()
                        now.append(popped_ele)

                    else:
                        break

                now.sort()
                ans_dict[level] = ans_dict[level]+now

            else:
                ans_dict[level] = [(ele.val,depth)]

            if ele.left:
                queue.append((ele.left,level-1,depth+1))

            if ele.right:
                queue.append((ele.right,level+1,depth+1))

        return ans_dict

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans_dict = self.bfs(root)
        my_keys = list(ans_dict.keys())
        my_keys.sort()
        ans = []
        for i in my_keys:
            cur_list = ans_dict[i]
            res = [j[0] for j in cur_list]
            ans.append(res)

        return ans
