class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        """
        obstacle = 1, space = 0; starting from [0][0], [ROWS-1][COLS-1]
        return possible unique paths! to reach the bot-right corner
        unique path is + in DFS, have to reset the visited set each trial

        """
        memo = {}
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or obstacleGrid[r][c] == 1):
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            path_count = dfs(r + 1, c) + dfs(r, c + 1)
            memo[(r, c)] = path_count
            return memo[(r, c)]
            

        return dfs(0, 0)
