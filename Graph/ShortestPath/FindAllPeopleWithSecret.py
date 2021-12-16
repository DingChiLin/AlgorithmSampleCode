from typing import List
from collections import deque, defaultdict
import heapq

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        edges = defaultdict(list)
        for x, y, t in meetings:
            edges[x].append((y, t))
            edges[y].append((x, t))

        ans = set()

        # Dijkstra
        heap = [(0, 0), (0, firstPerson)]
        distance = {}
        visited = set()
        while len(heap):
            d, n = heapq.heappop(heap)
            if n in visited:
                continue
            ans.add(n)
            visited.add(n)
            distance[n] = d
            for nn, nd in edges[n]:
                if nn not in visited and nd >= d :
                    heapq.heappush(heap, (nd, nn))

        return list(ans)

s = Solution()
n = 6
meetings = [[1,2,5],[2,3,8],[1,5,10]]
firstPerson = 1
print(s.findAllPeople(n, meetings, firstPerson))