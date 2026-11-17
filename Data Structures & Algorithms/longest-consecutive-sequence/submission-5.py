class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        filtered = set(nums)
        for n in filtered:
            if n - 1 not in filtered:
                streak = 1
                while n + streak in filtered:
                    streak += 1
                length = max(length, streak)
        return length