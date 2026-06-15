class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequency - set
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        #count = {1:3, 2:2, 3:1}
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()
        #arr = [[1, 3], [2, 2], [3, 1]]
        #  cnt num
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

