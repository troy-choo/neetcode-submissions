class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
                 0123456789
        let s = "abcabcdeab"
        l pointer should be updated and track 
                    
        """
        l = 0
        res = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res



