class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        0 fresh fruit remaining
        
        
        """   
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr in range(len(grid)) and nc in range(len(grid[0])) and
                    grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1