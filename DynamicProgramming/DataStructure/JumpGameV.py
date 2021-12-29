from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)
        sorted_arr = sorted([(v, i) for i, v in enumerate(arr)])
        dp = [0 for i in range(N)]
        for v, i in sorted_arr:
            # left
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                else:
                    break
            # right
            for k in range(i + 1, min(i + d + 1, N)):
                if arr[k] < arr[i]:
                    dp[i] = max(dp[i], 1 + dp[k])
                else:
                    break

        return max(dp) + 1

s = Solution()
arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2

arr = [7,1,7,1,7,1]
d = 2
print(s.maxJumps(arr, d))