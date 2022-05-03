from typing import List

class Solution:
    def dfs(self, x, y, matrix, visited, dp):
        visited.add((x, y))
        N = len(matrix)
        M = len(matrix[0])
        
        for nx, ny in [[x-1,y], [x+1,y], [x, y-1], [x, y+1]]:
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] > matrix[x][y]:
                if (nx, ny) not in visited:
                    self.dfs(nx, ny, matrix, visited, dp)
                dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        visited = set()
        dp = [[1 for j in range(M)] for _ in range(N)]
        for x in range(N):
            for y in range(M):
                if (x, y) not in visited:
                    self.dfs(x, y, matrix, visited, dp)		
        return max([max(row) for row in dp])
