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
        if not head:
            return None
        
        curr = head
        lookup = {None: None}
        
        while curr:
            copy = Node(curr.val)
            lookup[curr] = copy
            curr = curr.next
        
        curr = head

        while curr:
            copy = lookup[curr]
            copy.next = lookup[curr.next]
            copy.random = lookup[curr.random]
            curr = curr.next
        
        return lookup[head]
        