class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        starting from (0, 0) to (len(grid) - 1, len(grid) - 1)
        return the length of the shortest clear path - level matters
        """
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0],[0, 1],[-1, 0],[0, -1],
                      [1, 1],[1, -1],[-1, 1],[-1, -1]]
        visited = set()
        queue = deque()
        n = len(grid)

        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        queue.append((0, 0))
        visited.add((0, 0))
        length = 1

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                if row == n - 1 and col == n - 1:
                    return length

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 1):
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return -1
