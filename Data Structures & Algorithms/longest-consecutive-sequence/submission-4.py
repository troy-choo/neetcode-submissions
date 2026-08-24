class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        for n in numSet:
            if n - 1 not in numSet:
                streak = 1
                while n + streak in numSet:
                    streak += 1
                length = max(streak, length)
        return length
