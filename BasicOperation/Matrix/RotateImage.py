from typing import List

# rotate directly
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix[0])
        for i in range(N//2):
            for j in range((N+1)//2):
                matrix[j][N-1-i], matrix[N-1-i][N-1-j], matrix[N-1-j][i], matrix[i][j] = \
                matrix[i][j], matrix[j][N-1-i], matrix[N-1-i][N-1-j], matrix[N-1-j][i]

# combine with transpose + reflect
class Solution:
    def transpose(self, matrix):
        N = len(matrix[0])
        for i in range(N):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reflect(self, matrix):
        N = len(matrix[0])
        for j in range(N // 2):
            for i in range(N):
                matrix[i][j], matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        self.reflect(matrix)
        self.transpose(matrix)

s = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
print(matrix)