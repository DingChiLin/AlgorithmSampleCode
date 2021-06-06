from typing import List
from collections import defaultdict
import heapq

class MST:
    def find(self, nodes, edges):
        s = nodes[0]
        N = len(nodes)

        pq = []
        for v, w in edges[s]:
            heapq.heappush(pq, (w, s, v)) # (weight, u, v)
        visited = set([s])

        weight = 0
        while len(visited) < N:
            w, u, v = heapq.heappop(pq)
            if v in visited:
                continue
            visited.add(v)
            weight += w
            for nv, nw in edges[v]:
                if nv not in visited:
                    heapq.heappush(pq, (nw, v, nv))

        return weight

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        edges = defaultdict(list)
        for i in range(N):
            for j in range(i+1, N):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges[i].append([j, w])
                edges[j].append([i, w])
        
        return MST().find(list(range(N)), edges)

s = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(s.minCostConnectPoints(points))