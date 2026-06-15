class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        using dfs, since when we find 1, keep find its neighbors
        """
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        max_area = 0

        def bfs(r, c):
            #initiate the queue & add to the queue
            q = deque() 
            grid[r][c] = 0
            q.append((r, c))
            area = 1

            while q:
                #popleft() and check if its valid
                row, col = q.popleft()
                #4 directions of the popped grid
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 0):
                        continue
                    grid[nr][nc] = 0
                    q.append((nr, nc))
                    area += 1
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        return max_area
