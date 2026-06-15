class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        M = capacity
        cache = [[-1] * (M + 1) for _ in range(N)]
        return self.dfsHelper(0, profit, weight, capacity, cache)

    def dfsHelper(self, i, profit, weight, capacity, cache):
        if i == len(profit):
            return 0
        if cache[i][capacity] != -1:
            return cache[i][capacity]
        
        #skipping item i
        cache[i][capacity] = self.dfsHelper(i + 1, profit, weight, capacity, cache)

        #including item i
        newCapacity = capacity - weight[i]
        if newCapacity >= 0:
            p = profit[i] + self.dfsHelper(i + 1, profit, weight, newCapacity, cache)
            cache[i][capacity] = max(p, cache[i][capacity])
        return cache[i][capacity]
