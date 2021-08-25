from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # add a zero at tail for convenience
        N = len(heights)
        stk = []
        ans = 0
        for i in range(N):
            while(stk and heights[stk[-1]] > heights[i]):
                h = heights[stk[-1]]
                w = 0
                stk.pop()
                if not stk:
                    w = i
                else:
                    w = i - stk[-1] - 1
                ans = max(ans, h * w)
            stk.append(i)
        return ans

s = Solution()
heights = [2,1,5,6,2,3]
print(s.largestRectangleArea(heights))
