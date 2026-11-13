class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        removeDuplicate = set(nums)
        if len(nums) != len(removeDuplicate):
            return True
        return False