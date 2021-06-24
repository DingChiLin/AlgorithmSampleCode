from typing import List

class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, x, y, grid, remain):
        if grid[x][y] == 2:
            if remain == 0:
                self.ans += 1
            return

        grid[x][y] = -1
        N = len(grid)
        M = len(grid[0])
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] >= 0:
                self.dfs(nx, ny, grid, remain - 1)
        grid[x][y] = 0

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        start = []
        remain = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    remain += 1
                if grid[x][y] == 1:
                    start = [x, y]
        self.dfs(start[0], start[1], grid, remain + 1)
        return self.ans

s = Solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
print(s.uniquePathsIII(grid))