from typing import List
import heapq

class Solution:
    def __init__(self):
        self.moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def valid(self, x, y, N, M):
        return (0 <= x < N and 0 <= y < M)

    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        start = (0, 0)
        end = (N-1, M-1)
        pq = []
        heapq.heappush(pq, (grid[0][0], start))
        visited = [[False for _ in range(M)] for _ in range(N)]
        visited[0][0] = True
        ans = 0
        while(pq):
            v, (x, y) = heapq.heappop(pq)
            ans = max(ans, v)
            if (x, y) == end:
                return ans

            for (dx, dy) in self.moves:
                nx = x + dx
                ny = y + dy
                if self.valid(nx, ny, N, M) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(pq, (grid[nx][ny], (nx, ny)))

        return ans

s = Solution()
grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(s.swimInWater(grid))
