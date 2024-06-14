"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
            
        cur = head
        while cur != None:
            new_node = Node(cur.val,cur.next,None)
            next_node = cur.next
            cur.next = new_node
            new_node.next = next_node
            cur = next_node

        cur = head
        new_head = head.next
        while cur != None:
            next_node = cur.next.next
            random_ptr = None if cur.random is None else cur.random.next
            cur.next.random = random_ptr
            cur = next_node

        cur = head
        while cur != None:
            next_node = cur.next.next
            next_node_for_copy = None if next_node is None else next_node.next
            copied_node = cur.next
            copied_node.next = next_node_for_copy
            cur.next = next_node
            cur = next_node

        return new_head
