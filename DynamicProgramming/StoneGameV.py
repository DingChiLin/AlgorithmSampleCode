from typing import List
from math import inf, sqrt
from itertools import accumulate

'''
1. dp[i][j] = (for each k): the smaller one between `sum(nums[i:k+1]) + dp[i][k]` and `sum(nums[k+1:j+1]) + dp[k+1][j]`
2. 上述做法會是 O(N^3)，還需要額外優化到 O(N^2logN) 或 O(N^2)
'''

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        N = len(stoneValue)
        preSum = [0] + list(accumulate(stoneValue))

        dp = [[-inf for _ in range(N)] for _ in range(N)]
        left = [[-inf for _ in range(N)] for _ in range(N)]
        right = [[-inf for _ in range(N)] for _ in range(N)]
        for i in range(N):
            dp[i][i] = 0
            left[i][i] = stoneValue[i]
            right[i][i] = stoneValue[i]

        for i in range(N-1, -1, -1):
            k = i
            left_sum = stoneValue[k]
            for j in range(i + 1, N):
                tot = preSum[j+1] - preSum[i]
                while left_sum < tot / 2:
                    k += 1
                    left_sum += stoneValue[k]
                if left_sum == tot / 2:
                    dp[i][j] = max(left[i][k], right[k + 1][j])
                else:
                    dp[i][j] = max(
                        0 if k-1 < i else left[i][k-1],
                        0 if k+1 > j else right[k+1][j]
                    )
                left[i][j] = max(left[i][j-1], dp[i][j] + tot)
                right[i][j] = max(right[i+1][j], dp[i][j] + tot)
        return dp[0][N-1]

s = Solution()
stoneValue = [6,2,3,4,5,5]
# stoneValue = [7,7,7,7,7,7,7]
# stoneValue = [4]
print(s.stoneGameV(stoneValue))