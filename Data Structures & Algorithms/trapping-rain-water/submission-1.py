class Solution:
    def trap(self, height: List[int]) -> int:
        """
        [0,2,0,3,1,0,1,3,2,1]
         0 - 0
         2 - 2
         2 - 0 (+)
         3 - 3
         3 - 1 (+)
         3 - 0 (+)
         3 - 1 (+)
         3 - 3
         2 - 2
         1 - 1
        """
        l = 0
        r = len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r: #nothings left when terminated
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res