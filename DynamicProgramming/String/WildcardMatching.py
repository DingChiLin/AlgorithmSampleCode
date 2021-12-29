class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(len(p)):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j]
        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i] or p[j] == '?':
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j+1]

        return dp[-1][-1]