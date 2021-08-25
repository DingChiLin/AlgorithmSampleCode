from typing import List
import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        position = startFuel
        count = 0
        pq = []
        for p, f in stations:
            if position < p:
                while pq and position < p:
                    position += -heapq.heappop(pq)
                    count += 1
                if position < p:
                    return -1
                if position >= target:
                    break
            heapq.heappush(pq, -f)

        return count
