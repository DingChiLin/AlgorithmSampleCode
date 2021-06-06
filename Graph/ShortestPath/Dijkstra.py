import heapq
from math import inf

class Solution:
    def dijkstra(self, start, N, edges):
        pq = [(0, start)]
        dst = [inf for i in range(N)]
        dst[start] = 0

        while len(pq):
            d, n = heapq.heappop(pq)
            if d != dst[n]:
                continue
            dst[n] = d
            for nn, nd in edges[n]:
                if d + nd < dst[nn]:
                    dst[nn] = d + nd
                    heapq.heappush(pq, (dst[nn], nn))

        return dst

class Solution2:
    def dijkstra(self, start, N, edges):
        pq = [(0, start)]
        dst = [inf for i in range(N)]
        visited = [False for i in range(N)]

        while len(pq):
            d, n = heapq.heappop(pq)
            if visited[n]:
                continue
            visited[n] = True
            dst[n] = d # first time popped out

            for nn, nd in edges[n]:
                if not visited[nn]:
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
print(s.dijkstra(0, 6, edges))