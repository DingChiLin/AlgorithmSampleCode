from typing import List

# Basic DP solution
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = int(obstacleGrid[i][j] == 0)
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

# Little trick: add one more column and row for DP
class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        dp = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        dp[0][1] = 1
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[M][N]

s = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(s.uniquePathsWithObstacles(obstacleGrid))