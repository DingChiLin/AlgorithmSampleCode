from typing import List
from itertools import accumulate
from math import inf

# Bottom-Up
'''
dp[i][m] = max([sum(piles[i:i+x]) - dp[i+x][max(m, x)] for x in range(1, 2*m+1)] )
'''
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        preSum = [0] + list(accumulate(piles))

        dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
        for i in range(N-1, -1, -1):
            for m in range(1, N+1):
                dp[i][m] = -inf
                for x in range(1, min(N-i+1, 2*m+1)):
                    v = preSum[i+x] - preSum[i]
                    dp[i][m] = max(dp[i][m], v - dp[i+x][max(m, x)])

        return (sum(piles) + dp[0][1])//2

# Top-Down
from functools import lru_cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(None)
        def dfs(start, M):
            if start == len(piles)-1:
                return 0
            score = 0
            maxScore = -inf
            for X in range(1, min(len(piles)-start, 2*M + 1)):
                index = start + X
                score += piles[index]
                maxScore = max(maxScore, score - dfs(index, max(M, X)))
            return maxScore
        return (sum(piles) + dfs(-1, 1))//2

s = Solution()
piles = [2,7,9,4,4]
piles = [1,2,3,4,5,100]
print(s.stoneGameII(piles))