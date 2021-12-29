from typing import List

class Solution:
    def check(self, grid):
        N = len(grid)
        M = len(grid[0])
        cnt = 0
        for x in range(1, N):
            for y in range(1, M-1):
                if grid[x][y] and grid[x-1][y]:
                    grid[x][y] = min(grid[x-1][y-1], grid[x-1][y+1]) + 1
                    cnt += grid[x][y] - 1 
        return cnt

    def countPyramids(self, grid: List[List[int]]) -> int:
        reversed_grid = []
        for i in range(len(grid)-1, -1, -1):
            reversed_grid.append(grid[i][:])
        cnt1 = self.check(grid)
        cnt2 = self.check(reversed_grid)
        return cnt1 + cnt2