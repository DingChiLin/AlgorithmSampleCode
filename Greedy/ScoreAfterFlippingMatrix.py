from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        # let each row start with 1
        for i in range(N):
            # row start with 0
            if grid[i][0] == 0:
                # flip this row
                for j in range(M):
                    grid[i][j] = grid[i][j] ^ 1 # xor operation

        # let each column has as many 1s as possible
        for j in range(1, M):
            zero_cnt = 0
            # count zero of this column
            for i in range(N):
                if grid[i][j] == 0:
                    zero_cnt += 1
            if (zero_cnt > N/2):
                # flip this column
                for i in range(N):
                    grid[i][j] = grid[i][j] ^ 1

        ans = 0
        bit_value = 1
        for j in range(M-1, -1, -1):
            for i in range(N):
                ans += grid[i][j] * bit_value
            bit_value *= 2

        return ans

s = Solution()
grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(s.matrixScore(grid))