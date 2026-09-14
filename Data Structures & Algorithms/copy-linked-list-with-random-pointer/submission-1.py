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
        oldToCopy = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            if curr.next is not None:
                copy.next = oldToCopy[curr.next]
            else:
                copy.next = None
            
            if curr.random is not None:
                copy.random = oldToCopy[curr.random]
            else:
                copy.random = None
            curr = curr.next
        return oldToCopy[head]
        
        
        
