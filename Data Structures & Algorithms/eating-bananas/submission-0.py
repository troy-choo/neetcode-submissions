class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def hours_needed(k):
            total = 0
            for pile in piles:
                total += (pile + k - 1)// k
            return total
    
        while left <= right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left