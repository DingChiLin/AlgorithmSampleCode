from typing import List
from math import inf, sqrt
'''
dp[i] = True if any([not dp[i + j * j] for j in range(n + 1)])
'''
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(1, n + 1):
                if i + j * j > n:
                    break
                if not dp[i + j * j]:
                    dp[i] = True
                    break
        return dp[0]

s = Solution()
n = 5
print(s.winnerSquareGame(n))