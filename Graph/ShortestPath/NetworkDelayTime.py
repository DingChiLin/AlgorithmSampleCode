from typing import List
import heapq
from math import inf
from collections import defaultdict

class Solution:
    def dijkstra(self, start, N, edges):
        pq = [(0, start)]
        dst = [inf for _ in range(N)]
        visited = set()

        while pq:
            d, n = heapq.heappop(pq)
            if n in visited:
                continue
            visited.add(n)
            dst[n] = d 
            for nn, nd in edges[n]:
                if nn not in visited:
                    heapq.heappush(pq, (d + nd, nn))

        return dst

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n+1)]
        for u, v, w in times:
            edges[u].append((v,w))

        dst = self.dijkstra(k, n+1, edges)

        result = max(dst[1:])    
        return -1 if result == inf else result

s = Solution()
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(s.networkDelayTime(times, n, k))