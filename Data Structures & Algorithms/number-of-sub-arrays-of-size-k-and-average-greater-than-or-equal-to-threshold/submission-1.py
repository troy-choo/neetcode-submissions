class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        arr = [2,2,2,2,5,5,5,8], k = 3
               0 1 2 3 4 5 6 7
                         L << last L
        curSum = [0] + [1] (+ need to add 2 next)
        """ 
        res = 0
        curSum = sum(arr[:k - 1])
        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1] #keep adding next index
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[L] #removing first index in the window
        return res
            