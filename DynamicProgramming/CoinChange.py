# [Leetcode 518](https://leetcode.com/problems/coin-change-2/)

from typing import List
import math

# bottom-up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount + 1):
            for n in coins:
                if i >=n:
                    dp[i] = min(dp[i], dp[i-n] + 1)
        return dp[amount] if dp[amount] < math.inf else -1

s = Solution()
coins = [1,2,5]
amount = 11
print(s.coinChange(coins, amount))
