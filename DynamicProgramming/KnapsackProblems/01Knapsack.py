class Solution:
    def findMaxValue(self, capacity, items):
        N = len(items)
        dp = [[0 for j in range(capacity + 1)] for i in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, capacity + 1):
                weight, value = items[i-1]
                if (j - weight >= 0):
                    dp[i][j] = max(value + dp[i-1][j - weight], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[N][capacity]

capacity = 7
items = [[4, 9], [5, 15], [3, 8]] #[w, v]

s = Solution()
print(s.findMaxValue(capacity, items))