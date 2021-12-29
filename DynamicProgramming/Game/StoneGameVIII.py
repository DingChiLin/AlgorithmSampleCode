from typing import List
from itertools import accumulate

'''
dp[i] = sum(piles[0:i+1]) - max(dp[i+1:N])
'''

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        N = len(stones)
        preSum = [0] + list(accumulate(stones))
        dp = [0 for i in range(N)]
        dp[N-1] = sum(stones)
        rightMax = dp[N-1]
        for i in range(N-2, -1, -1):
            dp[i] = preSum[i+1] - rightMax 
            rightMax = max(dp[i], rightMax)
        return max(dp[1:])

s = Solution()
# stones = [-1,2,-3,4,-5]
stones = [7,-6,5,10,5,-2,-6]
# stones = [-10,-12]
print(s.stoneGameVIII(stones))