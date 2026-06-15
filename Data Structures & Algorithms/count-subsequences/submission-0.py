class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        
        dp = {}
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s): #t must be finished earlier than s does.
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = dfs(i + 1, j) #either include i or exclude it, and this is excluding first
            if s[i] == t[j]: #include i
                res += dfs(i + 1, j + 1)
            dp[(i, j)] = res
            return res

        return dfs(0, 0)