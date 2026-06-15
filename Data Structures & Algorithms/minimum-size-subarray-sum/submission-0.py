class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        sum >= target; 0 if None
        """
        L = 0
        length = float('inf')
        contents = 0
        for R in range(len(nums)):
            contents += nums[R]
            while contents >= target:
                length = min(length, R - L + 1)
                contents -= nums[L]
                L += 1
        return 0 if length == float('inf') else length