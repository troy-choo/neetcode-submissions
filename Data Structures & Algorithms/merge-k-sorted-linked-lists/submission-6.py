# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        def mergeTwoLists(list1, list2):
            res = ListNode(0)
            cur = res
            while list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next

            if list1:
                cur.next = list1
            else:
                cur.next = list2

            return res.next




        if not lists:
            return None
        
        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                merged = mergeTwoLists(list1, list2)
                merged_lists.append(merged)

            lists = merged_lists

        return lists[0]