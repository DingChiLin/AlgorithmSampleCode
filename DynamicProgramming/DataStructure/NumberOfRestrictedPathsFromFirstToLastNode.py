from typing import List
from collections import defaultdict
import heapq
from math import inf

class TopologicalSort: # by DFS (recursive)
    def __init__(self):
        self.ans = None
        self.index = None

    def dfs(self, node, edges, visited, curVisited, dst):
        for v in edges[node]:
            if dst[v] >= dst[node]:
                continue
            if v in curVisited:
                return False
            if v not in visited:
                visited.add(v)
                curVisited.add(v)
                if not self.dfs(v, edges, visited, curVisited, dst):
                    return False
                curVisited.remove(v)
        self.ans[self.index] = node      
        self.index -= 1
        return True

    def sort(self, nodes, edges, dst):
        N = len(nodes)
        self.ans = [None for _ in range(N)]
        self.index = N - 1
        visited = set()
        curVisited = set()
        for n in nodes:
            if n not in visited:
                visited.add(n)
                curVisited.add(n)
                if not self.dfs(n, edges, visited, curVisited, dst):
                    return []
                curVisited.remove(n)
        return self.ans

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

    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = int(1e9) + 7
        graph = defaultdict(list)
        graph2 = defaultdict(list)
        for x, y, d in edges:
            graph[x].append((y, d))       
            graph[y].append((x, d))
            graph2[x].append(y)
            graph2[y].append(x)
        dst = self.dijkstra(n, n+1, graph)

        TS = TopologicalSort()
        nodes = TS.sort([i for i in range(1, n+1)], graph2, dst)
        DP = [0 for i in range(n+1)]
        DP[n] = 1
        for i in range(len(nodes)-2, -1, -1):
            n = nodes[i]
            DP[n] = 0
            for nx in graph2[n]:
                if dst[nx] < dst[n]:
                    DP[n] += DP[nx]
                    DP[n] %= MOD

            if n == 1:
                return DP[n] % MOD

s = Solution()
n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]


n = 7
edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
print(s.countRestrictedPaths(n, edges))