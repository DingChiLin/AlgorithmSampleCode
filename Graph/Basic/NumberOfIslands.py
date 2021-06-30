from typing import List

class Solution:
    def dfs(self, x, y, N, M, grid):
        grid[x][y] = "0"
    
        for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= x < N and 0 <= y < M and grid[nx][ny] == "1":
                self.dfs(nx, ny, N, M, grid)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        N = len(grid)
        M = len(grid[0])
        for x in range(N):
            for y in range(M):
                if (grid[x][y] == "1"):
                    ans += 1
                    self.dfs(x, y, N, M, grid)

        return ans

s = Solution()
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(s.numIslands(grid))