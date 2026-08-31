class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                later = stack.pop()
                first = stack.pop()
                stack.append(first - later)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                later = stack.pop()
                first = stack.pop()
                stack.append(int(first / later))
            else:
                stack.append(int(c))
        return stack[0]