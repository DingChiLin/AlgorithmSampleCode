import heapq
from math import inf

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

class Solution2:
    def dijkstra(self, start, N, edges):
        pq = [(0, start)]
        dst = [inf for _ in range(N)]

        while pq:
            d, n = heapq.heappop(pq)
            if d >= dst[n]:
                continue
            dst[n] = d 
            for nn, nd in edges[n]:
                if d + nd < dst[nn]:
                    heapq.heappush(pq, (d + nd, nn))

        return dst

# direction: left -> right
#        5    7
#     1 -- 3 -- 5
#   1/   2/ 1\ /3 
#  0 -- 2 -- 4
#     3    8
#

s = Solution()
edges = [
    [[1,1], [2,3]],
    [[3,5]],
    [[3,2], [4,8]],
    [[4,1], [5,7]],
    [[5,3]],
    []
]
print(s.dijkstra(0, 6, edges)) # [0, 1, 3, 5, 6, 9]