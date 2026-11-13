class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            rest = target - n 
            if rest in dic:
                return [dic[rest], i]
            dic[n] = i