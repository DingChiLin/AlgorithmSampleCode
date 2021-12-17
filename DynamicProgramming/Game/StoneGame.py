from typing import List

# Bottom-Up
'''
dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
'''
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = piles[i]

        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        
        return dp[0][N-1] > 0

# Top-Down
from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)

        @lru_cache(None)
        def dp(x, y):
            if x == y:
                return piles[x]
            return max(piles[x] - dp(x + 1, y), piles[y] - dp(x, y - 1)) 
        return dp(0, N-1) > 0

s = Solution()
piles = [5,3,4,5]
print(s.stoneGame(piles))