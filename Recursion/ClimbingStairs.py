class Solution:
    def __init__(self):
        self.dp = {}

    def dfs(self, n):
        if n == 0 or n == 1:
            return 1
        if n in self.dp:
            return self.dp[n]
        res = self.dfs(n - 1) + self.dfs(n - 2)
        self.dp[n] = res
        return self.dp[n]
    
    def climbStairs(self, n: int) -> int:
        return self.dfs(n)