class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        
        
        """

        n = len(prices)
        l, r = 0, 1
        base = 0
        while r < n:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                base = max(base, profit)
            else:
                l = r
            r += 1
        return base