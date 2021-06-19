from typing import List
import heapq
from math import inf

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        N = len(quality)
        workers = []
        for i in range(N):
            q = quality[i]
            w = wage[i]
            workers.append((w / q, w, q))
        workers.sort() # sort by wage / quality ratio

        quality_max_heap = []
        total_quality = 0
        ans = inf
        for worker in workers:
            r, w, q = worker
            total_quality += q
            heapq.heappush(quality_max_heap, -q)
            if len(quality_max_heap) > k:
                pop_q = -heapq.heappop(quality_max_heap)
                total_quality -= pop_q
            if len(quality_max_heap) == k:
                ans = min(ans, total_quality * r)
 
        return ans

s = Solution()
quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
k = 3
print(s.mincostToHireWorkers(quality, wage, k))