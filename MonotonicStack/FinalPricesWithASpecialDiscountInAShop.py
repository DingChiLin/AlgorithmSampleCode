from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        ans = [0 for i in range(N)]
        stack = []
        for i in range(N):
            while stack and prices[i] <= prices[stack[-1]]:
                poped_index = stack.pop()
                ans[poped_index] = prices[poped_index] - prices[i]
            stack.append(i)
        for i in stack:
            ans[i] = prices[i]
        return ans

s = Solution()
prices = [8,4,6,2,3]
print(s.finalPrices(prices))