class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1 + dic.get(n, 0)
            dic[n] += 1
        sorted_dic = sorted(dic, key=dic.get, reverse=True)
        return sorted_dic[:k]