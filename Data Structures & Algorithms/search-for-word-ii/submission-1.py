class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        
        rows, cols = len(board), len(board[0])
        res = []

        def dfs(i, j, node):
            char = board[i][j]
            if char not in node.children:
                return
            nxt = node.children[char]
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None 

            board[i][j] = '#' #mark as visited
            for x, y in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < rows and 0 <= y < cols and board[x][y] != '#':
                    dfs(x, y, nxt)
            board[i][j] = char #restoring after visited.\

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        return res





