from typing import List
import heapq
from collections import defaultdict

class Solution:
    def dijkstra(self, start, N, edges):
        pq = [(-1, start)]
        dst = [0 for i in range(N)]
        dst[start] = -1

        while len(pq):
            p, n = heapq.heappop(pq)
            if p != dst[n]:
                continue
            dst[n] = p
            for nn, np in edges[n]:
                if p * np < dst[nn]:
                    dst[nn] = p * np
                    heapq.heappush(pq, (dst[nn], nn))

        return dst

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        edges_with_cost = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            edges_with_cost[u].append([v, succProb[i]])
            edges_with_cost[v].append([u, succProb[i]])
        dst = self.dijkstra(start, n, edges_with_cost)
        return -dst[end]


s = Solution()
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

n = 5
edges = [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
succProb = [0.37,0.17,0.93,0.23,0.39,0.04]
start = 3
end = 4
print(s.maxProbability(n, edges, succProb, start, end))