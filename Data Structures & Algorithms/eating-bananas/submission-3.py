class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        speed starts from 1
        """
        speed = 1
        """
        for each elements of piles,
        save the output with a variable of sth
        math.ceil (pile / speed)
        """
        while True:
        
            time = 0
            for p in piles:
                time += math.ceil(p / speed)
            """
            1)if the sum of each output is less than or equal to h:
            <= because if the sum exceed 1, have to add speed
            2)bigger than h
            """
            if time <= h:
                return speed
            elif time > h:
                speed += 1
        return speed
        