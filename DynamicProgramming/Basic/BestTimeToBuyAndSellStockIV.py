from typing import List
from math import inf

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if(len(prices) <= 1 or k < 1):
            return 0
        
        if(k > len(prices) / 2):
            profit = 0
            for i in range(1, len(prices)):
                profit += max(prices[i] - prices[i-1], 0)
                
            return profit
        else:
            buy = [-inf] * (k + 1)
            sell = [-inf] * (k + 1)     
            buy[0] = 0
            sell[0] = -prices[0]
            for p in prices:
                buy[0] = -inf
                sell[0] = 0
                for i in range(1, k+1):
                    buy[i] = max(buy[i], sell[i-1] - p)
                    sell[i] = max(sell[i], buy[i] + p)
            return sell[-1]

s = Solution()
k = 2
prices = [3,2,6,5,0,3]
print(s.maxProfit(k, prices))