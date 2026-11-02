# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0

        while curr:
            curr = curr.next
            length += 1
        
        target = length - n
        curr = head
        prev = None

        while target > 0:
            prev = curr
            curr = curr.next
            target -= 1

        if prev is None:  # removing head node
            return head.next
        else:
            prev.next = curr.next

        return head

