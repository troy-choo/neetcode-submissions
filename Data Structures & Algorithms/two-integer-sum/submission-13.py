class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            left = target - n
            if left in indices:
                return [indices[left], i]
        
            indices[n] = i
            
