class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v in edges:
            adj[u].append(v)
        """
        adj = {0:, 1:, 2:3, 3:1, 4:0,1, 5:0,2}, n = 6
        """
        topSort = []
        visited = set()
        visiting = set()

        def dfs(src):
            if src in visited:
                return True
            if src in visiting:
                return False

            visiting.add(src)

            for v in adj[src]:
                if not dfs(v):
                    return False
            visiting.remove(src)
            visited.add(src)
            topSort.append(src)
        
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()
        return topSort
