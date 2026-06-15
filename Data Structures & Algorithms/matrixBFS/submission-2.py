class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        no_such_path = -1
        n = len(grid)
        q.append((0, 0))
        visited.add((0, 0))
        length = 0

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 1):
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        return no_such_path
        
        