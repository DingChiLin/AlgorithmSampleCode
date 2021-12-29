from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
    
        N = len(matrix)
        M = len(matrix[0])
        DP = [[0 for _ in range(M+1)] for _ in range(N+1)]
        ans = 0
        for i in range(1, N+1):
            for j in range(1, M+1):
                if (matrix[i-1][j-1] == '0'):
                    DP[i][j] = 0
                else:
                    DP[i][j] = min(DP[i-1][j], min(DP[i][j-1], DP[i-1][j-1])) + 1
                    ans = max(ans, DP[i][j]*DP[i][j])
        return ans