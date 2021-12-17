class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True

        for i in range(1, len(s)+1):
            for w in wordDict:
                if i >= len(w) and s[i-len(w):i] == w:
                    dp[i] = dp[i] or dp[i-len(w)]

        return dp[-1]  