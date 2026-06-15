class Solution:
    def countSubstrings(self, s: str) -> int:
        length = 0
        count = 0
        for i in range(len(s)):
            #odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = (r - l + 1)
                count += 1
                l -= 1
                r += 1

            #even 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = (r - l + 1)
                count += 1
                l -= 1
                r += 1
        return count