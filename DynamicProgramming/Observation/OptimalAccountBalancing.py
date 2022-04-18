from math import inf
from typing import List
from collections import defaultdict

class Solution:
    def min_transfer_step(self, amounts):
        N = len(amounts)
        dp = [0 for i in range(1<<N)]
        sum_value = [0 for i in range(1<<N)]

        for mask in range(1, 1<<N):
            bit = 1
            max_set_cnt = 0
            for i in range(N):
                if mask & bit:
                    sum_value[mask] += amounts[i]
                    max_set_cnt = max(max_set_cnt, dp[mask ^ bit])
                bit <<= 1
            if sum_value[mask] == 0:
                dp[mask] = max_set_cnt + 1
            else:
                dp[mask] = max_set_cnt

        return N - dp[(1<<N)-1]

    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = defaultdict(int)
        for fro, to, amount in transactions:
            balance[fro] -= amount
            balance[to] += amount

        amounts = [value for value in balance.values() if value != 0]
        return self.min_transfer_step(amounts)

S = Solution()
print(S.min_transfer_step([-220, -200, -30, 220, 230]))