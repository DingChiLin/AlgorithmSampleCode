from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        buy = [0] * (N + 1)
        sell = [0] * (N + 1)
        cool = [0] * (N + 1)
        buy[0] = -inf
        sell[0] = 0 
        cool[0] = 0
        for i in range(1, N + 1):
            cool[i] = max(cool[i-1], sell[i-1])
            buy[i] = max(buy[i-1], cool[i-1] - prices[i-1])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i-1])
        return max(cool[-1], sell[-1])

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        c, b, s = 0, -inf, -inf 
        for p in prices:
            c, b, s = max(c, s), max(b, c-p), max(s, b + p)
        return max(c, s)

s = Solution()
prices = [1,2,3,0,2]
print(s.maxProfit(prices))