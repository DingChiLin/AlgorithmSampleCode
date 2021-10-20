from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        N = len(prices)
        discount = [0] * N
        stk = []
        for i in range(N):
            while stk and prices[i] <= prices[stk[-1]]:
                poped_index = stk.pop()
                discount[poped_index] = prices[i]
            stk.append(i)

        ans = [0] * N
        for i in range(N):
            ans[i] = prices[i] - discount[i]
        return ans

s = Solution()
prices = [8,4,6,2,3]
print(s.finalPrices(prices))