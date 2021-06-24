from typing import List
from math import inf

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M = len(dungeon)
        N = len(dungeon[0])
        dp = [[-inf for _ in range(N + 1)] for _ in range(M + 1)]
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                max_possible = max(dp[i+1][j], dp[i][j+1])
                if max_possible == -inf:
                    dp[i][j] = min(dungeon[i][j], 0)
                else:
                    dp[i][j] = min(max_possible + dungeon[i][j], 0)
        
        return -min(dp[0][0], 0) + 1

s = Solution()
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(s.calculateMinimumHP(dungeon))