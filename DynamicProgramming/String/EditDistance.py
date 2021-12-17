from typing import List

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        DP = [[0 for _ in range(M+1)] for _ in range(N+1)]
        for i in range(1, N+1):
            DP[i][0] = i
        for j in range(1, M+1):
            DP[0][j] = j
        for i in range(1, N+1):
            for j in range(1, M+1):
                if word1[i-1] == word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + 1
        return DP[N][M]

s = Solution()
word1 = "intention"
word2 = "execution" 
print(s.minDistance(word1, word2))