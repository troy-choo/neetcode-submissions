class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Total = 1
        zero_count = 0
        for num in nums:
            if num:
                Total *= num
            else:
                zero_count += 1
        if zero_count > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_count:
                res[i] = 0 if c else Total
            else:
                res[i] = Total // c
        return res
