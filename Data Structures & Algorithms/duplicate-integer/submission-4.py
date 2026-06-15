class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            seen.add(n)
        if len(nums) != len(seen):
            return True

        return False