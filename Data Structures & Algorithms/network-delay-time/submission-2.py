class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = [] #starting node
        for u, v, t in times:
            adj[u].append([v, t])
        """
        adj = {1:2,4 2:3 3:4 4:}
        """
        shortest = {}
        minHeap = [[0, k]]
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 in shortest: 
                    continue
                heapq.heappush(minHeap, [w1 + w2, n2])
        """
        {1:0 2:1 3:2 4:3}
        """
        if len(shortest) == n:
            return max(shortest.values())
        else:
            return -1
