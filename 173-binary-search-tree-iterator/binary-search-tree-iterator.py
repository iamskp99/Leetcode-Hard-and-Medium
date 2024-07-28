# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        while node is not None:
            self.stack.append(node)
            node = node.left        

    def next(self) -> int:
        node = self.stack.pop()
        data = node.val
        cur = node.right
        while cur is not None:
            self.stack.append(cur)
            cur = cur.left    

        return data

    def hasNext(self) -> bool:
        if len(self.stack) != 0:
            return True

        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()