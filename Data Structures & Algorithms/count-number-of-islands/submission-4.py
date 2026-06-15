class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        island = 0

        #Iterative_dfs
        def dfs(r, c): 
            stack = [] #Last In First Out
            stack.append((r, c))
            grid[r][c] = "0"

            while stack:
                row, col = stack.pop()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    #edge cases
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == "0"):
                        continue
                    grid[nr][nc] = "0"
                    stack.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    island += 1

        return island


        