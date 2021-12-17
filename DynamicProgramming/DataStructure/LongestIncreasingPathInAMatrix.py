from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        nums = []
        for x in range(N):
            for y in range(M):
                nums.append((matrix[x][y], x, y))
        nums.sort()

        length = [[1 for _ in range(M)] for _ in range(N)]
        maxLength = 0
        for n, x, y in nums:
            tmp = 0
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if (0 <= nx < N) and (0 <= ny < M):
                    if matrix[nx][ny] < matrix[x][y]:
                        tmp = max(tmp, length[nx][ny])
            length[x][y] = 1 + tmp
            maxLength = max(maxLength, length[x][y])

        return maxLength

s = Solution()
matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(s.longestIncreasingPath(matrix))