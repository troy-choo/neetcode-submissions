class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        L = 0
        maxL, maxR = 0, 0

        for R in range(len(nums)):
            #special case sum is (-)
            if curSum < 0:
                curSum = 0
                L = R
            
            curSum += nums[R]
            if curSum > maxSum:
                maxSum = curSum
                maxL, maxR = L, R
        
        return maxSum