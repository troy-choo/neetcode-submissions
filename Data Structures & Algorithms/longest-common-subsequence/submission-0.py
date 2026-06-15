class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        cat
        c - a, t
        a - t
        t - []
        crabt
        c - r, a, b, t
        r - a, b, t
        a - b, t
        b - t
        t - []
        
        memoize the possible outcomes by dfs and return num of common subsequences

        """
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)