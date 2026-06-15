class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        length = 0

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or 
                        nr >= ROWS or nc >= COLS or
                        grid[nr][nc] == 1 or (nr, nc) in visit):
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        return -1

        