from typing import List
from collections import deque

class Solution:

    def flip(self, x, y, N, M, grid):
        grid[x][y] = 2
        for (dx, dy) in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nx = x + dx
            ny = y + dy
            if (0 <= nx < N) and (0 <= ny < M) and grid[nx][ny] == 1:
                self.flip(nx, ny, N, M, grid)

    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        # flip one island from 1 to 2
        flag = True
        for x in range(N):
            if flag:
                for y in range(M):
                    if grid[x][y] == 1:
                        self.flip(x, y, N, M, grid)
                        flag = False
                        break

        # bfs start from island 1
        que = deque()
        for x in range(N):
            for y in range(M):
                if grid[x][y] == 1:
                    que.append((x, y, 0))

        while que:
            x, y, d = que.popleft()
            for (dx, dy) in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if (0 <= nx < N) and (0 <= ny < M):
                    if grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        que.append((nx, ny, d + 1))
                    elif grid[nx][ny] == 2: # find another island (island 2)
                        return d

s = Solution()
grid = [[0,1,0],[0,0,0],[0,0,1]]
print(s.shortestBridge(grid))
