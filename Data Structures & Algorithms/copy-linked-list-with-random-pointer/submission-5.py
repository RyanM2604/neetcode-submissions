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
        
        lookup = {}

        # first pass: create node copies
        curr = head
        while curr:
            lookup[curr] = Node(curr.val)
            curr = curr.next
        
        # second pass: wire up next/ random with map copies
        curr = head
        while curr:
            if curr.next:
                lookup[curr].next = lookup[curr.next]
            if curr.random: #if it has a random ptr at all
                lookup[curr].random = lookup[curr.random]
            curr = curr.next
        
        return lookup[head]
    
        # Input: [[3,null],[7,3],[4,0],[5,1]]
        # lookup