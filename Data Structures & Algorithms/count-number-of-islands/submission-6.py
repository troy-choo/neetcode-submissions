class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #define the boundary we're allowed to move
        ROWS, COLS = len(grid), len(grid[0])
        """
        we are only interested in the number of islands; not the size of the island
        we don't need to return 1 + dfs(r+nr, c+nc) form << only applies to the case
        when we are interested in the size of the islands
        """
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        islands = 0

        def dfs(r, c):
            stack = [(r, c)] # iterative dfs uses stack to implement the dfs attribute
            grid[r][c] = "0" # mark as visited

            while stack:
                row, col = stack.pop() 
                """by popping last element from the stack, track the closest grid of 1
                check if that is possibly be longer
                """
                for dr, dc in directions: #checking the near grids of current row, col
                    nr, nc = row + dr, col + dc # nr, nc can be NWSE of the current row, col
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1"): #in condition
                        grid[nr][nc] = "0" #mark as visited
                        stack.append((nr, nc)) #put in stack again and repeat the iteration.
                        continue #else condition; if out of bound, continue the iteration with the other nr, nc

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1 #regardless how big the size would be; count 1
        return islands