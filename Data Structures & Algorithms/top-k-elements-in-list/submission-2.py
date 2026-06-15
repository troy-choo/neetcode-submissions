class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        for num in nums:
            count[num] += count.get(num, 0) + 1
        #count e.g. {1:1, 2:2, 3:3}
        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort()
        #arr = [[1, 1], [2, 2], [3, 3]] freq, num
        while len(arr) > k:
            arr.pop(0)
        return [num for freq, num in arr]
        