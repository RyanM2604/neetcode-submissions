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
        curr = head
        lookup = {}

        while curr:
            lookup[curr] = Node(curr.val)
            curr = curr.next

        dummy = Node(0)
        new_curr = dummy
        curr = head

        while curr:
            new_curr.next = lookup[curr]
            if curr.next:
                new_curr.next.next = lookup[curr.next]
            if curr.random:
                new_curr.next.random = lookup[curr.random]

            curr = curr.next
            new_curr = new_curr.next
        
        return dummy.next
        
