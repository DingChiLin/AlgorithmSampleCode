from typing import List
from collections import defaultdict

MOD = int(1e9+7)

class Solution:
    def distinctSubseqII(self, S: str) -> int:
        N = len(S)
        dp = [0] * (N+1)
        records = defaultdict(int)

        for i in range(1, N+1):
            dp[i] = dp[i-1] * 2 + 1
            if S[i-1] in records:
                index = records[S[i-1]]
                dp[i] -= (dp[index-1] + 1)
            dp[i] %= MOD
            records[S[i-1]] = i

        return dp[N]
 
s = Solution()
ss = "aba"
ss = "abb"
print(s.distinctSubseqII(ss))