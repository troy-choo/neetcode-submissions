class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == target:
                    return True
        return False