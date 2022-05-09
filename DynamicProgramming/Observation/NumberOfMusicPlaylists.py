class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = int(1e9) + 7
        DP = [[0 for _ in range(n+1)] for _ in range(goal+1)]
        DP[0][0] = 1

        for i in range(1, goal+1):
            for j in range(1, n+1):
                if j > k:
                    DP[i][j] = (DP[i-1][j-1] * (n - (j-1)) + DP[i-1][j] * (j - k)) % MOD
                else:
                    DP[i][j] = (DP[i-1][j-1] * (n - (j-1))) % MOD

        return DP[goal][n]
