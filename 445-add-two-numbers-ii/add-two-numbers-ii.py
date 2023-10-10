# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self,l):
        prev,gg = None,0
        while l != None:
            temp = l.next
            l.next = prev
            prev = l
            l = temp
            gg += 1

        self.c = gg
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1,node2 = l1,l2
        self.c,c1,c2 = 0,0,0
        p1 = self.helper(l1)
        c1 = self.c
        p2 = self.helper(l2)
        c2 = self.c
        carry = 0
        if c2 < c1:
            p1,p2 = p2,p1

        head = p2
        prev = None
        while p1 != None or p2 != None:
            v1,v2 = 0,0
            if p1 != None:
                v1 = p1.val

            if p2 != None:
                v2 = p2.val

            gg = str(v1+v2+carry)
            # print(p2.val,"LL")
            if len(gg) == 2:
                carry = int(gg[0])
                p2.val = int(gg[-1])

            else:
                carry = 0
                p2.val = int(gg)

            if p1 != None:
                p1 = p1.next

            if p2 != None:
                temp = p2.next
                p2.next = prev
                prev = p2
                p2 = temp

        if carry != 0:
            tt = ListNode(val=carry)
            tt.next = prev
            return tt

        return prev

        

