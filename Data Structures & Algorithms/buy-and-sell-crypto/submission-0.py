class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        bruteforce: max(j - i)
        
        
        """
        base = 0
        n = len(prices)
        for i in range(n):
            buy = prices[i]
            for j in range(i + 1, n):
                sell = prices[j]
                base = max(base, sell - buy)
        return base