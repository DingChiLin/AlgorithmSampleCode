from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-s for s in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            s1 = heapq.heappop(pq)
            s2 = heapq.heappop(pq)
            if (s1 == s2):
                continue
            else:
                heapq.heappush(pq, s1 - s2)
        return 0 if not pq else -pq[0]

s = Solution()
stones = [2,2]
print(s.lastStoneWeight(stones))