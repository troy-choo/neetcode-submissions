class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        product = 1
        zero_count = 0

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product *= n
        
        for i, n in enumerate(nums):
            if zero_count >= 2:
                res[i] = 0
            elif zero_count == 1:
                if n == 0:
                    res[i] = product
                else:
                    res[i] = 0
            else:
                res[i] = product // n
        return res