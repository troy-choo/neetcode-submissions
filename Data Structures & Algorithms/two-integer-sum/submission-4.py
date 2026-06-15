class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = {}
        for i, n in enumerate(nums):
            map_[n] = i
        
        for i, n in enumerate(nums):
            complement = target - n
            if complement in map_ and map_[complement] != i:
                return [i, map_[complement]]
            
        return []