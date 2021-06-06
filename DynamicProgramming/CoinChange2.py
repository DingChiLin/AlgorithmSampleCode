# [Leetcode 518](https://leetcode.com/problems/coin-change-2/)

from typing import List
from collections import defaultdict

# bottom-up (1D Array)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1

        for n in coins:
            for i in range(amount + 1):
                if i >=n:
                    dp[i] += dp[i-n]
        return dp[amount]

# bottom-up (2D Array)
class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 1

        for i, c in enumerate(coins):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i-1][j]
                if j >= c:
                    dp[i][j] += dp[i][j-c]
        return dp[len(coins)-1][amount]

# top-down
class Solution3:
    def __init__(self):
        self.dp = None

    def helper(self, nums, start, remain):
        if start == len(nums):
            return 0
        if remain < 0:
            return 0
        if self.dp[start][remain] != None:
            return self.dp[start][remain]

        if remain == 0:
            self.dp[start][remain] = 1
            return 1

        self.dp[start][remain] = self.helper(nums, start + 1, remain) + self.helper(nums, start, remain - nums[start])
        return self.dp[start][remain]

    def change(self, amount: int, coins: List[int]) -> int:
        self.dp = [[None for _ in range(amount+1)] for _ in range(len(coins))]
        return self.helper(coins, 0, amount)

# Consider all possible Combination (TLE)
class Solution4_TLE:
    def __init__(self):
        self.ans = []

    def find(self, start, nums, target, comb):
        if target == 0: # find an valid combination
            self.ans += 1

        if target <= 0: # pruning
            return

        for i in range(start, len(nums)):
            comb.append(nums[i])
            self.find(i, nums,  target - nums[i], comb)
            comb.pop()

    def change(self, amount: int, coins: List[int]) -> int:
        self.ans = 0
        self.find(0, coins, amount, [])
        return self.ans


s = Solution()
amount = 5
coins = [1,2,5]
print(s.change(amount, coins))
