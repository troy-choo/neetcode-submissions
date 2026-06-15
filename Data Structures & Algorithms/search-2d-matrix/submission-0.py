class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix), len(matrix[0])

        for row in range(i):
            for col in range(j):
                if matrix[row][col] == target:
                    return True
        return False