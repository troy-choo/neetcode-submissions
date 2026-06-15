class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1 #count subarrays starting from index 0
        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            #if curr_sum - k seen before, add its count to the result
            count += prefix_sums[curr_sum - k]
            prefix_sums[curr_sum] += 1
        
        return count