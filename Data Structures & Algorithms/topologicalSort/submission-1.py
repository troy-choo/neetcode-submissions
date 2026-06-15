class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v in edges:
            adj[u].append(v)
        """
        n = 6, adj = {0:, 1:, 2:3, 3:1, 4:0,1, 5:0,2}
        """
        
        visiting = set()
        topSort = []

        def dfs(u):
            if adj[u] == []:
                return True
            if u in visiting:
                return False
            visiting.add(u)

            for v in adj[u]:
                if not dfs(v):
                    return False #cycle
            visiting.remove(u)
            adj[u] = []
            topSort.append(u)
            return True


        for i in range(n):
            if not dfs(i):
                return []
        topSort.reverse()
        return topSort