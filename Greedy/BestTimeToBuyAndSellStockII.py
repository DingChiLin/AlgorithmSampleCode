from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                ans += diff
        return ans

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))