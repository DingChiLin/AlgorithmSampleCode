'''
dp[n][k]: given n moves and K eggs, what is the maximum number of floor that we can check.
'''

'''
2D DP
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
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [0 for _ in range(k+1)]
        for i in range(1, n+1):
            for j in range(k, 0, -1):
                dp[j] = 1 + dp[j-1] + dp[j]
            if dp[k] >= n:
                return i