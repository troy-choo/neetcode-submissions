class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Brute Force
        n = len(nums)
        maxSum = nums[0]

        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                maxSum = max(curSum, maxSum)

        return maxSum
