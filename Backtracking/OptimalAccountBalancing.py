from math import inf
from typing import List
from collections import defaultdict

class Solution:
    def backtrack(self, amounts, index, step):
        N = len(amounts)
        # 已經跑完全部的人
        if index == N:
            self.min_step = min(self.min_step, step)
            return

        # 當前這個人已經被結清了，所以可以直接跳過
        if amounts[index] == 0:
            self.backtrack(amounts, index + 1, step)

        # 嘗試所有可能的人
        for i in range(index + 1, N):
            # 但僅挑狀態相反的人去結清（正的找負的，負的找正的）
            if amounts[i] * amounts[index] < 0: # 一個數學的小技巧
                amounts[i] += amounts[index]
                self.backtrack(amounts, index + 1, step + 1)
                amounts[i] -= amounts[index]

    def min_transfer_step(self, amounts):
        self.min_step = inf
        self.backtrack(amounts, 0, 0)
        return self.min_step

    def minTransfers(self, transactions: List[List[int]]) -> int:
        balanced = defaultdict(int)
        for giver, receiver, value in transactions:
            balanced[giver] -= value
            balanced[receiver] += value
        amounts = [amount for amount in balanced.values() if amount != 0]
        return self.min_transfer_step(amounts)

S = Solution()
print(S.min_transfer_step([-220, -200, -30, 220, 230]))