from typing import List
from math import inf

# 2D Array
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0 for _ in range(N + 1)] for _ in range(2)]

        dp[0][0] = -inf # buy
        dp[1][0] = 0 # sell
        maxProfit = 0
        for i in range(1, N + 1):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] - prices[i-1])
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] + prices[i-1])
            maxProfit = max(maxProfit, dp[1][i])
        print(dp)
        return maxProfit

# 2 * 1D Array
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        buy = [0 for _ in range(N + 1)]
        sell = [0 for _ in range(N + 1)]

        buy[0] = -inf
        sell[0] = 0
        for i in range(1, N + 1):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i-1])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i-1])

        return max(buy[-1], sell[-1])

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))