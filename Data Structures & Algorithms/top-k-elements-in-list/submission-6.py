class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        frequency_sorted = sorted(count, key=lambda n: count[n], reverse=True)
        return frequency_sorted[:k]