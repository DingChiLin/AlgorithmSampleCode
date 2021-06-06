from typing import List

# Binary search + DFS
class Solution:
    def canReach(self, heights, max_effort):
        N = len(heights)
        M = len(heights[0])
        visited = [[False for _ in range(M)] for _ in range(N)]

        def dfs(x, y):
            if (x == N-1 and y == M-1):
                return True
            for (dx, dy) in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if (0 <= nx < N and 0 <= ny < M) and \
                     not visited[nx][ny] and \
                     abs(heights[nx][ny] - heights[x][y]) <= max_effort:
                    visited[nx][ny] = True
                    if dfs(nx, ny):
                        return True
            return False
        return dfs(0, 0)

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        left, right = 0, 1000000
        while (left < right):
            mid = (left + right) // 2
            if self.canReach(heights, mid):
                right = mid
            else:
                left = mid + 1
        return left

# Dijkstra
import heapq
from math import inf

class Solution2:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pq = [(0, 0, 0)]
        N = len(heights)
        M = len(heights[0])
        dst = [[inf for _ in range(M)] for _ in range(N)]
        dst[0][0] = 0

        while pq:
            d, x, y = heapq.heappop(pq)
            if (x == N-1 and y == M-1):
                return d
            if d != dst[x][y]:
                continue
            for (dx, dy) in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if (0 <= nx < N and 0 <= ny < M):
                    nd = max(d, abs(heights[nx][ny] - heights[x][y]))
                    if nd < dst[nx][ny]:
                        dst[nx][ny] = nd
                        heapq.heappush(pq, (nd, nx, ny))

s = Solution()
heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
heights = [[1,2,2],[3,8,2],[5,3,5]]

print(s.minimumEffortPath(heights))

