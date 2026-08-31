class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = 1 + need.get(c, 0)
        
        res = ""
        l = 0
        window = {}
        res_len = float("inf")
        have = 0
        required = len(need)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == required:
                if (r - l + 1) < res_len:
                    res_len = (r - l + 1)
                    res = s[l: r + 1]
            
                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
        return res


