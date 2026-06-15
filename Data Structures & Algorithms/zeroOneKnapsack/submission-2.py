class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        return self.dfsHelper(0, profit, weight, capacity)

    def dfsHelper(self, i, profit, weight, capacity):
        if i == len(profit):
            return 0
        
        #skipping item i
        maxProfit = self.dfsHelper(i + 1, profit, weight, capacity)

        #including item i
        newCapacity = capacity - weight[i]
        if newCapacity >= 0:
            p = profit[i] + self.dfsHelper(i + 1, profit, weight, newCapacity)
            maxProfit = max(p, maxProfit)
        return maxProfit
