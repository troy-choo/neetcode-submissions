class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        count = {}
        major = 0
        res = 0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            major = max(count[s[R]], major)

            while (R - L + 1) - major > k:
                count[s[L]] -= 1
                L += 1
            res = max(R - L + 1, res) 
            #valid, update the longest window size
        return res