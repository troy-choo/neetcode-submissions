class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        using dfs, since when we find 1, keep find its neighbors
        """
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_area = 0

        #iterative DFS
        def dfs(r, c): 
            stack = []
            stack.append((r, c))
            grid[r][c] = 0
            area = 1

            while stack:
                row, col = stack.pop()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0): #edge cases
                        continue
                    grid[nr][nc] = 0
                    stack.append((nr, nc))
                    area += 1
                    
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area