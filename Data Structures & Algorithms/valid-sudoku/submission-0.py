class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checking rows
        for row in board:
            seen = set()
            for val in row:
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
        
        #checking cols
        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val != '.':
                    if val in seen:
                        return False
                    seen.add(val)
        
        #checking 3x3 subboxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != '.':
                            if val in seen:
                                return False
                            seen.add(val)
        return True

