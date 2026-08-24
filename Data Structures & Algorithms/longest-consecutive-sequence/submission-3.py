class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length = 0

        for n in num_set:
            if n - 1 not in num_set:
                curr = n
                streak = 1
                while curr + 1 in num_set:
                    curr += 1
                    streak += 1
                length = max(length, streak)
        return length