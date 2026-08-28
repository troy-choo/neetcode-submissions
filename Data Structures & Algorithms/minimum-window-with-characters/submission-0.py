class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = {}
        for c in t:
            need[c] = 1 + need.get(c, 0)
        
        window = {}
        have = 0
        required = len(need)

        res = ""
        res_len = float("inf")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
        
            if c in need and window[c] == need[c]:
                have += 1
            
            while have == required:
                if r - l + 1 < res_len:
                    res = s[l: r + 1]
                    res_len = r - l + 1

                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                
                l += 1
        return res