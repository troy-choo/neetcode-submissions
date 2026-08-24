class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seq = sorted(nums)
        res = []
        for i, n in enumerate(seq):
            if i > 0 and n == seq[i - 1]:
                continue

            l, r = i + 1, len(seq) - 1
            while l < r:
                threeSum = seq[l] + seq[r] + n
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, seq[l], seq[r]])
                    l += 1
                    r -= 1
                    while l < r and seq[l] == seq[l - 1]:
                        l += 1
        return res