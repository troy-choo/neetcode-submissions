class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
            
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0:
            default = False
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if (nr in range(ROWS) and
                                nc in range(COLS) and
                                grid[nr][nc] == 1):
                                grid[nr][nc] = 3 # arbitrary number
                                fresh -= 1
                                default = True
            
            if not default:
                return -1
            
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

            time += 1       

        return time