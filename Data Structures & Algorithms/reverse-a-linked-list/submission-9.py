# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        currHead = head
        if head.next:
            currHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return currHead