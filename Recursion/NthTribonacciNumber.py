class Solution:
    def __init__(self):
        self.dp = {}

    def dfs(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        if n in self.dp:
            return self.dp[n]
        res = self.dfs(n - 1) + self.dfs(n - 2) + self.dfs(n-3)
        self.dp[n] = res
        return self.dp[n]
    
    def tribonacci(self, n: int) -> int:
        return self.dfs(n)