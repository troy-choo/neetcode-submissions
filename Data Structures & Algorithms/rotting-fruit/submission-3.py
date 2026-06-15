class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # 1. 초기 상태 스캔: rotten enqueue, fresh count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        minutes = -1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        grid[nr][nc] == 1   # fresh일 때만 전염 가능
                    ):
                        grid[nr][nc] = 2   # 썩게 만든다
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1

        # 3. 아직 fresh 남아 있으면 실패
        return minutes if fresh == 0 else -1