from typing import List
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        N = len(isWater)
        M = len(isWater[0])
        que = deque()
        ans = [[-1 for _ in range(M)] for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if isWater[i][j]:
                    ans[i][j] = 0
                    que.append((i, j, 0))
    
        while que:
            x, y, d = que.popleft()
            ans[x][y] = d
            for dx, dy in [[1,0], [0,1], [-1,0], [0,-1]]:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                if ans[nx][ny] == -1:
                    ans[nx][ny] = d+1
                    que.append((nx, ny, d+1))
        return ans