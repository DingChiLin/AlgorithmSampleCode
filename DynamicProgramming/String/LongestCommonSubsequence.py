class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        N = len(text1)
        M = len(text2)
        DP = [[0 for _ in range(M+1)] for _ in range(N+1)]
        for i in range(1, N+1):
            pos = 0
            for j in range(1, M+1):
                if (text1[i-1] == text2[j-1]):
                    DP[i][j] = DP[i-1][j-1] + 1
                else:
                    DP[i][j] = max(DP[i-1][j], DP[i][j-1])
        return DP[N][M]