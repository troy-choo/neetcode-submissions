class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]


    """
    [3, 5, 2, 1, 6, 4]
    [1, 2, 3, 4, 5, 6]
     2, 1, 4, 3, 6, 5
     time complexity : O(NlogN) 



    i = 0: 3 <= 5
    i = 1: 5 >= 2
    i = 2: 2 <= 1 (swap) [3, 5, 1, 2, 6, 4]
    i = 3: 2 >= 6 (swap) [3, 5, 1, 6, 2, 4]
    i = 4: 2 <= 4 (ok)

    output: [3, 5, 1, 6, 2, 4] (valid)


    
    
    """