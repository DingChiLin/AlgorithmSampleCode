from typing import List
from collections import defaultdict, deque
from math import inf
import heapq

class Solution:
    def dijkstra(self, N, graph, start):
        heap = [(0, start)]
        distance = [inf] * (N + 1)
        visited = set()
        while len(heap):
            d, n = heapq.heappop(heap)
            if n in visited or d == distance[n]:
                continue

            if distance[n] == inf: # first min distance
                distance[n] = d
            elif d == distance[n] + 1 or d == distance[n] + 2: # second min distance
                distance[n] = d
                visited.add(n)
            else:
                continue

            for nn, nd in graph[n]:
                heapq.heappush(heap, (d+nd, nn))

        return distance

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append((y, 1))
            graph[y].append((x, 1))
        distances = self.dijkstra(n, graph, 1)

        # Greedy
        D = distances[n]
        ans = 0
        for i in range(D):
            ans += time
            key = (ans // change)
            if (i != D-1) and (key & 1):
                ans = change * (key + 1)
        return ans