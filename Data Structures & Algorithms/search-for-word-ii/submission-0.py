class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(row, col, word, idx, visited):
            if idx == len(word):
                return True
            if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0])
                or visited[row][col] or board[row][col] != word[idx]):
                return False
            visited[row][col] = True
            
            #explore neighbors
            found = (dfs(row + 1, col, word, idx + 1, visited) or
                     dfs(row - 1, col, word, idx + 1, visited) or
                     dfs(row, col + 1, word, idx + 1, visited) or
                     dfs(row, col - 1, word, idx + 1, visited))
            visited[row][col] = False
            return found 
        
        res = []
        for word in words:
            found = False
            for row in range(len(board)):
                for col in range(len(board[0])):
                    visited = [[False] * len(board[0]) for _ in range(len(board))]
                    if dfs(row, col, word, 0, visited):
                        res.append(word)
                        found = True
                        break
                if found:
                    break
        return res

            