from typing import List
from math import inf

'''
dp[i] = max([sum(stoneValue[i:i + k]) - dp[i + k] for k in range(1, 4)])
'''
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        dp = [-inf for _ in range(N + 1)]
        dp[N] = 0
        for i in range(N - 1, -1, -1):
            for k in range(1, 4):
                if i + k <= N:
                    dp[i] = max(dp[i], sum(stoneValue[i:i + k]) - dp[i + k])
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

s = Solution()
values = [1,2,3,7]
values = [1,2,3,-9]
values = [1,2,3,6]
print(s.stoneGameIII(values))