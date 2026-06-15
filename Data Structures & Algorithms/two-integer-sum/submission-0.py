class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, n in enumerate(nums):
            seen[n] = i

        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen and seen[complement] != i:
                return [i, seen[complement]]