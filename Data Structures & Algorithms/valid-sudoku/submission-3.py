class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        for row in range(ROWS):
            seen = set()
            for col in range(COLS):
                val = board[row][col]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        for col in range(COLS):
            seen = set()
            for row in range(ROWS):
                val = board[row][col]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        for row in range(0, ROWS, 3):
            for col in range(0, COLS, 3):
                seen = set()
                for r in range(row, row + 3):
                    for c in range(col, col +3):
                        val = board[r][c]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True
