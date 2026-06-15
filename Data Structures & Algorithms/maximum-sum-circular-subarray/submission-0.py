class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        for i in range(n):
            curSum = 0
            for j in range(i, i + n):
                curSum += nums[j % n]
                res = max(res, curSum)
        return res