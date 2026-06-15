class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in closeToOpen:
                if closeToOpen[c] == stack[-1]:
                    stack.pop()
            else:
                stack.append(c)    
        return True if not stack else False
