# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rec(self,node):
        if node.next == None:
            self.head = node
            return node

        cur = self.rec(node.next)
        cur.next = node
        return node


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        self.head = head
        node = self.rec(head)
        node.next = None
        return self.head