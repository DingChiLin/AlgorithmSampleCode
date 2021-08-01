from typing import List

# Two Pointer: Solution 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        i = 0
        ans = 0
        for j in range(N):
            ans = max(ans, prices[j] - prices[i])
            if prices[j] < prices[i]:
                i = j
        return ans

# Two Pointer: Solution 2
from math import inf
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        min_value = prices[0]
        ans = -inf
        for i in range(N):
            ans = max(ans, prices[i] - min_value)
            min_value = min(min_value, prices[i])
        return ans