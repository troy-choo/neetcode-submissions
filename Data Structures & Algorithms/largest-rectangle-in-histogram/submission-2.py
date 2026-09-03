class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                res = max(res, height * width)
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            width = len(heights) - i
            res = max(res, width * h)

        return res