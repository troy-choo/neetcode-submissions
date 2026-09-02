class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                res = max(res, width * height)
                start = index
            stack.append((start, h))
    
        for index, height in stack:
            width = len(heights) - index
            res = max(res, height * width)

        return res