from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self,node):
        if not node:
            return []

        ans = [[]]
        queue = deque([(node,0)])
        current,parity = 0,0
        while len(queue) > 0:
            ele = queue[-1] if parity else queue[0]
            if ele[1] != current:
                current = ele[1]
                parity = parity^1
                ans.append([])
                continue

            # print(queue)
            print(f"Current node value: {ele[0].val}, Level: {ele[1]}, Parity: {parity}")  # Debug statement
            ele = queue.pop() if parity else queue.popleft()
            # if ele[0] is None:
            #     print("Encountered a None node")  # Debug statement
            #     continue

            ans[-1].append(ele[0].val)
            if parity:
                if ele[0].right is not None:
                    if parity:
                        queue.appendleft((ele[0].right,ele[1]+1))

                    else:
                        queue.append((ele[0].right,ele[1]+1))


                if ele[0].left is not None:
                    if parity:
                        queue.appendleft((ele[0].left,ele[1]+1))

                    else:
                        queue.append((ele[0].left,ele[1]+1))

                continue

            if ele[0].left is not None:
                if parity:
                    queue.appendleft((ele[0].left,ele[1]+1))

                else:
                    queue.append((ele[0].left,ele[1]+1))

            if ele[0].right is not None:
                if parity:
                    queue.appendleft((ele[0].right,ele[1]+1))

                else:
                    queue.append((ele[0].right,ele[1]+1))

        return ans

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.bfs(root)