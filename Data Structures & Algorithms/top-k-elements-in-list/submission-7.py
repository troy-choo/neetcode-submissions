class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        
        sorted_nums = sorted(dic, key = dic.get, reverse=True)
        return sorted_nums[:k]