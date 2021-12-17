from typing import List
from collections import defaultdict

MOD = int(1e9+7)

# Like Distinct Subsequences II
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        N = len(binary)
        dp = [0] * (N+1)
        records = defaultdict(int)

        hasZero = False
        for i in range(1, N+1):
            if binary[i-1] == '0':
                hasZero = True
            dp[i] = dp[i-1] * 2 + (1 if binary[i-1] == '1' else 0)
            if binary[i-1] in records:
                index = records[binary[i-1]]
                dp[i] -= (dp[index-1] + (1 if binary[i-1] == '1' else 0))
            dp[i] %= MOD
            records[binary[i-1]] = i

        return dp[N] + (1 if hasZero else 0)

# Look at the ending digit
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        endWithZero = 0
        endWithOne = 0
        hasZero = 0
        for b in binary:
            if b == '1':
                endWithOne = (endWithOne + endWithZero + 1) % MOD
            else:
                endWithZero = (endWithOne + endWithZero) % MOD
                hasZero = 1
        return (endWithOne + endWithZero + hasZero) % MOD

# Do it reversely
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        N = len(binary)
        dp = [0] * (N+1)
        lastZero = N
        lastOne = N
        for i in range(N-1, -1, -1):
            dp[i] += 1
            dp[i] = (dp[i] + dp[lastZero]) % MOD
            dp[i] = (dp[i] + dp[lastOne]) % MOD
            if binary[i] == '0':
                lastZero = i
            else:
                lastOne = i
        return (dp[lastOne] + (1 if lastZero != N else 0)) % MOD

s = Solution()
ss = "101"
ss = "00"
ss = "100110"
print(s.numberOfUniqueGoodSubsequences(ss))