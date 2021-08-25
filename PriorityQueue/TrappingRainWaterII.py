from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        N = len(heightMap)
        M = len(heightMap[0])
        visited = set()
        pq = []

        for i in range(N):
            heapq.heappush(pq, (heightMap[i][0], (i, 0)))
            heapq.heappush(pq, (heightMap[i][M-1], (i, M-1)))
            visited.add((i, 0))
            visited.add((i, M-1))
        for j in range(1, M-1):
            heapq.heappush(pq, (heightMap[0][j], (0, j)))
            heapq.heappush(pq, (heightMap[N-1][j], (N-1, j)))
            visited.add((0, j))
            visited.add((N-1, j))
        ans = 0
        while pq:
            h, (x, y) = heapq.heappop(pq)
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if (nx, ny) not in visited and \
                    0 <= nx < N and 0 <= ny < M:
                    visited.add((nx, ny))
                    nh = heightMap[nx][ny]
                    if (nh >= h):
                        heapq.heappush(pq, (nh, (nx, ny)))
                    else:
                        ans += (h - nh)
                        heapq.heappush(pq, (h, (nx, ny))) 
        return ans

s = Solution()        
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print(s.trapRainWater(heightMap))