class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        checked = set()
        length = 0

        for R in range(len(s)):
            while s[R] in checked:
                checked.remove(s[L])
                L += 1
            checked.add(s[R])
            length = max(length, R-L+1)
        return length
