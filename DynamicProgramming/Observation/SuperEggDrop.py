'''
dp[m][k] means that, given K eggs and M moves,
what is the maximum number of floor that we can check.
'''

'''
1D DP
time: O(NK)
'''
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = 1 + dp[i-1][j-1] + dp[i-1][j]
        for i in range(n+1):
            if dp[i][k] >= n:
                return i

'''
1D DP
time: O(KlogN)
'''
class Solution:
    def superEggDrop(self, K, N):
        dp = [0, 0]
        m = 0
        while dp[-1] < N:
            for i in range(len(dp) - 1, 0, - 1):
                dp[i] += dp[i - 1] + 1
            if len(dp) < K + 1:
                dp.append(dp[-1])
            m += 1
        return m