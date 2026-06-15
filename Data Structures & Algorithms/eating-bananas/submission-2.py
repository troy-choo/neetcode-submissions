class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l + r) // 2 #starting standard

            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
