from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr # add zero at first place for convenience
        N = len(arr)
        MOD = int(1e9+7)
        stk = [0]
        dp = [0] * N
        for i in range(1, N): # start from index 1
            while stk and arr[i] < arr[stk[-1]]:
                stk.pop()
            dp[i] = (dp[stk[-1]] + (i - stk[-1]) * arr[i]) % MOD
            stk.append(i)
        return sum(dp) % MOD

s = Solution()
arr = [11,81,94,43,3]
print(s.sumSubarrayMins(arr))