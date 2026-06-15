"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} #we are going to store oldnode : newnode in a dictionary 
        def dfs(oldNode):
            #basecase, if already stored
            if oldNode in oldToNew:
                return oldToNew[oldNode]
            #if not stored yet,
            
            newNode = Node(oldNode.val)
            oldToNew[oldNode] = newNode
            
            for nei in oldNode.neighbors:
                newNode.neighbors.append(dfs(nei))
            return newNode

        return dfs(node) if node else None