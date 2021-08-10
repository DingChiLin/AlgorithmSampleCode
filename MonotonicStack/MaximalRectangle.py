from typing import List

class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        heights = A + [0] # add a zero at end for convenience
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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        if N == 0:
            return 0
        M = len(matrix[0])
        heights = [0 for _ in range(M)]
        ans = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.largestRectangleArea(heights))
        return ans

s = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(s.maximalRectangle(matrix))