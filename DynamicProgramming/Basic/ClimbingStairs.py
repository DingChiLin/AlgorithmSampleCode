# bottom-up
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# top-down
class Solution2:
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

s = Solution()
n = 3
print(s.climbStairs(n))