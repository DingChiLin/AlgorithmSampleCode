class Solution:
    def __init__(self):
        self.dp = {}

    def fibonacci(self, x):
        if x == 1 or x == 2:
            return 1
        if x in self.dp: # reuse
            return self.dp[x]

        # record answer for index x
        self.dp[x] = self.fibonacci(x-1) + self.fibonacci(x-2)
        return self.dp[x]

class Solution2:
    def fibonacci(self, x):
        dp = [0 for i in range(x+1)]
        dp[1] = 1
        dp[2] = 1
        for i in range(3, x+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[x]

s = Solution2()
print(s.fibonacci(100))