class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            
            b = dfs()
            a = dfs()

            if token == "+":
                return a + b
            elif token == "-":
                return a - b
            elif token == "*":
                return a * b
            elif token == "/":
                return int(a / b)
        
        return dfs()