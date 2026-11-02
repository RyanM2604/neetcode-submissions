# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # [0 -> 1 -> 2 -> 3], [6 -> 5 -> 4]

        first, second = head, prev

        while first and second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        