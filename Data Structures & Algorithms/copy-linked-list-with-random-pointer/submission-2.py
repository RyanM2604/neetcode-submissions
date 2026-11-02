class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        lookup = {}

        # 1st pass: create all nodes
        curr = head
        while curr:
            lookup[curr] = Node(curr.val)
            curr = curr.next

        # 2nd pass: assign next and random
        curr = head
        while curr:
            if curr.next:
                lookup[curr].next = lookup[curr.next]
            if curr.random:
                lookup[curr].random = lookup[curr.random]
            curr = curr.next

        return lookup[head]