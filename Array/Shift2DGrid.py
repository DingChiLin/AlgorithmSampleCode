from typing import List

'''
Time: O(N)
Space: O(N)
'''

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        N = len(grid)
        M = len(grid[0])
        res = [[0 for _ in range(M)] for _ in range(N)]
        for row in range(N):
            for col in range(M):
                new_col = (col + k) % M
                new_row = (row + ((col + k) // M)) % N
                res[new_row][new_col] = grid[row][col]
        return res 


'''
Time: O(N) (3 pass)
Space: O(1)
'''

class Solution:
    def reverse(self, grid, N, M, left, right):
        while left < right:
            r1, c1 = left // M, left % M
            r2, c2 = right // M, right % M
            grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]
            left += 1
            right -= 1

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        N = len(grid)
        M = len(grid[0])
        k %= N*M
        self.reverse(grid, N, M, 0, N*M-1)
        self.reverse(grid, N, M, 0, k-1)
        self.reverse(grid, N, M, k, N*M-1)
        return grid

