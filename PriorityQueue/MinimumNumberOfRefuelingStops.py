from typing import List
import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        curr = startFuel
        count = 0
        pq = []
        for p, f in stations:
            if curr < p:
                while pq and curr < p:
                    curr += -heapq.heappop(pq)
                    count += 1
                if curr >= target:
                    break
                if curr < p:
                    return -1
            heapq.heappush(pq, -f)

        return count
