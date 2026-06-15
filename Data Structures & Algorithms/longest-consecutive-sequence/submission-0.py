class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        1. length of the consecutive seq in an unsorted array of integers,
        2. O(n) time


        3. when array is empty return 0
        4. ignore duplicates
        5. negative numbers okay
        [1,2,3,4,  0 0. 0 0, 5,6,7,8,9,10,11 ]

        
        
        """
        num_set = set(nums)
        length = 0 #by default
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                streak = 1

                while current + 1 in num_set:
                    current += 1
                    streak += 1
                length = max(length, streak)
        return length