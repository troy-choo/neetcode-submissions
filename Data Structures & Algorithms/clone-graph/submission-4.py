"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque()
        q.append(node)
        oldToNew = {}
        oldToNew[node] = Node(node.val)

        while q:
            oldNode = q.popleft()
            
            for nei in oldNode.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[oldNode].neighbors.append(oldToNew[nei])
        return oldToNew[oldNode]
