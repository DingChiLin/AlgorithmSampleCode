from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop_routes = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                stop_routes[stop].append(i)

        que = deque()
        que.append((source, 0))
        visited_routes = set()

        while que:
            stop, d = que.popleft()
            if stop == target:
                return d
            for route in stop_routes[stop]:
                if route not in visited_routes:
                    visited_routes.add(route)
                    for stop in routes[route]:
                        que.append((stop, d + 1))

        return -1

s = Solution()
routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source = 15
target = 12

routes = [[1,2,7],[3,6,7]]
source = 1
target = 6
print(s.numBusesToDestination(routes, source, target))