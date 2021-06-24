# bottom-up
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]

# top-down
class Solution2:
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

s = Solution()
n = 25
print(s.climbStairs(n))