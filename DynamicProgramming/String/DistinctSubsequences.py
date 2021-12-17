from typing import List

# 2D Array
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(N):
            dp[0][i] = 1
        for i in range(1, M+1):
            for j in range(1, N+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[M][N]

# 1D Array
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)
        dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        for i in range(N):
            dp[0][i] = 1
        for i in range(1, M+1):
            for j in range(1, N+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[M][N]

s = Solution()
ss = "babgbag"
t = "bag"
print(s.numDistinct(ss, t))