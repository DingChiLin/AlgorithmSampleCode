from typing import List
from itertools import accumulate

'''
dp[i][j] = max(sum(piles[i+1:j+1]) - dp[i+1][j], sum(piles[i:j]) - dp[i][j-1])
'''

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        N = len(stones)
        preSum = [0] + list(accumulate(stones))
        dp = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N-1, -1, -1):
            for j in range(i + 1, N):
                dp[i][j] = max(
                    preSum[j+1] - preSum[i+1] - dp[i+1][j],
                    preSum[j] - preSum[i] - dp[i][j-1],
                )
        return dp[0][N-1]

s = Solution()
stones = [7,90,5,1,100,10,10,2]
stones = [5,3,1,4,2]
print(s.stoneGameVII(stones))